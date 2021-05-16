# Where to Open a Bar in 2021: New York vs. Boston

Using the Yelp API, we analyzed a total of 600 bars in NYC and Boston to determine what would be the best city to open up a bar in 2021. 

The objective of this project was to use Python to conduct EDA in order to assess where to open a bar, and the target demographic we would like to capture in order to maximize the profitability of our business. 

## Our Process:
We extracted the data using the Yelp API and utilized several different Python libraries to clean up our data set. The variables we looked into included Price, Rating, and Review Count.  We also used the Business ID metric to be able to extract additional information regarding customer satisfaction from the Yelp API and merge our two data sets together for further analysis.

From the analysis that we conducted, we found that there is an opportunity to open up a bar in Boston with a high rating (4.5 or greater) at a lower price point than what is currently being captured in the market.

## Findings from our EDA:
From our initial data extraction, there were several bars missing the Price scale criteria so we dropped them from our analysis.

Approximately 3% of our initial search results were dropped from the data set because they were missing Price values.

## Digging Into the Adjusted Data Set and Extrapalating Actionable Insight:

We created several charts to be able to assess the ideal location and environment for our business.

From our initial analysis, we found that Boston has a greater number of bars with less than a 4 star rating compared to New York.

We were surprised to find that there were several bars in Boston that had a rating below 3 stars, whereas the rating for New York bars were 3 or greater.

An additional metric we took in consideration was the amount of ratings received per price scale.  This allowed us to realize that there is a niche for a highly rated bar (> 4.5 Star Rating) with a low price rating in the city of Boston.  From the insight we gained through our data set, Boston generally has more expensive bars than New York. 

We also found that on average, the bars in Boston were more frequently reviewed thank New York bars, however, when it came down to bars on the higher end of review counts, New York bars surpassed Boston when it came down to 3K or greater reviews. 

## Below is a breakdown of what is captured in our repository: 

Data: This folder contains all of the formatted information from our Yelp API search in .csv format. 

Images: Visualizations from our data set are stored here. 

Business_Details_Questions Jupyter Notebook: This summarizes our findings from the data set based the questions we were tasked to answer. 

Call_Business_Details: This uses the Script_Use Python script to extract information from the business search Yelp API. 

Call_Reviews: This utilizes the Review_Helper script to pull bar reviews from the Yelp API. 

Phase_1_Project_Charts: We used this Jupyter Notebook to create visualizations to gain insight and convey the findings of our study. 

README.md: Provides a synopsis of the method and findings of our analysis. 

Presentation Link: https://docs.google.com/presentation/d/14YCahH-pm5YRGxEyc9EZXTN1FgwofhuJpoStWRfMHq0/edit#slide=id.p
