tarefas = []

def salvar_tarefas():
  
  with open("tarefas.txt", "w") as arquivo:
    for tarefa in tarefas:
      arquivo.write(tarefa + "\n")

def ver_tarefas():
 
 if not tarefas:
  print("Nenhuma tarefa ainda!")
  return
   
 for index, tarefa in enumerate(tarefas):
  print(f"{index} - {tarefa} ")

def concluir_tarefa():
  try:
   itemConcluido = int(input("Digite o item que deseja concluir: "))
   tarefa_removida = tarefas.pop(itemConcluido)
   print(f"Item '{tarefa_removida}' concluído com sucesso!")

  except ValueError:
    print("Digite um número válido!")

  except IndexError:
    print("Não existe tarefa com esse número!")
  

while True:
  print("\n1 Ver tarefas")
  print("2 Adicionar tarefa")
  print("3 Concluir tarefa")
  print("4 Sair")

  opcao = input("Escolha: ")

  try:
    opcao = int(opcao)
  except ValueError:
    print("Digite um número válido para a opção!")
    continue
 
  if opcao == 1:
    ver_tarefas()
  elif opcao == 2:
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")
  elif opcao == 3:
    concluir_tarefa()
    print("Tarefa concluida!")
  elif opcao == 4:
    salvar_tarefas()
    print("Tarefas salvas. Saindo..")
    break
  

  

