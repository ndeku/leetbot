import json
import os


class PostedLeetCodeQuestions:

    def __init__(self, data_file) -> None:
        self.data_file = data_file
        self.questions = self.__read_posted_questions()

    def __read_posted_questions(self) -> dict:
        if not os.path.exists(self.data_file):
            return {'posted_problem_ids' : []}

        with open(self.data_file) as f:
            probs = json.loads(f.read())

        return probs

    def write_posted_questions(self, data_file=None):
        if data_file is None:
            data_file = self.data_file

        with open(self.data_file, mode='w') as f:
            json.dump(self.questions, self.data_file)

