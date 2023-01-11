def fizz(n1):
    if n1 % 3 == 0  and n1 % 5 == 0:
        return 'FizzBuzz'
    elif n1 % 3 == 0:
        return 'Fizz'
    elif n1 % 5 == 0:
        return 'Buzz'
    else:
        return n1

fizz = fizz(n1 = 55) 
print(fizz)