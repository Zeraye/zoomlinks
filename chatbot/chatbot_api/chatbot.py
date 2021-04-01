import difflib
import random
import json
import os

# reading databse file
def read(file_name):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(dir_name, file_name + '.json')
    with open(db_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

# sentences similarity
similarity = lambda word1, word2: difflib.SequenceMatcher(None, word1, word2).ratio()

# simpfily sentence by removing special characters and lowering everything
def simplify(sentence):
    sentence = [sentence[i].lower() for i in range(len(sentence))]
    special_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
    counterpart_chars = ['a', 'c', 'e', 'l', 'n', 'o', 's', 'x', 'z']
    for char in sentence:
        if char in special_chars:
            sentence[sentence.index(char)] = counterpart_chars[special_chars.index(char)]
    return ''.join(sentence)

# getting response
def response(query):
    data = read('database')
    similarity_mesh = [0 for i in range(len(data))]

    # find most similar pattern
    position = 0
    for tag in data:
        for pattern in data[tag]["patterns"]:
            similarity_mesh[position] =  max(similarity(simplify(pattern), simplify(query)), similarity_mesh[position])
        position += 1

    # ONLY FOR DEVELOPMENT
    print('[dev] >> ' + str(max(similarity_mesh)))

    # select random response
    position = 0
    for tag in data:
        if position == similarity_mesh.index(max(similarity_mesh)):
            return random.choice(data[tag]["responses"])
        position += 1
