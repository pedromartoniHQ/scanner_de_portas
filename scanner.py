import socket as s
from sys import exit


def port_scan(alvo, porta_inicial, porta_final):
    print(f'\nEscaneando o alvo: {alvo}')
    print(f'Portas: {porta_inicial} até {porta_final}\n')
    portas_abertas = []

    for porta in range(porta_inicial, porta_final + 1):
        sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        sock.settimeout(1)

        resultado = sock.connect_ex((alvo, porta))

        if resultado == 0:
            print(f'✅ Porta {porta} — ABERTA')
            portas_abertas.append(porta)
        else:
            print(f'❌ Porta {porta} — fechada')

        sock.close()

    return portas_abertas


if __name__ == '__main__':
    alvo = input("Digite o IP alvo: ")
    porta_inicial = int(input("Digite a porta inicial: "))
    porta_final = int(input("Digite a porta final: "))

    portas_abertas = port_scan(alvo, porta_inicial, porta_final)

    print(f'\n📋 Scan finalizado!')
    print(f'Portas abertas: {portas_abertas}')