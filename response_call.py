from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
import voicebot as vb
app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()
    resp.say("Salam Aleykoum nanga def ?")
    resp.record(max_length="10", action="/handle-recording")
    vb.demo()
    
    return str(resp)

@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    resp = VoiceResponse()
    resp.say("Merci pour votre appel, à bientôt !")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)