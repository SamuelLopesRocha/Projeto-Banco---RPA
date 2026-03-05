from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

usuarios_collection = db["usuarios"]
contas_collection = db["contas"]

# ==============================
# 👤 USUÁRIOS (CADASTRO)
# ==============================

def get_usuarios_pendentes_email():
    return usuarios_collection.find({
        "email_enviado": {"$ne": True},
        "status_conta": "ATIVA"
    })


def marcar_email_usuario_enviado(usuario_id):
    usuarios_collection.update_one(
        {"usuario_id": usuario_id},
        {"$set": {"email_enviado": True}}
    )


# ==============================
# 💰 CONTAS POUPANÇA
# ==============================

def get_contas_poupanca_pendentes_email():
    return contas_collection.find({
        "tipo_conta": "POUPANCA",
        "email_enviado": {"$ne": True},
        "status_conta": "ATIVA"
    })


def marcar_email_poupanca_enviado(id_conta):
    contas_collection.update_one(
        {"id_conta": id_conta},
        {"$set": {"email_enviado": True}}
    )


# ==============================
# 🔎 BUSCAR USUÁRIO POR ID
# ==============================

def get_usuario_por_id(usuario_id):
    return usuarios_collection.find_one({
        "usuario_id": usuario_id
    })


def get_usuarios_pendentes_verificacao():
    return usuarios_collection.find({
        "status_conta": "PENDENTE",
        "token_verificacao": {"$ne": None},
        "email_verificacao_enviado": {"$ne": True},
    })

def marcar_email_verificacao_enviado(usuario_id):
    usuarios_collection.update_one(
        {"usuario_id": usuario_id},
        {"$set": {"email_verificacao_enviado": True}}
    )
        
