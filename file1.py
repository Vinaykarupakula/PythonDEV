def prime(num):
    if num==1:
        print(1, "is a prime nuber")
    elif num==2:
        print(num, "is a even prime number")
    else:
        if num>2:
            for i in range(2,num):
                if num%i==0:
                    print(num, "is not a prime number")
                    break
            else:
                print(num, "is a prime number")
prime(15)