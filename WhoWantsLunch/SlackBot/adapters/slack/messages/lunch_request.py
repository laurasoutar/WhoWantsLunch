def lunch_request(text, url):
    return {
        "text": text,
        "fallback": "Youse’uns Want Lunch?",
        "callback_id": "lunch_response",
        "color": "#c55100",
        "attachment_type": "default",
        "actions": [
            {
                "name": "lunch_yes",
                "text": "Yes",
                "type": "button",
                "value": url
            },
            {
                "name": "lunch_no",
                "text": "No",
                "type": "button",
                "value": url
            }
        ]
    }
