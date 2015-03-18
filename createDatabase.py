from pymongo import MongoClient
client = MongoClient()
db = client['Evoting']

db.voters.remove()

# Users collection
name = ['Abhilash', 'Bhavyanth', 'Subash']
username = ['121', '122', '123']
password = ['121', '122', '123']
encrpytedBallotId = ''
region = ['4','5','6']


for i in range(3):

	voter = {"Name":name[i],"UserName":username[i],"Password":password[i],"EncryptedBallotId":encrpytedBallotId,"Region":region[i]}
	db.voters.insert(voter)