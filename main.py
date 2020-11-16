from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Let us create the question bank and fill it with the data from the question bank.

question_bank = []
for i in range(len(question_data['results'])):
    question_bank.append(Question(question_data['results'][i]['question'], question_data['results'][i]['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"\nYour final score is {quiz.score} out of {quiz.question_number}.")
