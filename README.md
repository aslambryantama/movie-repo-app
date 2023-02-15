# Movie Repository App (with Streamlit and Bigquery)

Open the App : [abry-movie.streamlit.app](https://abry-movie.streamlit.app/)

## Description

This project is a continuation of the previous project about Movie Analysis Dataset on [here](https://github.com/aslambryantama/movie-dataset-analysis), but this project aims to be more customs and more personal based on user that have certain specified criteria. User can defined their own top movies based on their preferences, because in the previous analysis project we only conclude our analysis more on general results.

So this project gives users more freedom to choose and determine their own favorite. cause everybody has their own unique preference about what they want to see.

## About the App

This app is a web-based application developed using __Python__ mainly with __Streamlit__ and __Pandas__ library. The app uses database from __BigQuery__ in Google Cloud to store it's dataset, and to interact with it we use __Google Cloud API__ and connect it to our app to access the database. The app itself is deployed with streamlit cloud service so it can be accessed by everyone on the internet.

**APP Interface :**
![App interface](/description/home.png "Display APP")

You can start using the app right away with fill the **Sidebar** on the left side of the app, or if you on mobile you have to expand the menu first to show the form. with that form you can fill many criteria such as Title, Genre, Year Release, and even Movie Budget. user also can configure about how many movies will be shown. if you done fill your criteria you can click the **Submit** button on the bottom of the sidebar. and your movie will show like this

![App interface](/description/menu.png "Display APP")

If it's not enough, there is an '**Advanced Search**' dropdown menu. just click it and another form will be expanded and shown many more criteria to fill such as actor, director, franchise, and even production studio.

![App interface](/description/advanced.png "Display APP")

> You can test our app [here](https://abry-movie.streamlit.app/)

## Dataset

* Source Data for this app is using free dataset from [here](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) and shoutout to [Rounak Banik](https://www.kaggle.com/rounakbanik) for providing this dataset on kaggle.

* The dataset consists of movies released on and up to July 2017 with approximately up to 45,000 movies. There are 16 attributes column for this dataset

## App Requirements

This app uses python 3.9.2 and Streamlit 1.15.2 as its core. For more detail, open requirements.txt or simply install :
````python
pip install -r requirements.txt 
pip3 install -r requirements.txt
````

---
This app is stil far from perfect, but i am happy with the result. in the future I plan to expand the dataset even larger so more movies can be displayed without having too much issue, and adding more features like recomendation, etc.
