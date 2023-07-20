Analyzing Census Data with Python and SQL

This project is derived from the course Databases and SQL for Data Science with Python offered by IBM on Coursera.org https://www.coursera.org/learn/sql-data-science?specialization=ibm-data-engineer We first store the data from website in an SQLite database. Then we will do analysis to extract insights.

The city of Chicago released a dataset of socioeconomic data to the Chicago City Portal https://tinyurl.com/5xn6f5uj This dataset contains a selection of six socioeconomic indicators of public health significance and a “hardship index,” by Chicago community area, for the years 2008 – 2012. This dataset contains 78 rows and 9 columns.

The indicators are

Community Area Number (ca): Used to uniquely identify each row of the dataset, Community Area Name (community_area_name): The name of the region in the city of Chicago, Percent of Housing Crowded (percent_of_housing_crowded): the percent of occupied housing units with more than one person per room, Percent Households Below Poverty (percent_households_below_poverty): the percent of households living below the federal poverty level, Percent Aged 16+ Unemployed (percent_aged_16_unemployed): the percent of persons in the labor force over the age of 16 years that are unemployed, Percent Aged 25+ without High School Diploma (percent_aged_25_without_high_school_diploma): the percent of persons over the age of 25 years without a high school diploma, Percent Aged Under 18 or Over 64: the percent of population under 18 or over 64 years of age (percent_aged_under_18_or_over_64): (ie. dependency), Per Capita Income (per_capita_income_): Community Area per capita income is estimated as the sum of tract-level aggragate incomes divided by the total population, Hardship Index (hardship_index): Score that incorporates each of the six selected socioeconomic indicators.

Data analysis on correlations between indicators are done using Python and SQL. Data visualization are generated in matplotlib and seaborn.
