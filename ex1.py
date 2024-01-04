#!/usr/bin/python3

##########################################
# ex1.py: Números primos
# Autor: Ariella Aro
# Data: 27/04/2022 (primeiro arquivo enviado 22/04/2022)
##########################################

idkstart=True

while idkstart:
    n=input('\nVERIFICAÇÃO DE PRIMALIDADE\nInsira um número qualquer:')
    n=int(n)
    i=1

    while n<=1:
        m=input('O número inserido não é primo! Deseja tentar novamente? (s/n)')
        if m.lower()=='s':
            break
        if m.lower()=='n':
            print('\nProcesso finalizado.')
            idkstart=False
            break
        else:
            continue

    while i<n:
        i+=1
        if n%i==0 and n!=2:
            m=input('O número inserido não é primo! Deseja tentar novamente? (s/n)')
            if m.lower()=='s':
                break
            if m.lower()=='n':
                print('\nProcesso finalizado.')
                idkstart=False
                break
            else:
                continue
        elif n%i!=0 or n==2:
            m=input('O número inserido é primo! Deseja tentar novamente? (s/n)')
            if m.lower()=='s':
                break
            if m.lower()=='n':
                print('\nProcesso finalizado.')
                idkstart=False
                break
            else:
                continue
