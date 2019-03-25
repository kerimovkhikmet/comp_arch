#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import *  # Flask, url_for, jsonify, abort, request, unicode

app = Flask(__name__)


def make_public_game(game):
    """
    Make from with id -> uri
    0 -> http://127.0.0.1:5000/lab1/api/v1.0/games/0
    param task:
    return:
    """

    new_game = {}
    for field in game:
        if field == "id":
            new_game["uri"] = url_for("get_game", game_id=game["id"], _external=True)  # noqa
        else:
            new_game[field] = game[field]
    return new_game


games = [
    {
        "id": 1,
        "teams": u"Real Madrid - Liverpool",
        "score": u"3 - 1",
        "city": u"Kiev",
        "date": "2018-26-05",
    },
    {
        "id": 2,
        "teams": u"Real Madrid - Juventus",
        "score": u"4 - 1",
        "city": u"Cardiff",
        "date": "2017-03-06",
    },
    {
        "id": 3,
        "teams": u"Real Madrid - Atletico Madrid",
        "score": u"1 - 1 (5 - 3)",
        "city": u"Milan",
        "date": "2016-28-05",
    },
    {
        "id": 4,
        "teams": u"Barcelona - Juventus",
        "score": u"3 - 1",
        "city": u"Berlin",
        "date": "2015-05-06",
    },
    {
        "id": 5,
        "teams": u"Real Madrid - Atletico Madrid",
        "score": u"4 - 1",
        "city": u"Lisbon",
        "date": "2014-24-05",
    },
]


@app.route("/lab1/api/v1.0/games", methods=["GET"])
def get_games():
    """
    This function return all games
    return: json with games
    """

    return jsonify({"games": list(map(make_public_game, games))})


@app.route("/lab1/api/v1.0/games/<int:game_id>", methods=["GET"])
def get_game(game_id):
    """
    This function return game by id
    First find a game make uri for id
    and return json
    param game_id: id
    return: json
    """

    game = filter(lambda t: t["id"] == game_id, games)
    if len(game) == 0:
        abort(404)
    return jsonify({"game": game[0]})


@app.route("/lab1/api/v1.0/games/", methods=["POST"])
def add_game():
    """
    This function add new game in db
    return: json with the game
    """

    if (request.json or "teams") not in request.json:
        abort(400)
    game = {
        "id": games[-1]["id"] + 1,
        "teams": request.json["teams"],
        "score": request.json.get("score", ""),
        "city": request.json.get("city", ""),
        "date": request.json.get("date", ""),
    }
    games.append(game)
    return (jsonify({"game": game}), 201)


@app.route("/lab1/api/v1.0/games/", methods=["PUT"])
def update_game(game_id):
    """
    Edit game by id use
    param game_id: id of element measurement
    return: json with the game which was edit
    """

    game = filter(lambda t: t["id"] == game_id, games)
    if len(game) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if "teams" in request.json and type(request.json["teams"]) != unicode:
        abort(400)
    if "score" in request.json and type(request.json["score"]) is not unicode:
        abort(400)
    if "city" in request.json and type(request.json["city"]) is not unicode:
        abort(400)
    if "date" in request.json and type(request.json["date"]) is not unicode:
        abort(400)
    game[0]["teams"] = request.json.get("teams", game[0]["teams"])
    game[0]["score"] = request.json.get("score", game[0]["score"])
    game[0]["city"] = request.json.get("city", game[0]["city"])
    game[0]["date"] = request.json.get("date", game[0]["date"])
    return jsonify({"game": game[0]})


@app.route("/lab1/api/v1.0/games/", methods=["DELETE"])
def delete_game(game_id):
    """
    Delete game by id
    param game_id: id
    return: bool
    """

    game = filter(lambda t: t["id"] == game_id, games)
    if len(game) == 0:
        abort(404)
    games.remove(game[0])
    return jsonify({"result": True})


if __name__ == "__main__":
    app.run(debug=True)
