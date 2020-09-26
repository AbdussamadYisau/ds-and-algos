def fizzBuzz(n):

    for i in range(1,n):
        if (i% 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
            continue
        elif i % 3 == 0:
            print("fizz")
            continue
        elif i % 5 == 0:
            print("buzz")
            continue
        elif (i%5 != 0 or i%3 != 0):
            print(i)

print(fizzBuzz(15))