
# break and continue --- Two functional keywords in python.

# break keyword --- It is use to terminate the for loop and while loop in the middle
  # Basicaly, when we reached to a certain desired satisfying condition on runing while/for loop, we write break keyword as after reaching the desired result we don't want the loop keeps on execute. 


# Let's see how to usee break statement ?

'''int_list = [1,5,7,19,8,45,53,21]
# Ques. Find the even value from list ?
for num in int_list:
    print(num)
    if(num%2==0):
        print("Even number found in the int_list is",num)
        break'''
# Here in the above for loop, we had use break functional keyword as after finding the only even no. present in the list, i would not like any more iteration to keeps on going.


# Suppose if I don't use the break functional keyword in for loop

int_list = [1,5,7,19,8,45,53,21]
# Ques. Find the even value from list ?
for num in int_list:
    print(num)
    if(num%2==0):
        print("Even number found in the int_list is",num)
     
