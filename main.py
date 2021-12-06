from flask import Flask, request, abort, send_file, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

listFilename = ["test.jpg"]
# Cписок названий изображений, test.jpg стоит по умолчанию, 
# чтоб не сломать метод show при запуске

@app.route('/')
def index():
    # Вернет listFilename в отпаршенном json
    return jsonify(listFilename)

# Позволяет загрузить фотографию от пользователя на сервер.
# Создается запрос с form-data, где по ключу "the_file" передаётся файл.
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['the_file']
    filename = secure_filename(file.filename)
    file.save(filename)
    listFilename.append(filename)
    return ''

# Выводит последнюю подгруженную фотографию
@app.route('/show', methods=['GET'])
def show():
    return send_file(listFilename[len(listFilename)-1], mimetype='image/gif')

if __name__ == '__main__':
    app.run(debug=True)