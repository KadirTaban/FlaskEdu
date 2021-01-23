from src import app
from src.Users import api
from src.Users.api import home
@app.route('/')
def hello_world():
    return home


if __name__ == '__main__':
    app.run()