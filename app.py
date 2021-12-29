from flask import Flask, request, jsonify, send_from_directory
from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from src.graphql import schema
from src.database import Session
from flask_mail import Mail
from src.config import *

app = Flask(__name__)

app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)


@app.route('/graphql', methods=['GET'])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    context = {
        'session': Session(),
        'mail': mail,
    }
    success, result = graphql_sync(
        schema,
        data,
        context_value=context,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


@app.teardown_appcontext
def shutdown_session(exception=None):
    Session.remove()


@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)
