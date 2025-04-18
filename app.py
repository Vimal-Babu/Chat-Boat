from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot("ChatterBot")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods = ["POST"])
def get_response():
    user_input = request.form["user_input"]
    response = chatbot.get_response(user_input)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)