import os
mq, tq, mf, tf, C, Qlib, H, Horig = (0,)*8
os.system('cls' if os.name=='nt' else 'clear')
print("### ")
print("###  Entalc")
print("### ")
print("## Bem vindo ao Entalc")
print("## Entalc é um programa desenvolvido no IFBA Campus Porto Seguro")
print("## Turma de 3° TI 2017")
print(" ")
print(" Come ele você poderá realizar o cálculo da constante calorimétrica, calor liberado e Delta H.")
print(" ")
print(" Licença presente no arquivo 'LICENSE' (GPLv3)")
print(" ")
print(" Confira o código-fonte aqui: ")
print("   -> https://github.com/guiscaranse/entalc")
print(" ")
input("Pressione ENTER para começar.")
while(True):
    os.system('cls' if os.name=='nt' else 'clear')
    Horig = float(input("Por favor insira o Delta H (literatura) para a experiência que você está realizando: "))
    os.system('cls' if os.name=='nt' else 'clear')
    if(str(input("Você deseja calcular sua constante calorimétrica? (RECOMENDADO) [s/n] ")).lower() == "s"):
        print("# Calculo da constante calorimétrica #")
        mq = float(input("Insira a massa QUENTE (mq em Kg): "))
        tq = float(input("Insira a variação da água QUENTE (Delta tq em °C): "))
        mf = float(input("Insira a massa FRIA (mf em Kg): "))
        tf = float(input("Insira a variação da água FRIA (Delta tf em °C): "))
        C = float(1000*(((mq*4.18*tq) - (mf*4.18*tf))/tf))
        print("Sua constante calorimétrica (C) será:", C, "J/°C")
        if(str(input("Você está certo dos seus valores? [s/n] ")).lower() == "n"):
            continue
    else:
        C = float(input("Insira a sua constante calorimétrica: "))
    os.system('cls' if os.name=='nt' else 'clear')
    if(str(input("Você deseja calcular a quantidade de calor liberada pela água? (RECOMENDADO) [s/n] ")).lower() == "s"):
        while(True):
            print("# Calculo da quantidade de calor liberada pela água #")
            ma = float(input("Insira a massa da água em Kg: "))
            t = float(input("Insira a variação de temperatura em °C: "))
            Qlib = (-4.18*ma*t) + C*t
            print("Sua quantidade de calor liberada pela água (Q) será:", Qlib, "J")
            if(str(input("Você está certo dos seus valores? [s/n] ")).lower() == "n"):
                continue
            else:
                break
    else:
        Qlib = float(input("Insira a quantidade de calor liberada pela água (Q em J): "))
    os.system('cls' if os.name=='nt' else 'clear')
    con = float(input("Qual a quantidade de mols em questão? "))
    os.system('cls' if os.name=='nt' else 'clear')
    print("Constante calorimétrica (C): ", C, "J/°C")
    print("Calor liberado pela água (Q): ", Qlib, "J")
    print("Quantidade de mols (c): ", con, "mol(s)")
    if(str(input("Você está certo dos seus valores? [s/n] ")).lower() == "n"):
        continue
    H = (Qlib/1000)/con
    print("Delta H = ", H, 'KJ/mol (% de erro:', ((H - Horig)/H)*100, "%)")
    print("Pronto!")
    input("Pressione ENTER para repetir.")
