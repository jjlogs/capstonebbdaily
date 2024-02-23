from google_play_scraper import app
import pandas as pd
import numpy as np
from google_play_scraper import Sort, reviews_all

bbdaily_reviews = reviews_all(
    'com.raincan.android.hybrid',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
)

df_bb = pd.DataFrame(np.array(bbdaily_reviews),columns=['review'])


df_bb = df_bb.join(pd.DataFrame(df_bb.pop('review').tolist()))

df_bb.to_csv("GooglePlayStoreReviews.csv")