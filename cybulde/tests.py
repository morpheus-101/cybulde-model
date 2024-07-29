# # from cybulde.evaluation.tasks import common_evaluation_task

# # name: str = "binary_text_evaluation_task"
# # lightning_module: evaluation_lightning_module_schemas.PartialEvaluationLightningModuleConfig = (
# #     evaluation_lightning_module_schemas.BinaryTextEvaluationLightningModuleConfig()
# # )
# # data_module: data_module_schemas.DataModuleConfig = (
# #     data_module_schemas.ScrappedDataTextClassificationDataModuleConfig()
# # )
# # trainer: trainer_schemas.TrainerConfig = trainer_schemas.GPUDev()


# # def main() -> None:
# #     cet = CommonEvaluationTask(name=name,
# #                                data_module=data_module,
# #                                lightning_module=lightning_module,
# #                                trainer=trainer,
# #                                tar_model_path="/mlflow-artifact-store/0/e05abada5808441293f104b7021d6a38/artifacts/exported_model.tar.gz")
# #     print(cet)


# # if __name__ == "__main__":
# #     main()


# from __future__ import annotations

# from collections.abc import Iterable

# from google.cloud import compute_v1

# def list_instances(project_id: str, zone: str) -> Iterable[compute_v1.Instance]:
#     """
#     List all instances in the given zone in the specified project.

#     Args:
#         project_id: project ID or project number of the Cloud project you want to use.
#         zone: name of the zone you want to use. For example: “us-west3-b”
#     Returns:
#         An iterable collection of Instance objects.
#     """
#     instance_client = compute_v1.InstancesClient()
#     instance_list = instance_client.list(project=project_id, zone=zone)

#     print(f"Instances found in zone {zone}:")
#     for instance in instance_list:
#         print(f" - {instance.name} ({instance.machine_type})")
#     print(instance_list[0])
#     # return instance_list

# list_instances("deeplearning-platform-release", )
