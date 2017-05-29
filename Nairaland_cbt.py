# For Niaraland Programming Thread
# CBT stuff

import sys
import time
from time import *

def open_file(file_name, mode):
    """ Open the cbt.txt file. """
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Cannot locate the file", file_name, "Ending the program...", e)
        sleep(2)
        input("\n\nPress the enter key to exit. ")
        sys.exit()
    else:
        return the_file
    
def next_line(the_file):
    """This returns the next line from the cbt.txt file. """
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """This return the next block of data from the file. """
    category = next_line(the_file)
    question = next_line(the_file)

    answer = []
    for i in range(4):
        answer.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    return category, question, answer, correct

def subject_selector():
    print('please select the subject you want to start with\n')
    subject = str(input('enter A - for Arigultural Science\n'
                        'enter B - for Biology\n'
                        'enter M - for Mathematics\n'
                        'enter C - for Chemistry\n'
                        'enter P - for Physics\n'
                        'enter G - for Geography\n'
                        'enter Eng - for English\n'
                        'enter N - for Nairaland CBT\n:'))
    subject = subject.lower()
    choice_char = ["n"]

    while subject not in choice_char:
        print("Only the file for Niaraland CBT was created. Abeg No vex!")
        print("\nKindly select 'N' in the option")
        subject = str(input('\nenter A - for Arigultural Science\n'
                        'enter B - for Biology\n'
                        'enter M - for Mathematics\n'
                        'enter C - for Chemistry\n'
                        'enter P - for Physics\n'
                        'enter G - for Geography\n'
                        'enter Eng - for English\n'
                        'enter N - for Nairaland CBT\n:'))
    if subject == "n":
        welcome()
        
    

def welcome():
    """welcome  the student. """
    print("\t\tWElcome to the nairaland CBT Examination.\n")
    

def dmain():
    student_name = input("Enter your name to begin the test:")
    while not student_name:
        student_name = input("Enter your name to begin the test.")
    print(student_name, ", VERIFYING DETAILS...")
    sleep(2)

    subject_selector()
    start = time()
    cbt_file = open_file("cbt.txt", "r")
    title = next_line(cbt_file)
    score = 0

    #getting the first block
    category, question, answer, correct = next_block(cbt_file)
    while category:
        #the question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answer[i])

        #gettin the answer
        answer  = input("What is your answer?: ")

        #verify answer
        if answer == correct:
            score += 1
        else:
            score += 0

        #getting the next_block
        category, question, answer, correct = next_block(cbt_file)
    cbt_file.close()

    print("That was the last question!")
    stop = time()
    print("SUBMITTING...")
    sleep(2)
    print("Your Final score is", score, ", you used", stop - start, "seconds")
    
#Runniniggggggggggggggg
dmain()

input("\n\nPress the enter key to exit. ")

    
