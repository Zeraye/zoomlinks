import difflib
import json
import random
import os

def similarity(word1, word2):
    return difflib.SequenceMatcher(None,word1,word2).ratio()

def read():
    dir_name = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(dir_name, 'database.json')
    with open(full_path, "r") as file:
        new_data = json.load(file)
        return new_data

def write(data, new_data):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(dir_name, 'database.json')
    with open(full_path, "r+") as file:
        data.update(new_data)
        json.dump(data, file, indent=4)

def find_answer(word):
    data = read()
    best_accuracy = 0
    best_message = ""
    for message in data:
        if similarity(message, word) > best_accuracy:
            best_accuracy = similarity(message, word)
            best_message = message

    # answer, accuracy, original_message
    # return random.choice(data[best_message]), best_accuracy, best_message

    # answer
    return random.choice(data[best_message])

def new_find_answer(query):
    data = read()
    best_query = difflib.get_close_matches(query, data)
    return data[best_query[0]]

def add_answer(message, answer):
    data = read()
    new_data = data
    try:
        new_data[message] += [answer]
    except KeyError:
        new_data.update({message: [answer]})
    finally:
        write(data, new_data)

def test():
    print('test')
