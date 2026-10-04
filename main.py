meme_dict = {
            "CRINGE": "Something exceptionally weird or embarrassing",
            "LOL": "A common response to something funny ",
            "A SWEAT": "A person or player who takes an activity to a high degree of seriousness",
            "TO AGGRO": "To get aggressive/angry",
            "IRL": "In real life",
            "SHEESH":"Slight disapproval"
            }
word = input("Type in a word you don't understand (use all capital letters!): ")
if word in meme_dict.keys():
    # What should we do if the word was found?
    print(meme_dict[word])
else:
    print("Word is not in dictionary")
    # What should we do if the word wasn't found?
