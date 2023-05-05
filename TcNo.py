#Turkish Identitiy number  algorithm with python

"""
****RULES****
1-Your Id number must be 11 digits
2-The first digit cant be 0
3-The sum of 1., 3., 5., 7. and 9. digits must be multiplied with 7.The sum of 2., 4., 6. and 8. digits must be substracted from that number.The result divides by 10 and the remainder gives us the 10.digit of Id.
4-The sum of 1-10. digits must be divided by 10 and the remainder gives us the 11.digit of Id.

"""

Id = input("Please enter your Id:")
control = 0

while True:
    if len(Id) == 11:#If your Id has 11 digits then you can search for the other conditions
        for i in Id:
            if not i.isdigit():#Your Id must have only digits.If it does have other things
                print("Invalid Id!")
                control = 1 #then control turns 1 and the loop is done
                break
        
        if Id[0] == 0:
            print("Invalid Id")
            control = 1
            break

        sumOfEven = (int(Id[0]) + int(Id[2]) + int(Id[4]) + int(Id[6]) + int(Id[8])) * 7
        sumOfOdd = (int(Id[1]) + int(Id[3]) + int(Id[5]) + int(Id[7]))
        substraction = sumOfEven - sumOfOdd 

        if substraction % 10 != int(Id[9]):#since your Id is string you need to turn it into integer first.
            print("Invalid Id")
            control = 1
            break

        sumTillEleven = 0
        
        for i in range(10):
            sumTillEleven += int(Id[i])

        if sumTillEleven % 10 != int(Id[10]):
            print("Invalid Id")
            control = 1
            break
    else:#If your Id doesn't have 11 digits then control turns 1 and loop is done.
        print("Invalid Id")
        control = 1
        break

    if control == 0:
        print("Your Id is correct! " ,Id)
        break        
    
            


