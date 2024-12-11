x=float(input("Enter first number: "))
y=float(input("Enter second number: "))
z=(input("Enter an operator:eg(+ - * /): "))
match z:
    case'+':
        print("Answer = "+ str(x=y))
    case'-':
        print("Answer = "+str(x-y))
    case'*':
        print("Answer = "+ str(x*y))
    case'/':
        if y==0:
            print("Error Dividing by zero")
        else:
            print("Answer = "+ str(x/y))
print("Done by Futuretech...")