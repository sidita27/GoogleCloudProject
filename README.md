# GoogleCloudProject

The main branch contains the shell scripts and the python scripts of the required tasks. The Django Project is in the branch django_dev. 

The in the Google Cloud, activate the Cloud Shell. To create a new project, run the file 02_create_project.sh

To create a datastore, in the Cloud Shell run the file 03_create_datastore.sh

To create a new table with random data, run the file 04_create_table.sh or the Python script in 04_create_table.py

To save the table locally, in a csv format, run the file 05_save.sh

To create a table containing the GoogleAds from the csv file, run the 06_create_table.sh
The dataset source : https://www.kaggle.com/datasets/marceaxl82/shopping-mall-paid-search-campaign-dataset

The next step is loading the table from the python Script. The code is in 07_load_google_ads_table.py


![02_GCP_Project](https://user-images.githubusercontent.com/19204977/218255447-896bb45e-c866-41a0-b981-a076f2f33546.png)


To calculate the metrics, first run the 08_add_column_table.py and later insert the data by running 08_transform_google_ads_table.py

To pause an and and to run the Mock tests, run the files 09_pause_ad.py and 09_test.py

