# To load models from MLflow clinet using model name and model version 

# import os

# from fastapi import FastAPI
# from hydra.utils import instantiate

# from cybulde.models.common.exporter import TarModelLoader
# from cybulde.utils.config_utils import load_config
# from cybulde.utils.mlflow_utils import get_client

# config = load_config(config_path="../configs/automatically_generated", config_name="config")
# tokenizer = instantiate(config.tasks.binary_text_classification_task.data_module.transformation)

# model_name = "bert_tiny"
# model_version = "1"
# mlflow_client = get_client()

# mlflow_model = mlflow_client.get_model_version(name=model_name, version=model_version)
# model_path = os.path.join(mlflow_model.source, "exported_model.tar.gz")  # type: ignore
# model = TarModelLoader(model_path).load()
# model.eval()

# app = FastAPI()


# @app.get("/predict_cyberbullying")
# def predict_cyberbullying(text: str) -> dict[str, int]:
#     tokens = tokenizer([text])
#     probs = model(tokens)
#     classes = (probs >= 0.5).item()
#     return {"is_cyberbullying": int(classes)}

# =============================================================================

# To load models using a path from Google cloud storage

from fastapi import FastAPI
from hydra.utils import instantiate

from cybulde.models.common.exporter import TarModelLoader
from cybulde.utils.config_utils import load_config

config = load_config(config_path="../configs/automatically_generated", config_name="config")
tokenizer = instantiate(config.tasks.binary_text_classification_task.data_module.transformation)
# Path from my GCS bucket 
model_path = "gs://rbd-mlflow/367542467757527168/a221c00a525c4cd8bb75730be100b238/artifacts/exported_model.tar.gz"
model = TarModelLoader(model_path).load()
model.eval()

app = FastAPI()


@app.get("/predict_cyberbullying")
def predict_cyberbullying(text: str) -> dict[str, int]:
    tokens = tokenizer([text])
    probs = model(tokens)
    classes = (probs >= 0.5).item()
    return {"is_cyberbullying": int(classes)}