from dagster import Definitions, load_assets_from_modules
from dagster_k8s import PipesK8sClient

from .amazon import amazon
from .google import pipes

all_assets = load_assets_from_modules([
    amazon, 
    pipes
])

defs = Definitions(
    assets=all_assets,
    resources={
        "k8s_pipes_client": PipesK8sClient(),
    },
)
