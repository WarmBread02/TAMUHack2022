#import numpy as np
#import ast
#from ctypes import pointer
import csv
import names
import array as arr
from random import seed
from random import randint
from random import uniform
import random

from StateFarmPointSystem import criminalRecord, drivingRecord, insuranceType


choiceYN = ['Yes', 'No']
termChoice = ['Long', 'Short']
choiceG = ['Male', 'Female']


#name, smoke, medicalRecord, drugUse, prescriptions, drinkUse, drivingRecord, age, weight, height, criminalRecord, familyConditions, gender, hobbies, insuranceType
#John Smith, No, 5, Yes, 3, 2, 0, 21, 160, 6.0, 0, 2, Male, 1, Long
male_people = []
female_people = []

count = 0
for i in range(100):
    
    seed(count)
    rand_male = names.get_full_name(gender = 'male')
    person = []
    person.append(rand_male)

    #randint(0, 10) random number from 0 to 10
    person.append(random.choice(choiceYN))

    person.append(randint(0, 10))

    person.append(randint(0, 1))

    person.append(randint(0, 10))

    person.append(randint(0, 3))

    person.append(randint(0, 5))
    age_value = randint(0, 100)
    person.append(age_value)

    if((age_value >= 0) & (age_value <= 3)):
        person.append(randint(28, 33)) #weight
        person.append(uniform(1.0, 3.3)) #height
    elif((age_value >= 4) & (age_value <= 8)):
        person.append(randint(40, 57))
        person.append(uniform(3.4, 4.5))
    elif((age_value >= 9) & (age_value <= 12)):
        person.append(randint(60, 90))
        person.append(uniform(4.4, 5.0))
    elif((age_value >= 13) & (age_value <= 16)):
        person.append(randint(100, 134))
        person.append(uniform(5.0, 5.6))
    elif((age_value >= 17) & (age_value <= 20)):
        person.append(randint(140, 155))
        person.append(uniform(5.3, 6.5))
    elif((age_value >= 20) & (age_value <= 35)):
        person.append(randint(155, 200))
        person.append(uniform(5.3, 6.5))
    elif(age_value >= 36):
        person.append(randint(170, 220))
        person.append(uniform(5.3, 6.5))

    person.append(randint(0, 5))
    person.append(randint(0, 8))
    person.append('Male')
    person.append(randint(0, 5))
    person.append(random.choice(termChoice))
    male_people.append(person)
    count += 1

with open('testsMales.csv', 'w', newline= '') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(male_people)

count = 0
for i in range(100):
    
    seed(count)
    rand_female = names.get_full_name(gender = 'female')
    person = []
    person.append(rand_female)

    #randint(0, 10) random number from 0 to 10
    person.append(random.choice(choiceYN))

    person.append(randint(0, 10))

    person.append(randint(0, 1))

    person.append(randint(0, 10))

    person.append(randint(0, 3))

    person.append(randint(0, 5))
    age_value = randint(0, 100)
    person.append(age_value)

    if((age_value >= 0) & (age_value <= 3)):
        person.append(randint(28, 33)) #weight
        person.append(uniform(1.0, 3.3)) #height
    elif((age_value >= 4) & (age_value <= 8)):
        person.append(randint(40, 57))
        person.append(uniform(3.4, 4.5))
    elif((age_value >= 9) & (age_value <= 12)):
        person.append(randint(60, 90))
        person.append(uniform(4.4, 5.0))
    elif((age_value >= 13) & (age_value <= 16)):
        person.append(randint(100, 134))
        person.append(uniform(5.0, 5.6))
    elif((age_value >= 17) & (age_value <= 20)):
        person.append(randint(140, 155))
        person.append(uniform(5.3, 6.5))
    elif((age_value >= 20) & (age_value <= 35)):
        person.append(randint(155, 200))
        person.append(uniform(5.3, 6.5))
    elif(age_value >= 36):
        person.append(randint(170, 220))
        person.append(uniform(5.3, 6.5))

    person.append(randint(0, 5))
    person.append(randint(0, 8))
    person.append('Female')
    person.append(randint(0, 5))
    person.append(random.choice(termChoice))
    female_people.append(person)
    count += 1

with open('testsFemales.csv', 'w', newline= '') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(female_people)










