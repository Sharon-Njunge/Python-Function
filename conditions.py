def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print(number)


def print_odd_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 != 0:
            print(number)


def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(number)


def check_odd_even(n):
    numbers = range(n)
    for number in numbers:
        if number %2 == 0:
            print(f"{number} is even")

        else:
            print(f"{number} is not even")


def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is divisible by 2")
        
        elif number % 3 ==0:
            print(f"{number} is divisible by 3")
        
        elif number % 5 ==0:
            print(f"{number} is divisible by 5")
        
        else:
            print(f"{number} is not divisible by 2,3 or 5")


def fizz_buzz(n):
    numbers = range(n)
    for number in numbers:
        if number % 15 == 0:
            print("Fizzbuzz")
        
        elif number % 3 == 0:
            print("Fizz")
        
        elif number % 5 ==0:
            print("Buzz")

        else:






























            }|||||||||||||||||||||||||






















































































































































































































































































































































































































            
            print(number)

def count_down(n):
    while n > 0:
        print(n)
        n-=1

def count_down_to_five(n):
    while n > 0:
        print(n)
        if n == 5:
            break
        n-=1

def divisible_by_sum():
    x = 0
    while x <= n:
        x+=1
        if x% 7 != 0:
            continue
        print(f"{x} is divisisble by 7")
def check_if_odd_even(n):
    x = 0
    while x <= n:
        x+=1
        if x % 2 == 0:
            continue
        print(f"{x} is an odd number" )
  