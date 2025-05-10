def gay():
    print('------------------------')
    print('----- Lista de Day -----')
    print('------------------------')
    print('--add! - remove - list--')
    print('------------------------')


class ListaDeTarefas():
    def __init__(self):
        self.lista = ['a', 'b', 'c', 'd']

    def listarTarefa(self):
        if not self.lista:
            print('nenhuma tarefa encontrada.')
        else:
            print(f'\nAqui está sua lista princesa:')
            for i, tarefa in enumerate(self.lista, 1):
                print(f'{i}. {tarefa}')
        print()

    def adicionarTarefa(self, tarefa):
        self.lista.append(tarefa)
        print(f'Tarefa adicionada com sucesso!')

    def deletarTarefa(self, indice):
        if 0 < indice < len((self.lista):
            remover = self.lista.pop(indice -1)
            print(f'Tarefa {remover} removida com sucesso!\n')
