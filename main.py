import requests, getpass, hashlib

def request():
	password = getpass.getpass("Enter password : ")
	if len(password) == 0:
		print("Blank password, Try again\n")
		request()
	user_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
	url = "https://api.pwnedpasswords.com/range/" + user_password[:5]
	# print(url)
	res = requests.get(url)
	if res.status_code != 200:
		print(f"Error response code {res.status_code}")
	elif res.status_code == 200:
		# print(f"Success {res.status_code}")
		hashes = (line.split(":") for line in res.text.splitlines())
		all_passwords = []
		for passwords, count in hashes:
			all_passwords.append(int(count))		
		if max(all_passwords) > 1000:
			print(f"This password is been hacked (approx) {max(all_passwords)} times\n")
			print(f"Try using a different password") 
		elif max(all_passwords) < 1000 :
			print(f"This password has been hacked less then {max(all_passwords)} times\n")
			print(f"You can use this")
		elif max(all_passwords) == 0:
			print(f"Excellent password, it has been {max(all_passwords)} times\n")		
request()