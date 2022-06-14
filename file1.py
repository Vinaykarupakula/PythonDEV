def prime(num):
    if num>2:
        for i in range(2,num):
            if num%2==0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
prime(37)