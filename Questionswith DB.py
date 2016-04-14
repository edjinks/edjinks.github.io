import random
import sqlite3
import time
time = time.strftime('%Y-%m-%d %H:%M:%S')
print(time)

connection = sqlite3.connect("scores.db")#coneects to existing database or creates on if it does not exist

cursor = connection.cursor()#cursor allowsinteraction with the database

name = input("What is your name? ")
name = name.upper()

while True:#Loops if an invalid clas name is entered
    group = input("What class are you in? ")
    if  group =="class_1" or group=="class_2" or group=="class_3":
        break
    else:
        print ("Invalid class, follow synatx class_X")
        continue
  
print ("Hello",name, "from",group)
def addition():
    a = random.randint(10, 100)
    b = random.randint(10, 100)
    while True:#loop to ensure the user enters a valid input
        try:
            x = int(input("What is "+str(a)+" + "+str(b)+"? "))
        except ValueError:
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

def subtraction():
    a = random.randint(2, 50)
    b = random.randint(1, 49)
    while b > a:
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
    a = random.randint(1, 12)
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

def questionpicker():#chooses which type of question should be asked
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
    return score
total = questionpicker()
print("Total Score: "+str(total)+"/10")#Total score

    
cursor.execute("CREATE TABLE IF NOT EXISTS class_1 (NAME CHAR(10), TOTAL INT, DATE DATETIME)")#creates 3 tables, one for each class to store name and score.
cursor.execute("CREATE TABLE IF NOT EXISTS class_2 (NAME CHAR(10), TOTAL INT, DATE DATETIME)")
cursor.execute("CREATE TABLE IF NOT EXISTS class_3 (NAME CHAR(10), TOTAL INT, DATE DATETIME)")

cursor.execute("INSERT INTO "+group+" (name, total, date)VALUES ((\""+name+"\"), %d, '%s')"%(total, time))#inserts the data

def HighestScore():#lists highest score of each person, alphabetically
    datastruct = []
    allnames = []
    itr = cursor.execute("SELECT name FROM "+group+" GROUP BY name;").fetchall()#lists names in database
    for x in itr:
        
        if x not in allnames:
            allnames.append(x[0])
        else:
            False
    allnames.sort()
    for name in allnames:
        
        cursor.execute("SELECT total FROM "+group+" WHERE (\""+name+"\") = NAME ORDER BY DATE DESC LIMIT 3;")#3 most recent scores
        scores =(cursor.fetchall())
       scores = [i[0] for i in scores]
       x = 0
        for i in scores:
            if scores[x] >= i and len(scores) > 1:
                scores.remove(i)
                x = x+1
            else:
                x = x+1
        print(name,"s highest score = ",scores)

        datastruct.append ([name,scores])

    h = input("Would you like to see highest score, highest to lowest? (y/n)")#List highest score of each person, highest to lowest
    if h == 'y':
        
        for item in sorted(datastruct, key=lambda k:k[1], reverse = True):
            print("{},{}".format(item[0],item[1]))
    else:
        False
        
HighestScore()

def averagescore():#Lists average score, highest to lowest
    allnames = []
    datastruct = []
    itr = cursor.execute("SELECT name FROM "+group+" GROUP BY name;").fetchall()#lists names in database
    for x in itr:
        
        if x not in allnames:
            allnames.append(x[0])
        else:
            False
    allnames.sort()
    avg = 0
    number = 0

    for name in allnames:
        
        cursor.execute("SELECT total FROM "+group+" WHERE (\""+name+"\") = NAME ORDER BY DATE DESC LIMIT 3;")#3 most recent scores
        scores =(cursor.fetchall())     
        
        scores = [i[0] for i in scores]        
        avg = sum(scores)/len(scores)
        #print(name,"'s average is: ",avg,". From (up to) 3 most recent scores which were: ",scores,)
        
        datastruct.append ([name,avg,scores])
        avg = 0
    
    for item in sorted(datastruct, key=lambda k: k[1], reverse=True):
        print("{}'s avg is: {}. From (up to 3) most recent scores which were: {}".format(item[0], item[1], item[2]))

averagescore()

connection.commit()#saves the changes
connection.close()#closes the connection
