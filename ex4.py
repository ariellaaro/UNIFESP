#!/usr/bin/python3

##########################################
# ep4.py: Inteiro para romano
# Autor: Ariella Aro
# Data: 21/06/2022
##########################################

def romano(n):
    l = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    fim = ''
    for i, r in l:
        while n >= i:
            fim += r
            n -= i

    return fim

# parte que eu usei pra testar se funcionava
#n=int(input())
#print(romano(n))