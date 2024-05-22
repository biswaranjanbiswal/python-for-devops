import sys

def add (num1,num2):
    c = num1 + num2
    return (c)
    
def mul (num1,num2):
    c= num1*num2
    return (c)
    
num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

if operator == "add":
    result = add (num1,num2)
    print (result)
    # print (add (num1,num2))
elif operator == "mul":
    result = mul (num1,num2)
    print (result)
