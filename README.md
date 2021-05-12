## Jeffrey, the Real Estate RoboAdvisor

<p align="center">
<img src="https://github.com/padthai-sketch/Project-RealEstate-RoboAdvisor-Group-6-/blob/main/Images/logo.png?raw=true" alt="drawing" width="300"/></p>

**Team Members**

*Ingrid, Kaleb, Bowie*

**# Project Description**

The purpose of our project was to build a RoboAdvisor using AWS Lex that helps prospective homebuyers find their dream home in Austin, Texas. This to will act as mix of a mortgage calculator and a real estate website such as Zillow or Redfin. In order to get their recommendation, the user will be asked to provide the neccessary parameters as following:
- Name
- Age
- Credit Score
- Annual Household Income
- Amout Saved for a Downpayment
- Number of Bedrooms
- Number of Bathrooms 
- Square Footage

After that information is provided by the user, the bot will generate a list of a few properties that fit their preferences and provide the listings for each property. Don't waste time searching through houses that don't fit your preferences, let Jeffrey do the work for you!

**# Objectives** 

The Robo Advisor is able to suggest properties that meet the user criteria by filtering through the number of listing and providing the property detail and sale price. We will be using machine learning models: K-Means Clustering and Sentimental Analysis to group similar properties togehter and will be using deep learning model to train the data. We will also explore the possibility of using Google map to show the property in the area.

**# Data Sources (APIs, Datasets)**

ACTRIS Dataset from Bridge Interactive API - the real estate data in Austin, TX

**# Libraries**

sklearn
tensorflow
NLTK
Rough Breakdown of Tasks

*Backend*

- Collect data from Bridge Interactive API and import neccessary libraries.
- Clean and standardize data
- Create Lambda Function, featuring machine learning and deep learning models to train data.

*Frontend*

- Create the Real Estate RoboAdvisor name "Jeffrey" on AWS Lex
- Set up intents, utterances, and slots.
- Add Lambda function and test the bot
- Link Google Map with the bot (if possible)

After that information is provided by the user, the bot will generate a list of a few properties that fit their preferences and provide the listings for each property. Don't waste time searching through houses that don't fit your preferences, let Jeffrey do the work for you!

The Robo Advisor is able to suggest properties that meets the user's criteria by filtering through the number of listings in our dataset. We got this dataset from Bridge Interactive, using an API. This includes a large number of listings in Austin, Texas along with all of the property details for each listing. 

<p align="center">
<img src="https://github.com/padthai-sketch/Project_RealEstate-RoboAdvisor-Team6/blob/main/Images/JeffreyBot_Recording.gif" alt="drawing" width="800"/>
</p>

** We did not have enough time to trobleshoot the problem with Lambda function. Jeffrey would be more efficient if we were able to fix the issue. 
