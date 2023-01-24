from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "adsgproject.ads_datastore.google_ads"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("AdGroup", "STRING"),
        bigquery.SchemaField("Month", "STRING"),
        bigquery.SchemaField("Impressions", "INTEGER"),
        bigquery.SchemaField("Clicks", "INTEGER"),
        bigquery.SchemaField("CTR", "FLOAT"),
        bigquery.SchemaField("Conversions", "INTEGER"),
        bigquery.SchemaField("ConvRate", "FLOAT"),
        bigquery.SchemaField("Cost", "INTEGER"),
        bigquery.SchemaField("Revenue", "INTEGER"),
        bigquery.SchemaField("SaleAmount", "FLOAT"),
        bigquery.SchemaField("PL", "FLOAT")
    ],
    skip_leading_rows=1
)
uri = "gs://adsgbucket/shopping_mall_data.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Wait for the job to complete.

table = client.get_table(table_id)
print("Loaded {} rows to table {}".format(table.num_rows, table_id))