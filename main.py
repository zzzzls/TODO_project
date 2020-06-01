from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

if __name__ == "__main__":
    from views import app
    app.run(host="127.0.0.1", port="80", debug=True)
