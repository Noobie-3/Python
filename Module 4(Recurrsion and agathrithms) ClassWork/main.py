
import traceback
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else :
        return fib(num-1) + fib (num-2)


def main():
   for i in range(10):
       print(fib(i), end=", ")


main()



























