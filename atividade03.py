def ConfirmaNome():
    print("\ninsira seu nome compelto sem conjuncoes(de, da, etc..)")
    nome=input("nome:>")
    nome_split = nome.split()
    print(nome_split)
    for x in nome_split:        
        if len(x)>3:
            pass
        else:
            print("\nnome invalido:")
            print("1- para digitar de novo  2- para sair")#qualquer numero de dois pra cima sai
            continuar = int(input(">"))
            if continuar==1:
                ConfirmaNome()
            else:
                return False
    return nome

def ConfirmaSenha():
    print("\ninsira a senha contendo um número e um caractere especial ex: @") 
    senha=input(">")
    if len(senha)>5:
        for x in ["1","2","3","4","5","6","7","8","9"]:
            for i in senha:
                if x==i:
                    if "@" or "_" or "-" or "*" or "#" or "$" in senha:
                        return senha
    print("\nsenha invalida:")
    print("1- para digitar de novo  2- para sair")
    continuar = int(input(">"))
    if continuar==1:
        ConfirmaSenha()
    else:
        return False

def ConfirmaEmail():
    email=input("digite seu email:>")
    if "@" in email:
        return email
    else:
        print("\nemail invalida:")
    print("1- para digitar de novo  2- para sair")
    continuar = int(input(">"))
    if continuar==1:
        ConfirmaEmail()
    else:
        return False

def Cadastro():
    nome=ConfirmaNome()
    senha=ConfirmaSenha()
    email=ConfirmaEmail()
    cpf=input("cpf:")
    endereco=input("endereço:")
    celular=input("celular:")
    if nome==False or senha==False or email==False:
        print("credenciais incoretas")
        SystemExit()
    else:
        lista_nome.append(nome)
        lista_senha.append(senha)
        lista_email.append(email)
        lista_endereco.append(endereco)
        lista_cpf.append(cpf)
        lista_celular.append(celular)
        #lista_codigo=lista_nome.index(nome)
        codigo=lista_nome.index(nome)
        lista_saldo.append(0)
        print(codigo)
        ContaEscolha(codigo)

def Depositar(codigo):
    deposito=float(input("\nquanto voce deseja depositar:>"))
    if deposito>0:
        lista_saldo[codigo]+=deposito
    else:
        print("valor invalido")
        return

def Sacar(codigo):
    sacar=float(input("\nquanto voce deseja sacar:>"))
    if sacar <lista_saldo[codigo]:
        lista_saldo[codigo]=(lista_saldo[codigo])-(sacar)

def ConferirSaldo(codigo):
    print("\nseu saldo:", lista_saldo[codigo], "$")

def Trasferir(codigo):
    codigo_trasferencia=int(input("para que conta voce que mandar(codigo da conta enviar para uam conta inexiste resualtara em erro):"))
    valor_trasferencia=float(input("valor para enviar:"))
    if valor_trasferencia<=lista_saldo[codigo]:
        lista_saldo[codigo]+= -valor_trasferencia
        lista_saldo[codigo_trasferencia]+=valor_trasferencia

def ContaEscolha(codigo):
    while True:
        print("\noque vc deseja fazer na sua conta:")
        print("1-depositar")
        print("2-sacar")
        print("3-conferir o saldo")
        print("4-trasferir")
        print("5-encerar conta")
        escolha=int(input(">"))
        if escolha==1:
            Depositar(codigo)
        elif escolha==2:
            Sacar(codigo)
        elif escolha==3:
            ConferirSaldo(codigo)
        elif escolha==4:
            Trasferir(codigo)
        elif escolha==5:
            return
        print(lista_saldo)



def Escolha():
    while True:
        print("1-cadastrar 5-sair ")
        escolha = int(input(">"))
        if(escolha==5):
            break
        elif(escolha==1):
            Cadastro()
        elif(escolha==2):
            pass
    return
lista_nome=[]
lista_senha=[]
lista_email=[]
lista_endereco=[]
lista_cpf=[]
lista_celular=[]
lista_saldo=[]
lista_codigo=[]#pra facilitar a indentifcação da usuario
Escolha()