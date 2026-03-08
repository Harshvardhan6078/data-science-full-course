# lambda arguments: expression
a = lambda *arg: sum(arg)
print(a(1,2,3,4,5))



# difference between lambda vs normal function

# labmbda function --> no name
                    #    Lambda function no return value In fact it returns a function
                    #    Lambda Is written in one license                
                    #    Not reusable
                    #    Lambda functions are with higher order functions

                    
a = lambda s: "a" in s
a('harshvardhan')

b = lambda x : 'evan' if x%2==0 else 'odd'
print(b(1234323))

# higher order function
                  # if  any function take input a function or return output a function
                  #  