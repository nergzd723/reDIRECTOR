# this is a copyright claim, don't you dare to steal
from matrix_client.api import MatrixHttpApi
from matrix_client.client import MatrixClient
from matrix_client.room import Room


class Director:
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
	def callback_event(room, event):
		print(event)
		if event.get("content").get("membership") == "join":
			print("somewho joined")
			user_id = event.get("sender")
			print(user_id)
			d.target_room.send_notice("This room is not official postmarketOS room. Please join the #porting:postmarketos.org room")
			d.APIWrapper.invite_user(d.realRID, user_id)
	def mainThread(self):
		Users = self.target_room.get_joined_members()
		self.MainClient.add_listener(self.callback_event, event_type="m.room.member")
		self.MainClient.start_listener_thread()
		for user in Users:
			print(user.get_display_name())
		while True:
			input()
if __name__ == "__main__":
	d = Director()
	d.mainThread()