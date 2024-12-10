from ninja import NinjaAPI
from oauth_callback.api import router as oauth_callback

api = NinjaAPI(urls_namespace="oauth_api")
api.add_router("v1/oauth/", oauth_callback)
