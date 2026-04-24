import os

class Config:
    """
    Configurações gerais do backend.
    """
    SECRET_KEY = os.getenv("SECRET_KEY", "sua-chave-secreta-padrao")
    # Agora o framework usa a chave do Gemini por padrão
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")
    DEBUG = os.getenv("DEBUG", "True") == "True"
    PORT = int(os.getenv("PORT", 5000))
    HOST = os.getenv("HOST", "0.0.0.0")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
