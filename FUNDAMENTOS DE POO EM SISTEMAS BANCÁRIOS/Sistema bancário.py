class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

    def saldo_atual(self):
        return self.saldo


# Entrada
titular = input().strip()
valores = input().split(",")  # exemplo: 100, -50, 200, -300
valores = [int(v.strip()) for v in valores]

# Criando a conta
conta = ContaBancaria(titular)

# Processando as operações
operacoes = []

for valor in valores:
    if valor > 0:
        conta.depositar(valor)
        operacoes.append(f"+{valor}")
    elif valor < 0:
        if conta.sacar(-valor):
            operacoes.append(f"{valor}")
        else:
            operacoes.append("Saque não permitido")

# Saída formatada
print(f"Operações: {', '.join(operacoes)}; Saldo: {conta.saldo_atual()}")
