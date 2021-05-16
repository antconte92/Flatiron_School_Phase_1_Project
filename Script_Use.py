#Here created multiple functions to grab data from the Yelp API, we parsed through the data: going through each row and extracting the prarameters when we parse.  When we parse through the data we're looking at each index and we're extracting parameters from that index.  Those parameters are Name of each business, location, etc. After we parse through the parameters, we're going to turn each one of them into a DataFrame and save each one of them as a .csv file.  When we go to clean them, we're going to load that entire .csv as one DataFrame and add headers to each column, eliminating each index that does not have a price. Then we replace each price string with it's corresponding interger value.  This dataset is then loaded into the jupyter notebook.  


#You have to import pandas in this function script to be able to create DataFrames.
#You call a function by passing through the arguments that are associated with that function. In order to call it, you need to call the functions name and then pass in the arguments.  In below example, the arguments would be (url_params, api_key). 

import pandas as pd
def yelp_call(url_params, api_key):
    # You have to import requests in order to get your jupyter noteboook to work with the url. 
    import requests
    url = 'https://api.yelp.com/v3/businesses/search'
#headers is used to validate your API
    headers = {
        'Authorization': 'Bearer ' + api_key['key']
    }


#data is used to put everything together, you are putting together your url, your header and the parameters of your search.     
#data is a local variable within this function. Local variables exist within function, but not outside of functions, so we could have one in yelp_call and parse_data with the same lable but they will not affect each other. 
    data = requests.get(url, headers=headers, params=url_params)
    
#the return statement just returns the results of our function and without calling return the data would just stay within the function itself without being visible to the jupyter notebook   
    return data
 
    
#the parse_data function takes in the result of the API function above, it runs through the for loop and extracts each column of data that we want and then returns that data as a list.  

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

#this function just takes the reusults from above (we're grabbing a list from parsed data, passing in a save location(file path) and df_save will turn that list into a saved file as a .csv/a DataFrame. 

#df.to_csv(csv_filepath) - we're specifying that we are going to append a filepath which is what the mode ='a' is doing. Header = false means that we aren't going to include the column names in any of the indexes. 
def df_save(csv_filepath, parsed_results):
    
    df = pd.DataFrame(parsed_results, columns = ['Name', 'Address', 'ID', 'Rating', 'Review_Count','Coordinates', 'Price'])
    df.to_csv(csv_filepath, mode='a', header=False)
    

#The header list is passing in each name of our columns.  When we get down to the pd.read, we are specifying the file path to open. We're setting our index column to 0(zero) which gets rid of the double index.  Then we're passing in the header list as names which will assign the column descriptions to the DataFrame. 
#the df.dropna - we're dropping all of the indexes that do not have a price associated with it.  Dropping the rows where the column price is N/A...
#df['Price] - we're taking the price column, applying a lambda function to it which is essentially a for loop, and in that lambda function, we're taking the length of the string and return that as an interger.  

#df.reset_index - we're resetting the index, now we're making a new index based on the values that are left in the table (basically this subtracts the rows from your data set which were dropped because they didn't have values in the associated column that your filter is based off of. inplace means that we are going to reset those columns in place, if we drop a row with a 3 index, then we're going to create a new 3 index.  Then we're just returning the dataframe so that we can work with it in the jupyter notebook.  This function does not save the dataframe somewhere, and that is because we hard-coded this within the jupyter notebook where we are running this function. 

def df_clean(csv_filepath):
    
    header_list = ['Name','Address', 'Business ID', 'Rating', 'Review Count','Coordinates','Price']
    df = pd.read_csv(csv_filepath, index_col=0, names = header_list)
    df.dropna(subset = ['Price'], inplace = True)
    df['Price']= df[('Price')].apply(lambda x: len(x))
    df.reset_index(inplace = True, drop = True)
    return df 
    






