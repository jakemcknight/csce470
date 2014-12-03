__author__ = 'milesh'

class Review(object):
    def __init__(self, text, id, user_id):
        self.text = text
        self.id = id
        self.user_id = user_id
        self.good_score = 0
        self.bad_score = 0

