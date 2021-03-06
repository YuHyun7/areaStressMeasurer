# -*- coding: utf-8 -*-
from flask import request
from flask_api import status
from flask_restful import Resource

from app.models.user_token_model import token_generate
from app.modules import sibyl
from app.modules.auth.login import verify_password

_URL = '/auth'


class Auth(Resource):
    @sibyl.API
    def post(self):
        email = request.form.get('email', None)
        password = request.form.get('password', None)

        if verify_password(email, password):
            _return = {
                'data': token_generate(email=email)
            }
            return _return, status.HTTP_200_OK
        else:
            _return = {
                'message': 'User does not exist or the password does not match.'
            }
            return _return, status.HTTP_400_BAD_REQUEST
