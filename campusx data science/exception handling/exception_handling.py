# compile time error
# runtime Error
# logical error
# indention error

# index error , module not found error , keyerror , typeError , attribute error, nameError , 

# exeption
           # try , catch , except , else , finally , raise

try:
    m = 6
    f = open('sample.txt','r')
    print(f.read)
    l = [1,2,3,4,5]
    print(l[100])
except FileNotFoundError:
    print('file not found')
except Exception as e:
    print('we got',e , 'error')
else:
    print('thank you there is no error so this get executed')
finally:
    print('thank you')