import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
import category_encoders as ce
from scipy.spatial.distance import cdist
from sklearn.externals import joblib

from db_helper import DbHelper

cols = ['column_a', 'player', 'all_nba', 'all_star', 'draft_yr', 'pk', 'team', 'college', 'yrs', 'games',
        'minutes_played', 'pts', 'trb', 'ast', 'fg_percentage', 'tp_percentage', 'ft_percentage',
        'minutes_per_game', 'points_per_game', 'trb_per_game', 'assits_per_game', 'win_share', 'ws_per_game', 'bpm',
        'vorp', 'executive', 'tenure', 'exec_id', 'exec_draft_exp', 'attend_college', 'first_year', 'second_year',
        'third_year', 'fourth_year', 'fifth_year']

target = 'player'
features = ['all_nba', 'all_star', 'draft_yr', 'pk', 'team',
            'college', 'yrs', 'games', 'minutes_played', 'pts', 'trb', 'ast',
            'fg_percentage', 'tp_percentage', 'ft_percentage', 'minutes_per_game',
            'points_per_game', 'trb_per_game', 'assits_per_game', 'win_share',
            'ws_per_game', 'bpm', 'vorp', 'exec_id',
            'exec_draft_exp', 'attend_college', 'first_year', 'second_year',
            'third_year', 'fourth_year', 'fifth_year', 'retire_yr']


class Model():
    def __init__(self, name):
        db = DbHelper()
        self.all_players = db.query_all_players()
        self.player = db.query_player(name)

        return

    def wrangle_df(self):
        df = pd.DataFrame(self.all_players, columns=cols)
        player_df = pd.DataFrame(self.player).T
        player_df.columns = cols
        df['retire_yr'] = df['draft_yr'] + df['yrs']
        player_df['retire_yr'] = player_df['draft_yr'] + player_df['yrs']
        return df, player_df

    def build_similars(self):
        df, player_df = self.wrangle_df()
        encode_pipeline = Pipeline(steps=[('ord', ce.OrdinalEncoder(cols=['team', 'college'])),
                                          ('hot', ce.OneHotEncoder(
                                              cols=['attend_college', 'first_year', 'second_year', 'third_year',
                                                    'fourth_year', 'fifth_year']))])

        # encoding
        X = encode_pipeline['ord'].fit_transform(df[features])
        x_player = encode_pipeline['ord'].transform(player_df[features])
        X = encode_pipeline['hot'].fit_transform(X)
        x_player = encode_pipeline['hot'].transform(x_player)
        ary = cdist(x_player.values.reshape(1, -1), X.values, metric='euclidean')
        euclid = pd.DataFrame(ary).T.sort_values(by=0)
        top_three = euclid.iloc[1:4]
        top_three = df.iloc[top_three.index]
        return top_three

    def longevity(self):
        filename = 'model_longevity.sav'
        loaded_model = joblib.load(filename)
        longevity = loaded_model.predict(x_player)
        return (longevity)


if __name__ == '__main__':
    model = Model('Carl Ervin')

    print(model.build_similars())
    print(model.longevity())