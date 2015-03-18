from passlib.hash import pbkdf2_sha256
from pymongo import MongoClient
client = MongoClient()
db = client['Evoting']


# Users collection
name = ['Abhilash', 'Bhavyanth', 'Subash']
username = ['121', '122', '123']
rawPassword = ['121', '122', '123']
salted = b'=ruQ3.Xc,G/*i|D[+!+$Mo^gn|kM1m|X[QxDOX-=zptIZhzn,};?-(Djsl,&Fg<r' 
password = [pbkdf2_sha256.encrypt(x, rounds=8000, salt= salted) for x in rawPassword]
encrpytedBallotId = ''
region = ['4','5','6']


for i in range(3):

	voter = {"Name":name[i],"UserName":username[i],"Password":password[i],"EncryptedBallotId":encrpytedBallotId,"Region":region[i]}
	db.voters.insert(voter)

