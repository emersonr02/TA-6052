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
        dados.stock_notas = db.get("stock_notas", dados.stock_notas)
    else:
        print("Arquivo não encontrado. Iniciando base vazia.")

def encerrar_e_salvar():
    pacote = {
        "clientes": dados.clientes,
        "regtransferencias": dados.regtransferencias,
        "contadorNIB": dados.contadorNIB,
        "contadorMovimentos": dados.contadorMovimentos,
        "stock_notas": dados.stock_notas,
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
                    if op_u == "1": 
                        servicos.consultarSaldo(meuNIB) 
                    elif op_u == "2": 
                        servicos.realizarLevantamento(meuNIB)
                    elif op_u == "3": 
                        servicos.realizarDeposito(meuNIB)   
                    elif op_u == "4": 
                        servicos.realizarTransferencia(meuNIB)
                    elif op_u == "5": 
                        servicos.consultarMovimentos(meuNIB) 
                    elif op_u == "6": 
                        break
        
        elif opcao == "666": 
            if servicos.loginAdmin():
                while True:
                    op_a = interface.menuAdmin()
                    if op_a == "1": 
                        servicos.criarCliente()
                    elif op_a == "2": 
                        servicos.listarClientes()     
                    elif op_a == "3": 
                        servicos.pesquisarMovimentacao() 
                    elif op_a == "4": 
                        servicos.apagarCliente()         
                    elif op_a == "5": 
                        servicos.verEstatisticas()       
                    elif op_a == "6": 
                        break
        elif opcao == "0":
            encerrar_e_salvar() 
            print("Encerrando sistema... Ate a proxima!")
            break

if __name__ == "__main__":
    main()