#!/usr/bin/env python
# coding: utf-8

# import for flask app
from flask import Flask, request, jsonify
# import libraries
import pandas as pd
import numpy as np
# import for db
import sqlite3
# import for pkl from dump in ML_model_class
import pickle

# # from ML_model import ML_model_class
#
# Creating Flask APP
APP = Flask(__name__)
# Flask APP run if called
if __name__ == 'main':
    APP.run()
#
# # import data from data.world website
# nba = pd.read_csv('https://query.data.world/s/rfugrlxorfagiv2cxyac6rujtzz6fw')
#
# # create sqlite db
# conn = sqlite3.connect('nba_players.db')
#
# # create cursor to db
# curs = conn.cursor()
#
# # create table sql string for nba_players.db
# create_table = ("""CREATE TABLE players(
#             [Unnamed: 0] integer,  [Player] text, [All_NBA] integer, [All.Star] integer,
#             [Draft_Yr] integer, [Pk] integer,
#             [Team] text,[College] text,
#             [Yrs] integer, [Games] integer, [Minutes.Played] integer,
#             [PTS] integer, [TRB] integer, [AST] integer,
#             [FG_Percentage] real, [TP_Percentage] real, [FT_Percentage] real,
#             [Minutes.per.Game] real,
#             [Points.per.Game] real, [TRB.per.game] real, [Assits.per.Game] real,
#             [Win.Share] integer,
#             [WS_per_game] real, [BPM] real, [VORP] real, [Executive] text,
#             [Tenure] date, [Exec_ID] integer,
#             [Exec_draft_exp] integer, [attend_college] integer, [first_year] integer,
#             [second_year] integer,
#             [third_year] integer, [fourth_year] integer, [fifth_year] integer)"""
#             )
#
# # cursor creating table in db
# curs.execute(create_table)
#
# # closing create table cursor
# curs.close()
#
# # commit changes of creating table
# conn.commit()
#
# # create new cursor to insert to table
# curs2 = conn.cursor()
#
# # for loop to add data from df nba to table
# for player in range(len(nba)):
#   sequence = (tuple(nba.loc[player].values))
#   insert_player = """INSERT INTO players
#         VALUES """ + str(sequence) + ';'
#   curs2.execute(insert_player)
#
# # closing cursor and committing
# curs2.close()
# conn.commit()
#
# # query for table
# # open cursor
# curs3 = conn.cursor()
# curs3.execute('SELECT * FROM players;').fetchall()
# # test for working table
#
# # close cursor
# curs3.close()
#
# ### IDEA FLOW ###
#
# # Query to show stats result of player
#
# # Then pull from model to show similar players

# Flask request for player name
# Page request should look: www.website.com/player_search?player
@app.route('/player_search', methods = ['POST'])
def search_player():
    # create cursor for player search
    curs_player = conn.cursor()
    # get data
    player = request.args.get('player')
    # (a)send searched player info to webpage
    player_one = "SELECT * FROM player WHERE Player == '" + str(player) + "'"
    player_find = curs_player.execute(player_one).fetchone()
    # close curs_player
    curs_player.close()
    
    # TO DO: Pull class from model to predict other likely players
    # similar_nba = pickle.load(open('similar_model.pkl', 'rb'))
    # longevity_nba = pickle.load(open('longevity_model.pkl', 'rb'))
    # TO DO: sim_players = ML_model_class.predict(player)
    # predict_similar = similar_nba.predict(player)
    # predict_longevity = longevity_nba.predict(player)
    
    # List for predicted player stats
    predict_players = []
    
    # Loop for data search of predicted_players
    for single in sim_players:
        # create cursor for predicted_find
        curs_pred = conn.cursor()
        # query string for db
        pred_query = "SELECT * FROM players WHERE Player='" + str(sim_players[single]) + "'"
        # execute query
        finder = curs_pred.execute(pred_query)
        predict_players.append(finder)
        curs_pred.close()
    return jsonify(results=player_find), jsonify(results=predict_players)

