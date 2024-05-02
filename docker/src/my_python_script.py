# my_python_script.py
import pandas as pd
from dagster_pipes import open_dagster_pipes
from dagster import MetadataValue

with open_dagster_pipes() as pipes:
    # Stream log message back to Dagster
    pipes.log.info("Started computation")
    
    path = "http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2023.csv"
    pipes.log.info(f"Reading data from: {path}")
    
    df = pd.read_csv(path)
    pipes.log.info(f"Found {len(df)} rows")

    # ... your code that computes and persists the asset

    # Stream asset materialization metadata and data version back to Dagster.
    # This should be called after you've computed and stored the asset value. We
    # omit the asset key here because there is only one asset in scope, but for
    # multi-assets you can pass an `asset_key` parameter.
    pipes.report_asset_materialization(
        metadata={
            "preview": MetadataValue.md(df.head().to_markdown()),
        },
        data_version="alpha",
    )
