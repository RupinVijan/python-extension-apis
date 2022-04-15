from flask import Flask,jsonify,request
from textblob import TextBlob


app = Flask(__name__)

@app.route("/spellcheck" ,methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        words=request.json["word"]
        y=TextBlob(words)
        x=str(y.correct())
        jsonData = {
            "Word" : x
        }
        return jsonify(jsonData)




if __name__=="__main__":
    app.run(debug=True)