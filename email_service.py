import os
import requests
from config import EMAIL_REMETENTE, RESEND_API_KEY


def carregar_template(nome_template, dados):
    caminho = os.path.join(
        os.path.dirname(__file__),
        "templates",
        nome_template
    )

    with open(caminho, "r", encoding="utf-8") as file:
        html = file.read()

    for chave, valor in dados.items():
        html = html.replace(f"{{{{{chave}}}}}", str(valor))

    return html


def enviar_email(destinatario, assunto, nome_template, dados):
    html = carregar_template(nome_template, dados)

    response = requests.post(
        "https://api.mailersend.com/v1/email",
        headers={
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "from": {"name": "Banco Atlas", "email": EMAIL_REMETENTE},
            "to": [{"email": destinatario}],
            "subject": assunto,
            "html": html,
        }
    )

    if response.status_code not in (200, 202):
        raise Exception(f"Mailersend erro {response.status_code}: {response.text}")
