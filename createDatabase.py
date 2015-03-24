from passlib.hash import pbkdf2_sha256
from pymongo import MongoClient
client = MongoClient()
db = client['Evoting']

db.voters.remove()
db.candidates.remove()
db.regions.remove()

# Users collection
name = ['Abhilash', 'Bhavyanth', 'Subash']
username = ['121', '122', '123']
rawPassword = ['121', '122', '123']
salted = b'=ruQ3.Xc,G/*i|D[+!+$Mo^gn|kM1m|X[QxDOX-=zptIZhzn,};?-(Djsl,&Fg<r' 
password = [pbkdf2_sha256.encrypt(x, rounds=8000, salt= salted) for x in rawPassword]
encrpytedBallotId = ''
region = ['0','0','6']

#----------------VOTERS COLLECTION------------------
for i in range(3):

	voter = {"Name":name[i],"UserName":username[i],"Password":password[i],"EncryptedBallotId":encrpytedBallotId,"Region":region[i]}
	db.voters.insert(voter)

# Candidates
ContestantName = ['Pranav', 'Utkarsh', 'Amriteya', 'Aditya', 'Aman', 'Bhavyanth', 'Abhilash','Sonam','Sudhanshu']
IDs = [1,2,3,4,5,6,7,8,9]
Description =['A Microsoft enthusiast. Part time Jedi. Full time chutiya. Loves Google and Xiaomi more than Microsoft but will never admit it.','He claims he is an android developer. LOL!','He loves to eat!He loves to eat!He loves to eat!He loves to eat!He loves to eat!','He is fictional!He is fictional!He is fictional!He is fictional!He is fictional!','He does frontend. He writes fake testimonials for people.','He is an azole!He is an azole!He is an azole!He is an azole!','He is the most awesomest person ever. He can do so many things. Girls die for him. Guys want to be him.','Fictional Hot girl who likes abhilash.Fictional Hot girl who likes abhilash.Fictional Hot girl who likes abhilash.Fictional Hot girl who likes abhilash.','Not real!Not real!Not real!Not real!Not real!Not real!']
Position = ['President', 'President', 'President', 'Vice President', 'Vice President', 'President', 'Secretary','Secretary','Vice President']
Region = [0,0,0,0,0,0,0,0,0]

#------------------CANDIDATES COLLECTION------------
for i in range(9):
	election = {"Name":ContestantName[i],"ID":IDs[i],"Position":Position[i],"Region":Region[i],"Description":Description[i]}
	db.candidates.insert(election)

#-------- REGIONS COLLECTION----------
region = {'RegionId':'0', 'Positions':['President','Vice President','Secretary']}
db.regions.insert(region)

#Ballot 

