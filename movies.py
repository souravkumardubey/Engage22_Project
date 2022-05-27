
import pandas as pd
import flask
import json
import difflib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[2]:



app = flask.Flask(__name__, template_folder='templates')


# In[10]:


df2 = pd.read_csv('tmdb.csv',low_memory = False)


count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df2['title'])

count2 = CountVectorizer(stop_words='english')
count_matrix2 = count2.fit_transform(df2['genres'])

cosine_sim2 = cosine_similarity(count_matrix2, count_matrix2)

indices = pd.Series(df2.index, index=df2['title'])
#indices = pd.Series(i.lower() for i in df2['title'])
#indices = indices.str.lower()
# print(indices)

def get_title(m_name) :

    all_titles = [df2['title'][i] for i in range(len(df2['title']))]
    m_name = m_name.lower()
    flag = 0
    
    if m_name not in all_titles:
        search_words = m_name.split()
        to_be_searched = m_name.lower()
        prev = 0
        
        for titles in all_titles :
            new_title = titles.replace('-','')
            new_title2 = new_title.replace(':','')
            to_search_in = new_title2.lower()
            movie_words = to_search_in.split()
            c = 0
            for i in search_words :
                if i in movie_words :
                    #print(i)
                    
                    c = c + 1
            if ( c == len(to_be_searched) ) :

                flag = 1
                m_name = titles
                print(titles)
                break
            if ( c > prev ) :
                prev = c
                flag = 1
                m_name = titles;
    print(m_name)
    return m_name , flag

def get_recommendations_on_title(title):
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    #print(cosine_sim)
    #print(indices[title])
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[0:11]
    movie_indices = [i[0] for i in sim_scores]
    ids = df2['id'].iloc[movie_indices]
    tit = df2['title'].iloc[movie_indices]
    dat = df2['release_date'].iloc[movie_indices]
    rating = df2['vote_average'].iloc[movie_indices]
    posters = df2['poster'].iloc[movie_indices]
    overview = df2['overview'].iloc[movie_indices]
    return_df = pd.DataFrame(columns=['ID','Posters','Title','Year','Rating','Overview'])
    return_df['ID'] = ids
    return_df['Title'] = tit
    return_df['Year'] = dat
    return_df['Rating'] = rating
    return_df['Posters'] = posters
    return_df['Overview'] = overview
    return return_df


def get_recommendations_on_genres(title):
    cosine_sim2 = cosine_similarity(count_matrix2, count_matrix2)
    #print(cosine_sim)
    #print(indices[title])
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim2[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[0:11]
    movie_indices = [i[0] for i in sim_scores]
    ids = df2['id'].iloc[movie_indices]
    tit = df2['title'].iloc[movie_indices]
    dat = df2['release_date'].iloc[movie_indices]
    rating = df2['vote_average'].iloc[movie_indices]
    posters = df2['poster'].iloc[movie_indices]
    overview = df2['overview'].iloc[movie_indices]
    return_df = pd.DataFrame(columns=['ID','Posters','Title','Year','Rating','Overview'])
    return_df['ID'] = ids
    return_df['Title'] = tit
    return_df['Year'] = dat
    return_df['Rating'] = rating
    return_df['Posters'] = posters
    return_df['Overview'] = overview
    return return_df


def get_results(result_final) :
    names = []
    dates = []
    vote = []
    recommended_movies = list()
    for i in range(len(result_final)):

        movies = dict()

        movies['id'] = result_final.iloc[i][0]
        movies['poster'] = result_final.iloc[i][1]
        movies['movie_name'] = result_final.iloc[i][2]
        movies['year'] = result_final.iloc[i][3]
        movies['rating'] = result_final.iloc[i][4]
        movies['overview'] = result_final.iloc[i][5]
        recommended_movies.append(movies)

        names.append(result_final.iloc[i][0])
        dates.append(result_final.iloc[i][1])
        vote.append(result_final.iloc[i][2])
        
    return recommended_movies





