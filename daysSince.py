import datetime
sDate =  datetime.datetime.today()- datetime.datetime(2016,11,26) #put start date YYYY,MM,DD
eDate =  (datetime.datetime(2016,11,26) + datetime.timedelta(210)) - datetime.datetime.today() #210 = course length in days eg 7*30 = 210 for 7 month course
print "Days since start: {}".format(sDate)
print "Days until end: {}".format (eDate)
dTstrt = str(sDate)
dTstrt = dTstrt.split(" ")
dTstrt1 = int(dTstrt[0])
dTend = str(eDate)
dTend = dTend.split(" ")
dTend1 = int(dTend[0])
mgtaken = dTstrt1*60-(20*30) #dTstrt1 * DOSE/DAY - (difference in dose for first month before increase)
print mgtaken, "mg taken =", mgtaken/65, "mg/kg" #65 = weight in kg
print "End date = ", datetime.datetime(2016,11,26) + datetime.timedelta(210) #replace startdate and course length 
