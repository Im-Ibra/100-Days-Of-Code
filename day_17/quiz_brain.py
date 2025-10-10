class QuizBrain():

    def __init__(self, question_list):
        self.q_number = 0
        self.score = 0
        self.q_list = question_list

    def questions_left(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        c_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q. {self.q_number}: {c_question.question} (True/False): ")
        self.check_answer(user_answer, c_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct")
            self.score += 1
        else:
            print("Wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score: {self.score}/{self.q_number}")
        print("\n")