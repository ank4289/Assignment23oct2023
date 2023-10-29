# Write a Python program to find the largest number in a list

#Max Value with predefined list
list1=[3,7,9,1,6,9,22,17]
max_number=max(list1)
print(f"The largest number in the list is:{max_number}")

#Write a Python program to find the smallest number in a list.
list1=[3,7,9,1,6,9,22,17]
min_number=min(list1)
print(f"The largest number in the list is:{min_number}")

#rite a Python program to sum all numbers in a list.
listnew=[3,7,9,1,6,9,22,17]
Sum=0
for i in listnew:
 Sum=Sum+i
print("The sum of number is ",Sum)

#Write a Python program to multiply all numbers in a list.
listnew=[3,7,9,1,6,9,22,17]
mult=1
for i in listnew:
 mult=mult*i
print("The multiplication of number is ",mult)

# Write a Python program to count the number of strings in a list where the string length is
# 2 or more and the first and last character
# are the same.
a = input('please enter string for the List seperated by comma :\n').split(',')
print(a)
if len(a)>=2 and a[0]==a[-1]:
    x=len(a)
    print('The Length of the String is ::',x)
else:
    print('The Length of the string is less than 2 or the 1st and last character of the string is not same!!')