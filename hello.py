def hello():
    print("Hello Akirachix")

def hello(name):
    print(f"Hello{name}")

def year_of_birth(name,age):
    print(f"Hello {name}, you were born in {2024-age}")


def my_country(country = "Uganda"):
    print(f"Hello  Akirachix from {country}")

def greet(*names):
   for name in names:
       print(f"Hello {name}")

# A function that accepts any number of keyword arguments
def create_sentence(**words):
    print(words)
    sentence= " "
    for word in words.values():
        sentence+=word
        sentence+=" "
    
    return sentence

# Write a program that converts temperature from Celsius to Fahrenheit. The user should be prompted to enter the temperature in Celsius.
def convert_temperature(temp):
    converted_temp = temp * 9.0/5 + 32
    print(converted_temp)		

# def sum_and_greet(*args, **kwargs):
#     total = 0
#     for number in args:
#         total+=number
    
#     greeting = f"Hello {kwargs["first_name"]} {kwargs["last_name"]}, the sum of{lists(args)} is {total}"

#     return greeting

# def check(word):

#  Args: 
# word(str):
# char_count = {}
# for char in word:
#         if char in char_count:
#             char_count[char]+=1
#         else:
#             char_count[char]=1
# return max(char_count,key=char_count.get())
# print(check("Hello World"))

