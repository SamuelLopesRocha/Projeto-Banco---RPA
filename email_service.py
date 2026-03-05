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
        "https://api.brevo.com/v3/smtp/email",
        headers={
            "api-key": RESEND_API_KEY,
            "Content-Type": "application/json",
        },
        json={
            "sender": {"name": "Banco Atlas", "email": EMAIL_REMETENTE},
            "to": [{"email": destinatario}],
            "subject": assunto,
            "htmlContent": html,
        }
    )

    if response.status_code not in (200, 201, 202):
        raise Exception(f"Brevo erro {response.status_code}: {response.text}")
