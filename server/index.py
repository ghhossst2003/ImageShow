# coding=utf-8
from flask import render_template, request, send_from_directory, Response
from flask_cors import cross_origin
import fileutl

import os
import app
import time

from art_product import save_art_product
from author import get_authors
from art_product import get_works
from result import Status, reply


app.app.config['UPLOAD_FOLDER'] = 'image/'
app.app.config['THUMB_FOLDER'] = 'thumb/'
app.app.config['DOWNLOAD_FOLDER'] = 'upload/'


@app.app.route('/upload_works', methods=['POST'])
@cross_origin()
def upload_works():
    if request.method == 'POST':
        f = request.files['file']
        author = request.values.get('author')
        create_time = request.values.get('creation_time')
        description = request.values.get('description')
        upload_time = int(time.time()*1000)
        image_id = fileutl.save_file(app.app.config['UPLOAD_FOLDER'], f)
        save_art_product(author, image_id, description, create_time, upload_time)
        return reply(Status.SUCCESS)


@app.app.route('/files', methods=['POST'])
@cross_origin()
def files():
    if request.method == 'POST':
        files = request.files.getlist('files')
        for file in files:
            image_id = fileutl.save_file(app.app.config['UPLOAD_FOLDER'], file)
        print(files)
        return 'ok'

@app.app.route('/authors', methods=['GET'])
@cross_origin()
def authors():
    if request.method == 'GET':
        users = get_authors()
        return reply(Status.SUCCESS, '', users)


@app.app.route('/works', methods=['GET'])
@cross_origin()
def works():
    if request.method == 'GET':
        works = get_works()
        return reply(Status.SUCCESS, '', works)


if __name__ == '__main__':
    print(os.getcwd())
    print(os.listdir('./'))
    app.app.run(host='0.0.0.0', debug=True)
