
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
#from flask import Flask
#from pymongo import MongoClient
#import json

#client = MongoClient('mongodb+srv://Anusha:Anujesus@cluster0-c33k7.mongodb.net/task?retryWrites=true&w=majority')
#db = client.get_database('task')
#collection = db['speaker']
#app = Flask(__name__)

#@app.route('/speaker')
#def get():
 #   documents = collection.find()
  #  response = []
   # for document in documents:
    #    document['_id'] = str(document['_id'])
     #   response.append(document)
   # return json.dumps(response)


#-------------------------------------#
#----task4:retreiving data from relational database:mysql------#

from flask import Flask
from flask import g
from flask import Response
import json
import MySQLdb

app = Flask(__name__)

@app.before_request
def db_connect():
  g.conn = MySQLdb.connect(host='localhost',
                              user='root',
                              passwd='Anujesus@1994',
                              db='mydb')
  g.cursor = g.conn.cursor()

@app.after_request
def db_disconnect(response):
  g.cursor.close()
  g.conn.close()
  return response

def query_db(query, args=(), one=False):
  g.cursor.execute(query, args)
  rv = [dict((g.cursor.description[idx][0], value)
  for idx, value in enumerate(row)) for row in g.cursor.fetchall()]
  return (rv[0] if rv else None) if one else rv

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/names", methods=['GET'])
def names():
  result = query_db("SELECT name,age FROM login")
  data = json.dumps(result)
  resp = Response(data, status=200, mimetype='application/json')
  return resp







if __name__ == '__main__':
    app.run(debug=True)