import sys
import pandas as pd

from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):

    '''
    INPUT
    file paths of message and categories files
    
    OUTPUT
    a dataframe contains both dataset
    '''
    
    messages   = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    
    return pd.merge(messages, categories, on='id')

def clean_data(df):
    
    '''
    INPUT
    a dataframe with both messages and categories 
    
    OUTPUT
    cleaned dataframe, with new expanding columns for each message category
    '''
    
    ## Split categories into separate category columns
    categories = df.categories.str.split(';', expand=True)
    row = categories.iloc[0]
    category_colnames = row.apply(lambda x: x[:-2])
    categories.columns = category_colnames
    
    ## Convert category values to just numbers 0 or 1
    for column in categories:
    # set each value to be the last character of the string
        categories[column] = categories[column].str.split("-").str[1]
#       column
#     # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column],errors='coerce')
    
    ## Replace categories column in df with new category columns.
    df.drop(['categories'], axis=1, inplace= True)
    df = pd.concat([df, categories], axis=1)
    
    ## remove the related value which is greater than 2
    df = df[df.related < 2]
    
    ## drop duplicate
    df.drop_duplicates(inplace=True)
    
    return df
    


def save_data(df, database_filename):
    
    '''
    INPUT
    cleaned dataframe and the filepath for the SQL database for saving the dataframe
    
    OUTPUT
    None but dataframe is saved to database
    '''
        
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('InsertTableName', engine, index=False, if_exists='replace')
    engine.dispose()


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
