import json
import pandas as pd

# Load the JSON data from a file
with open('master_files/cleaned/cleaned_general_confidence_master.json') as f:
    data = json.load(f)

# Create a DataFrame from the JSON data
df = pd.DataFrame(data)

# Convert the 'created_at' column to datetime format
df['created_at'] = pd.to_datetime(df['created_at'])

# Extract the year from the 'created_at' column
df['year'] = df['created_at'].dt.year

# Group the data by 'author_id', 'year', and 'sentiment', and count the number of occurrences
count_df = df.groupby(['author_id', 'year', 'sentiment'])['sentiment'].count().reset_index(name='count')

# Pivot the data to show the number of occurrences of each sentiment for each author in each year
pivot_df = count_df.pivot_table(index=['author_id', 'year'], columns='sentiment', values='count', fill_value=0)

# Apply lambda function
pivot_df[['NEGATIVE_RATIO', 'NEUTRAL_RATIO', 'POSITIVE_RATIO']] = pivot_df[['NEGATIVE', 'NEUTRAL', 'POSITIVE']].apply(lambda x: x/x.sum(), axis=1)

# Apply group by to sentiment levels
sentiment_ratios = pivot_df.groupby("year")[["NEGATIVE_RATIO", "NEUTRAL_RATIO", "POSITIVE_RATIO"]].mean()

#Print the result
print(sentiment_ratios)

sentiment_ratios.to_excel('gen.xlsx')