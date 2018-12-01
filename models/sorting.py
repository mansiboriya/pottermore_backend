class Sorting:


  def questions():
    questions = [
        { "Id": 1,"question":"Dawn or dusk?" ,
            "choice": ["Dawn", "Dusk"]
        },
        { "Id": 2,
            "question":"Which road tempts you most?" ,
            "choice":[
                "The wide,sunny,grassy lane",
                "The narrow,dark,latern-lit alley"
            ]
        },
        { "Id": 3,
            "question":"What are you most looking forward to learning at Hogwarts" ,
            "choice": [
                "Apparition and Disapparition",
                "Transfiguration",
                "Jinxes and hexes",
                "Flying on a broomstick"
            ]
        },

        { "Id": 4,
            "question":"Which of the following do you find most difficult to deal with" ,
            "choice": ["Hunger", "Loniess"]
        },
        { "Id": 5,
            "question":"Given the choice,would you rather invent a potion that would gurantee you" ,
            "choice": ["Love", "Glory", "Courage", "Wisdom"]
        },

        { "Id": 6,
            "question":"Two goblets are placed before you.Which would you choose to drink?" ,
            "choice":[
                "The foaming, frothing, silver liquid",
                "The goldenliquid that is so bright that it hurts the eye",
                "The purple liquid that gives off the smell of chocolate and plum"
            ]
        },
        { "Id": 7,
            "question":"If you were attending Hogwarts, which pet would you choose to take with you?" ,
            "choice": ["Black cat", "Tawny owl", "Snowy Owl", "Dragon toad"]
        },
        { "Id": 8,"question":"Heads or tails" ,
            "choice": ["Heads", "Tails"]
        },
         { "Id": 9,"question":"How would you like to be known in history " ,
            "choice": ["The Wise", "The Bold", "The Good", "The Great"]
        },


    ]
    return questions

  def houses():
    houses = [
        { "id": 1, "Name":"Gryffindor" },
        { "id": 2, "Name":"Hufflepuff" },
        { "id": 3, "Name":"Ravenclaw" },
        { "id": 4, "Name":"Slytherin" }
    ]
    return houses
