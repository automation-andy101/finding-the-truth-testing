from behave.formatter import null


def new_user_session_bookmark_history_json():
    body = {
        "bookmark": {
            "history": {
                "5c9126fe3b767": {
                    "visited": True,
                    "experienced": True,
                    "parts": {}
                }
            },
            "inputs": {},
            "project": null,
            "current": "5c9126fe3b767.json",
            "version": "1"
        }
    }
    return body