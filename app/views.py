from flask import Flask,  render_template, request, jsonify
from app import bot


app = Flask(__name__)




@app.route('/', methods = ["GET","POST"])
def result():

    if request.method == 'POST':
        question = request.json
        query = bot.Bot(question)
        
        
        return query.MediaWiki(), query.GooglMapFrame()

    else:
        return render_template('index.html')
if __name__ == "__main__":
    app.run()