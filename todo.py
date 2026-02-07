tarefas = []


def ver_tarefas():
 
 if not tarefas:
  print("Nenhuma tarefa ainda!")
  return
   
 for index, tarefa in enumerate(tarefas):
  print(f"{index} - {tarefa} ")

def concluir_tarefa():
  itemConcluido = int(input("Digite o item que deseja concluir: "))
  if itemConcluido == ' ':
    print("Digite um número!")
  elif itemConcluido == ''
  concluir = tarefas.pop(itemConcluido)
  print("Item {} concluído com sucesso!".format(tarefas.index.value))

while True:
  print("\n1 Ver tarefas")
  print("2 Adicionar tarefa")
  print("3 Concluir tarefa")
  print("4 Sair")

  opcao = input("Escolha: ")

  opcao = int(opcao)
 
  if opcao == 1:
    ver_tarefas()
  elif opcao == 2:
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")
  elif opcao == 3:
    concluir_tarefa()
    print("Tarefa concluida!")
  

  

