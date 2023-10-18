from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

data = []

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/api/data', methods=['POST'])
def add_data():
    new_item = request.form.get('new-data')
    data.append(new_item)
    return render_template('index.html', data=data)

@app.route('/api/data/delete', methods=['POST'])
def delete_data():
    index_to_delete = int(request.form.get('delete-index'))
    if 0 <= index_to_delete < len(data):
        del data[index_to_delete]
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()