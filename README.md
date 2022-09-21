# Sentiment Analysis of College Facebook Confession Pages

### Overview
Natural Language Processing (NLP) sentiment analysis on annonymous Facebook posts at top tier colleges, categorizing the negativity of different academic environments. The University of Chicago's confessions page is called UChicago Secrets -- hence the name of this repo. This project was done by Gilad Turok, Philip Chenaux-Repond, and Issac Restrick during University of Chicago's Uncommon Hacks Hachathon in March of 2020. 

### Methodology
To study this effect, we first had to obtain the necessary data. We wanted to look at the annoymous confessions pages on Facebook from different top-tier universities. We chose this source of information because of its honesty and aggregation of a lot of information from many students in one place. We decided to use the confession pages of Caltech, Stanford, MIT, Columbia, and Uchicago because they (largely) had posts stretching back the farthest in time. We wanted to investigate more schools but were limited by the amount of time it took to scrape this information.

We originally planned to use Facebook APIs to aquire the necessary data, but they [changed their policy](https://developers.facebook.com/blog/post/2019/04/25/api-updates/) and no longer let develops access this data. So, instead we used a combination of beautiful soup and chrome driver to scrape these posts. A Facebook page shows very little of the total data at once. So, to get all the posts on one page, we had to continously scroll to the bottom with chrome driver. As pages often contained thousands of posts, this took an immensely long time. Then, when we reached the end of the page, we used beautiful soup to parse the actual text we wanted from the HTML code. 

Next we used Google's SDK with a google cloud account (they sponsered the hackathon) to acces their [sentiment analysis API](https://cloud.google.com/natural-language/docs/sentiment-tutorial) for analyzing our data. Sentiment analysis, a common task in Natural Language Processing, describes the 'character' of a given piece of text. They do this through two metrics -- score and mangitude -- which [Google explains consicely](https://cloud.google.com/natural-language/docs/basics#sentiment-analysis-values): "The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document." Basically, score is the emotion and the magnitude is the instensity with which it is conveyed. We then ran our data through Google's model and combined the two different sentiment metrics. (We combined them by multiplying them together and scaling them by 10. This choice was somewhat arbtrary as it made sense to us but was not based on any actual methodology.)

### Analysis and Results
We made a graph to summarize our results: 

![Final Results](https://github.com/gil2rok/Secrets_NLP/blob/master/secrets_hackathon_final_graph.jpg).

The graph shows time vs post sentiment from a variety of univeristy Facebook confession pages. Also, the University of Chicago runs on a quarter system so we divided the x axis according to our school's schedule.

From this exploratory data analysis, we concluded, first and formost, that UChicago is truly "where fun goes to die". For those that are unfamiliar, this is a common saying about UChicago, sort of like the school's unofficial motto. UChicago is by far the most negative out of its peer institutions. I find this hilarious.

Second, we concluded that generally as the school year wore on, the posts got more and more negative, suggesting that the longer students spent in school, the unhappier they were (to the extent that you can infer happiness from this data). 

### Limitations
First and foremost, we need more data to draw stronger conclusions. Although this was a lot of fun, to produce more meaningful results, we need to collect posts from more schools. Unfortunately, due to time constraints, we were unable to do so. Second, further investigation is needed to examine the correlation between Facebook posts and actual student body happiness. Although a correlation makes sense, there are many other factors to consider (only emotionally-charged students post, online personas not reflecting reality, sensationalism, etc.).

### Conclusion
We believe that this type of analysis can provide a dirt-cheap way of getting a low-resolution snapshot of student happiness. This could possibly inform decisions on academic rigor and requirements, university mental health programming, or perhaps duration of college breaks. Hopefully you found this as interesting as we did.

### Reproducibility 
Please note that this code is not meant for reproducibility or readability. We were coding to get the project done, not to make it look nice. Further, to use it you need to create a Google Cloud sdk account and buy access to their APIs. Because we were part of this hackathon, we were given credits to use this service for free. (Thank you Google!) If you do decide to do so, you need to add the credintials json file that Google Cloud gives you to the dependencies folder. Otherwise this entire setup won't work. 

