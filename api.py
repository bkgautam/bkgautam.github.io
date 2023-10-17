from flask import Flask, request, jsonify

app = Flask(__name__)

data = [12,13,14]

@app.route('/api/data' , methods=['GET'])
def get_data():
  return jsonify(data)

@app.route('/api/data', methods=['POST'])
def add_data():
  new_item=  request.get_json()
  data.append(new_item)
  return jsonify(new_item), 201

@app.route('/api/data/<int:index>', methods= ['DELETE'])
def delete_data(index):
  if 0<= index <len(data):
    deleted_item = data.pop(index)
    return jsonify(deleted_item)
  else:
    return "Index out of range", 200
  
if __name__ == '__main__':
  app.run()

