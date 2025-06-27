def validar_cpf(cpf):
   
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    return cpf[-2:] == f"{digito1}{digito2}"

cpf_input = input("Digite o CPF (apenas números ou com pontos e traço): ")
if validar_cpf(cpf_input):
    print("✅ CPF Válido!")
else:
    print("❌ CPF Inválido!")
