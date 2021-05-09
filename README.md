# imdb-movie-scraper

- Some weekend fun with [Python](https://www.python.org/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [Pandas](https://pandas.pydata.org/), and [NumPy](https://numpy.org/)
- **Short Description:** Web Scraper calling out to [iMDB](imdb.com/search/title/?groups=top_1000&ref_=adv_prv) grabbing all `HTML` elements for the Top-50 movies of all time and saving the results to a `.csv` file.
 
 1. Call out to [iMDB](imdb.com/search/title/?groups=top_1000&ref_=adv_prv).
 2. Save the `HTML` elements to a `results` object.
 3. Create a `movie_soup` [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) object that stores all the results as text.
 4. Create lists to extract all `HTML` attributes like name, years, runtime, ratings, metascores, number of cotes, and gross budget.
 5. Create a `movie_div` object to find all `div` objects in `movie_soup`.
 6. Loop through each object in the `movie_div`.
 7. Add each result from each attribute for each list.
 8. Build a movies `DataFrame`.
 9. Store all attributes into the movies `DataFrame`.
 10. Use Pandas `str.extract` to remove all String characters and save the value as type `int`.
 11. Export the results to a pretty little `top_50_movies.csv` file
