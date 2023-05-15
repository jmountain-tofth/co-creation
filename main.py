# shoutout to Max Braun, whose Wittgenstein code I am shamelessly reusing
# use Flask to run the app
from flask import abort
from flask import Flask
from flask import make_response
from flask import render_template
from flask import redirect
from flask import request
from flask import send_from_directory
from flask import url_for
from flask_minify import decorators
from flask_minify import minify
import numpy as np
import openai
import os
import random
# may use google cloud for hosting and storage
# from google.cloud import firestore
# from google.cloud import storage
# from google.cloud.firestore_v1.field_path import FieldPath

