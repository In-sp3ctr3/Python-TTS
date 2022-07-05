from lib2to3.pgen2.token import OP
import os
from flask import Flask, flash, request, Response, jsonify, send_file, redirect, render_template
from werkzeug.utils import secure_filename
import fileHandler as fileHandler
import speechHandler as speechHandler
from random import randrange
from languageProcessing.ProcessingEngine.processingEngine import Processing
from languageProcessing.parseUtils.parseHandler import Parsing



UPLOAD_FOLDER = './uploads'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['./uploads'], filename))
            return redirect(url_for('upload'))
    return render_template('index.html')

def allowed_file(filename):
    FileTypes = {'txt', 'pdf', 'docx', 'pptx'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in FileTypes

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         if 'file' not in request.files:
#             flash('No file part')
#             return Response("Bad Request",status=400)

#         file = request.files['file']

#         filename_fixed = file.filename.replace(" ", "_")

#         if file and allowed_file(filename_fixed):
#             filename = secure_filename(filename_fixed)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             randNum = randrange(1,900)
#             parse_tree_name = "parse-tree-"+str(randNum)+".pdf" 
#             text = fileHandler.file_read(filename, parse_tree_name)
#             result = Processing.runAnalysis(text)
#             fileName_fix = (filename.rsplit( ".", 1 )[ 0 ] )
#             speechHandler.text_to_speech(text)
#             path = 'parseDocs/' + parse_tree_name
#             Parsing.parser(result, parse_tree_name)
#             Parsing.print_named_entities(result)
#             if(result):
#                 return send_file(path, as_attachment=True)
#             else:
#                 return Response("Something went wrong, please check if your file is valid.",status=400)
#     except:
#         return Response("Something went wrong, please check if your file is valid.",status=500)



@app.route('/text', methods=['POST'])
def upload_text():
    text = request.form['text']

    randNum = randrange(1,900)
    parse_tree_name = "parse-tree-"+str(randNum)+".pdf" 
    result = Processing.runAnalysis(text)
    randNum = randrange(1,900)
    parse_tree_name = "parse-tree-"+str(randNum)+".pdf"
    path = 'parseDocs/' + parse_tree_name
    Parsing.parser(result, parse_tree_name)
    Parsing.print_named_entities(result)
    filename = secure_filename("temp" + str(randNum))
    res = [x[0] for x in result[0]]
    output = " ".join(res)
    speechHandler.text_to_speech(output)
    data = {'audio':filename+".mp3",
            'text':result}
    #return send_file(path, as_attachment=True)
    return render_template('index.html')

app.run(port=5000)