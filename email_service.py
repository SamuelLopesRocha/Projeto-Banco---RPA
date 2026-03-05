import os
from mailersend import emails
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

    mailer = emails.NewEmail(RESEND_API_KEY)

    mail_body = {}
    mailer.set_mail_from({"name": "Banco Atlas", "email": EMAIL_REMETENTE}, mail_body)
    mailer.set_mail_to([{"email": destinatario}], mail_body)
    mailer.set_subject(assunto, mail_body)
    mailer.set_html_content(html, mail_body)

    mailer.send(mail_body)
