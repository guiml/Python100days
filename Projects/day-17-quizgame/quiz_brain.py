
class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # TODO: (3) asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        usr_answer = input(f"Q.{self.question_number}: {current_question.text}  (True/False): ")
        self.correct_answer(usr_answer, current_question.answer)

    # TODO: (4) checking if we are at the end of the quiz
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    # TODO: (5) checking if the answer was correct
    def correct_answer(self, usr_answer, correct_answer):
        if usr_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Wrong answer!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
        
