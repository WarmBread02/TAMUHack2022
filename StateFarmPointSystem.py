import numpy as np
import ast
from ctypes import pointer
import csv



#Up to 1000 
points = 0

def medicalSeverity(medSevere):
    global points
    #Medical Severity (0 to 10)
    if(medSevere == 0):
        points += 200
    elif(medSevere == 1):
        points += 200
    elif(medSevere == 2):
        points += 150
    elif(medSevere == 3):
        points += 125
    elif(medSevere == 4):
        points += 100
    elif(medSevere == 5):
        points += 75
    elif(medSevere >= 6):
        points += 0

def prescriptionSeverity(presSev):
    global points
    if(presSev == 0):
        points += 100
    elif(presSev > 0 & presSev <= 3):
        points += 50
    elif(presSev > 3):
        points += 0


def smoker(smoke):
    global points
    #will read in data from input file
    if(smoke == 'No'):
        points += 100
    elif(smoke == 'Yes'):
        points += 0

def drugUse(use):
    global points
    #will read in data from input file
    if(use == 0):
        points += 100
    else:
        points += 0

def exercise():
    #bruh
    print('To be worked on.')


def drinkUse(drinkSev):
    global points
    #will read in data from input files
    #scale from 0 to 3 based on drinking usage
    # 1 - barely drink if not at all
    # 2 - sometimes drink
    # 3 - recreational drinker (3 or more times a week)
    if(drinkSev == 1):
        points += 50
    elif(drinkSev == 2):
        points += 25
    elif(drinkSev == 3):
        points += 0


def jobType():
    global points
    #will most likely need to be coupled with exercise and age later
    job = 'Unemployed'
    if(job == 'Unemployed'):
        points += 0
    elif(job == 'Indoors'):
        points += 100
    elif(job == 'Outdoors'):
        points += 100

def drivingRecord(drivingScale):
    global points
    #will read in data from input file
    if(drivingScale == 0):
        points += 100
    elif(drivingScale >= 1):
        points += 0


def age(age):
    global points
    if((age >= 0) & (age <= 17)):
        points += 100
    elif((age >= 18) & (age <= 22)):
        points += 70
    elif((age >= 23) & (age <= 34)):
        points += 50
    elif((age >= 35) & (age <= 49)):
        points += 70
    elif(age >= 50):
        points += 25

def body_mass_index(weight, height):
    global points
    bmi = weight / height** 2 * 703
    if bmi < 18.5:
        points += 0
    elif bmi < 25:
        points += 80
    elif bmi < 30:
        points += 0
    else:
        points += 0


def criminalRecord(crime):
    global points
    if(crime == 0):
        points += 50
    else:
        points += 0


def familyConditions(familySev):
    global points
    #will be read in as "How severe is your family's health conditions if there are any?"
    if(familySev >= 0 & familySev <= 3):
        points += 100
    else:
        points += 0


def gender(sex):
    global points
    if(sex == 'Female'):
        points += 50
    if(sex == 'Male'):
        points += 30


def hobbies(hobbyDanger):
    global points
    if(hobbyDanger >= 0 & hobbyDanger <= 3):
        points += 30
    else:
        points += 0

def positivity(term):
    global points
    points+=term

def negativity(term):
    global points 
    points-=term

def neutrality(term):
    global points
    points+=term/2

def insuranceType(term):
    #this will be separate from the point scale
    #long term will have a lower discount than short term as a base factor
    baseDiscount = 0
    if(term == 'Short'):
        baseDiscount = 2 #in terms of percent
    else:
        baseDiscount = 0.5 #in terms of percent
    return baseDiscount

def discountRate(points, baseDiscount):
    discount = 0 #in terms of percent
    if(points > 500):
        discount += 12
    elif(points > 400):
        discount += 10
    elif(points > 300):
        discount += 7
    elif(points > 200):
        discount += 5
    
    discount += baseDiscount

    return discount    


def PointDeterminate(filename):
    with open(filename+'.csv', mode = 'rt') as file:
        csvreader = csv.reader(file)
        line_count = 0
        for row in csvreader:
            if(line_count == 0):
                print(f'Records are shown as: {", ".join(row)}')
                line_count += 1
            else:
                #name, smoke, medicalRecord, drugUse, prescriptions, drinkUse, drivingRecord, age, weight, height, criminalRecord, familyConditions, gender, hobbies, insuranceType
                print('Name:', row[0])
                smoker(row[1])
                medicalSeverity(int(row[2]))
                drugUse(row[3])
                prescriptionSeverity(int(row[4]))
                drinkUse(int(row[5]))
                drivingRecord(int(row[6]))
                age(int(row[7]))
                body_mass_index(float(row[8]), float(row[9]))
                criminalRecord(int(row[10]))
                familyConditions(int(row[11]))
                gender(row[12])
                hobbies(int(row[13]))
                negativity(row[14])
                positivity(row[15])
                neutrality(row[16])

                print("Points are:", points)
                print("Discount Rate:", discountRate(points, insuranceType(row[14])),'%')
                if(points > 100):
                    print("Eligible for discount: Yes")
                else:
                    print("Eligible for discount: No")
                
                points = 0

                line_count += 1






