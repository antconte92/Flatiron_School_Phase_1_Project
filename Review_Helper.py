import json
import pandas as pd
import requests
import csv

with open('.secrets/creds.json') as f:
    api_key = json.load(f)
        
def yelp_reviews(ID, api_key):
    reviews_dict ={}
    url = f'https://api.yelp.com/v3/businesses/{ID}/reviews'
    

    headers = {
        'Authorization': 'Bearer ' + api_key['key']
    }


    data = requests.get(url, headers=headers)
    yelp_results = data.json()
    business = yelp_results['reviews']
    RL = []

    for review in business:
        review_tuple = (review['id'] , ID, review['text'], review['rating'])
        RL.append(review_tuple)
       
    return RL
    
    header_list = ['Review ID', 'Business ID', 'Review', 'Rating']
    df = pd.read_csv(csv_filepath ,names = header_list)
    df.reset_index(inplace = True, drop = True)
    df.to_csv(cleanedFile, header = True)
    return df 
