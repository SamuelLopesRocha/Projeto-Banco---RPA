# RPA Banco Atlas

Automação para envio de e-mails de boas-vindas (conta corrente) e criação de conta poupança, a partir de dados no MongoDB.

## Requisitos

- Python 3.10+
- MongoDB acessível pela URI
- Conta SMTP (ex.: Gmail com app password)

## Configuração

1) Crie o arquivo .env local com base em [.env.example](.env.example).

2) Preencha as credenciais no .env local.

3) Instale as dependências:

```
python -m pip install -r rpa/requirements.txt
```

## Executar

Na raiz do projeto:

```
python rpa/main.py
```

## O que o script faz

- Busca usuários com conta ATIVA e e-mail ainda não enviado.
- Envia o e-mail de boas-vindas usando o template.
- Marca o e-mail como enviado no banco.
- Busca contas poupança ATIVAS e pendentes.
- Envia o e-mail de conta poupança e marca como enviado.

## Templates de e-mail

- [rpa/templates/email_boas_vindas.html](rpa/templates/email_boas_vindas.html)
- [rpa/templates/email_conta_poupanca.html](rpa/templates/email_conta_poupanca.html)

## Agendamento (opcional)

Para executar periodicamente (ex.: a cada 5 minutos), use um agendador:

- Windows: Task Scheduler
- Linux/macOS: cron

## Segurança

- Nunca faça commit do .env
- O arquivo .env.example deve conter apenas placeholders
