def get_fizzbuzz(fizzbuzz):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        return "fizzbuzz"
    elif fizzbuzz % 3 == 0:
        return "fizz"
    elif fizzbuzz % 5 == 0:
        return "buzz"