target = int(input("enter the taget fizzbuzz number"))
for number in range(0,target+1) :
    if number%3 == 0 and number%5 == 0 :
        print("FizzBuzz")
    elif number % 3 == 0 :
        print("Fizz")
    elif number % 5 == 0 :
        print("Buzz")
    else :
        print(number)
        