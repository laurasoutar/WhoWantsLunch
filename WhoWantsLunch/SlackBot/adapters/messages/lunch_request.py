import time

def lunch_request(text, title, author, timestamp, menu_url, return_url):
    return {
        "text": text,
        "ts": timestamp,
        "author_name": author,
        "title": title,
        "title_link": menu_url,
        "fallback": "Who wants lunch?",
        "callback_id": "lunch_request",
        "color": "#c55100",
        "attachment_type": "default",
        "actions": [
            {
                "name": "lunch_yes",
                "text": "Yes",
                "type": "button",
                "value": return_url
            },
            {
                "name": "lunch_no",
                "style": "danger",
                "text": "No",
                "type": "button",
                "value": return_url
            }
        ]
    }
