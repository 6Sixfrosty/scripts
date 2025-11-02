from dotenv import dotenv_values, set_key
from pathlib import Path
import yagmail

CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

env_path = Path(".env")

setORnoset = input(
"""
╔══════════════════════════════════════╗
║       CONFIGURAÇÃO DE EMAIL          ║
╠══════════════════════════════════════╣
║ Se deseja mudar o email: ESCREVA     ║
║            (SIM)                     ║
║ Se não, apenas aperte Enter          ║
╚══════════════════════════════════════╝

Resposta: """
)

if setORnoset.lower() == "sim":
    new_EMAIL = input(f"""
{CYAN}>>> CONFIGURAÇÃO DE EMAIL <<<{RESET}

{YELLOW}→ Qual é o E-mail remetente?{RESET}
Email: """)
    
    new_PASS = input(f"""
{CYAN}>>> SENHA DE APP <<<{RESET}

{YELLOW}→ Informe a (senha de app) do E-mail acima{RESET}
Senha: """)
    
    set_key(env_path, "EMAIL", new_EMAIL)
    set_key(env_path, "PASS", new_PASS)


credentials = dotenv_values(".env")

SMTP_EMAIL = credentials["EMAIL"]
SMTP_PASS = credentials["PASS"]

recipient_email = input(f"""
{CYAN}>>> CONFIGURAÇÃO DO DESTINATÁRIO <<<{RESET}

{YELLOW}→ Informe o E-mail do destinatário:{RESET}
Email: """)

gmail = yagmail.SMTP(SMTP_EMAIL, SMTP_PASS)

gmail.send(
    to=recipient_email,
    subject="Teste",
    contents="Óla, esse é um E-mail de teste."
)

input(f"""
{CYAN}>>> ENVIO DE EMAIL <<< {RESET}

{GREEN}✔ Email enviado com sucesso para:{RESET} {YELLOW}{recipient_email}{RESET}

Pressione Enter para Finalizar...
""")
