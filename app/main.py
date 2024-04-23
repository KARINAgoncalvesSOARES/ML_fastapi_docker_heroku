from fastapi import FastAPI
from pydantic import BaseModel # valida dados de entrada e de saída
from app.modelo.model import predict_pipeline
from app.modelo.model import __version__ as model_version