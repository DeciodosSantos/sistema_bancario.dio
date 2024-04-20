valor_do_saque = 0
valor_do_deposito = 0
LIMITE_POR_SAQUE = 500
LIMITE_SAQUE_DIARIO = 0
Saldo = 0
extrato = ""

while True:
   

    print("Qual operação deseja realizar?", "1:DEPOSITO", "2:SAQUE", "3:EXTRATO", "4:SAIR" )
    operacao = int(input())

    if operacao == 1 :
        
        print("digite valor do deposito ")
        valor_do_deposito = float(input())
        
        if valor_do_deposito > 0:
            Saldo += valor_do_deposito
            extrato += f"Depósito: + R$ {valor_do_deposito:.2f}\n"

        else:
            print("voce nao pode realizar essa operação")

    if operacao == 2:
        
        print("digite o valor do saque")
        valor_do_saque = float(input())
        
        if valor_do_saque > LIMITE_POR_SAQUE:
            print("valor excede limite por saque")
            print("seu saldo e de R$", "%.2f" %Saldo)
        
        elif LIMITE_SAQUE_DIARIO == 3 :
            print("voce nao pode sacar mais")
            print("seu saldo e de R$", "%.2f" %Saldo)
        
        elif Saldo <= 0:
            print("voce nao tem saldo para realizar essa operração")
        
        else:
            Saldo -= valor_do_saque
            extrato += f"Saque: - R$ {valor_do_saque:.2f}\n"
            LIMITE_SAQUE_DIARIO += 1 
            print("seu saldo e de R$", "%.2f" %Saldo)

    if operacao == 3 :
       
       extrato +=  f"Saldo atual: R$ {Saldo:.2f}\n"
       print(extrato)
       print("seu saldo e de R$", "%.2f" %Saldo)
    
    if operacao == 4:
        print("obrigado por usar nosso banco")
        break