This project is from the Course ETL and Data Pipelines with Shell, Airflow and Kafka offered by IBM on Coursera.org.

The scenario is a data engineer at a data analytics consulting company has been assigned to a project that aims to de-congest 
the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different
toll operator with a different IT setup that uses different file formats. The first job is to collect data available in
different formats and consolidate it into a single file. A shell script is created using bash commands to:

1. Extract data from a csv file.
2. Extract data from a tsv file.
3. Extract data from a fixed width file.
4. Transform the data.
5. Load the transformed data into a new csv file.

As a vehicle passes a toll plaza, the vehicle's data like vehicle_id,vehicle_type,toll_plaza_id and timestamp are streamed to
Kafka. The second job is to create a data pipe line that collects the streaming data and loads it into a database. A streaming 
data pipe is created by performing these steps:

1. Start a MySQL Database server.
2. Create a table to hold the toll data.
3. Start the Kafka server.
4. Install the Kafka python driver.
5. Install the MySQL python driver.
6. Create a topic named toll in kafka.
7. Download streaming data generator program.
8. Customize the generator program to steam to toll topic.
9. Download and customise streaming data consumer.
10. Customize the consumer program to write into a MySQL database table.
11. Verify that streamed data is being collected in the database table.
