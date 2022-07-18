num1 = 0
num2 = 0
sign = None
ans = None
ans_new = None
new_num = None

num1 = input("Choose the first number: ")
while num1 not in "123456789 10":
    input("Please choose a single digit number: ")
num1 = int(num1)
num2 = input("Now choose the second number: ")
while num2 not in "123456789 10":
    input("Please choose a single digit number: ")
num2 = int(num2)
sign = input("Now what would you like to do with these numbers? [*/+-]: ")
while sign not in "*/+-" and len(sign) == 1:
    input("Please choose one of the four signs [*/+-]: ")
if sign == "*":
    ans = num1*num2
elif sign == "/":
    ans = num1/num2
elif sign == "+":
    ans = num1+num2
else:
    ans = num1-num2 
ans = int(ans)
print(f"The answer is {ans}")
x = 1
while x > 0:
    new_num = input("Now please choose another number: ")
    while new_num not in "123456789 10":
        new_num = input("Please choose single digit number: ")
    new_num = int(new_num)
    sign = input("What operation would you like to preform with the previous answer? [*/+-]: ")
    while sign not in "*/+-" and len(sign) == 1:
        sign = input("Please choose one of the signs [*/+-]: ")
    if sign == "*":
        ans= ans*new_num
    elif sign == "/":
        ans = ans/new_num
    elif sign == "+":
        ans = ans+new_num
    else:
        ans = ans-new_num 
    ans = int(ans)
    print(f"Your new number is {ans}")