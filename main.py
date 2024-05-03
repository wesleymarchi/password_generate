import generate_password as generate


if __name__ == '__main__':
    length = int(input('Quantos caracteres a senha deve conter?\n'))
    question = int(input("Quantas senhas gostaria de gerar?\n"))
    for pw in range(question):
        print(generate.generate_password(length))
