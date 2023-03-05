import json

with open("Banco de dados.txt", "r") as arquivo:
    lista_dicionarios = []

    for linha in arquivo:
        partes = linha.strip().split(":")
        lista_dicionarios.append(partes)


cont = 0
for c in lista_dicionarios:
    if c == ['']:
        lista_dicionarios.pop(cont)
    cont += 1


bd_relatorio = {'Name': [], 'Position Title': [], 'Department': [], 'Employee Annual Salary': []}
nome = []
posicao = []
departamento = []
salario = []


for c in lista_dicionarios:
    if c[0] == 'Name':
        nome.append(c[1])
    elif c[0] == 'Position Title':
        posicao.append(c[1])
    elif c[0] == 'Department':
        departamento.append(c[1])
    else:
        salario.append(c[1])

bd_relatorio['Name'] = nome
bd_relatorio['Position Title'] = posicao
bd_relatorio['Department'] = departamento
bd_relatorio['Employee Annual Salary'] = salario

with open('transformado_json.json', 'w') as arquivo:
    arquivo.write(json.dumps(bd_relatorio))

