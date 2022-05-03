def sum_add(num1,num2):
    a = num1 * num2

    if a <=1000:
        return a
    else:
        return num1+num2

a = sum_add(20,30)
print("the result is",a)
a = sum_add(30,40)
print("the result is",a)

