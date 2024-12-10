from ninja import Router
from django.conf import settings
import requests
from .schemas import OAuthCallbackOutSchema


TOKEN_URL = settings.TOKEN_URL
CLIENT_ID = settings.CLIENT_ID
CLIENT_SECRET = settings.CLIENT_SECRET
REDIRECT_URI = settings.REDIRECT_URI


router = Router()


@router.get("/callback", response=OAuthCallbackOutSchema)
def callback(request, code: str):
    if code:
        token_response = requests.post(
            TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": REDIRECT_URI,
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            },
        ).json()
        return token_response
    raise Exception("No code provided")
