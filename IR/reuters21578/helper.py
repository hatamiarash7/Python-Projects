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


class Token(object):
    def __init__(self, id, token, tf=None, df=None):
        self.id = id
        self.token = token
        self.tf = 0 if tf is None else tf
        self.df = 0 if df is None else df

    def get_id(self):
        return self.id

    def get_token(self):
        return self.token

    def get_tf(self):
        return self.tf

    def get_df(self):
        return self.df

    def set_tf(self, value):
        pass

    def set_df(self, value):
        self.df = value

    def inc_df(self):
        self.df += 1

    def inc_df_by(self, value):
        self.df += value

    def inc_tf(self):
        self.tf += 1

    def inc_tf_by(self, value):
        self.tf += value
