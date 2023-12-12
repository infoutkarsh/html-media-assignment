#!/usr/bin/env python
# coding: utf-8

# Q1. Create a python program to sort the given list of tuples based on integer value using a 
# lambda function. 
# 
# 
# [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

# In[1]:


data = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

data.sort(key=lambda x: x[1])

for player, runs in data:
    print(f'{player}: {runs} runs')


#  Q2.Write a Python Program to find the squares of all the numbers in the given list of integers using 
# lambda and map functions.
# 
# 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# In[5]:


L=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=list(map(lambda x:x**2,L))
print(result)


# Q.3 Write a python program to convert the given list of integers into a tuple of strings. Use map and 
# lambda functions
# 
# 
# Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

# In[15]:


s=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=tuple(map(lambda x:str(x),s))
print(result)


# Q.5  Write a python program using reduce function to compute the product of a list containing numbers 
# from 1 to 25.

# In[18]:


from functools import reduce

lst = list(range(1, 26))
result = reduce(lambda x, y: x * y, lst)

print(result)


# Q6.Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the 
# filter function.
# 
# 
# [2, 3, 6, 9, 27, 60, 90, 120, 55, 46

# In[19]:


l=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
list(filter(lambda x:x%2==0 and x%3==0,l))


# Q6. Write a python program to find palindromes in the given list of strings using lambda and filter 
# function.
# 
# 
# ['python', 'php', 'aba', 'radar', 'level']

# In[25]:


a=['python', 'php', 'aba', 'radar', 'level']
palindrome=list(filter(lambda x:x==x[::-1],a))
print("Palindrome:", palindrome)


# In[24]:


words = ['python', 'php', 'aba', 'radar', 'level']

is_palindrome = lambda s: s == s[::-1]

palindromes = list(filter(is_palindrome, words))

print("Palindromes:", palindromes)


# In[ ]:




