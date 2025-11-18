# Dataser Overview

## About Dataset
This project uses a dataset sourced from Kaggle, which focuses on to identify existing customers who possess the highest propensity to subscribe to a long-term deposit product.

It contains characteristics extracted from the marketing department of a Portuguese bank. The variables focus specifically on customer age, occupation, whether they have had a certain type of loan, whether they have been in credit default, and the type of contact the bank has had with them during previous marketing campaigns.

## Data Sources
There are two datasets: train.csv with all examples (32950) and 21 inputs including the target feature, ordered by date (from May 2008 to November 2010), very close to the data analyzed in [Moro et al., 2014]. Theis project only uses the train.csv file, as this is the only dataset that contains the target variable.

| Kaggle Dataset: [link](https://www.kaggle.com/datasets/rashmiranu/banking-dataset-classification?select=new_test.csv)

## Target variable
The target variable is binary and it's called `y`. This variable represents if the client has subscribed a term deposit ('yes','no').

## Columns description
| **Feature** | **Feature_Type** | **Description** |
| ------------- |-------------| -------------|
|age|	numeric|	age of a person|
|job|	Categorical, nominal|	type of job ('admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')|
|marital|	categorical, nominal|	marital status ('divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)|
|education|	categorical, nominal|	('basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')|
|default|	categorical, nominal|	has credit in default? ('no','yes','unknown')|
|housing|	categorical, nominal|	has housing loan? ('no','yes','unknown')|
|loan|	categorical, nominal|	has personal loan? ('no','yes','unknown')|
|contact|	categorical, nominal|	contact communication type ('cellular','telephone')|
|month|	categorical, ordinal|	last contact month of year ('jan', 'feb', 'mar', …, 'nov', 'dec')|
|day_of_week|	categorical, ordinal|	last contact day of the week ('mon','tue','wed','thu','fri')|
|duration|	numeric|	last contact duration, in seconds . Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no')|
|campaign|	numeric|	number of contacts performed during this campaign and for this client (includes last contact)|
|pdays|	numeric|	number of days that passed by after the client was last contacted from a previous campaign (999 means client was not previously contacted)|
|previous|	numeric|	number of contacts performed before this campaign and for this client|
|poutcome|	categorical, nominal|	outcome of the previous marketing campaign ('failure','nonexistent','success')|