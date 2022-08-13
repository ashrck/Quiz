from ast import excepthandler
import random as rand

from sklearn.utils import shuffle


print("Welcome to the Quiz")

print("In this quiz you will have to answer questions with multiple choice answers")


def start():
    enter = input("Type a number form 1-4 to begin: ")
    enter = int(enter)

    if (enter >= 1) and (enter <= 4):
        print('Correct')
        return True
    else:
        return False


while start() == False:
    if start() == True:
        print("Try again")


question_answer = {"Capital of USA": "Washington DC",
 "Capital of Egypt":"Cairo", "Capital of India": "New Dehli", "Capital of Brazil": "Brasillia",
 "Capital of England": "London", "Capital of Afghanistan":"Kabul",
 "Capital of Pakistan": "Islamabad", "Capital of Russia":"Moscow",
 "Capital of France":"Paris", "Capital of South Korea":"Seoul" }

questions = [question_answer.keys()]
answers = list(question_answer.values())

def question_choices(questions, answers, question_answer, score):
    question = rand.choice(list(rand.choice(questions)))
    print(question)
    answer = question_answer[question]
    answers.remove(answer) 
    choices = rand.sample(answers, 3)
    choices.append(answer)
    choices = shuffle(choices)
    print(choices)
    player_answer = int(input("Choose from 1-4: "))
    if choices[player_answer -1]== answer:
        print("correct")
        score += 1
        return score 
    else:
        print("wrong")
        return score


question_num = 0
score = 0

while question_num < 5:
    question_num += 1
    print("Question " + str(question_num))
    score = question_choices(questions, answers, question_answer,score)
    print("Score:" + str(score) +"/n")
