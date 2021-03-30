import os
from flask import render_template, Blueprint, send_file
from testingapp.forms import UploadDataset
from testingapp.utils import save_file

main = Blueprint('main', __name__)

@main.route("/", methods = ['GET', 'POST'])
@main.route("/home", methods = ['GET', 'POST'])
def home():

    
    return render_template('home.html')

@main.route('/download/<string:file_name>')
def download_file(file_name):
    return send_file('datasets/'+file_name, as_attachment=True)


