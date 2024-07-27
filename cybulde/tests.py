from cybulde.evaluation.tasks import common_evaluation_task

# name: str = "binary_text_evaluation_task"
# lightning_module: evaluation_lightning_module_schemas.PartialEvaluationLightningModuleConfig = (
#     evaluation_lightning_module_schemas.BinaryTextEvaluationLightningModuleConfig()
# )
# data_module: data_module_schemas.DataModuleConfig = (
#     data_module_schemas.ScrappedDataTextClassificationDataModuleConfig()
# )
# trainer: trainer_schemas.TrainerConfig = trainer_schemas.GPUDev()


# def main() -> None:
#     cet = CommonEvaluationTask(name=name,
#                                data_module=data_module,
#                                lightning_module=lightning_module,
#                                trainer=trainer,
#                                tar_model_path="/mlflow-artifact-store/0/e05abada5808441293f104b7021d6a38/artifacts/exported_model.tar.gz")
#     print(cet)


# if __name__ == "__main__":
#     main()