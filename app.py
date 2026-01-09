import re
from flask import Flask,render_template,request,jsonify, abort
from gpiozero import PWMLED , LED

import firebase_admin
from firebase_admin import credentials, auth

from gpiozero import Device
from gpiozero.pins.pigpio import PiGPIOFactory

Device.pin_factory = PiGPIOFactory()

app = Flask(__name__)

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

ADMIN_EMAILS = {
	"mohammad.muaj009@gmail.com",
	"admin@email.com"
}

def verify_firebase_token(require_admin=True):
	auth_header = request.headers.get("Authorization")
	if not auth_header:
		abort(401, "Missing Authorization header")
	
	try:
		token = auth_header.split(" ")[1]
		decoded = auth.verify_id_token(token)
	except Exception:
		abort(401)
	email = decoded.get("email")
	
	if require_admin and email not in ADMIN_EMAILS:
		abort(403,"Access Denied")
	return decoded

def split_commands(text):
	return re.split(r'\band\b|\bthen\b|,',text.lower())

R = PWMLED(17)
G = PWMLED(27)
B = PWMLED(22)

fan_power = False
last_speed = 0

def apply_speed_to_rgb(speed):
	x = speed/100.0
	if x <= .5:
		ratio = x/.5
		r = 0
		g = ratio
		b = 1 - ratio
	else:
		ratio = (x-.5)/.5
		r = ratio
		g = 1 - ratio
		b = 0
	R.value = r
	G.value = g
	B.value = b
	
	return r,g,b

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/fan/power/<action>")
def fan_power_control(action):
	verify_firebase_token(require_admin=True)
	global fan_power, last_speed
	
	if action == "on":
		fan_power = True
		apply_speed_to_rgb(last_speed)
		return f"Fan ON (speed {last_speed}%)"

	elif action == "off":
		fan_power = False
		R.value = G.value = B.value = 0
		return "Fan OFF"
	return "Invalid action"


@app.route("/fan/speed/<value>")
def fan_speed(value):
	verify_firebase_token(require_admin=True)
	global fan_power, last_speed
	speed = int(value)
	last_speed = speed
	if not fan_power:
		return "Fan is OFF (speed saved but not active)"
	
	r, g, b = apply_speed_to_rgb(speed)
	return f"Fan speed set to {speed}%, RGB=({r:.2f}, {g:.2f} , {b:.2f})"

light = LED(5)
@app.route("/light/<action>")
def light_control(action):
	verify_firebase_token(require_admin=True)
	if action == "on":
		light.on()
		return "Light ON"
	elif action == "off":
		light.off()
		return "Light OFF"
	return "Invalid action"

@app.route("/chat",methods = ["POST"])
def chat():
	verify_firebase_token(require_admin=True)
	global fan_power,last_speed
	msg = request.json["message"].lower()
	commands = split_commands(msg)
	reply_list = []
	for cmd in commands:
		cmd = cmd.strip()
	
		if "light" in cmd:
		
		#light_phrase = msg[msg.index("light") - 15 : msg.index("light") + 15]		
		
			if "on" in cmd:
				light.on()
				reply_list.append("Light Turned On")
			elif "off" in cmd:
				light.off()
				reply_list.append("Light Turned OFF")



		if "fan" in cmd:
		
			#fan_phrase = msg[msg.index("fan") - 15 : msg.index("fan") + 30]

			if "on" in cmd:
				fan_power =True
				apply_speed_to_rgb(last_speed)
				reply_list.append(f"Fan Turned ON with speed {last_speed}%")
			elif "off" in cmd:
				fan_power = False
				R.value =B.value = G.value = 0
				reply_list.append("Fan Turned OFF")

	
			nums = re.findall(r"\d+",msg)
			if  nums:
				last_speed = int(nums[0])
				if fan_power:
					apply_speed_to_rgb(last_speed)
					reply_list.append(f"Fan Speed set to {last_speed}%")
				else:
					reply_list.append(f"Fan is OFF, speed {last_speed}% saved")

	if not reply_list:
		reply_list.append("I did not understand")
	
	return jsonify({"reply": " | ".join(reply_list)})


if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000,use_reloader=False)











































