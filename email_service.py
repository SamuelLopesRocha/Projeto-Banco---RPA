import os
import resend
from config import EMAIL_REMETENTE, RESEND_API_KEY

resend.api_key = RESEND_API_KEY


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

    params: resend.Emails.SendParams = {
        "from": f"Banco Atlas <{EMAIL_REMETENTE}>",
        "to": [destinatario],
        "subject": assunto,
        "html": html,
    }

    resend.Emails.send(params)
