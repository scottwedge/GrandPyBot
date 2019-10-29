from flask import Flask,  render_template, request, jsonify
from app import bot


app = Flask(__name__)




@app.route('/', methods = ["GET","POST"])
def mediaResult():

    if request.method == 'POST':
        question = request.json
        query = bot.Bot(question)
        mediaResponse =  query.MediaWiki()
        
        
        return jsonify(mediaResponse) 

    else:
        return render_template('index.html')


@app.route('/map', methods=["GET","POST"])
def mapGoogle():
    if request.method == 'POST':
        question = request.json
        query = bot.Bot(question)
        mapResponse =  query.GooglMaplink()
        
        
        return jsonify(mapResponse) 

    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run()