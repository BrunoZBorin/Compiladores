from pilha import Pilha
from node import Node

cadeia_de_entrada = ['id', '*', '(', 'id' ,'+' ,'num' ,')','$']
pilha_de_entrada = Pilha() 
for x in reversed(cadeia_de_entrada):
    pilha_de_entrada.push(x)

pilha = Pilha()
pilha.push('$')
pilha.push('E')
print(pilha)

while pilha.__len__() > 1:
    if pilha.peek() == pilha_de_entrada.peek():
        pilha.pop()
        pilha_de_entrada.pop()

    if pilha.peek()=='E':
        if pilha_de_entrada.peek()=='id':
            pilha.pop()
            pilha.push('S')
            pilha.push('T')
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()=='num':
            pilha.pop()
            pilha.push('S')
            pilha.push('T')
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()=='(':
            pilha.pop()
            pilha.push('S')
            pilha.push('T')
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        else:
            print("Tabela nao reconhecida!!!")
            break
            
    elif pilha.peek()=='T':
        if pilha_de_entrada.peek()=='id':
            pilha.pop()
            pilha.push('G')
            pilha.push('F')
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()=='num':
            pilha.pop()
            pilha.push('G')
            pilha.push('F')
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()=='(':
            pilha.pop()
            pilha.push('G')
            pilha.push('F')
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        else:
            print("Tabela nao reconhecida!!!")
            break
            
    elif pilha.peek()=='S':
        if pilha_de_entrada.peek()=='+':
            pilha.pop()
            pilha.push('S')
            pilha.push('T')
            pilha.push('+')
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()=='-':
            pilha.pop()
            pilha.push('S')
            pilha.push('T')
            pilha.push('-')
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()==')':
            pilha.pop()
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()=='$':
            pilha.pop()
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        else:
            print("Tabela nao reconhecida!!!")
            break

    elif pilha.peek()=='G':
        if pilha_de_entrada.peek()=='+':
            pilha.pop()
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()=='-':
            pilha.pop()
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()=='*':
            pilha.pop()
            pilha.push('G')
            pilha.push('F')
            pilha.push('*')
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()=='/':
            pilha.pop()
            pilha.push('G')
            pilha.push('F')
            pilha.push('/')
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()==')':
            pilha.pop()
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()=='$':
            pilha.pop()
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        else:
            print("Tabela nao reconhecida!!!")
            break
    
    elif pilha.peek()=='F':
        if pilha_de_entrada.peek()=='id':
            pilha.pop()
            pilha.push('id')
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()=='num':
            pilha.pop()
            pilha.push('num')
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        elif pilha_de_entrada.peek()=='(':
            pilha.pop()
            pilha.push(')')
            pilha.push('E')
            pilha.push('(')
            print('************')
            print(pilha.inline())
            print('************')
            print(pilha_de_entrada.inline())
            print('************')
        else:
            print("Tabela nao reconhecida!!!")
            break
    else:
        print("Tabela nao reconhecida!!!")
        break

if pilha_de_entrada.__len__() == 1 and pilha.__len__() ==1:
    print('Tabela Reconhecida')
    print(pilha.inline())
    print('************')
    print(pilha_de_entrada.inline())
else:
    print('Tabela Nao Reconhecida')
    print(pilha.inline())
    print('************')
    print(pilha_de_entrada.inline())