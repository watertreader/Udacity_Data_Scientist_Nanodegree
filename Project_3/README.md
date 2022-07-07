
# Recommendation with IBM Project



### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#introduction)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Acknowledgements](#acknowledgement)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. The code should run with no issues using the latest Anaconda package version. All other libraries needed is declared within the file

## Project Introduction<a name="introduction"></a>

The project goal is to demonstrate my familiarity with the following subject matters:

    1: Exploratory Data Analysis.
	2: Recommendation System 
    	2a: Rank Based Recommendations
    	2b: User-User Based Collaborative Filtering
		42: Matrix Factorization

In this project, we will analyze the interactions that users have with articles on the IBM Watson Studio platform, and make recommendations to them about new articles they'll like.

The data is provided by IBM Watson Platform

## File Descriptions <a name="files"></a>
File structure of project is given by

	- README.md: read me file
	- ETL Pipeline Preparation.ipynb: contains ETL pipeline preparation code


## Installation <a name="Installation"></a>

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

## Acknowledgements <a name="acknowedgement"></a>

Thanks for Udacity Team

## Licensing <a name="licensing"></a>

All rights reserved

All source code and software in this repository are made available under the terms of the MIT license.



