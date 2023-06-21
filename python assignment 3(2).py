#!/usr/bin/env python
# coding: utf-8

# Q-1 Create a python program to sort the given list of tuples based on integer value a lambda function.
#     [('Sachin Tandulaker' ,34357),('Ricky Ponting',27483),('Jack Kalls',25534),('Virat Kohli',24936)] 

# In[3]:


list=[('Sachin Tandulaker' ,34357),('Ricky Ponting',27483),('Jack Kalls',25534),('Virat Kohli',24936)]
list.sort(key=lambda x:x[1])
print(list)


# Q-2  Write a python program to find the squares of all the numbers in the given list of integers using lambda and map funtion.
#       [1,2,3,4,5,6,7,8,9,10]
#       

# In[4]:


l=[1,2,3,4,5,6,7,8,9,10]
y=iter(l)
square=list(map(lambda y:y**2,y))
print(square)


# Q-3  Write a python program to convert the given list of integers into a tuple of strings. Usemap and lambda functions
#      Given string =[1,2,3,4,5,6,7,8,9,10]
#      Expected output =('1','2','3','4','5','6','7','8','9','10')

# In[5]:


l=[1,2,3,4,5,6,7,8,9,10]
output=tuple(map(lambda x:str(x),l))
print(output)


# Q-4  Write a python program using reduce function to complete the product of a list containing numbers from 1 to 25.

# In[10]:


from functools import reduce


# In[13]:


def product (x,y):
    return x*y
ans=reduce(product,range(1,25))
print(ans)


# Q-5  Write a program to filter the number in a given list that are divisible by 2 and 3 using the filter function.
#    [2,3,6,9,27,60,90,120,55,46]

# In[15]:


l=[2,3,6,9,27,60,90,120,55,46]
out=[]
for i in l:
    if i %2==0 or i %3==0:
        out.append(i)
        print(out)


# Q-6  Write a python program t find palindrome in the given list of sting using lambda and filter fuction .
#       ['python','php','aba','radar','level']

# In[18]:


text=['python','php','aba','radar','level']
result=list(filter(lambda x:(x=="" .join(reversed(x))),text))
print(result)


# In[ ]:




