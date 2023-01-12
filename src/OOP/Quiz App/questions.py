class Question:

    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, user_answer):
        if user_answer not in self.choices:
            raise ValueError("Your answer must be one of our choices!!")
        return self.answer == user_answer

