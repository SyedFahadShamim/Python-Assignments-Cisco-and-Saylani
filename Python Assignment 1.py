#!/usr/bin/env python
# coding: utf-8

# In[7]:


print("Twinkle, twinkle, little star, \n      How I wonder what you are! \n          Up above the world so high, \n          Like a diamond in the sky. \nTwinkle, twinkle, little star, \n      How I wonder what you are")


# In[9]:


import sys
print("Python version :" + sys.version)


# In[2]:


import datetime
Current_dateAndTime = datetime.datetime.now()
print("Date : " + Current_dateAndTime.strftime("%Y-%m-%d"))
print("Time : " + Current_dateAndTime.strftime("%I:%M:%S"))


# In[1]:


from math import pi
radius = float(input("Enter the value of Radius to Compute Area of Circle : "))
print("Area of circle: " + str(round( pi*(radius**2),2 )))


# In[4]:


FirstName = input("Enter your First Name :")
LastName = input("Now Enter your Last Name :")

print("Here is your Full name : " + FirstName +" "+ LastName)

reversedFirstName = ''.join(reversed(FirstName))
reversedLastName = ''.join(reversed(LastName))

print("And This is your Name in reversed Order : " + reversedFirstName +" "+ reversedLastName)


# In[6]:


print("Addition of two numbers")

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("Answer : " + str(num1+num2))


# In[ ]:




