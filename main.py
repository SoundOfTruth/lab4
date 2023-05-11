import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'C:\\Users\\Evgenii\\PycharmProjects\\flask_app\\files'
ALLOWED_EXTENSIONS = ['txt']
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', status="The file must have the extension txt")
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            f = open("files\\" + filename, "r", encoding="utf-8")
            punc = '''!()-[]№{};:'"\,<>./?@#$%^&*_~'''
            a = f.read().replace("\n", " ").lower()
            for ele in a:
                if ele in punc:
                    a = a.replace(ele, "")
            a = a.split()
            dictionary = {}
            answer = []
            for i in range(len(a)):
                dictionary[a[i]] = a.count(a[i])
            for key in dictionary.keys():
                if dictionary[key] == max(dictionary.values()):
                    answer.append(key)
            f.close()
            os.remove("files\\" + filename)
            result = "The most frequent word in a file it is : "+', '.join(answer)+"."
            return render_template('index.html', status=result)
        else:
            return render_template('index.html', status="The file must have the extension txt")


