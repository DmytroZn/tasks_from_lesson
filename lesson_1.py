# Task 1. Create a list of N items (0 to n in steps 1). 
# Display all even values in this list.
def couple_number(n):
    l = []
    for i in range(0, n+1):
        if i%2 == 0:
            print(i)

couple_number(10)


# Task 2. Create Dictionary Country:Capital. Create country list. 
# Not all countries from the list should agree with the names 
# of countries from the dictionary. With the help of the in operator, 
# check for the entry of the country element into the dictionary, 
# and if such a key really exists to write the capital.
country_cyty = {'Netherlands':'Amsterdam', 'Ukraine':'Kyiv', 'Russian':'Moscow'}
country = ['Afghanistan', 'Netherlands', 'Ukraine', 'Honduras']

for k, v in country_cyty.items():
    if k in country:
        print(k)


# Task 3. Write a program that displays a number from 1 to 100. 
# At the same time, instead of numbers that are multiples of three, 
# the program should output the word Fizz, and instead of numbers 
# that are multiples of five - the word Buzz. If the number 
# is multiple of fifteen, the program should output the word FizzBuzz.
def say_fizz_and_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            i = 'Fizz'
            print(i)
        elif i % 5 == 0:
            i = 'Buzz'
            print(i)
        elif i % 15 == 0:
            i = 'FizzBuzz'
            print(i)
        else:
            print(i)
    
say_fizz_and_buzz(100)


# Task 4. To realize the function of bank, which takes the 
# following arguments: The amount of deposit, the number of years, 
# and the percentage. The completion must result in an amount 
# after the deposit has expired.
def bank(summ_depoz, amount_year, procent):
    res = summ_depoz*(procent * 0.01)
    return str(res) + ' grn'

print(bank(10000, 1, 6))