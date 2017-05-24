import time

def lunch_request(notification, author, meal_name, meal_url, message, date_time, return_url):
    return {
        "text": message,
        "footer": date_time,
        "author_name": author,
        "title": meal_name,
        "title_link": meal_url,
        "fallback": notification,
        "callback_id": "lunch_request",
        "attachment_type": "default",
        "color": "#8F2ABB",
        "actions": [
            {
                "name": "lunch_yes",
                "style": "primary",
                "text": "✔ Yes",
                "type": "button",
                "value": return_url
            },
            {
                "name": "lunch_no",
                "style": "danger",
                "text": "✖ No",
                "type": "button",
                "value": return_url
            }
        ]
    }
