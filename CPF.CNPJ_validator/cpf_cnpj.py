from validate_docbr import CPF, CNPJ

cpf = CPF()
cnpj = CNPJ()

def unmask(number):
    number_only = ''.join(filter(str.isdigit, number))
    return number_only

input_number = input("Informe seu CPF ou CNPJ:\n")

number_only = unmask(input_number)

if len(number_only) == 11 and cpf.validate(number_only):
        formated = cpf.mask(number_only)
        print(f"CPF: {formated} é valido")
elif len(number_only) == 14 and cnpj.validate(number_only):
    formated = cnpj.mask(number_only)
    print(f"CNPJ: {formated} é valido")
else:
    print("Seu CPF ou CNPJ não existe ou é inválido")