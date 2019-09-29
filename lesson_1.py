def couple_number(n):
    l = []
    for i in range(0, n+1):
        if i%2 == 0:
            print(i)


# couple_number(10)

country_cyty = {'Netherlands':'Amsterdam', 'Ukraine':'Kyiv', 'Russian':'Moscow'}

country = ['Afghanistan', 'Netherlands', 'Ukraine', 'Honduras']

for k, v in country_cyty.items():
    if k in country:
        print(k)

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
    
# say_fizz_and_buzz(100)

def bank(summ_depoz, amount_year, procent):
    res = summ_depoz*(procent * 0.01)
    return str(res) + ' grn'

print(bank(10000, 1, 6))