import time
def organizer(exp):
    exp=exp.replace(" ","")
    array = []
    for i in exp:
        if i == "x" or i == "/" or i == "+" or i == "-":
            array.append(f" {i} ")
        else:
            array.append(i)
    array = "".join(array)
    array = array.split(" ")
    return array
    
def multiplicacao(exp):
    array = exp
    for i in range(1, len(array), 2):
        if array[i] == "x":
            result = float(array[i-1]) * float(array[i+1])
            del array[i+1]
            del array[i]
            del array[i-1]
            array.insert(i-1, str(result))
            break
    return array
    
def soma(exp):
    array = exp
    for i in range(1, len(array), 2):
        if array[i] == "+":
            result = float(array[i-1]) + float(array[i+1])
            del array[i+1]
            del array[i]
            del array[i-1]
            array.insert(i-1, str(result))
            break
    return array
    
def subtracao(exp):
    array = exp
    for i in range(1, len(array), 2):
        if array[i] == "-":
            result = float(array[i-1]) - float(array[i+1])
            del array[i+1]
            del array[i]
            del array[i-1]
            array.insert(i-1, str(result))
            break
    return array

def divisao(exp):
    array = exp
    for i in range(1, len(array), 2):
        if array[i] == "/":
            if array[i+1] == "0":
                return 0
            result = float(array[i-1]) / float(array[i+1])
            del array[i+1]
            del array[i]
            del array[i-1]
            array.insert(i-1, str(result))
            break
    return array
    
def calculadora(exp):
    exp = organizer(exp)
    for i in range(0,len(exp),2):
        if exp[i].isdigit() == False:
            print("Expressão Invalida")
            return 0
        else:
            array = exp
            mu = 0
            so = 0
            su = 0
            di = 0
            for i in range(1,len(exp), 2):
                if exp[i] == "x":
                    mu += 1
                elif exp[i] == "+":
                    so += 1
                elif exp[i] == "-":
                    su += 1
                elif exp[i] == "/":
                    di += 1
            for i in range (di):
                array = divisao(array)
                if array == 0:
                    print("Operação Ilegal")
                    return 0
            for i in range (mu):
                array = multiplicacao(array) 
                
            for i in range (so):
                array = soma(array)
            for i in range (su):
                array = subtracao(array)
            array = "".join(array)
            return float(array)

exp = input()
exp = calculadora(exp)
print(exp)
