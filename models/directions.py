class Directions:
  def questions():
    questions = [
      {
        "id": 0,
        "question": "Start?",
        "command": ["Yes"],
        "ignore": {
            "index": None
        }
      },
      {
        "id": 1,
        "question": "There is no light. Let's light it up! Yes or No?",
        "command": ["Yes"],
        "ignore": {
            "index": 2
        }
      },
      {
        "id": 2,
        "question": "The light has uncovered a room full of objects. There’s a Box you see in front of you.. Go forward or ignore?",
        "command": ["Go Forward"],
        "ignore": {
            "index": 51
        }
      },
      {
        "id": 3,
        "question": "The box is so ornately designed. Do you wanna peek inside? Inspect or ignore?",
        "command": ["Inspect"],
        "ignore": {
            "index": 6
        }
      },
      {
        "id": 4,
        "question": "Oh, good stuff, rookie! You found a letter! Keep it!",
        "command": ["Keep"],
        "letter": 1,
        "ignore": {
            "index": None
        }
      },
      {
        "id": 5,
        "question": "Let's continue. Go somewhere?",
        "command": ["Go Forward", "Go Back", "Go Left", "Go Right"],
        "index": 6,
        "ignore": {
            "index": None
        }
      },
      {
        "id": 6,
        "question": "There’s a painting here. Inspect or ignore?",
        "command": ["Inspect"],
        "ignore": {
            "index": 52
        }
      },
      {
        "id": 7,
        "question": "The painting is a horse running away in the field. Nothing unusual. Just Hogwarts stuff. Go somewhere else maybe?",
        "command": ["Go Forward", "Go Back", "Go Left", "Go Right"],
        "ignore": {
            "index": 8
        }
      },
      {
        "id": 8,
        "question": "Hmmm.. I see something shining. Must look. Inspect or ignore?",
        "command": ["Inspect"],
        "ignore": {
            "index": 53
        }
      },
      {
        "id": 9,
        "question": "That’s a shiney bowl with transparent liquid. Looks very pretty. I suggest let it be. What do you think? Inspect or ignore?",
        "command": ["Inspect"],
        "ignore": {
            "index": 13
        }
      },
      {
        "id": 10,
        "question": "You are smart, arent you? We see that the liquid is transparent and at the bottom of the bowl there’s a letter. Keep it!",
        "command": ["Keep"],
        "letter": 1,
        "ignore": {
            "index": None
        }
      },
      {
        "id": 11,
        "question": "Well Well, don't get impatient. Soon you’ll be able to get to the common room. Go somewhere?",
        "command": ["Go Forward", "Go Back", "Go Left", "Go Right"],
        "ignore": {
            "index": None
        }
      },
      {
        "id": 12,
        "question": "Wait a second. You kicked something by mistake. Did that sound like metal? You want to look for it?",
        "command": ["Yes"],
        "ignore": {
            "index": 51
        }
      },
      {
        "id": 13,
        "question": "Oh, that’s a key. Wonder what it opens. Keep it!",
        "command": ["Keep"],
        "ignore": {
            "index": None
        }
      },
      {
        "id": 14,
        "question": "Ooh, you see a scroll. Wonder what’s in it. Inspect or ignore?",
        "command": ["Inspect"],
        "ignore": {
            "index": 17
        }
      },
      {
        "id": 15,
        "question": "Hoorah! One more letter. Keep it!",
        "command": ["Keep"],
        "letter": 1,
        "ignore": {
            "index": 51
        }
      },
      {
        "id": 16,
        "question": "Feel good about your search? Let’s continue! Where do you want to go next?",
        "command": ["Go Forward", "Go Back", "Go Left", "Go Right"],
        "ignore": {
            "index": 51
        }
      },
      {
        "id": 17,
        "question": "Uh-oh! You’ve hit a wall. Go back?",
        "command": ["Go back"],
        "ignore": {
            "index": 17
        }
      },
      {
        "id": 18,
        "question": "Waaait! I see something. Is that a table or is it a chest? Inspect or ignore?",
        "command": ["Inspect"],
        "ignore": {
            "index": 23
        }
      },
      {
        "id": 19,
        "question": "It’s a chest. Looks like it needs a key. Do you have a key?",
        "command": ["Yes"],
        "ignore": {
            "index": 12
        }
      },
      {
        "id": 20,
        "question": "What next? Open the chest!",
        "command": ["Open"],
        "ignore": {
            "index": None
        }
      },
      {
        "id": 21,
        "question": "Whoa! You found TWO letters and you found food. Thank heavens. You look tired anyway. Keep it?",
        "command": ["Keep"],
        "letter": 2,
        "ignore": {
            "index": None
        }
      },
      {
        "id": 22,
        "question": "So, let's look for more. let’s keep walking. Go somewhere?",
        "command": ["Go Forward", "Go Back", "Go Left", "Go Right"],
        "ignore": {
            "index": 23
        }
      },
      {
        "id": 23,
        "question": "Nothing interesting. Keep walking",
        "command": ["Go Forward", "Go Back", "Go Left", "Go Right"],
        "ignore": {
            "index": 24
        }
      },
      {
        "id": 24,
        "question": "You pass through the painting again. Wait. Do you see a hidden letter in the corner of the painting? Inspect or ignore?",
        "command": ["Inspect"],
        "ignore": {
            "index": 53
        }
      },

      {
        "id": 25,
        "question": "Looks like you have all that you need. Check the letters you have and make a word to enter the common room. You will have only some time for it!",
        "command": ["Yes"],
        "ignore": {
            "index": None
        }
      },


      {
        "id": 50,
        "question": "The sorting hat is never wrong!! You are so good at this already. You found a letter. Keep it!",
        "command": ["Keep"],
        "letter": 1,
        "index": 8,
        "ignore": {
            "index": None
        }
      },
      {
        "id": 50,
        "question": "Let's try moving in the dark. Shall we?",
        "command": ["Yes"],
        "index": 8,
        "ignore": {
            "index": None
        }
      },
      {
        "id": 51,
        "question": "Okay then, let’s keep walking. Go somewhere?",
        "command": ["Go Forward", "Go Back", "Go Left", "Go Right"],
        "index": 8,
        "ignore": {
            "index": None
        }
      },
      {
        "id": 52,
        "question": "Alright then, walking it is. Go somewhere?",
        "command":["Go Forward", "Go Back", "Go Left", "Go Right"],
        "index": 8,
        "ignore": {
            "index": None
        }
      },
      {
        "id": 53,
        "question": "Go somewhere else?",
        "command":["Go Forward", "Go Back", "Go Left", "Go Right"],
        "index": 18,
        "ignore": {
            "index": None
        }
      }
    ]

    return questions

  def answers():
    answers = {
      "Slytherin": "LEADER",
      "Gryffindor": "BRAVE",
      "Hufflepuff": "LOYALTY",
      "Ravenclaw": "WISDOM"
    }