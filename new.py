# ====================
# Bibliotecas
from dotenv import load_dotenv ,dotenv_values, set_key
from pathlib import Path
from time import sleep
import os
import yagmail
import re

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

dynamics_credentials = {
    "EMAIL": "",
    "PASS": ""
}

# ====================
# Função de limpeza do terminal
def Clean():
    os.system("cls")
    #os.system("clear")
Clean()

# ====================
# Inicio do progama
input("""
===============================
💻          HERMES          💻 
===============================
Olá! Me chamo Hermes.
Comigo ao seu lado, vamos juntos tornar o seu envio de E-mails muito mais rapido.

Pressione [Enter] para iniciar...
""")

# ====================
# Funções utilitárias
def load_env(method):
    global credentials
    match method:
        case "load_dotenv":
            load_dotenv(dotenv_path=env_path, override=True)
        case "load_credentials":    
            credentials = dotenv_values(env_path)

def credentials_Verify():
    if not credentials.get("EMAIL"):
            return "❌ Nenhum e-mail de remetente encontrado!."
    else:
            return credentials["EMAIL"]

def emailValidate(email: str) -> bool:
    """
    Verifica se a string é um e-mail válido com serviço conhecido.
    Exemplo aceito: nome@gmail.com, teste@outlook.com.br
    """
    pattern = (
        r"^[a-zA-Z0-9._%+-]+@"              # parte antes do @ (nome do usuário)
        r"(gmail|outlook|hotmail|yahoo|icloud|protonmail)\."  # serviço de email
        r"[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$"  # domínio e extensão (.com, .com.br, etc)
    )
    return bool(re.match(pattern, email))


def init_gmail():
    global GMAIL
    if credentials.get("EMAIL") and credentials.get("PASS"):
        GMAIL = yagmail.SMTP(credentials["EMAIL"], credentials["PASS"])
    else:
        print("❌ E-mail ou senha não configurados.")
        try:
            choice = input("""
    ╔══════════════════════════════════════════════════════════════════════════════════╗          
    ║ Para prosseguir com o envio é necessario você escolha uma das opções abaixo:"    ║
    ║                                                                                  ║
    ║[1] Utilizar um E-mail Durante essa unica execução do progama                     ║
    ║[2] Salvar um E-mail( Estatica ), pra ser reutilizalo em outras execuções         ║
    ═══════════════════════════════════════════════════════════════════════════════════╝
     
     Opção Desejada: """)
            match choice:
                case 1:
                    print("")

                case 2:
                    print("")
                case _:
                    print("Opção invalida, ")
        except ValueError:
            print("Entrada invalida, insira apenas números")
            return     

def Env(method):
        Method_Selected = method()
        if Method_Selected is not None:
            return Method_Selected

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
                    load_env("load_credentials")
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
        try: 
            choice = int(input(f"""
    =======================================
    📨                                  📨
    📨         CENTRAL DE ENVIO         📨
    📨                                  📨
    =======================================
    📨  E-mail Remetente =  ( {Env(credentials_Verify)} ) 
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
# Configuração do .env
def configure_env():
    env_data = dotenv_values(env_path)
    missing_vars = []

    for var in ("EMAIL", "PASS"):
        if var not in env_data:
            missing_vars.append(var)

    if missing_vars:
        print(f"⚠️ Variáveis ausentes: {', '.join(missing_vars)}")
        print(); sleep(.8)
        for var in missing_vars:
            set_key(env_path, var, "''")
        print("✅ Variáveis adicionadas ao .env!")

    if not missing_vars:
        print("✅ Todas as variáveis estão configuradas corretamente.")

# ====================
# Função inicial
def Env_Data():
    load_env("load_dotenv")
    print("🔍 Verificador iniciado...\n")
    sleep(.8)
    print("Procurando arquivo [.env]...\n")
    sleep(.8)

    while True:
        if env_path.exists():
            print("✅ Arquivo [.env] encontrado.\n")
            sleep(.8)
            print("Verificando arquivo existente...\n")
            sleep(2)
            configure_env()
            print("✔️ Verificação concluída.\n")
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
            print("🔁 Rechecando arquivo...")
            sleep(1)
            continue
        elif choice == 2:
            env_path.touch()
            print("✅ Arquivo [.env] criado com sucesso.")
            sleep(1)
            configure_env()
            print("✔️ Verificação concluída.\n")
            break
        else:
            print("❌ Opção inválida.")

    print("Saindo do verificador...\n")
    menu()


# ====================
# Início do programa
Env_Data()

"""
📦 Programa HERMES
│
├── 🧩 Inicialização
│   ├── Importa bibliotecas (dotenv, yagmail, etc)
│   ├── Define cores (ANSI)
│   ├── Define variáveis globais (.env, credentials, GMAIL)
│   ├── Função Clean() → limpa terminal
│   └── Mensagem inicial (input para iniciar)
│
├── ⚙️ Funções utilitárias
│   ├── load_credentials() → carrega dados do .env
│   ├── init_gmail() → inicializa yagmail se EMAIL e PASS existirem
│   ├── configure_env()
│   │   ├── Chama load_credentials()
│   │   ├── Cria chaves EMAIL e PASS se não existirem
│   │   └── Salva no .env
│   └── Estatic_smtp_credentials()
│       ├── Mostra menu de configuração
│       ├── Solicita email e senha de app
│       ├── Exibe resumo e opções (salvar ou modificar)
│       ├── Salva credenciais no .env
│       └── Retorna ao menu
│
├── ✉️ Envio de Email
│   ├── simple_send()
│   │   ├── Solicita destinatário, assunto e conteúdo
│   │   ├── Envia via GMAIL.send()
│   │   ├── Exibe confirmação
│   │   └── Retorna ao menu
│
├── 🧭 menu()
│   ├── Exibe remetente atual (ou aviso se ausente)
│   ├── Mostra opções:
│   │   1 → Envio simples
│   │   2 → Envio em massa (em desenvolvimento)
│   │   3 → Configurar destinatários (em desenvolvimento)
│   │   4 → Configurar remetente (chama Estatic_smtp_credentials)
│   │   0 → Sair
│   ├── Valida entrada numérica
│   ├── Chama init_gmail()
│   ├── Executa ação conforme opção
│   └── Retorna ao menu se necessário
│
└── 🚀 Env_Data() (função inicial)
    ├── Verifica se .env existe
    │   ├── Se existir → chama configure_env()
    │   └── Se não existir:
    │       ├── Pergunta se cria novo .env
    │       ├── Cria arquivo se usuário escolher
    │       └── Configura e limpa tela
    └── Chama menu()

🏁 Execução final:
Env_Data() → configure_env() → menu() → (ações do usuário)


Estrutura nova:
 
 Funções:
 
 Env
 Smtp
 """
