# # python strings are sequence of unicode characters
# creating string 
# accessing strings 
# adding chars to string 
# editing strings 
# deleting strings 
# operations on strings 
# string functions

# creating string
str = 'hello world'
str1 = "harshvardhan"
str2 = ''' hi bro''' # for multiline strings
str3 = """ captain harshvardhan basude"""

print(str,str1,str2,str3,sep="\n")

#-------------------------------------------------------------------------------------------------------

# accessing the substring or character
s = " hi my name is harshvardhan dattatray basude"
print(s[17])

# negative string
print(s[-4])

# to get substring(slicing)
print(s[0:12:2])

print(s[:])

print(s[10:0:-1])

print(s[::-1])

#-------------------------------------------------------------------------------------------------------

# string are immutable but you can delet it

p = " hfbjkgvkgw "
del p
try:  
  print(p)
except:
  print("p is deleted")

#--------------------------------------------------------------------------------------------------------

# operations on strings

# 1- atithmatic operations (+ , -)
print('delhi'+'mumbai')
print('delhi'*10)

# logical
print("harsh" == "nhggv")

# relational (lexiographycally comparison)
print("ndelhi">"mumbai")

# logical 
print("hello" and "world")
print("hello" or "world")
print(".............................")
print("" and "world")
print(".............................")
print("" or "world")
print(not "hello")


# loops on string
for i in " harshvardhan basude":
  print(i)

# membership operators ( in , not in)
print("D" in "delhi")
print("g" not in "delhi")

#-------------------------------------------------------------------------------------------------------------
# string functions
# common functions ( works on all data types)
# the operations doing are happening temperory and not permenant changes in original string

print(len("hdvkhgfovbv"))       # len
print(max("hdvkhgfovbv"))       # max
print(min("hdvkhgfovbv"))       # min
print(sorted("hdvkhgfovbv"))    # sorted

s = "harshvardhan"
print(s)

print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.count('h'))
print(s.find('vardhan'))
print(s.endswith("dhan"))

print("-------------------------------------------------------------------------------------")
# format
print('hi my name is {} and i am {}'.format(s, 23))
print('hi my name is {1} and i am {0}'.format(24, s))

# to check only digit and numbers
print("harsh6078".isalnum())      # is only alphabet and numbers
print("harsh6078".isdigit())      # is fully digit
print("harsh6078".isalpha())      # is alphabet
print("harsh6078".isidentifier()) # VALID Identifier or not


#------------------------------------------------------------------------------------------------

# split(), sep('\n'),join(), replce("nitish","campusx"), strip()-->remove spaces, index('@')