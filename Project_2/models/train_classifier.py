import sys
import pandas as pd
import nltk
import re
import pickle

## for importing scikit-learn
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV

## for importing nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def load_data(database_filepath):
    engine = create_engine('sqlite:///' + database_filepath)
    connection = engine.connect()
    df = pd.read_sql_table(engine.table_names()[0], connection)
    
    X = df['message']
    Y = df.loc[:, df.columns != 'message']
    print(Y.columns)
    Y = Y.drop(columns=['id', 'original', 'genre', 'child_alone'], axis=1)
    
    #categories = df.categories.str.split(';', expand=True)
    #names= categories.iloc[0].apply(lambda x: x[:-2])
    
    return X, Y, Y.columns


def tokenize(text):
    '''
    INPUT
    text, the text we will want to breakdown into token
    
    OUTPUT
    tokens. the list of the words that we will watch for
    '''
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')

    stop_words = stopwords.words("english")
    lemmatizer = WordNetLemmatizer()
    
    # normalize case and remove punctuation
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    
    # tokenize text
    tokens = word_tokenize(text)
    
    # lemmatize andremove stop words
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

    return tokens


def build_model():
    pipeline = Pipeline([
        ('feat', FeatureUnion([
            ('pipeline', Pipeline([
                ('vect', CountVectorizer(tokenizer=tokenize)),
                ('tfidf', TfidfTransformer())
            ]))            
        ])),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    
    parameters = { 
    'clf__estimator__n_estimators': [100, 200, 300],
    'clf__estimator__min_samples_split' :[2,4,6],
    }

    cv =  GridSearchCV(pipeline, param_grid=parameters)
    
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    #model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    for category in category_names:
	    print('Category: {}'.format(category))
	    idx = Y_test.columns.get_loc(category)
	    print(classification_report(Y_test[category], y_pred[:,idx]))


def save_model(model, model_filepath):
    
    '''
    INPUT
    model, the pipeline we have created
    model_filepath, the file to save the model to
    
    OUTPUT
    None. The model is saved to filepath
    '''
    
    with open(model_filepath, 'wb') as file:  
        pickle.dump(model,file)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
