z = int(input("Which prime palindrome do you want to find?: "))
def prime(num):
    w = False
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, (num//2)+1):
            if num % i == 0:
                w = True
                break
            else:
                w = False
        if w is True:
            return False
        else:
            return True


def palindrome(string):
    if str(string) == str(string)[::-1]:
        return True
    else:
        return False


numtocheck = 0
count = 0
while True:
    if prime(numtocheck) is True:
        if palindrome(numtocheck) is True:
            count += 1
    if count == z:
        requirednumber=numtocheck
        break
    numtocheck += 1
print(z,"th Prime Palindrome is:",requirednumber)
