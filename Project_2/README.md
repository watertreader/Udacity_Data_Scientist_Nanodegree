
# Disaster Response Pipeline Project



### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#introduction)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Acknowledgements](#acknowledgement)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. The code should run with no issues using Python versions 3.*. All other libraries needed is declared within the file

If you are using firefox browser, checkout this Firefox plugin. Python Notebook Viewer.

This plugin lets you view/render python notebooks without running notebook server. Once installed, set Firefox as default app to open ipynb files. From now onwards, you can simply open ipynb files by simply double clicking on it!

Or else you can run google colab and upload this python notebook


## Project Introduction<a name="introduction"></a>

The project goal is to demonstrate my familiarity with the following subject matters:

    1: Extract, Transform, and Load process.
    2: Create a ML pipeline that uses NLTK, as well as scikit-learn's Pipeline and GridSearchCV to derive a final model.
    3: Data Visualization and Presentation

The project is about creating a Disaster Response Pipeline where it will help the disaster response worker to quicky determine the relief response needed from the message input to the terminal. ML pipeline created will be able to categorize the needs and response from messages to seek aid/help from appropriate disaster relief agency. A web based application will allow user to easily assess the application

The data is provided by Figure Eight 

## File Descriptions <a name="files"></a>
File structure of project is given by

- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- InsertDatabaseName.db   # database to save clean data to

- models
|- train_classifier.py
|- classifier.pkl  # saved model 

- README.md

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

Thanks for 

## Licensing <a name="licensing"></a>

All rights reserved

All source code and software in this repository are made available under the terms of the MIT license.



