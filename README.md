## Jeffrey, the Real Estate RoboAdvisor

<p align="center">
<img src="https://github.com/padthai-sketch/Project-RealEstate-RoboAdvisor-Group-6-/blob/main/Images/logo.png?raw=true" alt="drawing" width="300"/></p>

**Team Members**

*Ingrid, Kaleb, Bowie*

**Project Description**

The purpose of our project is to build the RoboAdvisor from AWS Lex that helps the prospective homebuyer find their dream home in Austin, Texas. In order to search for the house, the user will be asked to provide neccessary parameters as following. 
- personal annual income, 
- property type, 
- price range, 
- number of bedrooms, 
- number of bathrooms, 
- location, 
- the amount of down payment. 

After that, the bot will generate the list of property that similar to their preference and able to suggest the further process if the user decide to purchase the property. 

**Objectives / Project Questions to Answer**

The Robo Advisor is able to suggest the property that meet the user criteria by filtering through the number of listing and providing the property detail and sale price. We will be using machine learning models: K-Means Clustering and Sentimental Analysis to group similar properties togehter and will be using deep learning model to train the data. We will also explore the possibility of using Google map to show the property in the area.

**Data Sources (APIs, Datasets)**

ACTRIS Dataset from Bridge Interactive API - the real estate data in Austin, TX from 2020

**Libraries**

- sklearn
- tensorflow
- NLTK

**Rough Breakdown of Tasks**

<ins>Backend</ins>
1. Collect data from Bridge Interactive API and import neccessary libraries.
2. Clean and standardize data
3. Create Lambda Function, featuring machine learning and deep learning models to train data.

<ins>Frontend</ins>
1. Create the Real Estate RoboAdvisor name "Jeffrey" on AWS Lex
2. Set up intents, utterances, and slots.
3. Adding Lambda function and test the bot 


- Ingrid - Create the Power Point Presentation and README write-up Summary. Build LAMBDA Function.

- Kaleb - Import Data and Build LAMBDA Function.

- Bowie - Create the intend and the slot type in AWS Lex. Build LAMBDA Function.
