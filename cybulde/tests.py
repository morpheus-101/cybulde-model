# from cybulde.models.transformations import HuggingFaceTokenizationTransformation

# pretrained_tokenizer_name_or_path = "gs://rbd-mlflow/data/processed/rebalanced_splits/trained_tokenizer"
# max_sequence_length = 72

# tokenizer = HuggingFaceTokenizationTransformation(pretrained_tokenizer_name_or_path, max_sequence_length)
# texts = ["hi! how are you?"]
# output = tokenizer(texts)
# print(f"output = {output}")

import hydra
from omegaconf import DictConfig, OmegaConf
from hydra.utils import instantiate
from cybulde.config_schemas.training.training_task_schemas import setup_config
from cybulde.training.tasks.common_training_task import CommonTrainingTask
from cybulde.models.common.exporter import TarModelLoader

# setup_config()

# @hydra.main(config_name="test_training_task", version_base=None)
# def main(config: DictConfig) -> None:
#     print(60 * "#")
#     print(OmegaConf.to_yaml(config))
#     print(60 * "#")

    # model = instantiate(config)
    # texts = ["hello, how are you?", "i am doing good!"]
    # encodings = model.backbone.transformation(texts)
    # output = model(encodings)
    # print(f"{output.shape}")



def main() -> None:
    model_loader = TarModelLoader("/mlflow-artifact-store/0/87e6220c6cd04353adbafc90b319e096/artifacts/exported_model.tar.gz")
    model = model_loader.load()
    print(model)

if __name__ == "__main__":
    main()