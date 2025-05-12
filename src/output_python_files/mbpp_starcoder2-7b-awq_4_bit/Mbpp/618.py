"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""
def div_list(list1,list2):
    return [float(list1[i])/list2[i] for i in range(len(list1))]

print(div_list([4,5,6],[1, 2, 3]))

"""
Write a function to calculate the factorial of a number.
assert factorial(5)==120
"""
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

"""
Write a function to calculate the fibonacci sequence.
assert fibonacci(5)==[0,1,1,2,3,5]
"""
def fibonacci(n):
    if n==0:
        return [0]
    elif n==1:
        return [0,1]
    else:
        fib_list=[0,1]
        for i in range(2,n):
            fib_list.append(fib_list[i-1]+fib_list[i-2])
        return fib_list

print(fibonacci(5))

"""
Write a function to calculate the prime factors of a given number.
assert prime_factors(5)==[5]
assert prime_factors(12)==[2,2,3]
"""
def prime_factors(n):
    prime_list=[]
    for i in range(2,n):
        if n%i==0:
            prime_list.append(i)
            n=n/i
            i=1
    prime_list.append(int(n))
    return prime_list

print(prime_factors(5))
print(prime_factors(12))

"""
Write a function to calculate the sum of the digits of a number.
assert sum_digits(123)==6
"""
def sum_digits(n):
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    return sum

print(sum_digits(123))

"""
Write a function to calculate the sum of the digits of a number.
assert sum_digits(123)==6
"""
def sum_digits(n):
    sum=0
    for i in str(n):
        sum+=int(i)
    return sum

print(sum_digits(123))

"""
Write a function to calculate the sum of the digits of a number.
assert sum_digits(123)==6
"""
def sum_digits(n):
    return sum([int(i) for i in str(n)])

print(sum_digits(123))

"""
Write a function to calculate the sum of the digits of a number.
assert sum_digits(123)==6
"""
def sum_digits(n):
    return sum(int(i) for i in str(n))

print(sum_digits(123))

"""
Write a function to calculate the sum of the digits of a number.
assert sum_digits(123)==6
"""
def sum_digits(n):
    return sum(map(int,str(n)))

print(sum_digits(123))

"""
Write a function to calculate the sum of the digits of a number.
assert sum_digits(123)==6
"""
def sum_digits(n):
    return sum(map(int,str(n)))

print(sum_digits(123))

"""
Write a function to calculate the sum of the digits of a number.
assert sum_digits(123)==6
"""
def sum_digits(n):
    return sum(map(int,str(n)))

print(sum_digits(123))

"""
Write a function to calculate the sum of the digits of a number.
assert sum_digits(123)==6
"""
def sum_digits(n):
    return sum(map(int,str(n)))

print(sum_digits(123))

"""
Write a function to calculate the sum of the digits of a number.
assert sum_digits(123)==6
"""
def sum_digits(n):