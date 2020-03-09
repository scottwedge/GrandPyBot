from flask import Flask, render_template, request, jsonify
from app import bot


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def mediaResult():
    """
    Mediawiki Part
    This view, is made to recieve data from the front end logic,
    traite it with the methods in backend's logic with a final 
    tamplates...
    """
    if request.method == "POST":
        question = request.json
        query = bot.Bot(question)
        mediaResponse = query.media_Wiki_Resp()

        return jsonify(mediaResponse)

    else:
        return render_template("index.html")


@app.route("/map", methods=["GET", "POST"])
def mapGoogle():
    """
    googlemap Part
    This view, is made to recieve data from the front end logic,
    traite it with the methods in backend's logic with a final 
    tamplates containing the map...
    """
    if request.method == "POST":  # cheking request type
        question = request.json  # recieve the question from the form in the FE
        query = bot.Bot(question)  # sending the question to the back end
        mapResponse = query.GooglMaplink()
        return jsonify(mapResponse)  # jesonify the response from the server

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
