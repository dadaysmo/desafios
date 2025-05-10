class ListaDeTarefas():
    def __init__(self):
        self.lista = []

    def listarTarefa(self):
        if not self.lista:
            print('nenhuma tarefa encontrada.')
        else:
            print(f'Aqui está sua lista princesa:')
            for i, tarefa in enumerate(self.lista, 1):
                print(f'{i}. {tarefa}')
        print()

    def adicionarTarefa(self, tarefa):
        self.lista.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!\n")

    def deletarTarefa(self, indice):
        if 0 < indice <= len(self.lista):
            remover = self.lista.pop(indice - 1)
            print(f'Tarefa {remover} removida com sucesso!\n')
        else:
            print(f'Nenhuma tarefa encontrada, índice inexistente.\n')

def menu():
    lista = ListaDeTarefas()
    while True:
        print('-------------------------------')
        print('-======== Lista de Day =======-')
        print('-------------------------------')
        print('--- 1  -- 2  ----- 3  --   4---')
        print('--add! - remove - list - sair--')
        print('-------------------------------')
        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            tarefa = input('Digite a nova tarefa: ')
            lista.adicionarTarefa(tarefa)
        elif escolha == 2:
            try:
                numero = int(input('Digite o número da tarefa que deseja excluir: '))
                lista.deletarTarefa(numero)
            except ValueError:
                print('Digite um número válido,\n')
        elif escolha == 3:
            lista.listarTarefa()
        elif escolha == 4:
            print('Saindo do menu...')
            break
        else:
            print('Comando inválido.\n')

menu()