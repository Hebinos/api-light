from . import api
from flask import render_template, request, current_app
from app.exceptions import ValidationError
import base64

@api.route('/test', methods=['GET'])
def test():
    from app.create_response import create_response
    content = render_template('ok.json')
    status_code = 200
    mimetype = 'application/json'
    response = create_response(content, status_code, mimetype)

    return response
