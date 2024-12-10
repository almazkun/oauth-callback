from django.views.generic import TemplateView
from django.conf import settings

AUTH_URL = settings.AUTH_URL
CLIENT_ID = settings.CLIENT_ID
REDIRECT_URI = settings.REDIRECT_URI


# Create your views here.
class LoginView(TemplateView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        auth_url = f"{AUTH_URL}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code"
        context["auth_url"] = auth_url
        return context
