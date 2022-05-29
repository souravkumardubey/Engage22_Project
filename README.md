
# <p align="center"> Movie Recommendation Web App </p>
> Confused what to watch after finishing a movie? Do not worry Movie&Chill is here.

> Live project https://movieandchill.herokuapp.com 
> Dataset used https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
> Github Repo https://github.com/souravkumardubey/Engage22_Project
> [Project Demo](https://youtu.be/v6cmuAiuaNg)

### TABLE OF CONTENTS 📙

- PROJECT SETUP ON YOUR SYSTEM
- ABOUT THE CHALLENGE
- FEATURES
- WORKING
- FUTURE WORK

## HOSTING THE APP ON LOCALHOST
  - Clone or download this repository in your local machine
    <br>
    > git clone url_of_the_repo
  - Select your python interpreter, if there isn't one, then install python and then select interpreter.
  - Install libraries from requirements.txt using
    <br>
    > pip install -r requirements.txt
  - Open terminal or command prompt and type
    <br>
    > python main.py
  - Go to browser and type
    <br>
    > http://127.0.0.1:5000

## MICROSOFT ENGAGE 2022

- The challenge
  - Demonstrate through your app the different kinds of algorithms that a web-streaming app (like Netflix) or an audio-streaming app (like Spotify) may use for their Recommendation Engine.
  - Focus on any algorithm that you choose to highlight, for example:
    - Demonstrate what kind of role would a sorting algorithm play in a Recommendation Engine?
    - What is the most efficient sorting algorithm to use in this scenario, and why?
    - Demonstrate what kind of role would a search algorithm play in a Recommendation Engine? Which search algorithm does your app use, and why?

## FEATURES

- #### HOMEPAGE
  - A very simple and clean homepage consisting of navbar , a search bar.
  - Top rated movies recommendation
  - Top trending movies recommendation

- #### SEARCH RESULTS PAGE
    - As the user types something relavent in the search bar and click enter , he is redirected to the search results page where he gets the results for his entered movie title.

- #### MOVIE INFO PAGE
    -  Clicking on the poster of a movie , the user is redirected to a page where he will be given a brief about that particular movie, such as the release date, its rating, and overview of the movie.
    -  Along wiht the movie details, the user is also recommended with some movies which he might also like to watch.

- #### IMPLEMENTATION
    - ##### TECH STACKS USED
      - HTML
      - CSS
      - Python
      - Flask
      - For processing the data from the tmdb.csv file , Machine Learning library SkLearn has been implemented. It is completely based on <span style = "font-weight: bold;">Item Based Collaborative Filtering Algorithm</span>.

## WORKING
The basic function of a recommendation engine is to recommend items to the user based on the data available. For this project I have used a Machine learning library [scikit-learn](https://scikit-learn.org/stable/).
The purpose of the library is identifying which category an object ( movie searched by the user ) belongs to and predicting a continuous-valued attribute associated with an object.

- #### HOMEPAGE
  Based on the trends and rating of movie we recommend the users with 20 movies in each section, so that he/she gets a basic idea what this website is going to provide them with.
- #### PEROSNALISED RECOMMENDATIONS
  When the user searches for a movie title by entering it into the search bar, then they are redirected to a page where based of the title, recommendations have been provided. A user can give any input and if the input is valid ( i.e the title is perfect or at least in the title a single word is correct ) they get their desired results.
  - ##### GETTING RELAVENT TITLE
    - To find the relavent title out of all the movies user wants to find , I have used a basic algorithm knows as Longest Common Subsequence. By this the algorithm finds a relavent title and recommends movies based on the similar title.
  - ##### THE RECOMMENDATIONS
    I've used Item Based Collaborative Filtering algorithm. Item collaborative filtering is one kind of recommendation method which looks for similar items based on the items users have already liked or positively interacted with. 
    - To get recommendations, I used a Scikit learn function called cosine_similarity() and CountVectorizer().
    - cosine_similarity(X , Y) function computes cosine similarity between samples in X and Y i.e computes similarity as the normalized dot product of X and Y.
      > K(X, Y) = <X, Y> / (||X||*||Y||)
    - CountVectorizer() function converts a collection of text documents to a matrix of token counts. This implementation produces a sparse representation of the counts using scipy.sparse.csr_matrix
    
    After finding the count vectorizer of a dataset, we train the data using fit_transform() function which is used on the training data so that we can scale the training data and also learn the scaling parameters.
    
    When the user searches for a movie , then the title and the genre of the movie is used in the parameters of the above two functions. Then the fit_transform() results are used to build the cosine_similarity results , i.e this functions provides the finals recommendations.

## FUTURE WORK
  - Imporve the accuracy of the algorithm.
  - Also integrate user login auth so that user can feel much more personalised.
  - Implementing video streaming feature i.e to provide the trailer of a movie to the user.
