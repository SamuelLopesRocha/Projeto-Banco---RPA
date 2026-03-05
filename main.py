#cd "/c/Users/Familia Rocha/OneDrive/Anexos de email/Desktop/Projeto Banco/src/rpa"

import time
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

from db_connection import (
    get_usuarios_pendentes_verificacao,
    marcar_email_verificacao_enviado,
    get_usuarios_pendentes_email,
    marcar_email_usuario_enviado,
    get_contas_poupanca_pendentes_email,
    marcar_email_poupanca_enviado,
    get_usuario_por_id
)

from email_service import enviar_email

INTERVALO_SEGUNDOS = 30 # Tempo de espera entre cada execução. 30 Segundos é recomendado para não sobrecarregar o banco de dados e o serviço de email, mas pode ser ajustado conforme necessário.


def executar_rpa():
    print("Buscando usuarios pendentes...")

    # ==============================
    # 👤 VERIFICAÇÃO DE EMAIL
    # ==============================

    print("Buscando usuários pendentes de verificação...")

    pendentes_verificacao = get_usuarios_pendentes_verificacao()

    for usuario in pendentes_verificacao:
        nome = usuario["nome_completo"]
        email  = usuario["email"]
        usuario_id = usuario["usuario_id"]
        token = usuario["token_verificacao"]
        link = f"http://localhost:8000/usuarios/verificar-email?token={token}"

        print(f"Enviando email de verificação para {nome}")

        try:
            enviar_email(
                destinatario=email,
                assunto="Verifique seu e-mail para verificar sua conta! - Banco Atlas",
                nome_template="email_verificacao.html",
                dados={
                    "nome": nome,
                    "link_verificacao": link
                }
            )
            marcar_email_verificacao_enviado(usuario_id)
            print(f"Email de verificação enviado e confirmado para {nome}")
        except Exception as e:
            print(f"Erro ao enviar email de verificação para {nome}: {e}")


    # ==============================
    # 👤 CADASTRO
    # ==============================

    usuarios = get_usuarios_pendentes_email()

    for usuario in usuarios:
        nome = usuario["nome_completo"]
        email = usuario["email"]
        usuario_id = usuario["usuario_id"]

        print(f"Enviando email de cadastro para {nome}")

        try:
            enviar_email(
                destinatario=email,
                assunto=" Sua conta corrente foi criada!",
                nome_template="email_boas_vindas.html",
                dados={
                    "nome": nome,
                    "agencia": "0001",
                    "numero_conta": "123456",
                    "digito": "7"
                }
            )
            marcar_email_usuario_enviado(usuario_id)
            print(f"Email de cadastro enviado e confirmado para {nome}")
        except Exception as e:
            print(f"Erro ao enviar email de cadastro para {nome}: {e}")


    # ==============================
    # 💰 POUPANÇA
    # ==============================

    print("Buscando contas poupanca pendentes...")

    contas = get_contas_poupanca_pendentes_email()

    for conta in contas:
        usuario = get_usuario_por_id(conta["usuario_id"])

        nome = usuario["nome_completo"]
        email = usuario["email"]

        print(f"Enviando email poupança para {nome}")

        try:
            enviar_email(
                destinatario=email,
                assunto="Sua conta poupança foi criada!",
                nome_template="email_conta_poupanca.html",
                dados={
                    "nome": nome,
                    "agencia": conta["agencia"],
                    "numero_conta": conta["numero_conta"],
                    "digito": conta["digito"],
                    "taxa_rendimento": "0,5%"
                }
            )
            marcar_email_poupanca_enviado(conta["id_conta"])
            print(f"Email de poupança enviado e confirmado para {nome}")
        except Exception as e:
            print(f"Erro ao enviar email de poupança para {nome}: {e}")

    print("Processo finalizado.")


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        pass  # silencia logs do servidor HTTP


def iniciar_servidor():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()


threading.Thread(target=iniciar_servidor, daemon=True).start()

while True:
    executar_rpa()
    print(f"Aguardando {INTERVALO_SEGUNDOS} segundos para próxima execução...")
    time.sleep(INTERVALO_SEGUNDOS)