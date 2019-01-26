def main():
    #Going through a for loop to print everything from 1-100
    for x in range(1, 101):
        if x % 3 == 0 and not x % 5 == 0:
            print("Fizz")

        elif x % 5 == 0 and not x % 3 == 0:
            print("Buzz")

        elif x % 3 == 0 & x % 5 == 0:
            print("FizzBuzz")
        else:
            print(x)
  
main()
