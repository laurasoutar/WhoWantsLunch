def lunch_response(author, meal_name, meal_url, message, date_time):
    return {
        "text": message,
        "footer": date_time,
        "author_name": author,
        "title": meal_name,
        "title_link": meal_url,
        "callback_id": "lunch_response",
        "attachment_type": "default",
        "color": "#8F2ABB"
    }
