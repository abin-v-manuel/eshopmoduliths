
from app.modules.identity.infrastructure.keycloak_auth import keycloak_openid

def login(username: str, password: str):
    try:
        return keycloak_openid.token(username, password)
    except:
        return None