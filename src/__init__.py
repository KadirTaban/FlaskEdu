import sqlite3
from flask import Flask

app = Flask(__name__)
dbCon = sqlite3.connect("test.db", check_same_thread=False)