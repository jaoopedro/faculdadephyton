print("* VALIDAÇÃO DE CREDITO *")

nome = input("nome do cliente: ")
sal = float(input("Digite o salario Bruto: R$ "))
cpf = input("Tem Restrinção no cpf <S/N>: ")

if sal >1100 and cpf =='N':
    print("cliente",nome,'teve o credito Aprovado')
    print("Boas Compras")
else:
    print("Credito",nome,"Não teve o credito Reprovado")