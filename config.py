# coding=utf-8
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQLALCHEMY_DATABASE_URI = 'mysql://root:sheng123456@localhost:3306/r'
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'tmp/permidr')
SQLALCHEMY_TRACK_MODIFICATIONS = False