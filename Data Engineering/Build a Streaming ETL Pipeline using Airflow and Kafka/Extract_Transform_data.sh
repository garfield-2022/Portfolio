#!/bin/bash

# unzip the data
tar -xvzf /home/project/airflow/dags/tolldata.tgz \
        -C /home/project/airflow/dags

# extract the fields `Rowid`, `Timestamp`, `Anonymized Vehicle number`, and
# `Vehicle type` from the `vehicle-data.csv` file and save them into a file named
# `csv_data.csv`.
cut -d "," -f1-4 /home/project/airflow/dags/vehicle-data.csv > \
        /home/project/airflow/dags/csv_data.csv

# extract the fields `Number of axles`, `Tollplaza id`, and `Tollplaza code` from
#the `tollplaza-data.tsv` file and save it into a file named `tsv_data.csv`.
# try | sed "s/\t/,/g" | sed "s/.$//"
# 9 Practical Examples of the cut Command in Linux, https://www.makeuseof.com/cut-command-examples-linux/
cut -f5,6,7 /home/project/airflow/dags/tollplaza-data.tsv \
        | tr "\t" "," |tr -d "\r" > \
        /home/project/airflow/dags/tsv_data.csv
        
# extract the fields `Type of Payment code`, and `Vehicle Code` from the fixed
# width file `payment-data.txt` and save it into a file named
#`fixed_width_data.csv`.
cut -b 59-61,63-66 /home/project/airflow/dags/payment-data.txt > \
        /home/project/airflow/dags/fixed_width_data.csv --output-delimiter=','

# create a single csv file named `extracted_data.csv` by combining data
paste -d ',' /home/project/airflow/dags/csv_data.csv \
        /home/project/airflow/dags/tsv_data.csv \
        /home/project/airflow/dags/fixed_width_data.csv > \
        /home/project/airflow/dags/extracted_data.csv

# transform the vehicle_type field in `extracted_data.csv` into capital letters and
#save it into a file named `transformed_data.csv`
paste -d ',' \
    <( </home/project/airflow/dags/extracted_data.csv cut -d ',' -f1-3 ) \
    <( </home/project/airflow/dags/extracted_data.csv cut -d ',' -f4 | tr '[:lower:]' '[:upper:]' ) \
    <( </home/project/airflow/dags/extracted_data.csv cut -d ',' -f5-9 ) \
    > /home/project/airflow/dags/transformed_data.csv        
