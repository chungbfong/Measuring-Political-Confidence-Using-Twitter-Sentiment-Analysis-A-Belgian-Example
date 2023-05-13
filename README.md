# Measuring-Political-Confidence-Using-Twitter-Sentiment-Analysis-A-Belgian-Example

Welcome to the Github repository accompanying the "Measuring Political Confidence using Twitter Sentiment Analysis: A Belgian Example" paper.
Here you will be able to find both the code used to retrieve and analyze the tweet data we retrieved, as well as the keywords and removed account lists that
could be used to base a newer keyword list on.
## Keyword list + Removed Accounts
The keyword lists consist of multiple types of keywords, namely the keyword lists containing the names of government ministers (which are saved in separate folders by year) and the keywords containing the words generally used to tweet about politics. Each of these keyword lists have versions corresponding to the Flemish and federal (or Belgian) government level. There is also an extra keyword list file that combines the generally used words for both the federal and Flemish levels which is useful to retrieve all words that have to do with the Belgian governments. These keyword files are saved as .txt files.

The removed accounts are listed by category, namely the government institution accounts and the media institution accounts. They are saved as Excel files.

## Prerequisites

This is an example of how to list things you need to use the software and how to install them. 
* pip
  ```sh
  pip install -r requirements.txt
  ```

<!-- USAGE EXAMPLES -->
## Usage

The repo contains multiple python scripts which are the core of this paper. 

- smape.py
  - conducts Symmetric Mean Absolute Percentage Error
- use_autorank.py
  - conducts autorank 
- weighting.py
  - introduces weighting method as shown in the paper
- main.py
  - contains the main crawler and the sentiment model

## Contact

Marco Chi Chung Fong - marcochichung.fong@student.kuleuven.be
