def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
print("select operation.")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

while True:
    choice=input("Enter your choice:")
    if choice in  ('1','2','3','4'):
        
            num1=float(input("Enter the first number="))
            num2=float(input("Enter the second number="))
        
    if choice =='1':
            print(num1,"+",num2,"=",add(num1,num2))
    if choice =='2':
            print(num1,"-",num2,"=",sub(num1,num2))
    if choice =='3':
            print(num1,"/",num2,"=",mul(num1,num2))
    if choice =='4':
            print(num1,"+",num2,"=",div(num1,num2))
    again=input("NEXT CALCULATION? (yes/no)")
    if again =="no":
            break
    else:
            print("ENTER YOUR NEXT INPUT")

