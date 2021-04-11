# imports


# globals


# functions
def print_menu():
    print("** PyCalc **")
    print("-----------")
    print('[1] Sum')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divide')

    print('[q] Quit')


# instructions
opc = ''
while(opc != 'q'):
    print_menu()
    opc = input("Please select an option: ")

    if(opc == 'q'):
        break

    try:    
        num1 = float(input("Provide Num 1: "))
        num2 = float(input("Provide Num 2: "))

        if(opc == '1'):
            print("You want to sum")
            res = num1 + num2
            
        elif(opc == '2'):
            print("You want to subtract")
            res = num1 - num2

        elif(opc == '3'):
            print("You want to multiply")
            res = num1 * num2

        elif(opc == '4'):
            print("You want to divide")
            res = num1 / num2

        print("Result: " + str(res))
        # print(f"Result: {res}") this is interpolation
    
    except:
        print("****DIVISION BY 0 IS NOT SUPPORTED****")
        """print("***Error, verify and try again!)"""

print("Good Byte!")

"""
HW:
    - muliplication
    - division:
        NOTE: don't allow user to divide by 0....9/0
        SHOW AN ERROR "DIVISION BY 0 IS NOT SUPPORTED"

"""