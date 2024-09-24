class ContaBancaria:
    def __init__(self, titular, cpf, saldo=0.0):
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo

    def mostrar_conta(self):
        return f"TITULAR: {self.titular}\nCPF: {self.cpf}\nSALDO: R$ {self.saldo:.2f}"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"DEPÓSITO DE R$ {valor:.2f} REALIZADO COM SUCESSO!"
        else:
            return "VALOR DE DEPÓSITO INVÁLIDO."

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"SAQUE DE R$ {valor:.2f} REALIZADO COM SUCESSO!"
        else:
            return "SALDO INSUFICIENTE OU VALOR INVÁLIDO."

    def verificar_saldo(self):
        return f"SALDO ATUAL: R$ {self.saldo:.2f}"


class ContaCorrente(ContaBancaria):
    def __init__(self, titular, cpf, numerocc, saldo=0.0):
        super().__init__(titular, cpf, saldo)
        self.numerocc = numerocc

    def mostrarcc(self):
        return f"{self.mostrar_conta()}\nNÚMERO DA CONTA CORRENTE: {self.numerocc}"


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, cpf, rendimento, saldo=0.0):
        super().__init__(titular, cpf, saldo)
        self.rendimento = rendimento

    def ver_rendimento(self):
        return f"TAXA DE RENDIMENTO: {self.rendimento * 100:.2f}%"

    def render(self):
        rendimento = self.saldo * self.rendimento
        self.saldo += rendimento
        return f"RENDIMENTO APLICADO. NOVO SALDO: R$ {self.saldo:.2f}"


def menu():
    contas = []
    while True:
        print("\n" + "="*40)
        print("MENU PRINCIPAL BANCO CLAYTON ʕ•́ᴥ•̀ʔっ" )
        print("="*40)
        print("1. CRIAR CONTA CORRENTE")
        print("2. CRIAR CONTA POUPANÇA")
        print("3. DEPOSITAR")
        print("4. SACAR")
        print("5. VERIFICAR SALDO")
        print("6. MOSTRAR CONTA CORRENTE")
        print("7. VER RENDIMENTO DA POUPANÇA")
        print("8. APLICAR RENDIMENTO NA POUPANÇA")
        print("9. SAIR")
        print("="*40)
        
        opcao = input("ESCOLHA UMA OPÇÃO: ")
        
        if opcao == "1":
            titular = input("NOME DO TITULAR: ")
            cpf = input("CPF DO TITULAR: ")
            numerocc = input("NÚMERO DA CONTA CORRENTE: ")
            conta_corrente = ContaCorrente(titular, cpf, numerocc)
            contas.append(conta_corrente)
            print("CONTA CORRENTE CRIADA COM SUCESSO!")
        
        elif opcao == "2":
            titular = input("NOME DO TITULAR: ")
            cpf = input("CPF DO TITULAR: ")
            rendimento = float(input("TAXA DE RENDIMENTO DA POUPANÇA (EM DECIMAL, EX: 0.02 PARA 2%): "))
            conta_poupanca = ContaPoupanca(titular, cpf, rendimento)
            contas.append(conta_poupanca)
            print("CONTA POUPANÇA CRIADA COM SUCESSO!")
        
        elif opcao == "3":
            cpf = input("CPF DA CONTA: ")
            valor = float(input("VALOR A SER DEPOSITADO: "))
            conta = next((c for c in contas if c.cpf == cpf), None)
            if conta:
                print(conta.depositar(valor))
            else:
                print("CONTA NÃO ENCONTRADA.")
        
        elif opcao == "4":
            cpf = input("CPF DA CONTA: ")
            valor = float(input("VALOR A SER SACADO: "))
            conta = next((c for c in contas if c.cpf == cpf), None)
            if conta:
                print(conta.sacar(valor))
            else:
                print("CONTA NÃO ENCONTRADA.")
        
        elif opcao == "5":
            cpf = input("CPF DA CONTA: ")
            conta = next((c for c in contas if c.cpf == cpf), None)
            if conta:
                print(conta.verificar_saldo())
            else:
                print("CONTA NÃO ENCONTRADA.")
        
        elif opcao == "6":
            cpf = input("CPF DA CONTA CORRENTE: ")
            conta = next((c for c in contas if isinstance(c, ContaCorrente) and c.cpf == cpf), None)
            if conta:
                print(conta.mostrarcc())
            else:
                print("CONTA CORRENTE NÃO ENCONTRADA.")
        
        elif opcao == "7":
            cpf = input("CPF DA CONTA POUPANÇA: ")
            conta = next((c for c in contas if isinstance(c, ContaPoupanca) and c.cpf == cpf), None)
            if conta:
                print(conta.ver_rendimento())
            else:
                print("CONTA POUPANÇA NÃO ENCONTRADA.")
        
        elif opcao == "8":
            cpf = input("CPF DA CONTA POUPANÇA: ")
            conta = next((c for c in contas if isinstance(c, ContaPoupanca) and c.cpf == cpf), None)
            if conta:
                print(conta.render())
            else:
                print("CONTA POUPANÇA NÃO ENCONTRADA.")
        
        elif opcao == "9":
            print("SAINDO DO SISTEMAA... 👍( ͡❛ ͜ʖ ͡❛👍)")
            break
        
        else:
            print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")

if __name__ == "__main__":
    menu()