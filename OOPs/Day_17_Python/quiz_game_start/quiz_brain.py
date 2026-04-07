# from main import question_bank

class QuizBrain:
    def __init__(self, question):
        """This is a constructor, which takes list as a input and initilizes to question_list"""
        self.question_number = 0
        self.score = 0
        self.question_list = question

    def still_has_question(self):
        if self.question_number < (len(self.question_list)):
            return True
        else:
            return False

    def check_answer(self, user_answer):
        """This will chak the user answer with the correct answer and returns Correct or Wrong, text data"""
        if(user_answer == self.question_list[self.question_number].answer):
            self.score += 1
            return "Correct!!"
        else:
            return "Sorry!!, You are wrong"
        
    def ask_question(self):
        """This will prompt a question to uswer and prints if answer is correct"""
        while (self.still_has_question()):
            print(self.check_answer(input(f"Q.{self.question_number + 1} : {self.question_list[self.question_number].text}. (True/False): ")))
            self.question_number+= 1
            print(f"You got {self.get_score()} / {self.question_number} score")
        self.score_print()

    def score_print(self):
        print("\n\n")     
        print("You have completed the quiz")
        print(f"Your score is {self.get_score()} / {self.question_number}")

    def get_score(self):
        return self.score
