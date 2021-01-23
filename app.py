from src import app
from src.Users import api
from src.Users.api import users
@app.route('/')
def hello_world():
    return users


if __name__ == '__main__':
    app.run()