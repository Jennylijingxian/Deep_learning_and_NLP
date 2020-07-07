# Deep_learning_and_NLP
A collection of deep learning &amp; NLP projects
- **Deep_learning** 
  - **text_classification_bow.ipynb:** Created a bag of word model for [subjective/objective movie review](http://www.cs.cornell.edu/people/pabo/movie-review-data/) classification and obtained an accuracy of 0.911. 
  - **quora_questions_pair_classification.ipynb:** Identified [if two quora questions have the same intention](https://www.kaggle.com/c/quora-question-pairs) using Manhattan_LSTM.
  - **sentiment_classification_gru.ipynb:** Performed sentiment classification with GRU on the [imdb dataset](http://ai.stanford.edu/~amaas/data/sentiment/).
  - **last_name_cnn.ipynb:** Classified last names with character-level CNN and obtained an accuracy of 0.77.

- **BBC_articles_recommendation**
  Built [BBC article](http://mlg.ucd.ie/datasets/bbc.html) recommendation engines using word2vec and launched server on AWS.
  Here's a example of how it works:  
  <img src="https://github.com/Jennylijingxian/Deep_learning_and_NLP/blob/master/images/article_recommendation.jpg" width="400">  
  For every article, there will be the content of article on the left and 5 similar articles recommended on the righte. If you click the the title of a specific similar article, it will direct you to another page with the same structure.

- **Tweet_sentiment_analysis**
  Pulled tweets using the [tweepy](http://www.tweepy.org/) wrapper around the twitter API and performed sentiment analysis using the [vaderSentiment](https://github.com/cjhutto/vaderSentiment) library. Launched server that display tweets of a user and who he/she has been following. The gradient color of the tweets represent sentiment attitude(red for negative, green for positive).
  Here's two examples:   
    
  Tweets and who antlr_guy (my grad school professor) follows:  
  <img src="https://github.com/Jennylijingxian/Deep_learning_and_NLP/blob/master/images/ex1_antlr_guy.jpg" width="800">    
  <img src="https://github.com/Jennylijingxian/Deep_learning_and_NLP/blob/master/images/ex1_antlr_followedby.jpg" width="250">  
    
  Tweets and who Donald Trump follows:  
  <img src="https://github.com/Jennylijingxian/Deep_learning_and_NLP/blob/master/images/ex2_trump.jpg" width="800">  
  <img src="https://github.com/Jennylijingxian/Deep_learning_and_NLP/blob/master/images/ex3_trump_followedby.jpg" width="250">  
