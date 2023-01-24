#!/bin/bash

bq mk \
  --table \
  --expiration 3600 \
  --description "Table contains google ads data" \
  --label organization:development \
  adsdata.ads_sample