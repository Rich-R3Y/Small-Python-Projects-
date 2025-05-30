from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for quest in question_data:
    question = Question(quest['text'], quest['answer'])
    question_bank.append(question)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f'Your final score was {quiz.score}/{quiz.question_number}')
