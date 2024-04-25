"""
Execução do script
==================

$ uvicorn main:app --reload  
ou
$ python main.py 

"""
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel # valida dados de entrada e de saída
from aplicativo.modelo.model import predict_pipeline # Módulo específicado em minha aplicação (meu modelo)
from aplicativo.modelo.model import __version__ as model_version


# Criando instância
app = FastAPI()

# Valida od dados de entrada que a minha api espera receber
class TextIn(BaseModel):
    text: str

# Valida os dados de saída que o modelo irá retornar
class PredictionOut(BaseModel):
    language: str
    
# Verificação de integridade
@app.get("/")
def home():
    return {"checando desempenho do modelo": "OK", "model_version": model_version}

# Solicitação HTTP POST(enviar dados)
@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)