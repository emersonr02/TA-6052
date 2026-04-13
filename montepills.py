# -*- coding: utf-8 -*-
# main.py
import database
import dados
import interface
import servicos

def inicializar_sistema():
    db = database.carregar_dados()
    if db:
        dados.clientes = db["clientes"]
        dados.regtransferencias = db["regtransferencias"]
        dados.contadorNIB = db["contadorNIB"]
        dados.contadorMovimentos = db["contadorMovimentos"]
    else:
        print("Arquivo não encontrado. Iniciando base vazia.")

def encerrar_e_salvar():
    pacote = {
        "clientes": dados.clientes,
        "regtransferencias": dados.regtransferencias,
        "contadorNIB": dados.contadorNIB,
        "contadorMovimentos": dados.contadorMovimentos
    }
    database.salvar_dados(pacote)

def main():
    inicializar_sistema() 
    while True:
        opcao = interface.menuInicial()
        
        if opcao == "1":
            meuNIB = servicos.loginUtilizador()
            if meuNIB:
                while True:
                    op_u = interface.menuUtilizador()
                    if op_u == "1": print(f"Saldo: {dados.clientes[meuNIB]['saldo']}€")
                    elif op_u == "2": servicos.realizarLevantamento(meuNIB)
                    elif op_u == "4": servicos.realizarTransferencia(meuNIB)
                    elif op_u == "6": break
        
        elif opcao == "666": 
            if servicos.loginAdmin():
                while True:
                    op_a = interface.menuAdmin()
                    if op_a == "1": servicos.criarCliente()
                    elif op_a == "6": break
                    
        elif opcao == "0":
            encerrar_e_salvar()
            print("Encerrando sistema...")
            break