import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# grab the top 1000, sort by title
imdb_url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"

# setting headers
headers = {"Accept-Language": "en-US, en;q=0.5"}

# save all values to the results objects coming back from the .get on IMDB URL
results = requests.get(imdb_url, headers=headers)

# parsing the results object to movie_soup using the html parser
movie_soup = BeautifulSoup(results.text, "html.parser")

# i want to extract these attributes (to a list) from the movie_soup
movie_name = []
movie_years = []
movie_runtime = []
imdb_ratings = []
metascores = []
number_votes = []
us_gross = []

movie_div = movie_soup.find_all('div', class_='lister-item mode-advanced')

for container in movie_div:

        # name
        name = container.h3.a.text
        movie_name.append(name)

        # year
        year = container.h3.find('span', class_='lister-item-year').text
        movie_years.append(year)

        # runtime
        runtime = container.p.find('span', class_='runtime').text if container.p.find('span', class_='runtime').text else '-'
        movie_runtime.append(runtime)

        # IMDB rating
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)

        # metascore
        m_score = container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-'
        metascores.append(m_score)

        # There are two NV containers, grab both of them as they hold both the votes and the grosses
        nv = container.find_all('span', attrs={'name': 'nv'})

        # filter nv for votes
        vote = nv[0].text
        number_votes.append(vote)

        # filter nv for gross
        grosses = nv[1].text if len(nv) > 1 else '-'
        us_gross.append(grosses)

# building the Pandas dataframe         
movies = pd.DataFrame({
'movie_name': movie_name,
'movie_year': movie_years,
'movie_runtime': movie_runtime,
'imdb_ratings': imdb_ratings,
'metascore': metascores,
'number_votes': number_votes,
'us_gross_millions': us_gross,
})

# cleaning up the data with Pandas
movies['movie_year'] = movies['movie_year'].str.extract('(\d+)').astype(int)
movies['movie_runtime'] = movies['movie_runtime'].str.extract('(\d+)').astype(int)
movies['metascore'] = movies['metascore'].astype(int)
movies['number_votes'] = movies['number_votes'].str.replace(',', '').astype(int)
movies['us_gross_millions'] = movies['us_gross_millions'].map(lambda x: x.lstrip('$').rstrip('M'))
movies['us_gross_millions'] = pd.to_numeric(movies['us_gross_millions'], errors='coerce')

# exporting our results to a pretty little .csv 
movies.to_csv('top_50_movies.csv')
