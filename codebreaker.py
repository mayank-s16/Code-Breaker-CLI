import random
digits=list(range(10))
random.shuffle(digits)
shuffledigits=digits[:3]
ulist=list()
print("Computer has selected a 3 digit number and you have to crack it by entering the digit at correct place only !!!!@@@")
print("")
while(ulist!=shuffledigits):
    a=int(input("enter the first digit   "))
    if a!=shuffledigits[0] and a!=shuffledigits[1] and a!=shuffledigits[2]:
        print("your digit does not match any digit of the number")
        ulist=list()
        continue
    else:
        if a!=shuffledigits[0]:
            print("!! your digit is in the number but at wrong position!!")
            ulist=list()
            continue
        else:
            print("Congrats first digit match successfully!!")
            ulist.append(a)
            b=int(input("enter the second digit  "))
            if b!=shuffledigits[0] and b!=shuffledigits[1] and b!=shuffledigits[2]:
                print("your digit does not match any digit of number")
                ulist=list()
                continue
            else:
                if b!=shuffledigits[1]:
                    print("your digit is in the number!!! But you cannot crack this number ")
                    ulist=list()
                    continue
                else:
                    print("Congrats2")
                    ulist.append(b)
                    c=int(input("Most Welcome!! This is the final digit of the number!!!  "))
                    if c!=shuffledigits[0] and c!=shuffledigits[1] and c!=shuffledigits[2]:
                        print("Your digit is not even in the number!!!!")
                        ulist=list()
                        continue
                    else:
                        if c!=shuffledigits[2]:
                            print("your digit is in the number!!! but you cannot won bro")
                            ulist=list()
                            continue
                        else:
                            print("And finally you wonnnn!!!! Congratulationsssss!!! ")
                            ulist.append(c)




                     
            
          
       


