# Databricks notebook source
print('hello')

print('hi')


keys_list = ['A', 'B', 'C']
values_list = ['blue', 'red', 'bold']

#There are 3 ways to convert these two lists into a dictionary
#1- Using Python's zip, dict functionz
some other change here

#2- Using the zip function with dictionary comprehensions
dict_method_2 = {key:value for key, value in zip(keys_list, values_list)}

# some really long comment so that we can see what happens when a string runs off the side of the page wow this is so long i would hope that our linter catches it wowow

#3- Using the zip function with a loop
items_tuples = zip(keys_list, values_list) 
dict_method_3 = {} 
for key, value in items_tuples: 
    if key in dict_method_3: 
        pass # To avoid repeating keys.
    else: 
        dict_method_3[key] = value
        
# some new commit

# COMMAND ----------

blah
