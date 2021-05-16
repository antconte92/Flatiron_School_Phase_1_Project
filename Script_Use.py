import pandas as pd

def yelp_call(url_params, api_key):
    import requests
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {
        'Authorization': 'Bearer ' + api_key['key']
    }

    data = requests.get(url, headers=headers, params=url_params)
    
    return data
 
def parse_data(list_of_data):
  
    PD = []
     
    for business in list_of_data:
        if 'price' in business:
                biz_tuple = (business['name'], business['location']['display_address'], business['id'],   business['rating'],
                      business['review_count'],business['coordinates'], business['price']) 
        else:
                biz_tuple = (business['name'], business['location']['display_address'], business['id'], business['rating'], business['review_count'],business['coordinates'] )
    
        PD.append(biz_tuple)
    
    return PD

def df_save(csv_filepath, parsed_results):
    
    df = pd.DataFrame(parsed_results, columns = ['Name', 'Address', 'ID', 'Rating', 'Review_Count','Coordinates', 'Price'])
    df.to_csv(csv_filepath, mode='a', header=False)
    
def df_clean(csv_filepath):
    
    header_list = ['Name','Address', 'Business ID', 'Rating', 'Review Count','Coordinates','Price']
    df = pd.read_csv(csv_filepath, index_col=0, names = header_list)
    df.dropna(subset = ['Price'], inplace = True)
    df['Price']= df[('Price')].apply(lambda x: len(x))
    df.reset_index(inplace = True, drop = True)
    return df 
    






