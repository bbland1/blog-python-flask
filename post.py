from datetime import datetime
class Post:
    def __init__(self, id, title, subtitle, body, author, date) -> None:
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.author = author
        date_info = datetime.strptime(date, '%m%d%y').date()
        self.date = date_info.strftime("%B %d, %Y")