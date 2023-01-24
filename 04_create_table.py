from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

table_id = 'adsgproject.ads_datastore.a_table'

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "INTEGER"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("bikes_count", "INTEGER"),
        bigquery.SchemaField("terminal_id", "STRING")
    ],
    skip_leading_rows=1
)

uri = "gs://adsgbucket/london_bicycles.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Wait for the job to complete.

table = client.get_table(table_id)
print("Loaded {} rows to table {}".format(table.num_rows, table_id))