import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.websocket
import tornado.httpclient
from tornado import gen
import os.path
import json
import requests
import random
import tornado.escape
#---------------------------------------------------------------------------

from tornado.options import define, options, parse_command_line
define('port',default=8888,type=int)

#---------------------------------------------------------------------------

from pymongo import MongoClient
client = MongoClient()
db = client['Evoting']


#-------------------------------------------------------

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/")
            return

class LoginHandler(BaseHandler):
    def get(self):
        self.redirect('/')

    def post(self):
        self.db = db
        username = tornado.escape.xhtml_escape(self.get_argument("u"))
        password = tornado.escape.xhtml_escape(self.get_argument("p"))
        
        userCollectionFromDb = self.db.voters.find_one({"UserName":username})

        if userCollectionFromDb:

            if password == userCollectionFromDb['Password']:

                print(userCollectionFromDb['Name'])

                self.set_secure_cookie("user", username)
                self.render('index2.html')
            else:

                self.redirect('/')
        else:
            self.redirect('/')



        
            

class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect('/')

class WSHandler(tornado.websocket.WebSocketHandler):
     
    def open(self):
        print("socket opened server side")
            
    def on_message(self, message):
        pass
        
        # messageFromClient = json.loads(message)
        # messageType = str(messageFromClient['messageType'])
        # messageData = str(messageFromClient['messageData'])
        #         dataDict = {'messageType':'serverVerifiedLoginDetails'}
            
        #         messageToClient = json.dumps(dataDict)
            
        #         self.write_message(messageToClient)
        #         self.set_secret_cookie


            
        
    def on_close(self):
        print("Socket closed server side")
        
handlers = [
    (r'/',IndexHandler),
    (r'/ws',WSHandler),
    (r'/home',LoginHandler),
    (r'/logout',LogoutHandler),
]

#---------------------------------------------------------------------------

if __name__ == "__main__":
    parse_command_line()
    # template path should be given here only unlike handlers
    app = tornado.web.Application(handlers, template_path=os.path.join(os.path.dirname(__file__), "templates"),
                                  static_path=os.path.join(os.path.dirname(__file__), "static"), cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=", debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
