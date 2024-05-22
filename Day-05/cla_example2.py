import sys
def add (num1,num2):
    c = num1 + num2
    return (c)
def mul (num1,num2):
    c = num1 * num2
    return (c)
num1 = sys.argv[1]
num2 = sys.argv[2]
operator = sys.argv[3]
print (sys.argv[0])
print ("num1 is : ", num1)
print ("num2 is: ", num2)
print ("operator is: ",operator)
if operator == "add":
    result = add (num1,num2)
    print ("result is: ", result)
print (sys.argv)
print (type(sys.argv))
