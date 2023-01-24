#!/bin/bash

bq extract \  
--compression GZIP \  
'ads_datastore.a_table' \  
gs://adsgbucket/london_bicycles.csv