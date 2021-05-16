#importing all of the libraries we need to use the functionaly needed to be able to do our analysis.  
import json
import pandas as pd
import requests
import csv

#We need to establish a key within the notebook in order to be able to pull the information from the Yelp API.  Since API's are 'private information' we need to extract these variables that live in a hidden folder to be able to use them for our python script. The API key is the keycard that allows us to use the Yelp API and extract information from it.  

with open('.secrets/creds.json') as f:
    api_key = json.load(f)
    
#Similar functionality to what we pulled for the business results, however, we are now passing in two arguments.  ID will change depending on our for loop, API Key will stay the same, and we're pulling the Reviews, Review ID, and the Review Rating and creating a list with that information.  We're returning one string of tuples in this function.  The tuple is basically creating a set of variables that are derived from the initial data set.  
    
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
    
        
        
#We then return that list of tuples as a list with the return RL line.     
    return RL


#This function essentially creates a new DataFrame from the data that we grabbed above.  First we got rid of the axis from when we extracted the above data.  Then, we're saving the DataFrame to a new filepath that doesn't mutate the original .csv file. We're passing in 2 arguments here, the unclean .csv file and the location for where the clean .csv file needs to be saved. 

def review_clean(csv_filepath , cleanedFile):
    
    header_list = ['Review ID', 'Business ID', 'Review', 'Rating']
    df = pd.read_csv(csv_filepath ,names = header_list)
    df.reset_index(inplace = True, drop = True)
    df.to_csv(cleanedFile, header = True)
    return df 