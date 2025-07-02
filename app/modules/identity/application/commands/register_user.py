from app.modules.identity.infrastructure.keycloak_auth import keycloak_admin
from app.shared.result import Result

def register(username: str, password: str, email: str) -> Result:
    try:
        response = keycloak_admin.create_user({
            "username": username,
            "email": email,
            "enabled": True,
            "credentials": [{
                "value": password,
                "type": "password",
                "temporary": False
            }]
        })

        if response == 201:
            return Result.ok("user_created")
        elif response == 409:
            return Result.fail("Username already exists")
        else:
            return Result.fail(f"Unexpected Keycloak response: {response}")

    except Exception as e:
        import traceback
        traceback.print_exc()  # <-- show full stacktrace in terminal
        return Result.fail(f"Keycloak Exception: {str(e)}")