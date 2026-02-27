import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Variáveis de configuração (MONGO_URI, DB_NAME, EMAIL_REMETENTE, EMAIL_SENHA, SMTP_SERVIDOR, SMTP_PORTA) diretamente do MongoDB Atlas e do Gmail

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
EMAIL_SENHA = os.getenv("EMAIL_SENHA")
SMTP_SERVIDOR = os.getenv("SMTP_SERVIDOR")
SMTP_PORTA = int(os.getenv("SMTP_PORTA", 587)) # Porta padrão para SMTP é 587, mas pode ser configurada via .env

