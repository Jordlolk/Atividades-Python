#Calculadora
import functions_calc as modulo

print("-"*35)
print("Calculadora")

while True:
    print("-"*35)
    print("|Type:1,to add:")
    print("|Type:2,to subtraction:")
    print("|Type:3,to multiplication:")
    print("|Type:4,to division:")
    print("|Type:5,to exit:")
    print("-"*35)

    print("WHAT DO YOU WANT TO DO?")
    num = input("")

    if num == "1":
        num1 = float(input("Digite um número: "))
        num2 = float(input('Ditite um segundo número: '))
        modulo.add(num1,num2)
    elif num == "2":
        num1 = float(input("Digite um número: "))
        num2 = float(input('Ditite um segundo número: '))
        modulo.subtraction(num1,num2)
    elif num == "3":
        num1 = float(input("Digite um número: "))
        num2 = float(input('Ditite um segundo número: '))
        modulo.multiplication(num1,num2)
    elif num == "4":
        num1 = float(input("Digite um número: "))
        num2 = float(input('Ditite um segundo número: '))
        modulo.division(num1,num2)
    elif num == "5":
        break
    else:
        print("ERROR: Insert a correct value!")