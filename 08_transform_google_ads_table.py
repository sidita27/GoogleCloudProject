from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the destination table.
table_id = "adsgproject.ads_datastore.google_ads"

#CPA is calculated Total Amount Spent / Conversions

QUERY = (
        "UPDATE `adsgproject.ads_datastore.google_ads` SET CPA = cast(SaleAmount as DECIMAL) / cast(Conversions as DECIMAL) Where Conversions > 0;"
    )
query_job = client.query(QUERY)
rows = query_job.result()

# CPC is calculated as Cost / Clicks
QUERY = (
        "UPDATE `adsgproject.ads_datastore.google_ads` SET CPC = cast(Cost as DECIMAL) / cast(Clicks as DECIMAL)Where Clicks > 0;"
    )
query_job = client.query(QUERY)
rows = query_job.result()

# ROAS is calculated as (Revenue from advertising / Cost of advertising) * 100
QUERY = (
        "UPDATE `adsgproject.ads_datastore.google_ads` SET ROAS = cast(Revenue as DECIMAL) / cast(Cost as DECIMAL) * 100 Where Cost > 0;"
    )
query_job = client.query(QUERY)
rows = query_job.result()


