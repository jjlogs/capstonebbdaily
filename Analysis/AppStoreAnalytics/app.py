import pandas as pd
import numpy as np
import json
from app_store_scraper import AppStore

bbdaily = AppStore(country='in', app_name='bbdaily', app_id = '1148331468')

bbdaily.review(how_many=17200)

bbdaily_df = pd.DataFrame(np.array(bbdaily.reviews),columns=['review'])
bbdaily_reviews_df = bbdaily_df.join(pd.DataFrame(bbdaily_df.pop('review').tolist()))

bbdaily_reviews_df.to_csv("AppStoreReviews.csv")
