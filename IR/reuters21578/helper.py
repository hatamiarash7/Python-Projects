class News(object):
    def __init__(self, id, title, body, date, time, topics):
        self.id = id
        self.title = title
        self.body = body
        self.date = date
        self.time = time
        self.topics = topics

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_topics(self):
        return self.topics
