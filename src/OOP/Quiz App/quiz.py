from questions import Question
import random


class Quiz:
    def __init__(self, questions):
        self.questions = random.sample(questions, len(questions))
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestionAndChoices(self):
        question = self.getQuestion()

        print(f"Question {self.questionIndex + 1}: {question.text}")

        for choice in question.choices:
            print("-" + choice)

        user_input = input("Please enter your result: ")
        if question.checkAnswer(user_input):
            self.score += 1

        self.questionIndex += 1
        self.loadQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestionAndChoices()

    def displayScore(self):
        print("Summary Of Your Test".center(100, '*'))
        score = 100 / len(self.questions)
        total_score = round(self.score * score)
        print("Your Result:", total_score)

    def displayProgress(self):
        total_question = len(self.questions)
        question_number = self.questionIndex + 1

        print(f"You Are In  {question_number}. Question Of {total_question} Questions ".center(100, '*'))


first_question = Question("which one is best programming language?", ["python", "c#", "dart", "java"], "python")
second_question = Question("which programming language is fastest?", ["python", "java", "c#", "dart"], "python")
third_question = Question("which programming language is easy to use?", ["python", "dart", "c#", "java"], "python")

quiz = Quiz([first_question, second_question, third_question])

quiz.displayQuestionAndChoices()
