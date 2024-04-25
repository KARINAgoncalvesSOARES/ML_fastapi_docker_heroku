import pickle
import re
from pathlib import Path # Caminhos de arquivos

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent # caminho atual do arquivo para obter diretório base

# Confirmando o caminho e versão do arquivo pickle
with open(f"{BASE_DIR}/trained_pipeline-{__version__}.pkl", "rb") as f: 
    
    # Desserializa o arquivo transformando novamente em arquivo Python
    model = pickle.load(f) 
    
# Classes do códificador de rótulos
    classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portugeese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish",
]

# Pré processamento   
def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    
    # Previsão
    pred = model.predict([text])
    return classes[pred[0]]