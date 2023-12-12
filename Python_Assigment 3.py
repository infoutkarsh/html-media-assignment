#!/usr/bin/env python
# coding: utf-8

# Assignment3

# Answer1.The keyword used to create a function in Python is def. Here's an example of how you can use it to create a function that returns a list of odd numbers in the range of 1 to 25:

# In[15]:


def get_odd_numbers():
    odd_numbers = []
    for num in range(1, 26):
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

result = get_odd_numbers()
print(result)


# Answer2.*args and **kwargs are used in function definitions to allow a variable number of arguments to be passed to a function. They provide flexibility when you want to create functions that can accept an arbitrary number of positional and keyword arguments.

# In[20]:


def return_args(*args):
    return list(args)

result_list = return_args(1, 2, 3, "four")
print(result_list)


# In[2]:


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="John", age=25, city="New York")


# In[4]:


def pr(**kwargs):
    return list(kwargs)
result=pr(a=1,b=2,c=3,d="four")
print(result)

#keyword_argument


# Answer3.In Python, an iterator is an object that represents a stream of data and allows you to iterate over the elements of that stream. It provides two main methods: __iter__() and __next__().
# 
# __iter__(): This method is called when you create an iterator object. It should return the iterator object itself.
# 
# __next__(): This method is called to get the next element in the sequence. If there are no more elements, it should raise the StopIteration exception.

# In[6]:


my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

my_iterator = iter(my_list)

for i in range(5):
    print(next(my_iterator))


# Answer4. Generator function in Python is a special type of function that allows you to iterate over a potentially large sequence of data efficiently. It uses the yield keyword instead of return. The yield statement pauses the function's execution and returns a value to the caller, but the function's state is retained, allowing it to resume from where it left off when the next value is requested.
# 
# The yield keyword is used to produce a series of values for iteration, and it maintains the state of the function between successive calls.

# In[7]:


def square_numbers(n):
    for i in range(n):
        yield i ** 2

my_generator = square_numbers(5)

for num in my_generator:
    print(num)


# Answer 5:Generator function for prime numbers less than 1000. Use the next() method to print the 
# first 20 prime numbers.

# In[8]:


def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def prime_generator():
    n = 2
    count = 0
    while count < 20:
        if is_prime(n):
            yield n
            count += 1
        n += 1


# In[12]:


# Using the generator to print the first 20 prime numbers
my_prime_generator = prime_generator()

for i in range(20):
    print(next(my_prime_generator))


# In[ ]:




