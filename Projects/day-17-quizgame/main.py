#from tkinter.messagebox import QUESTION

## TRIVIA URL https://opentdb.com/
## https://opentdb.com/api.php?amount=10&category=23&type=boolean



from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# TODO: Create a question bank

question_bank = []
for q in question_data:
    question_text  = q['question']
    question_answer = q['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#print(question_bank[0].text)
#QuizBrain(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")