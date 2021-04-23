# -*- coding: utf-8 -*-

class Lista():
    def constrói():
        print("Digite a quantidade de vetores a serem utilizados na lista: ")
        a = int(input())
        
        n = [0]*a
        
        print("")
        print("")
        
        i = 0
        while(i<a):
            print("Digite um elemento qualquer na lista: ")
            n[i] = input()
            
            i = i + 1
        
        print("")
        print("")
        print("ELEMENTOS NA LISTA: ")
        
        b = 0
        while(b<i):
            print(n[b])
            
            b = b + 1
        
        print("")
        print("")
        
        op = 0
        print("Digite 1 para adicionar elementos na lista.")
        print("Digite 2 para remover elementos da lista.")
        print("Digite qualquer número diferente para sair.")
        
        op = int(input())
        print("")
        print("")
        
        if(op==1):
            j = 1
            while(j>0):
                print("Digite o elemento que deseja adicionar: ")
                k = input()
                n.append(k)
                
                print("")
                
                print("Digite 1 para continuar ou 0 para sair: ")
                j = int(input())
                print("")
        
        if(op==2):
            j = 1
            while(j>0):
                print("Digite o elemento que deseja remover: ")
                k = int(input())
                n.pop(k)
                
                print("")
                
                print("Digite 1 para continuar ou 0 para sair: ")
                j = int(input())
                print("")
        
        print(n)
        
class Fila():
    def constrói():
        print("Digite a quantidade de vetores a serem utilizados na Fila: ")
        a = int(input())
        
        n = [0]*a
        
        print("")
        print("")
        
        i = 0
        while(i<a):
            print("Digite um elemento qualquer na Fila: ")
            n[i] = input()
            
            i = i + 1
        
        print("")
        print("")
        print("ELEMENTOS NA FILA: ")
        print(n)        
        
        print("")
        print("")
        
        op = 0
        print("Digite 1 para adicionar elementos na fila.")
        print("Digite 2 para remover elementos da fila.")
        print("Digite qualquer número diferente para sair.")
        
        op = int(input())
        print("")
        print("")
        
        if(op==1):
            j = 1
            while(j>0):
                print("Digite o elemento que deseja adicionar: ")
                k = input()
                n.append(k)
                
                print("")
                
                print("Digite 1 para continuar ou 0 para sair: ")
                j = int(input())
                print("")
        
        if(op==2):
            j = 1
            while(j>0):
                n.pop(0)               
                print(n)
                print("Digite 1 para continuar ou 0 para sair: ")
                j = int(input())
                print("")
        
        print(n)

class Pilha():
    def constrói():
        print("Digite a quantidade de vetores a serem utilizados na Pilha: ")
        a = int(input())
        
        n = [0]*a
        
        print("")
        print("")
        
        i = 0
        while(i<a):
            print("Digite um elemento qualquer na Pilha: ")
            n[i] = input()
            
            i = i + 1
        
        print("")
        print("")
        print("ELEMENTOS NA PILHA: ")
        n.reverse()
        b = 0
        while(b<i):
            print(n[b])
            b = b + 1
        
        print("")
        print("")
        
        op = 0
        print("Digite 1 para adicionar elementos na pilha.")
        print("Digite 2 para remover elementos da pilha.")
        print("Digite qualquer número diferente para sair.")
        
        op = int(input())
        print("")
        print("")
        
        if(op==1):
            j = 1
            while(j>0):
                print("Digite o elemento que deseja adicionar: ")
                k = input()
                n.append(k)
                
                print("")
                
                print("Digite 1 para continuar ou 0 para sair: ")
                j = int(input())
                print("")
        
        if(op==2):
            j = 1
            while(j>0):
                n.pop(0)               
                print(n)
                print("Digite 1 para continuar ou 0 para sair: ")
                j = int(input())
                print("")
        
        print(n)
        
        
opção = 0
print("Digite 1 para Lista")
print("Digite 2 para Fila")
print("Digite 3 para Pilha")
opção = int(input())

if(opção==1):
    l = Lista
    l.constrói()       

if(opção==2):
    f = Fila
    f.constrói()

if(opção==3):
    p = Pilha
    p.constrói()

input()
        
        