import re

amountCon = int(input("Amount of constraints 2-4: "))

#INPUT
variable = ['x', 'y', 'z', 'r', 's', 'value']
if amountCon == 3:
   variable = ['x', 'y', 'z', 'r', 's', 't', 'value']
if amountCon == 4:
   variable = ['x', 'y', 'z', 'r', 's', 't', 'u', 'value']


pcolumn = 0
prow = ''
prowname = ''
previousProw = []
previousPcolumn = []

bvn = ['r', 's']
nbvn = ['r', 's']

if amountCon == 3:
   nbvn = ['r', 's', 't']
   bvn = ['r', 's', 't']
if amountCon == 4:
   nbvn = ['r', 's', 't', 'u']
   bvn = ['r', 's', 't', 'u']
   
p = input("Input objective function e.g P = 5x + 4y - 3z, as 5, 4, -3 ")
p = p.split(',')
i = 0
for x in p:
   p[i] = int(x)*-1
   i = i + 1
k = 0
j = amountCon+1
while k < j:
    p.append(0)
    k= k+1

def inputInt():
    print ("Enter constraint coefficients in format ",variable)
    constraint = input()
    constraint = constraint.split(',')
    i = 0
    for x in constraint:
       constraint[i] = int(x)
       i = i + 1
    return constraint

r = inputInt()
s = inputInt()

if amountCon >= 3:
   t = inputInt()
   
   if amountCon == 4:
      u = inputInt()


#CALCULATION
#checks to see if any negatives in p row

lastt = float("inf")
lastu = float("inf")


count = 0
for x in p:
    if x < 0:
        count = count+1
if count > 0:
    negatives = True
else:
    negatives = False
loop = 0

#finds optimal solution
while negatives is True:
    

    previousProw.append(prowname)
    previousPcolumn.append(pcolumn)
    i = 0
    temp = 0
    
    #finds pivot column by finding most negative value
    for x in p:
        if p[i] < temp:
            temp = p[i]
            pcolumn = i
        i = i+1
    
    #finds pivot row by finding smallest positive value
    if r[pcolumn] !=0:
        lastr = r[-1]/r[pcolumn]
        if lastr <= 0:
            lastr = float("inf")
    else:
        lastr = float("inf")
        
    if s[pcolumn] !=0:
        lasts = s[-1]/s[pcolumn]
        if lasts <= 0:
            lasts = float("inf")
    else:
        lasts = float("inf")

    if amountCon >= 3:
       if t[pcolumn] !=0:
           lastt = t[-1]/t[pcolumn]
           if lastt <= 0:
               lastt = float("inf")
       else:
           lastt = float("inf")
           
       if amountCon == 4:
          if u[pcolumn] !=0:
              lastu = u[-1]/u[pcolumn]
              if lastu <= 0:
                  lastu = float("inf")
          else:
              lastu = float("inf")

    
    if lastr<lasts and lastr<lastt and lastr<lastu and lastr>0:
        prow = r
        prowname = 'r'
        otherrow = s
        if amountCon >= 3: 
           otherrow2 = t
           if amountCon == 4: 
              otherrow3 = u

    elif lasts<lastr and lasts<lastt and lasts<lastu and lasts>0:
        prow = s
        prowname = 's'
        otherrow = r
        if amountCon >= 3: 
           otherrow2 = t
           if amountCon == 4: 
              otherrow3 = u
        
    elif amountCon >= 3:       
       if lastt<lastr and lastt<lasts and lastt<lastu and lastt>0:
           prow = t
           prowname = 't'
           otherrow = r
           otherrow2 = s
           if amountCon ==4:
              otherrow3 = u

       if amountCon == 4:
          if lastu<lastr and lastu<lasts and lastu<lastt and lastu>0:
              prow = u
              prowname = 'u'
              otherrow = r
              otherrow2 = s
              otherrow3 = t
        
    else:
       print("ERROR values are",lastr,lasts)
       if amountCon >= 3:
          print(lastt)
          if amountCon == 4:
             print(lastu) 
       
    #divides pivot row by pivot value    
    i = 0
    pivot = prow[pcolumn]
    
    for x in prow:
        prow[i] = prow[i]/pivot
        i = i+1

    #changes basic variable to pivot column variable
   
    bvnpos = nbvn.index(prowname)
    bvn.pop(bvnpos)    
    bvn.insert(bvnpos, variable[pcolumn])
   
   
    #removes variable from other row i.e make pcolumn 0
    multiple = otherrow[pcolumn]/prow[pcolumn]
    i = 0

    for x in otherrow:
        otherrow[i] = otherrow[i] - (multiple*prow[i])
        i = i+1
   
    #removes variable from other row2 i.e make pcolumn 0
    if amountCon >= 3:
      
       multiple = otherrow2[pcolumn]/prow[pcolumn]
       i = 0

       for x in otherrow2:
           otherrow2[i] = otherrow2[i] - (multiple*prow[i])
           i = i+1

       #removes variable from other row3 i.e make pcolumn 0
       if amountCon == 4:
          multiple = otherrow3[pcolumn]/prow[pcolumn]
          i = 0

          for x in otherrow3:
              otherrow3[i] = otherrow3[i] - (multiple*prow[i])
              i = i+1

    #removes variable from p row i.e make pcolumn 0
    
    multiple = p[pcolumn]/prow[pcolumn]
    i = 0

    for x in p:
        p[i] = p[i] - (multiple*prow[i])
        i = i+1
    loop = loop + 1
    #negative reevaluation
    count = 0
    for x in p:
        if x < 0:
            count = count+1
    if count > 0:
        negatives = True
    else:
        negatives = False
        
print (bvn[0]," = ", r[-1])
print (bvn[1]," = ", s[-1])
if amountCon >= 3:
   print(bvn[2]," = ", t[-1])
   if amountCon == 4:
      print(bvn[3]," = ", u[-1])
print("P = ", p[-1])
    
