#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request
import pandas as pd
# from ML_model import ML_model_class

# Creating Flask APP
APP = Flask(__name__)
# Flask APP run if called
if __name__ == 'main':
    APP.run()


# In[2]:


# import data from data.world website
nba = pd.read_csv('https://query.data.world/s/rfugrlxorfagiv2cxyac6rujtzz6fw')


# In[3]:


### IDEA FLOW ###

# Query to show stats result of player

# Then pull from model to show similar players


# In[ ]:


# Flask request for player name
# Page request should look: www.website.com/player_search?player
@app.route('/player_search')
def search_player():
    player = request.args.get('player')
    # (a)send searched player info to webpage
    player_one = nba.loc[nba['Player'] == player]
    
    # Pull class from model to predict other likely players
    # sim_players = ML_model_class.predict(player)
    
    # List for predicted player stats
    predict_players = []
    
    # Loop for data search of predicted_players
    for single in sim_players:
        finder = nba.loc[nba['Player'] == single]
        predict_players.append(finder)
    return player_one, predict_players

