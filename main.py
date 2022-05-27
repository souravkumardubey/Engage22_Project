from crypt import methods
from distutils.log import debug
from pydoc import render_doc
import string
from flask import Flask , render_template , request , redirect, url_for
import movies
import csv  
import pandas as pd
import string
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home() :
    csvData = pd.read_csv("tmdb.csv",low_memory=False)
    csvData.sort_values(["vote_average"], 
                    axis=0,
                    ascending=[False], 
                    inplace=True)

    top_10 = list()
    i = 0
    for i in range(20) :

        top_10.append(csvData.iloc[i])

    csvData.sort_values(["popularity"], 
                    axis=0,
                    ascending=[False], 
                    inplace=True)

    trending_results = list()
    i = 0
    for i in range(20) :
        
        trending_results.append(csvData.iloc[i])

    return render_template("home.html",top_10 = top_10 , trending_results = trending_results)

@app.route("/search",methods=['POST','GET'])
def search() :
    if ( request.method == 'POST' ) :
        m_name = request.form["m_name"]
        final_title , result = movies.get_title(m_name)
        if ( result ) :
            recommendations = movies.get_recommendations_on_title(final_title)
            movies_results = movies.get_results(recommendations)
            return render_template("search.html", movies_results = movies_results)
        else :
            return render_template("error.html");

@app.route("/about",methods=['GET'])
def about() :
    return render_template("about.html");


@app.route('/movies/<int:m_id>',methods=['GET']) 
def movie(m_id) :
    result = list()
    print(m_id)
    print("hellow")
    input = "tmdb.csv"
    print(type(m_id))

    with open(input) as file_obj :
        render_obj = csv.reader(file_obj)
        for row in render_obj :

            if ( (row[0]) == str(m_id) ) :
                movie = dict()
                movie['rating'] = row[19]
                movie['poster'] = row[3]
                movie['title'] = row[18]
                movie['year'] = row[12]
                movie['overview'] = row[8]

                result.append(movie)
                final_title = movie['title']
                recommendations = movies.get_recommendations_on_genres(final_title)
                movies_results = movies.get_results(recommendations)
                return render_template('movie.html',result=result , movies_results = movies_results)
       
    

if __name__ == "__main__" :
    app.run(debug=True)
# 
