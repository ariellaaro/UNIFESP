#!/usr/bin/python3

##########################################
# ex2.py: Estatística básica
# Autor: Ariella Aro
# Data: 01/05/2022 (corrigido em 07/05/2022)
##########################################

qnt=int(input('Quantidade de números na lista: '))
nova=[]
print('Escreva os números: ')

for i in range(0, qnt):
    a=float(input())
    nova.append(a)

nova.sort()

#mínimo, máximo e média ---------------
media=sum(nova)/len(nova)
print(f'Valor mínimo: {nova[0]}\nValor máximo: {nova[-1]}\nMédia: {media}')

#mediana ---------------
n=len(nova)//2
if len(nova)%2==0:
    print(f'Mediana: {(nova[n]+nova[n-1])/2}')
else:
    print(f'Mediana: {nova[((len(nova)+1)//2)-1]}')

#desvio padrão ---------------
un=[]
for i in range(0, len(nova)):
    un.append((nova[i]-media)**2)
m=sum(un)
print(f'Desvio padrão: {(m/len(nova))**(1/2)}')
