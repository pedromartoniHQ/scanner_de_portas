
import socket as s
from sys import exit
from datetime import datetime

def escaneamento_port(alvo, porta_inicial, porta_final):
    # Correção da Linha 11: Validar o host antes de iniciar o loop
    try:
        alvo_resolvido = s.gethostbyname(alvo)
    except s.gaierror:
        return None # Retorna None para indicar que o host é inválido

    print(f'\nEscaneando o alvo: {alvo_resolvido}')
    portas_abertas = []

    for porta in range(porta_inicial, porta_final + 1):
        with s.socket(s.AF_INET, s.SOCK_STREAM) as sock:
            sock.settimeout(0.1)
            if sock.connect_ex((alvo_resolvido, porta)) == 0:
                print(f'✅ Porta {porta} — ABERTA')
                portas_abertas.append(porta)
    return portas_abertas

if __name__ == '__main__':
    try:
        # Correção da Linha 38 e arredores: Organização do fluxo de entrada
        alvo_input = input("Digite o IP alvo: ")
        p_ini = int(input("Digite a porta inicial: "))
        p_fim = int(input("Digite a porta final: "))

        resultado = escaneamento_port(alvo_input, p_ini, p_fim)
        horario_atual=datetime.now().strftime("%d/%m/%y")
        if resultado is None:
            print("❌ Erro: Host inválido ou inacessível.")
        else:
            print(f'\n📋 Scan finalizado! Portas abertas: {resultado}')
        print(f"o scanner foi iniciado em: {horario_atual}")

    except ValueError:
        print("❌ Erro: Digite números válidos para as portas.")
    except KeyboardInterrupt:
        print("\nSaindo...")
        exit()

