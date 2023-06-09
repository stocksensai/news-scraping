from api.telegram.connection import interface


def error(error: Exception):
    return interface.request(["message"], method="post", json={
        "text": f"""
🟥Error : {type(error).__name__}
📥Message : {str(error)}
"""
    })
