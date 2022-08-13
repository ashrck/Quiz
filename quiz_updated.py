import random as rand

from sklearn.utils import shuffle

#Intro
print("Welcome to the Quiz")

print("In this quiz you will have to answer questions with multiple choice answers")


#Player starts game
def start_game():
    enter = input("Type a number form 1-4 to begin: \n")
    enter = int(enter)

    if (enter >= 1) and (enter <= 4):
        print("Quiz Started\n")
        return True
    else:
        return False

#Setup dictionary and list of question and answers 
question_answer = {"Capital of USA": "Washington DC",
 "Capital of Egypt":"Cairo", "Capital of India": "New Dehli", "Capital of Brazil": "Brasillia",
 "Capital of England": "London", "Capital of Afghanistan":"Kabul",
 "Capital of Pakistan": "Islamabad", "Capital of Russia":"Moscow",
 "Capital of France":"Paris", "Capital of South Korea":"Seoul",
 "Capital of Germany": "Berlin" }
questions = list(question_answer.keys())
answers = list(question_answer.values())

#Functions for setting up questions
def select_print_question(questions):
    question = rand.choice(questions)
    questions.remove(question)
    print(question)
    return question

def find_answer(question):
    answer = question_answer[question]
    return answer

def print_choices(answers, answer): 
    answers.remove(answer)
    choices = rand.sample(answers, 3)
    choices.append(answer)
    choices = shuffle(choices)
    print(choices)
    return choices

def check_choose_answer(answer,choices,score):
    player_answer = int(input("Choose from 1-4: "))
    if choices[player_answer -1]== answer:
        print("correct")
        score += 1
        return score 
    else:
        print("incorrect")
        return score

#Check player started game 
while start_game() == False:
    if start_game() == True:
        print("Try again")

#Score question and total questions
question_num = 0
score = 0
no_questions = 7
print(f"hello, i have {no_questions} questions")
#Loop for listing each question
while question_num < no_questions:
    question_num += 1
    print("Question " + str(question_num))
    question = select_print_question(questions)
    answer = find_answer(question)
    choices = print_choices(answers, answer)
    score = check_choose_answer(answer,choices,score)
    print("Score: " + str(score) + "\n")

#Print final score
print ("Final Score: " + str(score) + "/" + str(no_questions))