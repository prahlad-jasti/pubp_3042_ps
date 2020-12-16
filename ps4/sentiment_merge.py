import pandas as pd

sentiment_data = pd.read_csv('plugshare-processed-sentiment.csv') 
true_labels = pd.read_csv('true-sentiments.csv')

merged_data = sentiment_data.merge(true_labels, left_on = 'Id (Review)', right_on = 'Id (Review)')

merged_data.to_csv('final-dataset.csv')
print(merged_data)

print(len(merged_data[merged_data['Rating'].str.lower() == merged_data['True Sentiment'].str.lower()]))
