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
    valor_trasferencia=float(input("valor para enviar 0 cancela a operacao:"))
    if valor_trasferencia<=0:
        return
    elif valor_trasferencia<=lista_saldo[codigo]:
        lista_saldo[codigo]+= -valor_trasferencia
        lista_saldo[codigo_trasferencia]+=valor_trasferencia
    else:
        print("\nvoce n possui este valor!!!!")
        return


def Login():
    login_email=input("\ndigiti seu email:>")
    login_senha=input("digite sua senha:>")
    if login_email in lista_email:
        if (login_senha in lista_senha) and (lista_email.index(login_email)==lista_senha.index(login_senha)):
                ContaEscolha(lista_email.index(login_email))
        else:
            print("senha errada digite o email e a senha novamente:")
            Login()
    else:
        print("\nemail nao existe ou n foi cadastrado:")
        escolha=input("1-tentar novamente  qualquer tecla-voltar:>")
        if escolha =="1":
            Login()
        else:
            return

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

def ConsultarCliente(codigo):
    print("\ncodigo:",codigo)
    print("nome:",lista_nome[codigo])
    print("senha:",lista_senha[codigo])
    print("email:",lista_email[codigo])
    print("endereco:",lista_endereco[codigo])
    print("cpf:",lista_cpf[codigo])
    print("celular:",lista_celular[codigo])
    print("saldo:",lista_saldo[codigo])

def AdministracaoLogin():
    nome=input("\nnome:")
    senha=input("senha:")
    if nome=="admin" and senha=="123456":
        return True
    else:
        return False
def Deletar(codigo):
    del lista_nome[codigo]
    del lista_senha[codigo]
    del lista_email[codigo]
    del lista_endereco[codigo]
    del lista_cpf[codigo]
    del lista_celular[codigo]
    del lista_saldo[codigo]
    del lista_codigo[codigo]

def Atualizar(codigo):
    print("\ninformacoes atuais do cliente:")
    ConsultarCliente(codigo)
    lista_nome[codigo]=ConfirmaNome()
    lista_senha[codigo]=ConfirmaSenha()
    lista_email[codigo]=ConfirmaEmail()
    lista_endereco[codigo]=input("endereco")
    lista_cpf[codigo]=input("cpf")
    lista_celular[codigo]=input("celular")
    lista_saldo[codigo]=input("saldo")

def ConsultarLista():
    for codigo in range(len(lista_nome)):
        print("\ncodigo:",codigo)
        print("nome:",lista_nome[codigo])
        print("senha:",lista_senha[codigo])
        print("email:",lista_email[codigo])
        print("endereco:",lista_endereco[codigo])
        print("cpf:",lista_cpf[codigo])
        print("celular:",lista_celular[codigo])
        print("saldo:",lista_saldo[codigo])

def Administracao():
    if AdministracaoLogin()==True:
        while True:
            print("\n1-consultar cliente")
            print("2-consultar lista de clientes")
            print("3-deletar um cliente")
            print("4-atualizar dados de um cliente")
            escolha=int(input(">"))
            if escolha==1:
                codigo=int(input("\ncodigo do cliente a ser consultado:>"))
                ConsultarCliente(codigo)
            if escolha==2:
                ConsultarLista()
            if escolha==3:
                codigo=int(input("\ncodigo do cliente a ser deletado:>"))
                Deletar(codigo)
            if escolha==4:
                codigo=int(input("\ncodigo do cliente a ser atualizado:>"))
                Atualizar(codigo)
            if escolha==5:
                break
    else:
        print("login errrado")
        return

def Escolha():
    while True:
        print("1-cadastrar 2-login 3-administracao  3-sair ")
        escolha = int(input(">"))
        if(escolha==1):
            Cadastro()
        elif(escolha==2):
            Login()
        elif(escolha==3):
            Administracao()
        if(escolha==3):
            break
    return
#da pra botar valores na lista para testar
lista_nome=[]
lista_senha=[]
lista_email=[]
lista_endereco=[]
lista_cpf=[]
lista_celular=[]
lista_saldo=[]
lista_codigo=[]#pra facilitar a indentifcação da usuario
Escolha()