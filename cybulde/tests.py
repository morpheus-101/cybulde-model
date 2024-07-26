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

from cybulde.config_schemas import data_module_schemas
from cybulde.config_schemas.base_schemas import TaskConfig
from cybulde.config_schemas.trainer import trainer_schemas
from cybulde.config_schemas.training import training_lightning_module_schemas

name: str = "binary_text_classfication_task"
data_module: data_module_schemas.DataModuleConfig = (
    data_module_schemas.ScrappedDataTextClassificationDataModuleConfig()
)
lightning_module: training_lightning_module_schemas.TrainingLightningModuleConfig = (
    training_lightning_module_schemas.CybuldeBinaryTextClassificationTrainingLightningModuleConfig()
)
trainer: trainer_schemas.TrainerConfig = trainer_schemas.GPUDev()
ctt = CommonTrainingTask(name=name,
                         data_module=data_module,
                         lightning_module=lightning_module,
                         trainer=trainer,
                         best_training_checkpoint='best',
                         last_training_checkpoint='last')
print(ctt)

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






# if __name__ == "__main__":
#     main()