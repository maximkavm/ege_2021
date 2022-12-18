def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sumOfDigits(s):
    sum = 0
    for c in s:
        if c in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            sum += int(c)
    return sum

for n in range(1000000):
    s = ">" + 39 * "0" + n * "1" + 39 * "2"

    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>")

    print(sumOfDigits(s))
    if isPrime(sumOfDigits(s)):
        print(n)
        break


