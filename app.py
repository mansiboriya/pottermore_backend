from flask import Flask,render_template,request,redirect,url_for, jsonify
from pymongo import MongoClient
from models.sorting import Sorting
from models.directions import Directions
import random
from flask_cors import CORS, cross_origin
from models.user import User
from flask_login import LoginManager, login_user, logout_user , current_user , login_required
import json
from bson import json_util
from bson.objectid import ObjectId
from flask import abort


app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'mansiboriya'
login_manager = LoginManager()
login_manager.init_app(app)

client = MongoClient("mongodb://127.0.0.1:27017") #host uri
db = client.adventure_quest #Select the database
users = db.users #Select the collection name

@app.route('/')
def demo():
  return "Hello World"


# ################   Authentication    #################### #

@app.route("/login/sddsd", methods=['POST'])
def login():
  req = request.get_json(silent=True)
  id = req.get('user_id')
  user1 = User.get(users, id)
  login_user(user1)
  return json_util.dumps(user1.__dict__, default=lambda o: o.__dict__)

@app.route("/login", methods=['POST'])
def login_password():
  req = request.get_json(silent=True)
  username = req.get('username')
  password = req.get('password')
  user1 = User.get_by_password(users, username, password)
  if user1 is not None:
      login_user(user1)
  return json_util.dumps(current_user.__dict__, default=lambda o: o.__dict__)

@app.route("/logout", methods=['POST'])
def logout():
  logout_user()
  return {'status': True}

@app.route("/register", methods=['POST'])
def register():
  req = request.get_json(silent=True)
  username = req.get('username')
  password = req.get('password')
  r_user = User.registerUser(users, username, password)
  return json_util.dumps(r_user.__dict__, default=lambda o: o.__dict__)

@app.route("/edituser", methods=['POST'])
@login_required
def edituder():
  req = request.get_json(silent=True)
  role = req.get('role')
  u = users.update_one({"_id": ObjectId(current_user.id) }, {"$set": {"role": role}})
  u1 = getUser(current_user.id)
  return json_util.dumps(u1, default=lambda o: o.__dict__)

def getUser(id):
  u = users.find_one({"user.id": id })
  return u


# ################   SORTING    #################### #

@app.route('/houses', methods=['GET'])
def get_houses():
    return jsonify({'houses': Sorting.houses})

@app.route('/sortedhouse',methods=['GET'])
@login_required
def get_randomhouse():
    id = random.randint(1,4)
    house = list(filter(lambda h: h['id'] == id, Sorting.houses()))
    print(house)
 #if true, return this element , if not return 404
    if len(Sorting.houses()) == 0:
        abort(404)
    return jsonify({'house': house[0]})


@app.route('/houses/<int:house_id>', methods=['GET'])
def get_house(house_id):
#check the elements in the questions
    house = list(filter(lambda h: h['id'] == house_id, Sorting.houses()))
 #if true, return this element , if not return 404
    if len(Sorting.houses()) == 0:
        abort(404)
    return jsonify({'house': house[0]})


#get all the questions
@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify({'questions': Sorting.questions()})


@app.route('/questions/<int:question_Id>', methods=['GET'])
def get_question(question_Id):
#check the elements in the questions
    question = list(filter(lambda q: q['Id'] == question_Id, Sorting.questions()))
 #if true, return this element , if not return 404
    if len(question) == 0:
        abort(404)
    return jsonify({'question': question[0]})


# ################   QUEST    #################### #
@app.route('/directions', methods=['GET'])
def get_directions():
    return jsonify({'directions': Directions.questions()})

@app.route('/answers', methods=['GET'])
def get_answers():
    return jsonify({'answers': Directions.answers()})


@login_manager.header_loader
def load_user_from_header(header_val):
    header_val = header_val.replace('Basic ', '', 1)
    if header_val is not None:
      print(header_val)
      header_val = json_util.loads(header_val)
      username = header_val.get('username')
      password = header_val.get('password')
      u = User.get_by_password(users, username, password)
      return u


if __name__ == "__main__":
  app.run()

