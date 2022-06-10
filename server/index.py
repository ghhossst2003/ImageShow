# coding=utf-8
from flask import render_template, request, send_from_directory, Response
from flask_cors import cross_origin
from log import loggin_init

import logging
import fileutl
import os
import time
import user

from art_product import save_art_product
from author import get_authors
from art_product import get_works
from art_product import get_works1
from result import Status, reply
from system_exception import UsersException
import session

from flask import Flask
app = Flask(__name__)
loggin_init("flaskserver")
logging.info("hello world, flask!")
session.init_session()

app.config['UPLOAD_FOLDER'] = 'static/'
app.config['THUMB_FOLDER'] = 'thumb/'
app.config['DOWNLOAD_FOLDER'] = 'upload/'


@app.route('/upload_works', methods=['POST'])
@cross_origin()
def upload_works():
    if request.method == 'POST':
        print(request)
        f = request.files['file']
        author = request.values.get('author')
        create_time = request.values.get('creation_time')
        description = request.values.get('description')
        upload_time = int(time.time()*1000)
        image_id = fileutl.save_file(app.config['UPLOAD_FOLDER'], f)
        save_art_product(author, image_id, description, create_time, upload_time)
        return reply(Status.SUCCESS)


@app.route('/files', methods=['POST'])
@cross_origin()
def files():
    if request.method == 'POST':
        files = request.files.getlist('files')
        for file in files:
            image_id = fileutl.save_file(app.config['UPLOAD_FOLDER'], file)
        print(files)
        return 'ok'


@app.route('/authors', methods=['GET'])
@cross_origin()
def authors():
    if request.method == 'GET':
        users = get_authors()
        return reply(Status.SUCCESS, '', users)


@app.route('/login', methods=['GET'])
@cross_origin()
def login():
    if request.method == 'GET':
        try:
            username = request.values.get('username', '')
            password = request.values.get('password', '')
            info = user.login(username, password)
            return reply(Status.SUCCESS, '', info)
        except UsersException as e:
            return reply(Status.FAILURE, str(e))
        except Exception as e:
            logging.exception(e)


@app.route('/works', methods=['GET'])
@cross_origin()
def works():
    if request.method == 'GET':
        works = get_works()
        return reply(Status.SUCCESS, '', works)


@app.route('/works_page/<page>', methods=['GET'])
@cross_origin()
def works_page(page):
    if request.method == 'GET':
        works = get_works1(page=int(page))
        return reply(Status.SUCCESS, '', works)


if __name__ == '__main__':
    print(os.getcwd())
    print(os.listdir('./'))
    app.run(host='0.0.0.0', debug=True)
