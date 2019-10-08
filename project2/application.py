from flask import Flask
from flask_socketio import SocketIO, emit
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
socketio = SocketIO(app)

# list of all future channels
channelList = []

# returns home page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# change display name page
@app.route("/cdn", methods=["GET"])
def cdn():
    return render_template("cdn.html")

# access point to all channels, redirected here if original username already picked
@app.route("/channels", methods=["GET"])
def channels():
    global channelList
    return render_template("channels.html", channels=channelList)

# create a new chat. Redirected here straight from picking original display name
@app.route("/cnc", methods=["GET", "POST"])
def cnc():
    global channelList
    if request.method == "GET":
        return render_template("cnc.html")
    else:
        chatName = request.form.get("chatname")
        # checks to make sure channel with same name doesn't exist
        for i in range(len(channelList)):
            if channelList[i] == chatName:
                # returns error if conflict
                return render_template("error.html", message = "that chatname is already taken")
        # appends chatname to channel list
        channelList.append(chatName)
        return redirect("/chat/" + chatName)

# route to specific channel
@app.route("/chat/<chatName>", methods=["GET"])
def chat(chatName):
    return render_template("chat.html", chatName=chatName)

# about page
@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

# socketio function 
@socketio.on("submit chat")
def chat(data):
    chat = data["chat"]
    user = data["user"]
    emit("chats", {"chat":chat, "user":user}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
