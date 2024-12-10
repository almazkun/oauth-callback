from ninja import Schema


class OAuthCallbackInSchema(Schema):
    code: str


class OAuthCallbackOutSchema(Schema):
    # {
    #   'access_token': '4rFe44HBQhwkk6VwRhdS2KgbU5T9MW',
    #   'expires_in': 36000,
    #   'token_type': 'Bearer',
    #   'scope': 'read write',
    #   'refresh_token':
    #   'O5o2N3WAmLGamYrsAT20YXrBYi9VKn
    # '}
    access_token: str
    expires_in: int
    token_type: str
    scope: str
    refresh_token: str
