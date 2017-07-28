import os
mq, tq, mf, tf, C, Qlib, H, Horig = (0,)*8
while(True):
    Horig = float(input("Por favor insira o ΔH >TABULADO< para a experiência que você está realizando: "))
    os.system('cls' if os.name=='nt' else 'clear')
    if(str(input("Você deseja calcular sua constante calorimétrica? (RECOMENDADO) [s/n] ")).lower() == "s"):
        print("# Calculo da constante calorimétrica #")
        mq = float(input("Insira a massa QUENTE (mq): "))
        tq = float(input("Insira a variação da água QUENTE (Δtq): "))
        mf = float(input("Insira a massa FRIA (mf): "))
        tf = float(input("Insira a variação da água FRIA (Δtf): "))
        C = float(-1*(((mq*4.18*tq) - (mf*4.18*tf))/tf))
        print("Sua constante calorimétrica (C) será:", C, "J/°C")
        if(str(input("Você está certo dos seus valores? [s/n] ")).lower() == "n"):
            continue
    else:
        C = float(input("Insira a sua constante calorimétrica: "))
    os.system('cls' if os.name=='nt' else 'clear')
    if(str(input("Você deseja calcular a quantidade de calor liberada pela água? (RECOMENDADO) [s/n] ")).lower() == "s"):
        while(True):
            print("# Calculo da quantidade de calor liberada pela água #")
            ma = float(input("Insira a massa da água: "))
            t = float(input("Insira a variação de temperatura: "))
            Qlib = 4.18*ma*t + C*t
            print("Sua quantidade de calor liberada pela água (Q) será:", Qlib, "J")
            if(str(input("Você está certo dos seus valores? [s/n] ")).lower() == "n"):
                continue
            else:
                break
    else:
        Qlib = float(input("Insira a quantidade de calor liberada pela água (Q): "))
    os.system('cls' if os.name=='nt' else 'clear')
    con = float(input("Qual a concentração da substância em questão (em mol/L)? "))
    os.system('cls' if os.name=='nt' else 'clear')
    print("Constante calorimétrica (C): ", C, "J/°C")
    print("Calor liberado pela água (Q): ", Qlib, "J")
    print("Concentração da Substância (c): ", con, "mol/L")
    if(str(input("Você está certo dos seus valores? [s/n] ")).lower() == "n"):
        continue
    H = Qlib/con
    print("ΔH = ", H, '(%% de erro:', ((H - Horig)/H)*100)
    print("Pronto!")
    input("Pressione ENTER para repetir.")