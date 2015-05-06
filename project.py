# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 22:50:05 2015

@author: Mohammad Omar
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import csv


Businesses={}
Reviews={}
Tips={}
users={}




#################################################################################
#################################################################################
######################      DEALING WITH USERS     ##############################
#################################################################################
#################################################################################

print("We want to find if a particular user has vaid reviews, meaning whether the user is credible or not")
print("So basically one particular user has these attributes:"+
"\naverage_stars\nfriends\ntype\nreview_count\nelite\nvotes"+
"\ncompliments\nuser_id\nyelping_since\nfans\nname")
print("Based on votes(democaracy) we will figure out if a particular user has credibility.")
print("votes have three categories: funny, useful and cool. Cool and funny are often used interchangebly,\n")
print("so we will focus mostly on useful. Thereofre if the useful votes are greater than the otyher two combined\n"+
"and there atleast  50 useful votes only then the user can be classified as credible.")
print("After looing at the data, one more criteria has to be mat and that is the user must have an average star rating\n"+
"of greater trhan 4.5.")


file=open('yelp_academic_dataset_user.json','r')

userList = []     
userName= []
userRatings=[]        

    
 
filestrings=file.readlines()

countUser=0
for line in filestrings:
    countUser=countUser+1
    filedic=json.loads(line)
    userDict= {} 
    
    
    for i in filedic:
       if i == 'votes':
           total = filedic[i]['funny'] + filedic[i]['cool']
           useful = filedic[i]['useful']    
       elif i == 'average_stars':
           stars = filedic[i]
       elif i == 'user_id':
           user_id = filedic[i]
       else:
           continue
    if useful > total and useful > 50 and stars >= 4.5:
        userDict['user_id'] = user_id
        userDict['useful'] = useful
        userDict['average_stars'] = stars
        users[countUser] = userDict
    

print(users)
print("\n")
print("#########################################################################")
print("##############   printing the graph of the number of users ##############")
print("##############      and where they currently stand      #################")
print("#########################################################################")

N = countUser
x = np.random.rand(N)
y = np.random.rand(N)

plt.scatter(x, y)
plt.show()


file.close()  
# print(filedic.keys())


#################################################################################
#################################################################################
####################      DEALING WITH BUSINNESS     ############################
#################################################################################
#################################################################################

#The business has the following attributes:
#     city type name review_count open hours attributes categories stars neighborhoods 
#     business_id longitude latitude state full_address 


file=open('yelp_academic_dataset_business.json','r')

filestrings=file.readlines()
bussNames = []
bussCities = []
bussAddress = []
bussStates = []
countBuss=0
for line in filestrings:
    countBuss = countBuss+1
    filedict=json.loads(line)
    for i in filedict:
        if i == 'stars':
            star =  filedict[i]
        elif i == 'name':
            name = filedict[i]
        elif i == 'open':
            bOpen = filedict[i]
        elif i == 'city':
            city = filedict[i]
        elif i == 'full_address':
            address = filedict[i]
        elif i == 'state':
            state = filedict[i]
        else:
            continue
    if star > 3 :
        bussNames.append(name)
        bussCities.append(city)
        bussAddress.append(address)
        bussStates.append(state)
    countBuss += 1 
       
print("The most popular Businesses are(based on attributes):")
i = 0
length = len(bussCities)
print(length)
while i < length:
    print("name:",bussNames[i],"  address: ", bussAddress[i], "  city: "+   bussCities[i], "state: ",bussStates[i])
    i+=1

print()
print()
print("Plotting the graph of most popular businesses")
N = length
x = np.random.rand(N)
y = np.random.rand(N)

plt.scatter(x, y)
plt.show()


file.close()  

#for i in filedic:
 #   print(i)
#for keys, values in users.items():
 #   print(keys, values)

# print(filedic.keys())

# print(filedic.keys())


'''
#################################################################################
#################################################################################
#######################     DEALING WITH TIPS     ###############################
#################################################################################
#################################################################################

file=open('C:\\Users\\Mohammad Omar\\Desktop\\DataMiningCSE4331\\yelp_dataset_challenge_academic_dataset\\yelp_dataset_challenge_academic_dataset\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_business.json','r')

filestrings=file.readlines()

countUser=0
for line in filestrings:
    countUser=countUser+1
    filedic=json.loads(line)
    users[countUser] = filedic
    if countUser == 2:
        break

print(users)

for keys, values in users.items():
    print(keys, values)
file.close()  
# print(filedic.keys())



#################################################################################
#################################################################################
######################     DEALING WITH Reviews     #############################
#################################################################################
#################################################################################




file=open('C:\\Users\\Mohammad Omar\\Desktop\\DataMiningCSE4331\\yelp_dataset_challenge_academic_dataset\\yelp_dataset_challenge_academic_dataset\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_business.json','r')

filestrings=file.readlines()

countUser=0
for line in filestrings:
    countUser=countUser+1
    filedic=json.loads(line)
    users[countUser] = filedic
    if countUser == 2:
        break

print(users)

for keys, values in users.items():
    print(keys, values)
file.close()  
# print(filedic.keys())




#################################################################################
#################################################################################
#######################     DEALING WITH CHECKINS    ############################
#################################################################################
#################################################################################


file=open('C:\\Users\\Mohammad Omar\\Desktop\\DataMiningCSE4331\\yelp_dataset_challenge_academic_dataset\\yelp_dataset_challenge_academic_dataset\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_business.json','r')

filestrings=file.readlines()

countUser=0
for line in filestrings:
    countUser=countUser+1
    filedic=json.loads(line)
    users[countUser] = filedic
    if countUser == 2:
        break

print(users)

for keys, values in users.items():
    print(keys, values)
file.close()  
# print(filedic.keys())










# for keys, values in users.items():
    #    print(keys, values)
   
   # print(filedic.keys())











   
writer = csv.writer(open('dict.csv', 'wb'))
for key, value in mydict.items():
   writer.writerow([key, value])
    #if filedic[user_id]>3:#count%1000==0:#
#print(filedic)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   for i in filedic:
        if i == 'average_stars':
            print(i, ": ",filedic[i])
        elif i == 'friends':
            print(i, ": ",filedic[i])
        elif i == 'type':
            print(i, ": ",filedic[i])
        elif i == 'review_count':
            print(i, ": ",filedic[i])
        elif i == 'elite':
            print(i, ": ",filedic[i])
        elif i == 'votes':
            print(i, ": ",filedic[i])
        elif i == 'compliments':
            print(i, ": ",filedic[i])
        elif i == 'user_id':
            print(i, ": ",filedic[i])
        elif i == 'yelping_since':
            print(i, ": ",filedic[i])
        elif i == 'fans':
            print(i, ": ",filedic[i])
        else:
            print(i, ": ",filedic[i])
'''
