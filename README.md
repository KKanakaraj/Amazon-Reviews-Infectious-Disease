# Improvement of the Amazon Recommendation System

# Abstract
In our project, we aim at improving the Amazon Product Recommendation System for groceries by assessing and analyzing reviews of users. Using Natural Language Processing (NLP) on the [Amazon Grocery and Gourmet Food Product reviews](http://jmcauley.ucsd.edu/data/amazon/) database and [FDA food recalls](https://open.fda.gov/downloads/), we want to detect products that may be harmful and provide alternative options to customers. This may be done by graph based time-link prediction.

In our data story we will try show how a general bad review of a product (i.e. because of personal taste or false expectations of the user) should be distinguished from health related ones. Using the FDA dataset will help us relating reviews to actual recalls of food products.

The overall goal is to enhance Amazon's user experience by considering possible health threats. This would encourage retailers to maintain quality standards, could improve quality of food products and eventually enhance health and life quality of people.

# Research questions
* Can possibly harmful products from Amazon's grocery and food products be detected by analyzing user reviews?
* Is the FDA recall system effective? Are there hints on possibly dangerous food products that have not been recalled by the FDA?
* Can insights from our research be used to improve Amazon's Recommendation system in regard to protecting Amazon users' health?

# Dataset

We plan to get the two datasets from Julian McAuley
* [Amazon's Grocery and Gourmet Food product reviews](http://jmcauley.ucsd.edu/data/amazon/) from Julian McAuley, UCSD (University of California, Sandiego)
* [Amazon's Grocery and Gourmet Food product metadata](http://jmcauley.ucsd.edu/data/amazon/) (to be able to link the reviews' asin field with an actual product name) from Julian McAuley, UCSD (University of California, Sandiego)
* Food Recall Enforcement Reports from [FDA](https://open.fda.gov/downloads/) from Food and Drug Administration (FDA)

Below Table shows the number of user reviews and number of products for Amazon's Grocery and Gourmet Food:


| Number\ Category  | Grocery and Gourmet  |
| ------------- | ------------- |
|Reviews  | 1,297,156   |
| Products  | 171,760  |

The format of the files for both metadata and reviews dataset was json. The size of each
raw data set is presented in the Table below:

| Size\Category  | Grocery and Gourmet Food  |
| ------------- | ------------- |
|Reviews  | 733.5 MB   |
| Products  | 196.8 MB  |



The data collected is very huge spanning from 2000-2014. Therefore first the data was
analyzed for number of reviews for each year in order to choose the years for parsing the
data set for testing and validating phase for the recommender system.

Below is an example of Amazon product Review parser(year wise) code:
![Screenshot](Review_Parser.png)


![Screenshot](histogram_year.png)


From the above chart it clearly visible that larger reviews are available only in few years,
that is in the case:
* Grocery and Gourmet Food- (2012 - 192903), (2013 - 466834), (2014 - 338303)

# A list of internal milestones up until project milestone 2
* Explore various Natural Language Processing (NLP) algorithms to detect and classify possibly harmful products by analyzing user product reviews.

* Explore various Graph mining algorithms to detect and classify possibly harmful products by analyzing user product reviews.

* Convert data to snap formart

* Compare time points of health related negative reviews and FDA product recalls.

# Questions for TAa
* Which of the Amazon's dataset are we actually supposed to use? The dataset's name on the google docs indicate that we are supposed to use only the reviews from the Grocery and Gourmet Food category, but the indicated size is for all the categories.

* Related to the previous, the source for the dataset links to the 2014 version, but there is a new 2018 updated one. Thus, all the links for data download on the source's page redirects us to the new, updated version. Which one will be made available on the cluster?
