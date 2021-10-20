# this is a copyright claim, don't you dare to steal
from matrix_client.api import MatrixHttpApi
from matrix_client.client import MatrixClient
from matrix_client.room import Room

class Redirector:
	def __init__(self):
		self.BOTUSERNAME = "pmos_redirector_bot"
		self.BOTPASSWORD = "pmossamplepass"
		self.BOTSERVO = "matrix.org"
		self.RID = "!RnpiUpFIsfzZfHdHQf:matrix.org"
		self.realRID = "!obQcCWaLRAUgiGBvMg:postmarketos.org"
		self.MainClient = MatrixClient("https://"+self.BOTSERVO)
		self.token = self.MainClient.login_with_password(username=self.BOTUSERNAME, password=self.BOTPASSWORD)
		self.APIWrapper = MatrixHttpApi("https://"+self.BOTSERVO, token=self.token)
		self.target_room = Room(self.MainClient, self.RID)
		print("ready")
	def mainThread(self):
		self.MainClient.add_listener(self.callback_event, event_type="m.room.member")
		self.MainClient.start_listener_thread()
		while True:
			input()
	def callback_event(room, event):
		if event.get("content").get("membership") == "join":
			user_id = event.get("sender")
			d.target_room.send_html('This room is not an official postmarketOS room. Please join the <a href="https://matrix.to/#/#porting:postmarketos.org">#porting:postmarketos.org</a> room!')
			try:
				d.APIWrapper.invite_user(d.realRID, user_id)
			except:
				pass # user already joined the rooms
if __name__ == "__main__":
	d = Redirector()
	d.mainThread()
