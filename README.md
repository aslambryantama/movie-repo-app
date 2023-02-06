# Movie Repository App

Open the App : [abry-movie.streamlit.app](https://abry-movie.streamlit.app/)

## Project Description

This project is kelanjutan from previous project about Movie Analysis Dataset, but this project aim to be more personal and customs based on user criteria that want to know their own top movie based on their preference, because in previous analysis project we only conclude our analysis more on general result.

So this project give user more freedom to choose and determine their own favourite. cause everybody has their own unique preference about what they want to see.

This app is a web-based application developed using Python mainly with streamlit and pandas library. The app use database from BigQuery in Google Cloud to store it's dataset, and to interact we use Google Cloud API to connect the app and the database. The app itself is deployed with streamlit cloud service so it can be used for everybody who open the link.

**APP Interface :**
![App interface](/description/home.png "Display APP")

You can start using the app right away with fill the **Sidebar** on the left side of the app, or if you on mobile you have to expand the menu first to show the form. with that form you can fill many criteria such as Title, Genre, Year Release, and even Movie Budget. user also can configure about how many movies will be shown. if you done fill your criteria you can click the **Submit** button on the bottom of the sidebar. and your movie will show like this
![App interface](/description/menu.png "Display APP")

If it's not enough, there is an **Advanced Search** dropdown. just click and there will be shown many more criteria to fill such as actor, director, franchise, and production studio.
![App interface](/description/advanced.png "Display APP")

## Dataset

>Source Data for this app is using free dataset from [here](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) and shoutout to [Rounak Banik](https://www.kaggle.com/rounakbanik) for providing this dataset pm kaggle.

>The dataset consists of movies released on and up to July 2017 with approximately up to 45,000 movies. There are 16 attributes column for this dataset

## App Requirements

This app uses python 3.9.2 and Streamlit 1.15.2, for more detail open requirements.txt and for instalation :
````python
pip install -r requirements.txt 
pip3 install -r requirements.txt
````

---
This app is stil far from perfect, but i am happy with the result. in the future I plan to expand the dataset even larger so more movies can be displayed without having too much issue, and adding more features like recomendation, etc.
