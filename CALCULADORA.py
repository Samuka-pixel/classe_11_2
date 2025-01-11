import math
Num = float(input("número: "))
Res = 0
X = "Sim"
while X == "Sim":
    Func = str(input("função: "))
    if Func == "/":
        Num2 = float(input("número: "))
        Res =Num / Num2
        print(Res)
    elif Func == "*":
        Num2 = float(input("número: "))
        Res = Num * Num2
        print(Res)
    elif Func == "+":
        Num2 = float(input("número: "))
        Res = Num + Num2
        print(Res)
    elif Func == "-":
        Num2 = float(input("número: "))
        Res = Num - Num2
        print(Res)
    elif Func == "^":
        Num2 = float(input("número: "))
        Res = Num ** Num2
        print(Res)
    elif Func == "/r":
        Num2 = float(input("número: "))
        Res = Num ** (1/Num2)
        print(Res)
    else:
        print("erro")
    Num = Res
    X = str(input("Continuar?: "))