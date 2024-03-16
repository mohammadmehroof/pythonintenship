# def my_function():
#     print("my name is fousi")

# my_function()


# def add_num(a,b):
#     sum=a+b
#     return sum
# num1=25
# num2=55
# print("the sum is",add_num(num1,num2))    


# def multiply_num(a,b):
#     product=a*b
#     return product
# num1=5
# num2=2
# print("the product is",multiply_num(num1,num2))    

# def check_odd_even(number):
#     if number % 2==0:
#         return"Even"
#     else:
#         return"odd"

# num=25
# result=check_odd_even(num)
# print(result)    
 
# def find_square(num):
#     result=num*num
#     return result
# square=find_square(3)

# print(square)

# def find_cube(num):
#     result=num*num*num
#     return result
# cube=find_cube(3)

# print(cube)

# #default argument
# def add_numbers(a=7,b=8):
#     sum=a+b
#     print("sum",sum)
# #add_numbers(2,3)

# add_numbers(4)


# #keyword argument
# def display_info(first_name,last_name):
#     print('first name:',first_name)
#     print('last name:',last_name)

# display_info(last_name='fall',first_name='rain')    

#program to find sum of multiple add_numbers

def find_sum(*numbers):
    result=0
    for num in numbers:
        result=result+num

    print("sum=",result)


find_sum(1,2,3)