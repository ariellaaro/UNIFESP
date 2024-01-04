#!/usr/bin/python3

##########################################
# cpf.py: Implementando um algoritmo
# Autor: Ariella Aro
# Data: 12/06/2022
##########################################

#eu acho que funciona agora; me avise de qualquer problema que precise ser corrigido, pf :")
#e na última aula foi dito q a str TINHA q ser chamada strCPF mas apesar de ela começar como strcpf
#depois da linha 22 ela vira strCPF como pedido

import random

def checaCPF(strcpf):
    if len(strcpf) > 14 or len(strcpf) < 11:
        return False
    strCPF=[]
    for n in strcpf:
        if n.isdigit():
            strCPF.append(n)
    if len(strCPF) != 11:
        return False
    novocpf=[int(char) for char in strCPF]
    for i in range(9, 11):
        m = sum((novocpf[num] * ((i+1) - num) for num in range(0, i)))
        n = ((m * 10) % 11) % 10
        if n != novocpf[i]:
            return False
    return True

def geraCPF():
    #9 primeiros n (aleatórios)
    cpf = [random.randint(0, 9) for i in range(9)]

    #primeiro n verificador
    longo=(cpf[0]*10)+(cpf[1]*9)+(cpf[2]*8)+(cpf[3]*7)+(cpf[4]*6)+(cpf[5]*5)+(cpf[6]*4)+(cpf[7]*3)+(cpf[8]*2)
    n=longo%11

    if n==0 or n==1:
        n1=0
    else:
        n1=11-n

    cpf.append(n1) 

    #segundo n verificador
    longoo=(cpf[0]*11)+(cpf[1]*10)+(cpf[2]*9)+(cpf[3]*8)+(cpf[4]*7)+(cpf[5]*6)+(cpf[6]*5)+(cpf[7]*4)+(cpf[8]*3)+(n1*2)
    m=longoo%11

    if m==0 or m==1:
        n2=0
    else:
        n2=11-m

    cpf.append(n2)

    cpfnovo = ''.join(str(x) for x in cpf)
    
    return cpfnovo