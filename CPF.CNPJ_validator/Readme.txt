Nesse codigo para validar CPF e CNPJ foi utilizado a biblioteca Python( validate_docbr)

instalação = pip install validate_docbr

como usar: from validate_docbr import CPF, CNPJ

Essa biblioteca( validate_docbr ) possui duas Classes, São elas: CPF() e CNPJ

A Classes CPF e CNPJ, possui os mesmos metodos, são eles : validate(), mask(), unmask(), generate(), generate_list(n),validate_list(list)

Metodos:

    validate() - esse metodo retorna unicamente (True) ou (False), com base nas verificações citadas abaixo.

        -  Limpeza de entrada: remove todos os caracteres que não são números

        -  Checagem de tamanho: Aqui ele realiza uma checagem do tamanho do cpf( deve ser 11) e do CNPJ, mas a uma possivel falha na validação do CPF.
            - Falha na Checagem de tamanho: Com base em Testes realizados é possivel que ele aceite entradas com menos dígitos, após limpeza
                                            entradas com menos de 11 digitos, se passarem, resultando em uma possivel falha, que vai retornar (True).

        -  Números Repitidos: Retornam (False)
        -  Cálculo: Aplica o calculo do (módulo 11)

    mask() -  Esse metodo vai formatar o CPF/CNPJ para a exibição no padrão brasileiro, Descrição de uso abaixo:

        Exemplo( CPF ): entrada(11111111111) - formatação = cpf.mask(entrada) - saída esperada: "111.111.111-11"
        Exemplo( CNPJ ):

    unmask() - Esse metodo remove todos os caracteres não numéricos do CPF ou CNPJ

        Exemplo( CPF ): entrada(111.111.111-11) - remoção = cpf.unmask(entrada) - saída esperada: "11111111111"
        Exemplo( CNPJ ):