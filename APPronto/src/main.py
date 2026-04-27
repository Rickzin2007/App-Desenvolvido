# main.py - API principal EcoControl

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#  INICIALIZAÇÃO DA API

app = FastAPI(
    title="EcoControl API",
    description="API do sistema de sustentabilidade",
    version="1.0.0"
)


#  CORS (LIBERA FRONTEND)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, troque pelo seu domínio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#  IMPORTAÇÃO DAS ROTAS

from src.routers.CadastroRotas import user_router
from src.routers.ConsumoRotas import consumo_router
from src.routers.loginRota import login_router
from src.routers.MetasRotas import metas_router
from src.routers.PasswordRota import router_senha
from src.routers.OcrRota import ocr_route

# IMPORTANTE: só mantém se existir esse arquivo!
from src.middlewares.authGoogle import router as google_router


#  REGISTRO DAS ROTAS

app.include_router(user_router, prefix="/Usuario")
app.include_router(login_router)
app.include_router(consumo_router)
app.include_router(metas_router)
app.include_router(router_senha)
app.include_router(ocr_route)
app.include_router(google_router)


# CONFIGURAÇÃO DO BANCO

from src.config.database import engine
from src.models.base import Base

# Importar TODOS os models
import src.models.consumoModel
import src.models.metaModel
import src.models.usuarioModel
import src.models.ocrModel

# Criar tabelas
Base.metadata.create_all(bind=engine)


# DEBUG

from src.config.settings import DATABASE_URL

print("MAIN DATABASE:", DATABASE_URL)


# ROTA TESTE

@app.get("/")
def home():
    return {"mensagem": "API EcoControl rodando 🚀"}