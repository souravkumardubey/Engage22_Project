
# <p align="center"> Movie Recommendation Web App </p>
> Confused what to watch after finishing a movie? Do not worry Movie&Chill is here.

> [Live project](movieandchill.herokuapp.com)

### Table of Contents 📙

- About the challenge
- Features
- Requirements to run on local host
- Future Work

## Microsoft Engage 2022

- The challenge
  - Demonstrate through your app the different kinds of algorithms that a web-streaming app (like Netflix) or an audio-streaming app (like Spotify) may use for their Recommendation Engine.
  - Focus on any algorithm that you choose to highlight, for example:
    - Demonstrate what kind of role would a sorting algorithm play in a Recommendation Engine?
    - What is the most efficient sorting algorithm to use in this scenario, and why?
    - Demonstrate what kind of role would a search algorithm play in a Recommendation Engine? Which search algorithm does your app use, and why?

## Featues

- #### Homepage
  - A very simple and clean homepage consisting of navbar , a search bar.
  - Top rated movies recommendation
  - Top trending movies recommendation

- #### Search results page
    - As the user types something relavent in the search bar and click enter , he is redirected to the search results page where he gets the results for his entered movie title.

- #### Movie info page
    -  Clicking on the poster of a movie , the user is redirected to a page where he will be given a brief about that particular movie, such as the release date, its rating, and overview of the movie.
    -  Along wiht the movie details, the user is also recommended with some movies which he might also like to watch.
- #### Responsiveness
  - The website is completely responsive on all the devices such as on phone, tab, and desktop.

## Implementation Details
  - ##### Tech Stacks Used
    - HTML
    - CSS
    - Python
    - Flask
    - For processing the data from the tmdb.csv file , Machine Learning library SkLearn has been implemented. It is completely based on <span style = "font-weight: bold;">Item Based Collaborative Filtering Algorithm</span>.
  - ##### Clone Repo and run on your local host
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

## 
