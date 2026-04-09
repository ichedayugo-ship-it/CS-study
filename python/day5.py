def check_age(age):
    if age>18:
        print("Adult")
    else:
        print("Minor")

check_age(25)

def check_number(check):
    if check >0:
        print("Positive")
    elif check ==0:
        print("Zero")
    else:
        print("Negative")

check_number(-7)

def show_even(n):
    for i in range(1, 1+n):
        if i % 2==0:
            print(i)
        
show_even(10)

def show_even(n):
    for i in range(1, 1+n):
        if i % 2!=0:
            print(i)
        
show_even(10)

def show_multiples_of_3(n):
    for i in range(1,1+n):
        if i %3==0:
            print(i)

show_multiples_of_3(15)

def show_multiples_of_5(n):
    for i in range(1,n+1):
        if i %5==0:
            print(i)

show_multiples_of_5(20) 

def check_even(number):
    if number%2 == 0:
        print("Even")
    else:
        print("Odd")

check_even(20)            

def show_big_numbers(n):
    for i in range(1, n+1):
        if i >5:
            print(i)

show_big_numbers(10) 