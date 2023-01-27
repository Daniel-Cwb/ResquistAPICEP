import requests

#
# Colocando dentro da função Main
#
def main():
    print("########################")
    print("##### Consulta CEP #####")
    print("########################")

    cep = input('Digite o CEP: ')


    #
    # Validando se a quantidade e Caracter é 8, CEP tem 8 caracter 81170-7855
    #
    while len(cep) != 8:
        print('Quantidade de caracter invalida!')
        main()
    else:
        print('Quantidade de caracter está Correta!')

    r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    #
    # Validando se o CEP está correto
    #
    result_data = r.json()

    #
    # Validando se o resultado não contém erro
    #

    if 'erro' not in result_data:
        print('==> CEP Encontrado <==')
        print('CEP: {}'.format(result_data['cep']))
        print('UF: {}'.format(result_data['uf']))
        print('DDD: {}'.format(result_data['ddd']))
        print('Cidade: {}'.format(result_data['localidade']))
        print('Bairro: {}'.format(result_data['bairro']))
        print('Logradouro: {}'.format(result_data['logradouro']))
    else:
        print('{}: CEP Inválido!!!!'.format(cep))


if __name__ == '__main__':
    main()
