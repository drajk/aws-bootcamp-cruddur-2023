from functools import wraps
from flask import request, abort
import os

# -- Cognito JWT verifier
from lib.cognito_jwt_verify import CognitoJwtToken, extract_access_token, TokenVerifyError

def auth_cognito(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        current_user = {
            'authenticated': False,
            "username": "unknown"
        }

        access_token = None
        if "Authorization" in request.headers:
            access_token = extract_access_token(request.headers)

        # return when token is not provided in headers 
        if not access_token:
            return f(current_user, *args, **kwargs)

        cognito_jwt_token = CognitoJwtToken(
            user_pool_id=os.getenv("AWS_COGNITO_USER_POOL_ID"), 
            user_pool_client_id=os.getenv("AWS_COGNITO_USER_POOL_CLIENT_ID"),
            region=os.getenv("AWS_DEFAULT_REGION")
        )

        try:
            # handle authenicatied requests

            claims = cognito_jwt_token.verify(access_token)
            current_user["authenticated"] = True
            current_user["username"] = claims["username"]
        except TokenVerifyError as e:
            # handle unauthenicatied requests
            # abort(403)
            current_user["authenticated"] = False

        return f(current_user, *args, **kwargs)

    return decorated