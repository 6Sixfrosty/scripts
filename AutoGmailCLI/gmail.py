# ====================
# Bibliotecas
from dotenv import dotenv_values, set_key
from pathlib import Path
from time import sleep
import os
import yagmail

# ====================
# Cores
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

# ====================
# Variáveis globais
env_path = Path(".env")
credentials = {}
GMAIL = None

# ====================
# Funções utilitárias
def Clean():
    os.system("cls")
    os.system("clear")
Clean()
# ====================
# Inicio do progama
input("""
===============================
💻          E-mailzada         💻 
===============================
Olá! Me chamo E-mailzada.
Sou eu quem vai facilitar o seu envio de e-mails.

Pressione [Enter] para iniciar...
""")

def load_credentials():
    global credentials
    credentials = dotenv_values(env_path)
def init_gmail():
    """Inicializa GMAIL apenas se email e senha existirem"""
    global GMAIL
    if credentials.get("EMAIL") and credentials.get("PASS"):
        GMAIL = yagmail.SMTP(credentials["EMAIL"], credentials["PASS"])
    else:
        print("❌ E-mail ou senha não configurados.")

# ====================
# Configuração do .env
def configure_env():
    load_credentials()

    if not credentials.get("EMAIL"):
        set_key(env_path, "EMAIL", "")
        credentials["EMAIL"] = ""
    if not credentials.get("PASS"):
        set_key(env_path, "PASS", "")
        credentials["PASS"] = ""    

# ====================
# Configuração do email e senha(de app) estaticos
def Estatic_smtp_credentials():
    Clean()
    configuratonBOLEAN=False
    while True:
        try:
            choice = int(input("""
    ╔══════════════════════════════════════════╗
    ║ CONFIGURAÇÃO DO E-MAIL ( REMETENTE )     ║
    ║══════════════════════════════════════════║
    ║[1] PROSSEGUIR COM A CONFIGURAÇÃO         ║
    ║[2] VOLTAR                                ║
    ║══════════════════════════════════════════╝
    
    Opção Desejada: """))
            match choice:
                case 1: sleep(.8); configuratonBOLEAN=True ;break
                case 2: print(); print("Voltando...."); sleep(.8); Clean(); menu();break
                case _: print("opção invalida")
        except ValueError:
            print("Entrada invalida, insira apenas números")

    while configuratonBOLEAN:
        email_defined = input(f"\n{CYAN}>>> INFORME O E-MAIL REMETENTE (GMAIL ONLY) <<<{RESET}\n{YELLOW}→ Informe o E-mail: {RESET}")
        pass_defined = input(f"{CYAN}>>> SENHA DE APP DO E-MAIL (REMETENTE) <<<{RESET}\n{YELLOW}→ Informe a Senha de APP: {RESET}")
        Clean()
        try:
            user_input = int(input(f"""
===================================
{CYAN}CONFIGURAÇÃO ATUAL{RESET}
Email: {email_defined}
Senha: {pass_defined}
===================================
[1] Salvar
[2] Modificar
===================================
Opção Desejada: """))
            match user_input:
                case 1:
                    print("Salvando ...."); 
                    set_key(env_path, "EMAIL", email_defined)
                    set_key(env_path, "PASS", pass_defined)
                    load_credentials()
                    sleep(1); print("Credenciais Salvas, voltando para o menu"); Clean(); menu();break
                case 2:
                    continue
                case _:
                    print("Opção invalida")
                    continue
        except ValueError:
            print("Entrada invalida, insira apenas números")

# ====================
# Função de Envio Simples
def simple_send():
    info = {
        "to": input("Informe o E-mail( Destinatário): "),
        "subject": input("\nInforme o Assunto da mensagem: "),
        "contents": input("\nInforme o conteudo da mensagem:")
        }
    GMAIL.send(
        to=info["to"],
        subject=info["subject"],
        contents=info["contents"]
    )
    Clean(); input(f"Informações:{info.values()}\nE-mail Enviado com sucesso\nPressione ENTER para voltar pro Menu....")
    menu()



# ====================
# Menu principal
def menu():
        if not credentials.get("EMAIL"):
            EmailExistsTest = "❌ Nenhum e-mail de remetente encontrado!."
        else:
            EmailExistsTest = credentials["EMAIL"]
        try: 
            choice = int(input(f"""
    =======================================
    📨                                     📨
    📨         CENTRAL DE ENVIO            📨
    📨                                     📨
    =======================================
    📨  E-mail Remetente =  ( {EmailExistsTest} ) 
    =======================================
    📨  Observação: Se não definir um E-mail de remetente( Estático )
                   O progama sempre vai pedir um E-mail de remetente
    =======================================
    Selecione uma opção de envio:

    [1] 📤 Envio simples — envia uma mensagem apenas para um e-mail
    [2] 📝 Envio em Massa — mesma mensagem para vários destinatários 
    [3] ⚙️ Configurar E-mails de Destinatário (Opção em Desenvolvimento) 
    [4] ⚙️ Configurar Remetente( Estatico )— definir e-mail e senha de app  
    [0] ❌ Sair — encerrar o programa

    ========================================
    Digite o número da opção desejada: """))
        except ValueError:
            Clean()
            print("❌ Opção inválida. Digite apenas números.")
            sleep(2); Clean()
            menu()
        if choice == 1 or 2:
            init_gmail()
        match choice:
            case 1: Clean(); simple_send()
            case 2: Clean(); print("DESENv"); sleep(2); Clean(); menu()
            case 3: Clean(); print("Opção em desenvolvimento"); sleep(2); Clean(); menu()
            case 4: Clean(); Estatic_smtp_credentials()
            case 0: print("\n\nAdeusss :)"); sleep(.3); Clean(); print("Progama encerrado")

# ====================
# Função inicial
def Env_Data():
    print("Veficador iniciado\n"); sleep(.8)
    print("Procurando arquivo [.env]")
    sleep(.8); print("....."); sleep(.8); print("......"); sleep(.8); print

    while True:
        if env_path.exists():
            print("Arquivo [.env] encontrado.\n"); sleep(.8)
            print("Configurando arquivo existente..."); sleep(2)
            configure_env()
            Clean()
            break

        try:
            choice = int(input("""
Arquivo [.env] não foi encontrado!
[1] Procurar novamente
[2] Criar novo arquivo [.env]
Digite o número da opção desejada: """))
        except ValueError:
            print("❌ Opção inválida. Digite apenas números.")
            continue

        if choice == 1:
            print("🔍 Rechecando arquivo...")
            sleep(1)
            continue

        elif choice == 2:
            env_path.touch()
            print("✅ Arquivo [.env] criado com sucesso.")
            sleep(.5)
            print("Configurando o arquivo [.env]")
            configure_env()
            print("O arquivo [.env] foi configurado\n"); sleep(.5)
            print("Saindo do verificador..."); sleep(.5)
            Clean()
            break
        else:
            print("❌ Opção inválida.")
    menu()


# ====================
# Início do programa
Env_Data()



