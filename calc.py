def count(number):
    order = len(str(number))
    sums = 0
    org = number
    while number > 0:
        digit = number % 10
        sums += digit ** order
        number = number // 10

    if sums == org:
        return True
    return False
