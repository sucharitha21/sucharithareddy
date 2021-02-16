import random
def guess_number(number_in_mind):
    num=random.randrange(1,11)
    print(num)
    if num==number_in_mind :
        print("you have got it right!!!")
    elif num>number_in_mind :
        print("number is high")
    else :
        print("number is low")
        
     # remove pass and write your logic here

#use the print statements given below wherever applicable
#print ('Number is low')
#print ('Number is high')
#print ('You have got it right!!!')

#Provide different values for number_in_mind and test your program
guess_number(4)
