# variables are containers that are used for future data storage

# variable declaration
# dynamic typing ( where we dont tell data type ) python automatically detect data type

# name = "harshvardhan"
# num = 12
# pie = 3.14

# # dynamic binding
# a = 5
# print(type(a), a)

# a = "harshvardhan"
# print(type(a),a)


# # other ways to create variable

# a , b , c =12, 13, 14
# print(a,b,c)

# a=b=c=5
# print(a,b,c)

#----------------------------------------------------------------------------------------------

# this is sngle line comments commnent
"""this 
is 
muliline
comments"""

# ----------------------------------------------------------------------------------------------
# keywords 
# these are special type of words or reserved words whose meaning is already defined by pyton ( you cant use them for variables)
# if, else , for , ......

#----------------------------------------------------------------------------------------------
# identifiers
# you can create identifiers by following rules
# cant be keywords
# cant start with numbers and special characters
# can use underscore
# no Space 


#-----------------------------------------------------------------------------------------------

# # user input 
# name = input(" please enter name")  # default data type is string (because string is universal data format)

# implicit = print(5 + 5.5) --> automatically python convert it to float as it is bigger data type and can contain int value also
# explicite 
# age = int(input("input your age"))  # its way of convertig string to int (typecasting) - implicite and eplicite tyoe conversion



# # printing it
# print(name)
# print(age) 


#-----------------------------------------------------------------------------------------------

#literals  (value assigned to variables is literal  eg- a = 25 here 25 is literal)
# a = 0b100101010101010010
# print(a)

# b = 100

# c= 0o310

# d = 0x12c

# x = 7 + 3.14j

# print(a,b,c,d,x)

# print(x.real)
# print(x.imag)

# #------------------------------------------------------------------------------------------------------

# # string 
# name = "harshvardhan"
# name = 'harshvardhan'

# #-------------------------------------------------------------------------------------------------------
# boolean =(True or False) # True = 1 , False = 0  so 2 + True = 3 and 2 + False = 2
# print(type(boolean))


# #-------------------------------------------------------------------------------------------------------
a = None
print(type(a))

a = 5
print(type(a))


