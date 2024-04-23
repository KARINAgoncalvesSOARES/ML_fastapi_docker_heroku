from fastapi import FastAPI
from pydantic import BaseModel # valida dados de entrada e de saída
from app.modelo.model import predict_pipeline # Módulo específicado em minha aplicação (meu modelo)
from app.modelo.model import __version__ as model_version


# Criando instância
app = FastAPI()

# Valida od dados de entrada que a minha api espera receber
class TextIn(BaseModel):
    text: str

# Valida os dados de saída que o modelo irá retornar
class PredictionOut(BaseModel):
    language: str
    
# Rota de solicitação HTTP GET(usuário)
@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

# Solicitação HTTP POST(enviar dados)
@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}