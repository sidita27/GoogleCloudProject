#!/bin/bash

#Creates a new empty table

bq mk \
  --table \
  --description "New table with random data" \
  --label organization:development \
  ads_datastore.a_table


#Creates a bucket. This name is unique
gcloud storage buckets create gs://adsgbucket

BUCKET=$1
PROJECT=$(gcloud config get-value project)

#Load data table

bq load \
    --autodetect \
    --source_format=CSV \
    'adsgproject.ads_datastore.a_table' \
    gs://${BUCKET}/london_bicycles.csv
