def isArmstrong(n):
    temp = n
    sum = 0
    digits = len(str(n))

    while n > 0:
        digit = n % 10
        sum = sum + digit ** digits
        n = n // 10

    if sum == temp:
        return True
    else:
        return False