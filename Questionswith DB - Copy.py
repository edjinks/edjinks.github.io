import random
import sqlite3
import time
time = time.strftime('%Y-%m-%d %H:%M:%S')
print(time)

connection = sqlite3.connect("scores.db")#coneects to existing database or creates on if it does not exist

cursor = connection.cursor()#cursor allowsinteraction with the database
while True:#Finds out what class the user is in, loops if an invalid class name is entered
    group = input("What class are you in? ")
    if  group =="class_1" or group=="class_2" or group=="class_3":
        break
    else:
        print ("Invalid class, follow syntax class_X")
        continue   

def addition():#generates a random addition question, checks answer and outputs a correct answer
    a = random.randint(10, 100)#chooses a random number between 10 and 100
    b = random.randint(10, 100)
    while True:#loop to ensure the user enters a valid input
        try:
            x = int(input("What is "+str(a)+" + "+str(b)+"? "))
        except ValueError:#if a number is not entered the program will loop and reask te question
            print ("Invalid Answer")
            continue
        else:
            break
    if x == a + b:
        print ("Correct")
        return 1#adds a point to the score total
    else:
        print ("Incorrect,the answer was",a + b,)#outputs the correct answer
        return 0#doesnt add a point to the score table

def subtraction():#generates a random subtraction question, checks answer and outputs a correct answer
    a = random.randint(2, 50)
    b = random.randint(1, 49)
    while b > a:#ensures the answer wont be negative
        b = random.randint(1, 49)
    while True:
        try:
           x = int(input("What is "+str(a)+" - "+str(b)+"? "))     
        except ValueError:
            print ("Invalid Answer")
            continue
        else:
            break      
    if x == a - b:
        print ("Correct")
        return 1
    else:
        print ("Incorrect,the answer was",a - b,)
        return 0

def multiplication():
    a = random.randint(1, 12)#only asks questions from 1-12 times tables
    b = random.randint(1, 12)
    while True:
        try:
            x = int(input("What is "+str(a)+" x "+str(b)+"? "))
        except ValueError:
            print ("Invalid Answer")
            continue
        else:
            break    
    if x == a * b:
        print ("Correct")
        return 1
    else:
        print ("Incorrect,the answer was",a * b,)
        return 0

def questionpicker():#chooses which type of question should be asked, runs quiz
    name = input("What is your name? ")      
    print ("Hello",name, "from",group)
    name = name.upper()#capitalises name for continuity
    y = 1
    score = 0
    while y <= 10:#loops for 10 questions
        x = random.randint(1, 3)
        print (str(y)+")")#question number eg 1)
        if x == 1:
            score=score+ addition()
        if x == 2:
            score=score+ subtraction()
        if x == 3:
            score=score+ multiplication()
        y = y + 1
        if y == 11:
            break    
    total = score
    print("Total Score: "+str(total)+"/10")#Total score        
    cursor.execute("CREATE TABLE IF NOT EXISTS class_1 (NAME CHAR(10), TOTAL INT, DATE DATETIME)")#creates 3 tables, one for each class to store name and score.
    cursor.execute("CREATE TABLE IF NOT EXISTS class_2 (NAME CHAR(10), TOTAL INT, DATE DATETIME)")
    cursor.execute("CREATE TABLE IF NOT EXISTS class_3 (NAME CHAR(10), TOTAL INT, DATE DATETIME)")
    cursor.execute("INSERT INTO "+group+" (name, total, date)VALUES ((\""+name+"\"), %d, '%s')"%(total, time))#inserts the data

def HighestScore():#lists highest score of each person, alphabetically
    datastruct = []
    allnames = []
    itr = cursor.execute("SELECT name FROM "+group+" GROUP BY name;").fetchall()#lists names in database
    for x in itr:   #makes a list of each nme in database with no duplicates     
        if x not in allnames:
            allnames.append(x[0])
        else:
            False
    allnames.sort()    
    for name in allnames:      #for every name in e database te highest score is found and added to a list
        cursor.execute("SELECT total FROM "+group+" WHERE (\""+name+"\") = NAME ORDER BY DATE DESC LIMIT 3;")#3 most recent scores
        scores =(cursor.fetchall())
        scores = [i[0] for i in scores]#turns tuples returned from database into integers
        x = 0        
        scores = sorted(scores)#sorts scores lowest to highest        
        datastruct.append ([name,scores[-1]])#adds name and highest score to datastruct
    a = int(input("Would you like to see \n 1)Alphabetically \n 2)Highest to lowest - "))
    if a == 1:
        for x in datastruct:#output each item in datastruct on a new line
            print (x)         
    elif a ==2:         
         for item in sorted(datastruct, key=lambda k:k[1], reverse = True):#sorts datastruct by highest score to lowest
              print("{},{}".format(item[0],item[1]))#output NAME, HIGHEST SCORE for ach person

def averagescore():#Lists average score, highest to lowest
    allnames = []
    datastruct = []
    itr = cursor.execute("SELECT name FROM "+group+" GROUP BY name;").fetchall()#lists names in database
    for x in itr:   #makes a list of each nme in database with no duplicates     
            allnames.append(x[0])
    
    allnames.sort()
    avg = 0
    for name in allnames:        
        cursor.execute("SELECT total FROM "+group+" WHERE (\""+name+"\") = NAME ORDER BY DATE DESC LIMIT 3;")#3 most recent scores
        scores =(cursor.fetchall())         
        scores = [i[0] for i in scores] #turns tuples from database into integers       
        avg = sum(scores)/len(scores)
        datastruct.append ([name,avg,scores])
        avg = 0    
    for item in sorted(datastruct, key=lambda k: k[1], reverse=True):
        print("{}'s avg is: {}. From (up to 3) most recent scores which were: {}".format(item[0], item[1], item[2]))

def scoreviewer():#lets the user choose which scoreboard to view
    b = 1
    while b == 1:
        a = int(input("What would you like to see \n 1) Averages or \n 2) Highest score? - "))
        if a == 1:
            averagescore()
            b = int(input("Would you like to 1) See More 2) Exit"))
        if a == 2:
            HighestScore()
            b = int(input("Would you like to 1) See More 2) Exit "))    

choice = int(input("Would you like to \n 1) Do the quiz \n 2) See the scoreboards? -  "))
if choice == 1:
    questionpicker()
elif choice == 2:
    scoreviewer()
    
connection.commit()#saves the changes
connection.close()#closes the connection
