import time

print("This is a number guessing game. Think of a number from 1-10. No decimals.")
print("Make sure to type in exactly 'yes' or 'no' or the command won't run your answer")







k = input("Is your number less than 5 and odd. Please input yes or no: ")

if ( k == 'yes'):
   
    m= input("Is your value less than 3?")
    if (m=='yes'):
        print('your value is 1')
        exit()

    else:
        print('your value is 3')
        exit()
    
    
else:
    print("still caluclating")

h = input("Is your number less than 5 and even. Please input yes or no: ")

if (h == 'yes'):
   
    g = input('Is you value less than 4?: ')
    
    if (g== 'yes'):
        print("your value is 2")
        exit()
    else:
        print("Your value is 4")
        exit()
n = input("Is your value the half of 10. Please input yes or no:")
if (n=='yes'):
    print("Your value is 5.")
    exit()
else:
    print("Continue")
z = input("Is your number more than 5 and odd. Please input yes or no: ")

if (z=='yes'):
    
    u= input("Is your value less than 9. Please input yes or no: ")
    if (u=='yes'):
        print("Your value is 7.")
        exit()
    else:
        print("Your value is 9.")
        exit()



o = input("Is your number less than 5 and even. Please input yes or no: ")

if (o=="yes"):
    
    exit()
    x = input("Is your value less than 8. Please input yes or no: ")
    if(x=='yes'):
        print("Your value is 6.")
        exit()
    else:
        print("Your value is 8.")
        exit()
    
    
    
else:
 print("Your value is 10")
 exit()






    

