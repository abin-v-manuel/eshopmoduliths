from keycloak import KeycloakAdmin, KeycloakOpenID
import os
from dotenv import load_dotenv

load_dotenv()

# Admin client setup (for creating users, managing roles etc.)
keycloak_admin = KeycloakAdmin(
    server_url=os.getenv("KEYCLOAK_URL", "http://localhost:8080/"),
    username=os.getenv("KEYCLOAK_ADMIN_USER", "admin"),
    password=os.getenv("KEYCLOAK_ADMIN_PASS", "admin"),
    realm_name=os.getenv("KEYCLOAK_REALM", "eshop"),
    client_id="admin-cli",
    verify=True
)

# OpenID client setup (for login/token handling)
keycloak_openid = KeycloakOpenID(
    server_url=os.getenv("KEYCLOAK_URL", "http://localhost:8080/"),
    client_id=os.getenv("KEYCLOAK_CLIENT_ID", "eshop-client"),
    realm_name=os.getenv("KEYCLOAK_REALM", "eshop"),
    client_secret_key=os.getenv("KEYCLOAK_CLIENT_SECRET", "SECRET")
)