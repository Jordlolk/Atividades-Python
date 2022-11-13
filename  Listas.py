#from collections import namedtuple
#sao_paulo = namedtuple('Estados' , ['sigla' ,'nome'])
#estado_sp = sao_paulo('SP' , 'são paulo')
#print(estado_sp)

#list = list(("amendoin" , True , 45 , "@"))
#print(len(list))

#Descrição do método
#append() Adiciona um elemento no final da lista
#clear() Remove todos os elementos da lista
#copy() Retorna uma cópia da lista
#count() Retorna o número de elementos com o valor especificado
#extend() Adiciona os elementos de uma lista (ou qualquer iterável), ao final da lista atual
#index() Retorna o índice do primeiro elemento com o valor especificado
#insert() Adiciona um elemento na posição especificada
#pop() Remove o elemento na posição especificada
#remove() Remove o item com o valor especificado
#reverse() Inverte a ordem da lista
#sort() Classifica a lista

#  DATA E HORA
# É Necessário importar a biblioteca DATETIME, depois disso para puxar a data e hora
# Dê o valor a variavél  datetime.datetime.now()
# Ápos isso é so chamar a variavél, aqui em baixo existe comandos especifcos para formatar a date.
# O date.STRFTIME.() transforma o valor da string retornada.
# strftime.("%x") Retorna data , strftime("%X") retorna Hora ,  strftime("%C") retorna século. strftime("%B") retorna nome do mẽs.
#TREINO
#  FAZER UM PROGRAMA QUE SALVE EDIT A LISTA E APAGUE ELA.
#   O USUÁRIO PODE ADICIONAR UMA TAREFA A LISTA
#       EDITAR UMA TAREFA


#from operator import index
#import os
#from time import strftime
#from turtle import clear, position
#import datetime
#
#def add():
#    nome = input("Adicionar um nome: ")                                                                    
#    agenda.append(nome)
#    print("Salvo!")
#
#def limpar():
#    agenda.clear()
#
#def clear():
#    os.system("clear")
#
#def edit():
#    for i, nome in enumerate(agenda):
#        print(i,nome)
#    index = int(input("Qual item deseja editar: "))
#    new = input("Insira o novo item: ")
#    agenda.remove(agenda[index])
#    agenda.insert(index,new)
#
#exit = 0
#agenda = []
#data = (datetime.datetime.now())
#while(exit == 0):
#    
#    print(agenda)    
#    print("-"*40)
#    print("Hora:" + data.strftime("%X"))
#    print("Data: " + data.strftime("%x"))
#    print("Digite  2 : Limpar lista")
#    print("Digite  0 : sair")
#    print("Digite  3 : Editar lista")
#    action =  input("Insira o valor: ")
#    print("-"*40)
#    if action == "1" :
#        clear()
#        add()
#    elif action == "2":
#        clear()
#        limpar()
#    elif action == "3":
#        if len(agenda):
#            clear()
#            edit()
#        else:
#            print("Burro")
#    elif action == "0":
#        exit = 1


#agenda = ["Nome1","nome2", "nome3"]
#for nome in agenda:
#    print(nome)

#hora = int(input("Insira o número de horas: "))
#salario = int(input("Insira o salário por hora: "))
#res = salario*hora
#print(res)

from random import randint


def shuffle_words():

    user_input = input('Type any word to suffle: ')
    length = len(user_input)

    shuffled_word = []
    word_list = list(user_input)

    if length == 0:
        print('Error: cannot shuffle.')
    else:
        count = 0
        while count < length:
            random_idx = randint(0, len(word_list) - 1)
            shuffled_word.append(
                word_list.pop(random_idx)
            )
            #print(random_idx)
            count += 1
    
    print(*shuffled_word, sep="")


shuffle_words()