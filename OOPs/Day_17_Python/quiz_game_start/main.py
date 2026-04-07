from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dictionary in question_data:
    question_object = Question(dictionary['text'], dictionary["answer"])
    question_bank.append(question_object)
# print(question_bank)
question_ask = QuizBrain(question_bank)
question_ask.ask_question()