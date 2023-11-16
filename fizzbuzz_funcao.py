def fizzbuzz(x):
    d3 = x % 3
    d5 = x % 5
    if d3 == 0 and d5 != 0:
        return "Fizz"
    elif d3 != 0 and d5 == 0:
        return "Buzz"
    elif d3 == 0 and d5 == 0:
        return "FizzBuzz"
    else:
        return x
