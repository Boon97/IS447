from flask import Flask

app = Flask(__name__)

# @app.route('/')

@app.route('/home/users/<string:name>/<int:id>') # routing urls to show pages
def hello(name, id):
    return 'Hello ' + name + str(id)

@app.route('/onlyget', methods=['GET']) # this webpage only allows get requests
def get_req():
    return 'You can only get this webpage'


if __name__ == '__main__':
    app.run(debug=True)