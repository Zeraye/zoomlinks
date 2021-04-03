class Chatbot:
    from typing import Optional

    def __init__(
        self,
        query: Optional[str] = "",
        db_name: Optional[str] = "database"):
        self.query = query
        self.db_name = db_name

    def db_read(self):
        # getting dir
        import os
        dir_name = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(dir_name, self.db_name + ".json")

        # opening file
        import json
        with open(db_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    def calc_simi(self, word1, word2):
        # getting similarity ratio
        import difflib
        simi_value = difflib.SequenceMatcher(None, word1, word2).ratio()

        return simi_value

    def simplify_senc(self, senc):
        # lower everything
        senc = [senc[i].lower() for i in range(len(senc))]

        # remove special characters
        sp_chars = ["ą", "ć", "ę", "ł", "ń", "ó", "ś", "ź", "ż"]
        cp_chars = ["a", "c", "e", "l", "n", "o", "s", "x", "z"]
        for char in senc:
            if char in sp_chars:
                senc[senc.index(char)] = cp_chars[sp_chars.index(char)]

        # remove dots and commans
        senc = [senc[i] for i in range(len(senc)) if
                   (senc[i] != "." and senc[i] != ",")]

        return "".join(senc)


    def response(self):
        # read database
        data = self.db_read()
        simi_mesh = [0 for i in range(len(data))]

        # find most similar pattern
        pos = 0
        for tag in data:
            for pattern in data[tag]["patterns"]:
                simi_mesh[pos] = max(
                    self.calc_simi(self.simplify_senc(pattern),
                                   self.simplify_senc(self.query)),
                    simi_mesh[pos])
            pos += 1

        # getting best similarity value
        simi_value = max(simi_mesh)

        # no proper response, similarity is too small
        if simi_value < 0.2:
            return ("""Niestety nie znam odpowiedzi na te pytanie.
                       Spróbuj je sformułować inaczej.""",
                       simi_value)

        # select random response
        import random
        pos = 0
        for tag in data:
            if pos == simi_mesh.index(max(simi_mesh)):
                responses = data[tag]["responses"]
                # don't allow to response and query be identical
                # expection (only one response & response == query)
                if (len(responses) == 1 and\
                    responses[0] == self.query):
                    return self.query, simi_value
                else:
                    if self.query in responses:
                        responses.remove(self.query)
                    return random.choice(data[tag]["responses"]), simi_value
            pos += 1
