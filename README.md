## ML-ZoomCamp - Midterm-project

# Term deposit prediction

## Introduction
This project was undertaken as part of the Midterm Project Assignment for the Machine Learning Zoomcamp 2025. The dataset has taken from Kaggle [link](https://www.kaggle.com/datasets/rashmiranu/banking-dataset-classification?select=new_test.csv)

# Problem:
A Portuguese Bank has experienced a decline in revenue. Analysis of this situation identified a critical root cause: the low rate of customer investment in long-term deposits.

# Objective:
To counteract this trend, the priority is to implement a focused customer marketing strategy. The core objective is to identify existing customers who possess the highest propensity to subscribe to a long-term deposit product.
By segmenting and directing marketing efforts exclusively toward this high-propensity group, the bank seeks to optimize resource allocation and drive long-term deposit subscriptions to restore profitability.
To achieve this objective, classification models (logistic regression and trees) will be used to determine which customers are most likely to take out long-term deposits based on various variables available to the marketing team, enabling them to optimize future direct marketing efforts.

## Dataset
This data relates to direct marketing campaigns conducted by a Portuguese banking institution, specifically utilizing phone calls to offer clients a bank term deposit. The campaigns often required multiple contacts with the same client. The objective of the analysis is to predict the outcome of the subscription. The dataset to be used is the train dataset.

# Data Atributtes
Target Variable: The primary goal is a binary classification task, to predict whether a client will subscribe to the term deposit (variable y).

Feautures
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
