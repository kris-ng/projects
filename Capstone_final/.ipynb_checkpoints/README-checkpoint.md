## Capstone Project

**Background:** 

Over the past few years living with the pandemic, all of us have had to cut down on social gatherings and stayed home way more than we used to. With most of our time spent within the confines of the same four walls, it is no surprise our [mental health has suffered](https://www.channelnewsasia.com/singapore/singapore-mental-health-awareness-stigma-conditions-depression-1973166). 

**Problem Statement:** 

As a natural consequence of the extended time spent at home, our presence on virtual platforms has [increased sharply](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7280123/). 

A department in the Mental Health Institute is looking into tapping on social media platforms to reach out to the public. Its main aim is to pick out users who can do with help and support as they navigate their way around the negative emotions, ideally before they urgently require intervention. At the same time, it will be a bonus to also connect with those recorded as to be in the pink of (mental) health. 

Goal: To construct a model that can detect the emotion(s) in a comment.

**Data Science Process:**

**Dataset:**

Comments were taken from the subreddit r/depressed.

**Data Dictionary:**

|Feature|Type|Dataset|Description|
|---|---|---|---|
|author|object|df_depressed|The author of the comment.| 
|created_utc|int|df_depressed|The unix timestamp. | 
|body|object|df_depressed|The comment. | 

**EDA:**

Various aspects of the data were explored: 
1. Sentiment Analysis using different libraries
2. Time of posts
3. Length of comments
4. Authors of comments
5. Top words

**Model Building:** 

1) Dataset:

A large dataset [GoEmotions](https://huggingface.co/datasets/mrm8488/goemotions) compiling carefully curated comments extracted from Reddit was the source upon which I built my model. This comprehensive dataset contained comments that were categorised into a total of 27 emotions + 'neutral' classes. 

2) Data Cleaning & Feature Engineering:  

An initial attempt to build a model was met with much delay because of the sheer number of emotions. As such, I tapered it down to only the main 6 emotions as defined by [Ekman](https://www.frontiersin.org/articles/10.3389/fpsyg.2019.00781/full#:~:text=Ekman%20proposed%20seven%20basic%20emotions,sadness%2C%20disgust%2C%20and%20surprise.) as well as a 'neutral' class. 

I also took the opportunity to apply a few ready-made sentiment analysis models from hugging face to observe how they each performed in predicting the emotion of the comment.

3) Data Dictionary:  

|Feature|Type|Dataset|Description|
|---|---|---|---|
|body_alltext|object|df_tomodel|The comment with emojis converted to text.| 
|Sentiment_type |object|df_tomodel|The classification by Vader.| 
|huggingface_sentiment|object|df_tomodel|The classification by a sentiment analyzer from hugging face. |
|t5_emot|object|df_tomodel|The classification by an emotion recognition tool from hugging face. |

4) Preprocessing:

Due to the imbalance in the dataset where 'neutral' took up more than half the data, I made use of class weights to counter this. Beyond this I did the usual cleaning steps by removing punctuation and symbols as well as lemmatized the text. 

5) Modelling & Evaluation:

a) Multiclass classification:

| Model | train score | test score |
| --- | --- | --- |
| MultinomialNB | 0.70 | 0.70 |
| Random Forest | 0.68 | 0.68 |
| LogReg | 0.51 | 0.48 |
| AdaBoost | 0.70 | 0.70 |
| Voting Classifier | 0.76 | 0.74 |
| SVC | 0.79 | 0.74 |

b) Multilabel classification:

| Model | train score | test score |
| --- | --- | --- |
| OneVsRest Classifier | 0.75 | 0.72 |

**Recommendation:**

By using this tool that predicts the emotion(s) in a comment, the system can collate the most recent ~50 posts of each user, detect the majority of the emotion detected and consider doing the following:

i) send user a quote for motivation; 

ii) send user an article for reading; 

iii) activate a chatbot to find out more about what user is going through;

iv) link user up with other useful resources; 

v) connect user with relevant agencies for further help.

**Future Works:**

The model can be continually refined by feeding it with new comments that keep up with the current topic of interests and economical situations so that it better interprets the sentiments. Where resources allow, the model can predict a wider range of emotions to better cater to users' needs. 

If this model takes off, the project can be taken further by availing a user-initiated chat where users can choose to access at various points in time to check on themselves in order to take the appropriate actions to enhance their state of mental health.

**Resources:** 

1. Sentiment analysis libraries:

a) [Vader](https://towardsdatascience.com/sentimental-analysis-using-vader-a3415fef7664)

b) [Adamchell library](https://huggingface.co/adam-chell/tweet-sentiment-analyzer)

c) [t5 emotion recognition](https://huggingface.co/mrm8488/t5-small-finetuned-emotion)

2. Articles about depression:

a) [Mood swings](https://www.webmd.com/bipolar-disorder/are-my-mood-swings-normal#:~:text=Many%20things%20can%20affect%20how,symptom%20of%20a%20mental%20illness.)

b) [Why Am I Only Depressed at Night?](https://www.verywellmind.com/why-am-i-depressed-only-at-night-1066892)

c) [Morning Depression](https://www.webmd.com/depression/morning-depression-overview)

3. Sample of project goal 

[HealthHub](https://www.healthhub.sg/programmes/186/mindsg/caring-for-yourself/managing-our-emotions?utm_source=google&utm_medium=sem&utm_campaign=fy21mh_okay&utm_content=emotions_ad_group)


