def fun():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = input("Enter choice(1/2/3/4): ")
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))      
    if choice == '1':
        print(num1, "+", num2, "=",num1+num2)
    elif choice == '2':
        print(num1, "-", num2, "=", num1-num2)
    elif choice == '3':
        print(num1, "*", num2, "=", num1*num2)
    elif choice == '4':
        print(num1, "/", num2, "=", num1/num2)
    else:
        print("Invalid Input")
fun()
m=input("let's to do next calculation(yes/no):")
while m=="yes":
    fun()
    m=input("let's to do next calculation(yes/no):")
else:
    print("thankyou")
