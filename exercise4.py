import sys

name = input('Enter your name: ')
print("Hello",name)



# Exercise 3.2
hour = 0
rate = 0
pay =0

hr = input('Enter Hours: ')
rt = input('Enter Rate: ')
try:
    hour = float(hr)
    rate = float(rt)
except:
    print('Error, please enter numeric input')
    sys.exit()
    
if hour > 40:
    pay = hour*rate + (hour-40)*rate*0.5
else:
    pay = hour * rate
    
print('Pay:',pay)



# Exercise 3.3
score = 0.0
grade = ''

inp = input('Enter score: ')
try:
    score = float(inp)
except:
    print('Bad score')
    quit()

'''
for float number-use "and"/"or"
 & and / are for integers
'''
# if 0.0 <= score <= 1.0:
if 0.0 <= score and score <= 1.0:
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
        
print(grade)


# Exercise 4.6
def computepay(hour, rate):     
    if hour > 40:
        pay = hour*rate + (hour-40)*rate*0.5
    else:
        pay = hour * rate        
    return pay


hr = input('Enter Hours: ')
rt = input('Enter Rate: ')

hour = float(hr)
rate = float(rt)
    
pay=computepay(hour, rate)
    
print('Pay:',pay)


# Exercise 4.7
def computegrade(score):     
    if 0.0 <= score and score <= 1.0:
        if score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7:
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        else:
            grade = 'F'     
    return grade

inp = input('Enter score: ')
try:
    score = float(inp)
except:
    print('Bad score')
    sys.exit()
    
print(computegrade(score))
        
print(computegrade(0.96))




