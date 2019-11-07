# import for flask app
from flask import Flask, request, jsonify
# import for db connection

from model import Model
# import for pkl from dump in ML_model_class
import pickle

# TODO: from ML_model import ML_model_class
# OR PKL File below


# Creating Flask APP
APP = Flask(__name__)


# database connect info to backend group webserver

### IDEA FLOW ###

# Query to show stats result of player

# Then pull from model to show similar players
@APP.route('/')
def index():
    welcome = '''<h1>Data Predictions for DS Build Week. Use the following endpoints:<h1> <br>
                /similarities --> get top 3 similar players'''
    return welcome


@APP.route('/similarities/<string:player>/')
def similar_players(player: str):
    similar = Model(player)
    top_three = similar.build_similars()

    return top_three.to_json(orient='index')


# Flask request for player name
# Page request should look: www.website.com/player_search?player
@APP.route('/player_search', methods=['GET'])
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


if __name__ == '__main__':
    APP.run(debug=True)

