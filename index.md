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

Since it was founded in 1994, Amazon is constantly growing....

Our research questions ....

#### What our dataset is about

The reviews in our dataset do mainly come from 2012, 2013 and 2014. Though our analysis cannot claim for actuality, we can assume the data's characteristics (i.e. the length or the the vocabulary used in the reviews) has not changed. Conclusions about the potential danger of individual products, however, can not be made.

<center><img src="assets/plots/histogram_year.png" alt="Reviews per year in dataset" width="60%" /></center>

A good measurement for the overall satisfaction of customers with a product probably is the rating, given in one to five stars. As we can see, most ratings were excellent. That's not ideal for us as we want to focus on negative reviews, even on particularly health related ones. 


<center><img src="assets/plots/B1_bar" alt="Barchart of Reviews per Overall Rating" width="50%" /></center>

At least the following boxplot shows that the number of words per review might be sufficient to perform text analysis methods on them. 

<center><img src="assets/plots/B2b_boxplot" alt="Boxplot of words per review per rating" width="50%" /></center>

That wasn't necessarily expectable, if one takes a look at the following histogram of review length frequency. As one can see, does the distribution follow a power law. Most reviews are very short and longer ones are rare, but not very rare.

<center><img src="assets/plots/B2a_bar" alt="Histogram of review lengths" width="70%" /></center>

What was expectable and can nicely be shown in the following histogram is the distribution of individual word frequencies over the whole dataset. It was observed that this distribution commonly follows a power law which is called Zipf's law in text analysis. 

<center><img src="assets/plots/B6_zipf" alt="Distribution of word frequencies in reviews" width="70%" /></center>

To be able to label the reviews in the dataset as potentially health threatening or not, we tried to link the corresponding products in two other datasets of food recalls and press releases of the US American Food and Drug Administration (FDA). Unfortunately, this was not possible as Amazon and the FDA use different Product IDs which cannot be matched (free of charge). In consequence, we had to find a work around. We analyzed the notes coming with the product recalls from FDA and tried to find specific vocabulary which is used in health threat related issues.  
In the following wordcloud it is clearly visible that this will still remain a challenging task, as there are general groceries like "egg" or "peanuts" and specialist terms like "monocytogenes" as well.
<center><img src="assets/plots/C3_wordcloud_press" alt="Most frequent words in FDA press releases" width="60%" /></center>













