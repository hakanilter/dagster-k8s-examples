from dagster import AssetExecutionContext, asset
from dagster_k8s import PipesK8sClient


@asset(group_name="google")
def k8s_pipes_asset(context: AssetExecutionContext, k8s_pipes_client: PipesK8sClient):
  return k8s_pipes_client.run(
      context=context,
      image="pipes-example:v1",
  ).get_materialize_result()

@asset(group_name="google")
def k8s_other_asset(context: AssetExecutionContext, k8s_pipes_client: PipesK8sClient):
  return k8s_pipes_client.run(
      context=context,
      image="pipes-example:v1",
  ).get_materialize_result()
