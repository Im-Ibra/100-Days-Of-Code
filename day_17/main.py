from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    question = Question(question= question_text, answer= question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.questions_left():
    quiz.next_question()

print(f"Final score: {quiz.score}/{quiz.q_number}")