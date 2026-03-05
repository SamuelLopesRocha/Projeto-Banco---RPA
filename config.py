import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env na mesma pasta deste arquivo
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
RESEND_API_KEY = os.getenv("RESEND_API_KEY")

