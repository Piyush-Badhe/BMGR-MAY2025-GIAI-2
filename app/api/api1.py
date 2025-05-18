import json
BASE_DIR = "/Users/Paddy/BMGR-MAY2025-GIAI-2/"
def read_user():
    with open(f"{BASE_DIR}data/users.json") as stream:
        users = json.load(stream)
        return users


def read_questions(position: int):
    with open(f"{BASE_DIR}data/questions.json") as stream:
        questions = json.load(stream)

    for question in questions:
     if question['position'] == position:
            res = question.get('question')
            print(res)
    return res