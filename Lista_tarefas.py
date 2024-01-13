import pymongo
import sys

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Lista_De_Tarefas"]
collection = db["tarefas da col"]

def adicionar_tarefa():
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    horario = input("Horário: ")
    data = input("Data: ")
    cod = input("Código: ")
    importancia = input("Importância: ")
    estado = input("Estado (1 para sim, 0 para não): ")

    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "horario": horario,
        "data": data,
        "cod": cod,
        "importancia": importancia,
        "estado": int(estado),
    }

    collection.insert_one(tarefa)
    print("Tarefa adicionada com sucesso!")

def alterar_tarefa():
    codigo = input("Digite o Código da Tarefa que deseja alterar: ")
    tarefa = collection.find_one({"cod": codigo})

    if tarefa:
        print("Tarefa encontrada:")
        for key, value in tarefa.items():
            print(f"{key}: {value}")

        opcao = input("O que você deseja alterar (Digite o nome do campo) ou 'cancelar' para sair: ")
        if opcao != "cancelar":
            novo_valor = input(f"Digite o novo valor para {opcao}: ")
            collection.update_one({"cod": codigo}, {"$set": {opcao: novo_valor}})
            print("Tarefa alterada com sucesso!")

    else:
        print("Tarefa não encontrada.")

def excluir_tarefa():
    codigo = input("Digite o Código da Tarefa que deseja excluir: ")
    result = collection.delete_one({"cod": codigo})

    if result.deleted_count == 1:
        print("Tarefa excluída com sucesso!")
        sys.stdout.flush()
    else:
        print("Tarefa não encontrada.")

def listar_tarefas():
    tarefas = collection.find()
    for tarefa in tarefas:
        print("\nTarefa:")
        for key, value in tarefa.items():
            print(f"{key}: {value}")

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar Tarefa")
        print("2. Alterar Tarefa")
        print("3. Excluir Tarefa")
        print("4. Listar Tarefas")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa()

        elif escolha == "2":
            alterar_tarefa()

        elif escolha == "3":
            excluir_tarefa()

        elif escolha == "4":
            listar_tarefas()

        elif escolha == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()