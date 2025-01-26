import random, pickle
import numpy as np

welcomeMessage = '''Welcome to Homework 1!
    This homework is designed to test your understanding of Python basics.
    Please answer the questions in the homework by filling in the variables q1, q2, etc.
    Each time you fill in a variables, run the saveResults() function to save your answers.
    Good luck!'''
xData = [100*random.random() for i in range(20)]
number = 5+random.randint(8,20)
fruit = 'apples'
day = 'Saturday'
string_4 = 'An alacritous abalone accelerates along an alarming aquatic ascent.'
string_5 = 'A                       large space was here.'
string_6 = 'ATCGTGCATGCTGAGTGGCGAGCGGCGGCCGTACGCTGTTACTTAAAACGTAGCTGTAAAAAAC\
            GCTGCTGATGCTGTGCATGTGACTAGCTGCATGTGTGACTGACTGCTGACGTACTGTACGTACG\
            ATGGTTCGTGCGATGCGCTTGACGTGTCGTAGTGCATGCTGCTAGCTGATCGATGTGTCGAGTC'
nDigits = 6
nPower = 3
List10 = ['apples','bananas','pears','pears','blueberries','apples','strawberries']
Student_IDs = [1,2,3,4,5]
Student_names = ['Jim','John','Jenna','Jamal','Jaden']
List12 = [1,2,3,4,5,6,7,8]

q1 = 'xxx'
q2 = 'XXX'
q3 = 'XXX'
q4 = 123
q5 = 'XXX'
q6 = 123
q7 = 'XXX'
q8 = 1.23
q8 = 'xxx'
q9 = 'xxx'
q10 = List10
q11 = 'xxx'
q12 = [1,2,3,4,5,6,7,8]

fnDat = 'Hwk1Data.pkl'
dataDict = {'xData':xData,'number':number,'fruit':fruit,'day':day,'string_4':string_4,
    'string_5':string_5,'string_6':string_6,'nDigits':nDigits,'nPower':nPower,
    'Student_IDs':Student_IDs,'Student_names':Student_names,'List10':List10,'List12':List12}
with open(fnDat, 'wb') as file:
    pickle.dump(dataDict, file)

answerDict = {'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5,'q6':q6,'q7':q7,'q8':q8,
                'q9':q9,'q10':q10,'q11':q11,'q12':q12}

def saveResults(qs,ans):
    fn = 'Hwk1Answers.pkl'

    #Update answerDict
    answerDict.update({qs:ans})

    with open(fn, 'wb') as file:
        pickle.dump(answerDict, file)

    #Read and print 
    with open(fn, 'rb') as file:
        loaded_dict = pickle.load(file)
    
    print("Your answers so far are:")
    print(loaded_dict)