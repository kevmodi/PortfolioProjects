#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator
# https://mercer-health.com/services/weight-management-center/bmi-calculator#:~:text=Body%20Mass%20Index%2C%20or%20BMI,inches%20x%20height%20in%20inches
# 
# 

# #BMI = (weight in pounds x 703) / (height in inches x height in inches)

# Under 18.5: Underweight
# 
# 18.5 - 24.9: Normal Weight
# 
# 25 - 29.9: Overweight
# 
# 30 - 34.9: Obese
# 
# 35 - 39.9: Severely Obese
# 
# 40 and over: Morbidly Obese

# In[4]:


name = input("Please enter your name: ")
weight = input("Please enter your weight in pounds: ")
height = input("Please enter your height in inches: ")
weight = float(weight)
height = float(height)
BMI = (weight*703)/(height*height)
print("Your BMI is " + str(BMI))



# In[5]:


if BMI>0:
    if BMI<=18.5:
        print(name +", you are underwight.")
    elif BMI<=24.9 and BMI>18.5:
        print(name +", you are normal weight.")
    elif BMI<=29.9 and BMI>24.9:
        print(name +", you are overweight. You need to exercise more and stop sitting and writing so many python tutorials.")
    elif BMI<=34.9 and BMI>29.9:
        print(name +", you are obese.")
    elif BMI<=39.9 and BMI>34.9:
        print(name +", you are severely obese.")
    elif BMI >=40:
        print(name +", you are morbidly obese.")
else:
    print("Enter valid input")

