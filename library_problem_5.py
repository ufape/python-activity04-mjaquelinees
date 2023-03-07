def e_primo(num):
    """
    Verifica se um número é primo ou não.
    :param num: o número a ser verificado
    :return: True se o número for primo, False caso contrário
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def teste():
    n = int(input("Digite quantos testes realizará: "))
    for i in range(1, n+1):
        x = int(input("Teste {}: ".format(i)))
        if e_primo(x):
            print("{} é primo.".format(x))
        else:
            print("{} não é primo.".format(x))


