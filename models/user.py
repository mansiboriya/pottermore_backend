from models.role import Role
from bson.objectid import ObjectId

class User:
  id = ""
  def __init__(self, name, role, password):
    self.name = name
    self.role = Role(role).name
    self.password = password

  def get(users, id):
    user = users.find_one({"_id": ObjectId(id)})
    user_auth = User(user.get('name'), user.get('role'), user.get('password'))
    user_auth.id = str(user.get('_id'))
    return user_auth

  def get_by_password(users, username, password):
      user = users.find_one({"name": username, "password": password})
      if user is None:
          return None
      user_auth = User(user.get('name'), user.get('role'), user.get('password'))
      user_auth.id = str(user.get('_id'))
      return user_auth

  def registerUser(users, username, password):
    user = users.find_one({"name": username, "password": password})
    print(user)
    if user:
      return None
    r_user = User(username, "participant", password)
    r = users.insert_one(r_user.__dict__)
    return r_user

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    return self.id

  def __repr__(self):
    return '<User %r>' % (self.name)