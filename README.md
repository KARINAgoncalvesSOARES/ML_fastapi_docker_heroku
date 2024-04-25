# Implante modelos de ML com FastAPI, Docker e Heroku

![image](https://github.com/KARINAgoncalvesSOARES/ML_fastapi_docker_heroku/assets/104592210/39a6c0bb-e081-4efa-a3fe-5167d3dfc17c)

Link de estudo:

* [Deploy ML models with FastAPI, Docker, and Heroku | Tutorial](https://www.youtube.com/watch?v=h5wLuVDr0oc&ab_channel=AssemblyAI)

* [Imagem oficial do Docker com Gunicorn - Uvicorn](https://fastapi.tiangolo.com/deployment/docker/#official-docker-image-with-gunicorn-uvicorn)

## 1. Desenvolva e salve o modelo.

    arquivo: ml_fastapi_docker_heroku.ipynb


## 2. Crie um contêiner Docker

    docker build -t app-name .

    docker run -p 80:80 app-name