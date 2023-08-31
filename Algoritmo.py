from Classes import *
import os

def main():
        
    sair = False
    while sair == False:
        os.system("cls")
        print("---MENU---")
        print("01 - TAREFAS")
        print("02 - ADICIONAR TAREFAS")
        print("00 - SAIR")
        print("--------")
        print("")
        print("Qual opção deseja?")
        menu = int(input(">> "))
        os.system("pause")