---
#
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: home
---

![Image of Fruits](assets/maha_banner.jpeg "Vegetable Lot from pexels.com/@pixabay")

## Teaser*

People buy anything on Amazon nowadays, because it’s so unbelievably simple. You just order it and when you don’t like it, you send it back. This concept might work well for electronic devices or clothing, but gets difficult when it comes to food and groceries. Once you have your food intoxication, you can maybe try to sue Amazon for that, but before you’re successfull you might already have passed away. Of course this can also happen in your local store, the advantage of Amazon is the BIG DATA that comes along with it. Usually, people don’t die directly from contaminated food, so they have time to complain about their purchases - and they do! When being displeased with products, they write angry reviews about them. The question for a data scientist now is: **by analyzing Amazon reviews of food products and groceries, can we detect dangerous, possibly contaminated or intoxicated products?** That question was part of our project and will be adressed in the following data story!

*[not to be taken seriously]

## Introduction

Since it was founded in 1994, Amazon is constantly growing. More and more customers as well as dealers use Amazon, because it simplifies daily life. Nowadays, you can even buy food on Amazon. This may offer great possibilties for health agencies as the U.S. Food and Drug Agency (FDA). Amazon knows exactly who sold and who bought each product and could use this information to inform dealers and customers about warnings and recalls for specific products by the FDA. This would provide a great service to the public, e.g. for allergic people when the FDA found a missing declaration of allergens.

However, one could even go a step further by trying to detect potential health issues before the FDA even took a look at it. We propose that it may be possible to detect potentially hazardeous food products on Amazon by analyzing customer reviews. In the following article, we are going to show several approaches to classify Amazon reviews of food products in regard to whether their product being a potential health threat or not.

#### What our dataset is about

The main dataset we used contained Amazon reviews of food products from several years. Each datapoint had information about the reviewer's ID, the product ID, the date of purchase, the review text itself and the overall rating the customer gave the product (an integer score going from one star (worst option) to five stars (best option). The reviews in our dataset do mainly come from 2012, 2013 and 2014. Though our analysis cannot claim for actuality, we can assume the data's characteristics (i.e. the length or the the vocabulary used in the reviews) has not changed since then. Conclusions about the potential danger of individual products, however, can not be made.

<center><img src="assets/plots/histogram_year.png" alt="Reviews per year in dataset" width="60%" /></center>

A good measurement for the overall satisfaction of customers with a product probably is the rating, given in one to five stars. As we can see, most ratings were excellent. That's not ideal for us as we want to focus on negative reviews, even on particularly health related ones. 


<center><img src="assets/plots/B1_bar" alt="Barchart of Reviews per Overall Rating" width="50%" /></center>

At least the following boxplot shows that the number of words per review might be sufficient to perform text analysis methods on them. 

<center><img src="assets/plots/B2b_boxplot" alt="Boxplot of words per review per rating" width="50%" /></center>

That wasn't necessarily expectable, if one takes a look at the following histogram of review length frequency. As one can see, the distribution does follow a power law. Most reviews are very short and longer ones are rare, but not very rare.

<center><img src="assets/plots/B2a_bar" alt="Histogram of review lengths" width="70%" /></center>

What was expectable and can nicely be shown in the following histogram is the distribution of individual word frequencies over the whole dataset. It was observed that this distribution commonly follows a power law which is called Zipf's law in text analysis. 

<center><img src="assets/plots/B6_zipf" alt="Distribution of word frequencies in reviews" width="70%" /></center>

Our goal was now to build a model and train a supervised machine learning based classifier on our dataset of Amazon reviews in order to be able to classify reviews as either "potentially health threatening" (or short "dangerous") or as "probably not health threatening" (or short "safe"). The most challenging part of this was to distinguish between general dislikes and health concerning dislikes.

Training the classifier means showing many many examples of reviews and thereby telling it whether they are dangerous or safe. As the model our classifier is based on we chose a [Random Forest](https://en.wikipedia.org/wiki/Random_forest) algorithm. A Random Forest is basically a bunch of many decision trees, each is trained on a different bootstrap sample of the whole data. A majority vote among all trees then classifies the input.

However, for training the classifier, we need labeled data. To be able to label the reviews in the dataset as potentially health threatening or not, we thought of different approaches:
* One approach was to use [AFINN Sentiment Analysis](https://darenr.github.io/afinn/) (Rowe et al, 2011). Afinn is a python library for [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis), i.e. it classifies a text document as positive, neutral or negative by summing up scores or individual words. E.g. the word "horrible" has a score of -3, the word "inconvenient" has a score of -2, meaning it is less severe than "horrible". Afinn also contains health related words (e.g. "headache" or "vomit"), nevertheless we chose not to use it for labelling the reviews. Sentiment analysis is obviously made for distinguishing general emotion and not for assessing health issues in text.
* The second idea was to link the reviews to corresponding products in two other datasets of food recalls and press releases of the US American [Food and Drug Administration](https://www.fda.gov/) (FDA). This would have provided us very reliable labels made by professionals. Unfortunately, it was not possible as Amazon and the FDA use different Product IDs which cannot be matched (free of charge). In consequence, we had to find a work around:
* From various sources (see below) we imported words related to food, food safety, symptoms and pathogens (e.g. bacteria like salmonella)

| **Pathogen and disease words (e.g. salmonella)** |  |
| --- | --- |
| EU safe food | [Link](https://www.safefood.eu/SafeFood/media/SafeFoodLibrary/Documents/Education/safefood%20for%20life/NI/section2_1.pdf) |
| Foodsafety.gov bacteria and viruses words | [Link](https://www.foodsafety.gov/food-poisoning/bacteria-and-viruses) |
| CDC foodborne illness words | [Link](https://www.cdc.gov/foodsafety/diseases/index.html) |
| CDC national outbreak reporting system | [Link](https://wwwn.cdc.gov/norsdashboard/) |
| **Symptom words (e.g. embolism)** |  |
| EU safe food | [Link](https://www.safefood.eu/SafeFood/media/SafeFoodLibrary/Documents/Education/safefood%20for%20life/NI/section2_1.pdf) |
| Foodsafety.gov symptom words: | [Link](https://www.foodsafety.gov/food-poisoning) |
| Symptom dictionary  | [Link](https://github.com/sekharvth/symptom-disease) |
| **Food words (e.g. egg)** |  |
| Exhaustive list of all foods & food items in the world | [Link](https://github.com/CurtisGrayeBabin/List-of-all-Foods) |

By analyzing these sources together with the FDA datasets we created lists of words that relate to either pathogens and diseases or symptoms, respectively. However, we decided not to use them for labelling but for post classification analysis as they contain actual threats like the names of bacteria and not vocabulary that might be used to describe their effects.

* The fourth approach, which we used in the end, is based on [Empath](https://github.com/Ejhfast/empath-client). Empath is a python library for sentiment analysis and topic detection. It was created by Fast et al. (2016). 

)### empath C1
create  lexicon of words related to "health", "danger", "food poisoning"  
new column: health score  
new column: danger: healthScore > 0 AND rating smaller than 4  
danger is either 1 or NaN  
3755 reviews labeled with 1  
take sample of all danger=NaN reviews  -> negative_sample  
in empathy, replace danger=NaN with danger=0  
save empathy to pickle  

#### afinn C2
add afinn columns by processing stemmed df  
add afinn columns by processing stemmed_frequent=stemmed.copy(), afinn calculations done on list of frequentWords (are actually same as all words as there are only ~25000 words.  

No actual labelling  

#### FDA datasets
find frequent words in both FDA datasets  

We analyzed the notes coming with the product recalls from FDA and tried to find specific vocabulary which is used in health threat related issues.  
In the following wordcloud it is clearly visible that this will still remain a challenging task, as there are general groceries like "egg" or "peanuts" and specialist terms like "monocytogenes" as well.
<center><img src="assets/plots/C3_wordcloud_press" alt="Most frequent words in FDA press releases" width="60%" /></center>


### Classification
load pickle empath
drop columns date, categories, brand, overall
tokenReviews -> tokenize, remove stopwords, stem
vectorize tokenReviews -> feature column
train the classifier (random forest) with all reviews that have danger=1

Accuracy of classifier = 0,839

take all so far unlabelled reviews (danger=NaN), classify them
merge them into the df from previously labelled/classified reviews


### Bibliography
* Finn Årup Nielsen, "A new ANEW: evaluation of a word list for sentiment analysis in microblogs", Proceedings of the ESWC2011 Workshop on 'Making Sense of Microposts': Big things come in small packages. Volume 718 in CEUR Workshop Proceedings: 93-98. 2011 May. Matthew Rowe, Milan Stankovic, Aba-Sah Dadzie, Mariann Hardey (editors)
* Fast E, Chen B, Bernstein MS. Empath: Understanding topic signals in large-scale text. In: Conference on Human Factors in Computing Systems - Proceedings. ; 2016. doi:10.1145/2858036.2858535











