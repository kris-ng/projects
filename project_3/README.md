# Project 3 - Web APIs & NLP


### The Data Science Process

**Problem Statement**

On a typical workday while performing maintenance, an engineer accidentally deleted multiple posts from the subreddits r/nottheonion and r/theonion. The former writes true stories that are mind-blowingly ridiculous, so much so that one would have thought it's from the latter which publishes satirical articles on international, national and local news. Despite the engineer's quick follow-up action, it was unfortunate that he could only recover the titles of the lost posts. 

Our team has been engaged to build a classification model which would train on posts submitted before 01 Jan 2022 to correctly sort the recovered posts back to their respective subreddits, r/nottheonion and r/theonion, based solely on the post titles.

In employing NLP to help us build various models such as the Multinomial Naive Bayes, Random Forest, Logistic Regression etc, we will peg success to the initial accuracy scores across our cross validations. Beyond that, we will dive deeper into studying the confusion matrices together with the f1 scores to pick out the best model(s).

As it is now, our primary stakeholders - the volunteer moderators of each subreddit thread - have to spend a substantial amount of time reviewing user reports and deleting spam posts from the subreddits. This is especially so with the increase in bots spamming subreddits with irrelevant posts. With this classifier model, we can use it as a proof of concept for the development of an automated moderator which would automatically delete posts that do not belong to the subreddit that they have been posted to. This in turn helps to free up time for our human moderators. As a consequence, our secondary stakeholders - the subreddit community as a whole - can enjoy their daily reads without being bothered by disparate frills.


**Data Collection**

Using Pushshift's API, I carried out Data Wrangling by scrapping ~2000 posts from each of the two subreddit threads - The Onion and Not the Onion. But because there were many repeat posts especially in the latter presumably as a means to get more likes by the thread's readers, I had to ensure that I picked out only unique posts from each thread before taking further action on the dataframe collected.  


**Data Cleaning and EDA**

In cleaning the data, I carried out the standard steps in Natural Language Processing such as removing punctuation, changing to lower cases to be able to convert standard text data into a format that allows for analysis and subsequent modeling.

Initial EDAs I did include looking into the length and number of words in the titles to get a sense of the average titles we are dealing with. With the posts not being of a substantial length, I did question if my subsequent model will have sufficient data to predict well. I also looked at the top authors in each thread just to get a sense that they aren't the same people. I also picked out the top unigrams and bigrams in each thread to get an idea of how distinct the lists were. 

**Preprocessing**
Since the goal was to shift the mixed posts back into the subreddit thread Not The Onion, I created the binary labels '0' for Not The Onion and '1' for The Onion. 

Once I defined the titles of the posts as the independent variable X and the subreddit post as the target y, I carried out the train test split before proceeding to try out the various models.

**Data Dictionary**

|Feature|Dataset|Description|
|---|---|---|
|subreddit|df|The subreddit thread the post was taken from.| 
|author|df|The author of the post. | 
|title|df|The title in the post. | 
|title_length|df|The letters in the title of the post. | 
|title_word_count|df|The number of words in the title of the post. | 
|predicted_subreddit|summary|The subreddit it is predicted to be from. | 
|original_subreddit|wrongpred|The original subreddit thread the post is from. | 


**Modeling** 

In Classification Modeling, I started off with the Dummy Classifier from sklearn as the baseline model. 

Following that, I tried out both the CountVectorizer and TfidfVectorizer on the Multinomial NB but saw no marked improvement despite my understanding that TfidfVectorizer typically improves the prediction because of how intensive it goes into calculating the word count in relation to the rest of the words. I continue to build other models such as Random Forest, Knn, Logistic Regression etc using TfidfVectorizer.

From trying the simpler models like the Logistic Regression to the more complex ones such as the AdaBoost, the scores stayed mostly within the region of 80+ in training score and 70+ in test score. 


**Evaluation** 

I summarise the results of my tests below.

| Model | Train score |Test score |
| --- | --- |--- |
| CountVect Dummy Classifier | 0.51 | 0.48 |
| CountVect Multinomial NB | 0.79| 0.73 |
| TfidfVect Multinomial NB | 0.80| 0.72 |
| TfidfVect Random Forest | 0.73| 0.68 |
| TfidfVect Knn | 0.90| 0.67 |
| TfidfVect Logistic Regression | 0.82| 0.73 |
| CountVect Logistic Regression | 0.83| 0.72 |
| TfidfVect AdaBoost (Decision Tree) | 0.85| 0.68 |
| TfidfVect Voting Classifier | 0.80| 0.68 |
| TfidfVect SVC | 0.95| 0.76 |

I followed up the scores with the confusion matrices for the top performing models ie Multinomial NB, Logistic Regression and SVC so as to analyse their performances deeper using the f1 score.

All in all, SVC turned out to be the best performing since its f1 score is the highest, signifying that both precision and recall were optimized. The Logistic Regression on the other hand, was able to balance the number of False Negatives and False Positives, getting a ratio of 0.97. 

I also attempted to venture into unfamiliar grounds using ROC and AUC graphs. From my understanding, the closer to 1 AUC is the better, so with an AUC of 0.81 it tells me that the SVC model has a 81% chance that it will be able to distinguish between the positive and negative classes which is a decent score.

**Conclusion and Recommendations** 

As a conclusion, I would say that my model is sufficiently good since it can correctly classify 76% of the posts, which means almost 80% of lost data can be restored accurately. Although I'm rather contented with the performance of my SVC model, I do wonder if implementing a trigram or beyond approach would help me reduce the number of wrong predictions. Having said that, I did run GridSearch which picked out the best ngram_range as [1,2] instead of [1,3] so I shan't pick on it.

Perhaps the posts from these two subreddit threads are to a certain extent rather similar in terms of their topics and vocabulary used hence my accuracy scores never quite hit the mark of 0.80.

Considering the accuracy score improved from 0.6+ to 0.7+ by me scrapping an extra 1000 posts per subreddit, I do think my model can do even better if I scrapped more posts. However, with limited time and processing power, the engineer in question should be happy to implement this model in sorting out the posts. On another note, I do believe that if I had more columns of data besides just the title text, my model's performance may be enhanced even further. In the long run, machine learning models are in fact very much feasible for automated moderation in a bit to lighten the human moderator's workload. Having said that, I must also state a caveat that no matter what model we have, such a classification is still somewhat of a blackbox because we cannot say for certain that specific words determine the source of the subreddit since it really depends on the context of the word use. 


### References
1. These two subreddit threads were what we picked out because we wanted the challenge of similar yet implicitly different content to test if we can come up with a good model that predicted as close to perfection as possible. 

[r/The Onion](https://www.reddit.com/r/TheOnion/)  

[r/nottheonion](https://www.reddit.com/r/nottheonion/)  

2. This [video](https://youtu.be/AcrjEWsMi_E) was extremely helpful in guiding me step by step on how to scrap the posts needed for this project.






