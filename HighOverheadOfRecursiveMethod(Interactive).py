# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 07:30:31 2020

@author: Yehuda Peiser
"""


''' 
Fibonnacci sequence
Objective:
To demonstrate the high overhead of the recursive method 
compared to the List-Iterative and Non-List-Iterative methods.

Pseudo Code:
Begin the sequence with 0,1, ... and then calculate each successive number from 
the sum of the previous two.
fibRec(n) = fibRec(n-1)  + fibRec(n-2) whre n is  the index in the Fibonacci sequence.
'''


def Greeting(msg,main=True) :
    '''msg = string
       main = Main messages will have long string of hyphens on each side and above and below
    '''
    if main:
        print("-"*len(msg)*2); print("-"*(len(msg)//2), msg ,"-"*(len(msg)//2)) ;print("-"*len(msg)*2)
    else:
        print('-'*5,msg,'-'*5)


'''Recursive method'''

def fibRec(indx):
    global IwasInRecursion
    IwasInRecursion +=1
    
    if indx == 0:
        return 0
    elif indx == 1:
        return 0
    elif indx == 2:
        return 1
    else:
        return fibRec(indx-1)+fibRec(indx-2)



'''Iterative method'''

'''
Make a Lsit
add a list item  to the list. The loop is merely a counter and a stop. The 
value of new item is a simple function of L[n-1]+L[n-2]
When loop is finished return last value in teh List.
'''

def fibIter(indx):
    L = []
    for n in range(0,indx+1):
        if n == 0 :
            L.append(0)
        elif n == 1:
            L.append(0)
        elif n == 2 :
            L.append( 1)
        else:
            L.append(L[n-1] + L[n-2])
    return L[n]


def fibIterNoList(indx):
    ''' Just using a few variables in loop '''
    if indx ==1:
        return 0
    elif indx ==2:
        return 1
    else:
        prev2 = 0
        prev1 = 1
        new = prev1+prev2
        for n in range(3,indx):
            prev2 = prev1
            prev1 = new
            new = prev1+prev2
        return new
    
    
def elaps(sTime, Machine)    :
    ''' Calc & Print time elapsed for the operation 
        Also to compile a dictionary of durations per calculation method'''
        
    elapsTime = (datetime.datetime.now() - sTime).total_seconds()
    print("        Total time elapsed for operation", elapsTime, " seconds." )    
    scores[Machine][indx]= elapsTime

def userMachineSelection():
    global MachineType
    '''The user selects the method of calculation.'''
    print('--'*35+'--------------------------')    
    MachineType = input("We have 3 machines to calculate Fibonacci values. \n\
                        Please choose which calculator-machine you would like to use.  \n\
                        (Thereafter you will be asked to provide the index \n\
                         number for the Fibonacci sequence value you would like.) \n\
    \n\
             *R*ecursive Machine \n\
             *I*terative Machine (using lists) \n\
             *N*on-List Iterative Machine (using dummy variables only, no lists) \n\
    \n\
             *A*ll the above machines  \n\
             \n\
                     *V*iew comparative DURATION values from this session \n\
    \n\
              Which machine/option would you like? \n\
                  - Enter R / I / N / A / V \n\
                     (or Q to quit the program)>" )
    if len(MachineType) >1 or MachineType not in "qQrinRINAavV" :
        print('Faulty input.')
        if not Continue():
            MachineType = 'Q';
            return MachineType
        return userMachineSelection()
    else:
        MachineType = MachineType.upper() # The 'try' statement in the main program as at play here
        return MachineType


def CallRecurs():
    global Indx, IwasInRecursion
    flag = 1
    if indx >34:
        proceed = input(str("For the Resursive Machine, the index "+ str(indx)+" you have chosen is a pretty high index.\n\
                         An index of 45 for example will typically take over 11 minutes to calculate (and 35 can be like 8 seconds).\n\
                         Would you like to continue neverless? (Y/N)>"))
        if not proceed.upper() =='Y':
            flag = 0                
    if flag == 1: # indx is under 35 or it's over 35 and the user nevertheless confirmed
        start = datetime.datetime.now()
        print("*R*ecursive Machine output for Fibonacci index ", indx, "is", fibRec(indx))
        elaps(start, "R")
        print("                     And the number of recursions -",IwasInRecursion)
        IwasInRecursion = 0

def CallIter():
    start = datetime.datetime.now()
    print("*I*terative Machine output for Fibonacci index ", indx, "is", fibIter(indx))  
    elaps(start, "I")    

def CallNonList():
    start = datetime.datetime.now()
    print("*N*on-List Iterative Machine output for Fibonacci index ", indx, "is", fibIterNoList(indx))
    elaps(start, "N")

def userIndexSelect():
    global indx, MachineType
    indx = int(input("Enter the index of the Fibonacci number you want (or any letter to quit):>"))
    if   MachineType == 'R':
        CallRecurs()
    elif MachineType == 'I':
        CallIter()
    elif MachineType == "N":
        CallNonList()
    elif MachineType == 'A':
        CallRecurs()
        CallIter()
        CallNonList()
    elif MachineType == 'V':
        results()       
    else:
        print('Debugging:',MachineType)
    
def results():
    ''' Print comparative figures '''
    #Rename abrevioations for meaningful headers in output
    try:
        scores['Recursion']=scores.pop('R')
        scores['Iterative']=scores.pop('I')
        scores['Non-List_Iterative']= scores.pop('N')
    except:
        print('No new values were calculated')
    Greeting("Calculation times (in seconds)",False)
    df= pd.DataFrame(scores)
    print(df)
    # Put abbreviations back
    try:
        scores['R']=scores.pop('Recursion')
        scores['I']=scores.pop('Iterative')
        scores['N']= scores.pop('Non-List_Iterative')
    except:
        print('see "results" function - during replacing key names.') # debug statement
    
    
def Continue():
    try:
        return 'Y' == input('Would you like to continue using these machines (y/n)?').upper()
    except:
        return False
    else:
        return False
    
    
'''Program Start'''
import datetime
import pandas as pd  #Panda DataFrames for visual effect



Greeting("Welcome to the Tri-Calculator Fibonacci Machines")
Greeting("This program primarily COMPARES the durations of the calculation types you choose",False)
Greeting('The objective is to display the inefficiency of the otherwise acclaimed Recursive Method',False)


scores={ 'R': {1:0},
         'I': {1:0},
         'N': {1:0}
         }
IwasInRecursion = 0

indx = 0
MachineType = 'R'
while MachineType.upper() != 'Q' : #"VvRrIiNnAa": 
    try:
        MachineType = userMachineSelection()
    except: # Not alpha
        print('\n\n\n User chooses an option other than the ones provided. User chooses to quit program.')
        break
    if   MachineType == 'Q' :  # not in "rinRINAa":
        print('User chooses to quit program.')
        break
    elif MachineType == 'V' :
        results()             
        if not Continue():
            break
        else:
            continue
        
    try:
        indx = userIndexSelect()
    except:
        print('A non-integer (or negative number) entered. User chooses to quit.')
        break
        
    if not Continue():
        break


Greeting('Upon closing...',True)
Greeting(' We provide you with durations of calculation results from this session.',False)    
results()
Greeting("Thank you for using the Fibonacci Tri-Calculator Fibonacci Machines")

