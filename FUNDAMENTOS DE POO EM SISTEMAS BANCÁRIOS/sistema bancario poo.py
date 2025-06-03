class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        return f"+{valor}"

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"-{valor}"
        else:
            return "Saque não permitido"

    def saldo_atual(self):
        return self.saldo


# Entrada
titular = input()
valores = input().split(", ")

# Criação da conta
conta = ContaBancaria(titular)

# Processamento das operações
operacoes = []
for val in valores:
    val_int = int(val)
    if val_int > 0:
        operacoes.append(conta.depositar(val_int))
    elif val_int < 0:
        resultado = conta.sacar(abs(val_int))
        operacoes.append(resultado)
    else:
        operacoes.append("0")

# Saída
print(f"Operações: {', '.join(operacoes)}; Saldo: {conta.saldo_atual()}")
