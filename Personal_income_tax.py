#conding = utf8
serlary = input('Enter your monthly salary\n')
temp = int(serlary) - 3500
#Start calculating
if temp <= 0:
    print("您的月薪为%d元，不需要纳税"%int(serlary))
elif 0 < temp <= 1500:
    tax = temp * 0.03
elif 1500 < temp <= 4500:
    tax = (temp - 1500) * 0.1 + 45
elif 4500 < temp <= 9000:
    tax = (temp - 4500) * 0.2 + 345
elif 9000 < temp <= 35000:
    tax = (temp - 9000) * 0.25 + 1245
elif 35000 < temp <= 55000:
    tax = (temp - 3500) * 0.3 + 7745
elif 55000 < temp <= 80000:
    tax = (temp - 55000) * 0.35 + 13475
elif temp > 80000:
    tax = (temp - 80000) * 0.45 + 22495
print("您的月薪为%d元，应缴纳%d元"%(int(serlary), tax))