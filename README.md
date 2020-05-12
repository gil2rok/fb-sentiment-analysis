# Secrets_NLP
### Overview
Sentiment analysis on annonymous Facebook posts at top tier colleges, categorizing the negativity of different academic environments. This project was done by Gilad Turok, Philip Chenaux-Repond, and Issac Restrick during UChicago's Uncommon Hacks Hachathon in March of 2020. 

### Summary
To study this effect, we first had to obtain the necessary data. We wanted to look at the annoymous confessions pages on Facebook from different top-tier universities. We chose this source of information because of its honesty and aggregation of a lot of information from many students in one place. We decided to use the confession pages of Caltech, Stanford, MIT, Columbia, and Uchicago because they (largely) had posts stretching back the farthest in time. We wanted to investigate more schools but were limited by the amount of time it took to scape this information.

We originally planned to use Facebook APIs to aquire the necessary data, but they [changed their policy](https://developers.facebook.com/blog/post/2019/04/25/api-updates/) and no longer let develops access this data. So, instead we used a combination of beautiful soup and chrome driver to scrape these Facebook posts.

Then we used Google's SDK with a google cloud account (they sponsered the hackathon) to acces their [sentiment analysis API](https://cloud.google.com/natural-language/docs/sentiment-tutorial) for analyzing our data. Sentiment analysis, a common task in Natural Language Processing, describes the 'character' of a given piece of text. They do this through two metrics -- score and mangitude -- which [Google explains consicely](https://cloud.google.com/natural-language/docs/basics#sentiment-analysis-values): "The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document." Basically, score is the emotion and the magnitude is the instensity with which it is conveyed. We then ran our data through Google's model and combined the two different sentiment metrics. (We combined them by multiplying them together and scaling them by 10. This choice was somewhat arbtrary as it made sense to us but was not based on any actual methodology.)

After this, we made a graph to summarize our results:

We were limited by the amount of time it took to scape this information
we used Google's Natural Lannguage Processing (NLP) API for sentiment analysis, allowing us to Secrets Facebook Page NLP Sentiment Analysis

