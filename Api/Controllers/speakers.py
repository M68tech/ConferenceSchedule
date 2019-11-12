
#task1

#from flask import Flask
#from flask import jsonify

#app = Flask(__name__)

#@app.route('/speaker/<id>', methods=['GET'])
#def get_one_speaker(id):
 # return jsonify({'result' : 'anusha'})

#------------------------------------------------------------#

#task2:specific name

#from flask import Flask
#from flask import jsonify
#from flask import request

#app = Flask(__name__)
#@app.route('/speaker' , methods=['GET'])
#def get_all_room(user=""):
 #  user = request.args.get('user', user)
  # return jsonify({'results' : "Wow we did it"})

#--------------------------------------------------------#
#task3:getting data from mongodb
from flask import Flask
from flask import request

import pymongo
import urllib
import json

#client = pymongo.MongoClient('mongodb://Anusha:Anusha@1994@cluster0-shard-00-00-c33k7.mongodb.net:27017,cluster0-shard-00-01-c33k7.mongodb.net:27017,cluster0-shard-00-02-c33k7.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')

#mongo_uri = "mongodb://username:" + urllib.parse.quote("p@ssword") + "@127.0.0.1:27001/"

#db = client['task']
#collection = db['speaker']
#mongo_uri = "mongodb://username:" + urllib.quote("p@ssword") + "@127.0.0.1:27001/"
client = pymongo.MongoClient('localhost:27017')
db = client['task']
collection = db['speaker']
app = Flask(__name__)



@app.route('/')
def get():
    documents = collection.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)


if __name__ == '__main__':
    app.run(debug=True)