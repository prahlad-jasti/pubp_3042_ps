import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, EntitiesOptions, KeywordsOptions
import pandas as pd
dataset = pd.read_csv('plugshare-small.csv')

review_data = dataset
review_data = review_data[review_data['Review'].notna()].copy()

def get_sentiment(input):
    authenticator = IAMAuthenticator('vpVCzfGx6R83YgKE_vz_aoldL3tDjT_F3svSZbv5YSya')
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2020-08-01',
        authenticator=authenticator
    )
    
    natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/f23d06b9-65a4-4b6c-b87a-43d1a61ac90c')
                                                   
    response = natural_language_understanding.analyze(
        text = input,
        language = 'en',
        features=Features(sentiment=SentimentOptions())).get_result()
    
    sentiment = response['sentiment']['document']['label']
    score = response['sentiment']['document']['score']

    return [sentiment, score]
    
  review_list = []
print("- Passing reviews to Watson API..")
print("- This may take some time as we have thousands of API calls.")
i = 0
for review in review_data['Review']:
    try:
        print(i)
        i = i + 1
        review_list.append(get_sentiment(review))
    except:
        review_list.append(['error', 'error'])

        
# Combine the output from Watson into our original Dataframe
review_data['Output'] = pd.Series(review_list).values


# UDF to help split [Sentiment, Output] into 2 separate columns
def split_output(df):
    def get_rating(row):
        return row['Output'][0]
    def get_score(row):
        return row['Output'][1]

    df['Rating'] = df.apply(get_rating, axis=1)
    df['Score'] = df.apply(get_score, axis=1)
    df = df.drop('Output', 1)

    return df

review_data = split_output(review_data)


# Save our dataframe into csv
review_data.to_csv('plugshare-processed-sentiment.csv', index=False)
print("- Output successfully saved!")
