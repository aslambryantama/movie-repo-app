import streamlit as st
import numpy as np
import pandas as pd
from IPython.display import HTML
from google.oauth2 import service_account
from google.cloud import bigquery
from google.cloud import bigquery_storage

with open("style/style.css") as style:
  st.markdown(f"<style>{style.read()}<style", unsafe_allow_html=True)

@st.experimental_singleton
def connection():
  credentials = service_account.Credentials.from_service_account_file('services/movie-repo.json')
  project_id = 'movie-app-376013'
  client = bigquery.Client(credentials= credentials,project=project_id)

  table_name = "movie-app-376013.movie_tmdb.all_movie"
  query_job = client.query(f"""
   SELECT *
   FROM {table_name}
   """)
  return query_job

@st.experimental_memo
def load_data():
  df = connection().result().to_arrow(create_bqstorage_client=True).to_pandas()
  df["release_date"] = pd.to_datetime(df["release_date"], dayfirst=True)
  df["movie_release"] = df["release_date"].dt.strftime('%d %B %Y')
  df["genres_list"] = df["genres"].str.split('|').tolist()

  df["belongs_to_collection"] = df["belongs_to_collection"].fillna("-")
  df["production_companies"] = df["production_companies"].fillna("-")

  df['poster_path'] = df['poster_path'].str.replace('100px','300px')
  df['genres'] = df['genres'].str.replace('|',', ')

  df = df.rename(columns={'revenue_musd': 'Revenue', 'budget_musd': 'Budget', 'release_date': 'Release Date', 'vote_average': 'Rating', 'popularity': 'Popularity'})
  return df

df = load_data()

pd.options.display.float_format = '{:,.1f}'.format

gens = ['Animation', 'Comedy', 'Family', 'Adventure', 'Fantasy', 'Romance',
       'Drama', 'Action', 'Crime', 'Thriller', 'Horror', 'History',
       'Science Fiction', 'Mystery', 'War', 'Foreign', 'Music',
       'Documentary', 'Western', 'TV Movie']

min_year = 1874
max_year = 2017
max_budget = int(df["Budget"].max())
years = [year for year in range(min_year, max_year+1)]

#st.dataframe(df)
with st.sidebar:
  with st.form("my_form"):
    st.header("🍿 Find your Movie")
    movie_titles = st.text_input("Movie Title :")
    genre = st.multiselect('Genres :', gens)
    a1, a2 = st.columns([1,1])
    with a1:
      year_min = st.selectbox("From", years, index=0)
    with a2:
      year_max = st.selectbox("To", years, index=143)
    tesa, tesb = st.slider(
      'Select Movie Budgets (In Millions)',
      0, max_budget, (0, max_budget), key="slids")
    nums = st.number_input('How Many Movies to Show', 5, 100)
    with st.expander('Advanced Search'):
      actors = st.text_input("Write the Actor's name")
      dirs = st.text_input("Write the Director's name")
      frans = st.text_input("Part Of Franchise?")
      stud = st.text_input("Studio who Produces the  Movie")
    sorts = st.radio('Sort Movies by :', ['Popularity', 'Release Date', 'Rating', 'Revenue', 'Budget'])
    
   # Every form must have a submit button.
    submitted = st.form_submit_button("🔍 Submit")
    #st.markdown("""---""")
    st.markdown("""<div style="height:1px;border:none;background-color:rgba(0, 0, 0, .3);" /> """, unsafe_allow_html=True)
    st.caption('Press "F5" to Refresh your search')
    
    if submitted:
      movie_titles = movie_titles.lower()
      dirs = dirs.lower()
      actors = actors.lower()
      frans = frans.lower()
      stud = stud.lower()

def gens(x):
  lst = list()
  if isinstance(x, list):
    for i in genre:
      if i in x :
        lst.append(True)
      else:
        lst.append(False)
  else:
    return False
  
  if False in lst:
    return False
  else:
    return True

df_best = df[df["genres_list"].apply(lambda x: gens(x)) & (df["cast"].str.lower().str.contains(actors)) & (df["title"].str.lower().str.contains(movie_titles)) & \
  (df["director"].str.lower().str.contains(dirs)) & \
    (df["production_companies"].str.lower().str.contains(stud)) & \
      (df["belongs_to_collection"].str.lower().str.contains(frans)) & \
        (df["Budget"] > tesa) & (df["Budget"] < tesb) & \
          (df['Release Date'].dt.year >= year_min) & (df['Release Date'].dt.year <= year_max)].sort_values(by = sorts, ascending = False).head(nums)
df_best.index = np.arange(1, len(df_best) + 1)

#if submitted == True:
    #st.write(HTML(df_best.to_html(escape=False)))

if submitted:
  n = 0
  for index, row in df_best.iterrows():
    n = n + 1
  st.subheader(f"{n} Movies Found 🎬")
  st.markdown("""<div style="height:1px;border:none;background-color:rgba(0, 0, 0, .2);" /> """, unsafe_allow_html=True)
  for index, row in df_best.iterrows():
    with st.container():
      col1, col2 = st.columns([1,2])
      with col1:
        st.write(HTML(row["poster_path"]))
      with col2:
        st.subheader(row['title'])
        st.caption(f"( {row['genres']} )")
        st.caption(f"{row['runtime']} Minutes, Release {row['movie_release']}")
        st.markdown("#")
        st.write(f"Director : **{row['director']}**")
        st.caption(f"In Collection With : {row['belongs_to_collection']}")
        st.write(f"Budget  : $ {round(row['Budget'],1)} Million")
        st.write(f"Revenue : $ {round(row['Revenue'],1)} Million")
        st.text(f"Rating : {row['Rating']}")
        st.progress(float(row["Rating"])/10)
  
  if n == 0:
    st.error("No Movies Found, Please Cross Check your Input")
  elif n < nums:
    st.warning("The List Ends Here, No More movies based on your search")
  else:
    st.success("Your Movies Found!, you can expand your list on the sidebar")

else:
  st.header('🎬 Movie Repository App')
  with open("description/descript.md") as dd:
    dd = dd.read()
    st.write(dd)
  st.subheader("Thank You! 💕")
  st.caption("by Aslam Bryantama")

