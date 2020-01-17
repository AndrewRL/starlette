from datetime import datetime
from json import loads
from base64 import b64decode


class Post:
    def __init__(self, post):
        self.id = post['id']
        self.title = post['title']
        self.timestamp = datetime.strptime(post['timestamp'], '%Y-%m-%d %H:%M:%S')
        self.length_in_min = post['length_in_min']
        self.short_summary = post['short_summary']
        self.long_summary = post['long_summary']
        self.thumbnail = post['thumbnail']
        self.lead_image = post['lead_image']
        self.body = post['body']
        self.margin_notes = loads(b64decode(post['margin_notes']))
        self.refs = loads(b64decode(post['refs']))
        self.tags = loads(b64decode(post['tags']))

    def to_dict(self):
        return vars(self)


class Project:
    def __init__(self, project):
        self.id = project['id']
        self.name = project['name']
        self.github = project['github']
        self.docs = project['docs']
        self.created = datetime.strptime(project['created'], '%Y-%m-%d %H:%M:%S')
        self.updated = datetime.strptime(project['updated'], '%Y-%m-%d %H:%M:%S')
        self.thumbnail = project['thumbnail']
        self.lead_image = project['lead_image']
        self.short_summary = project['short_summary']
        self.long_summary = project['long_summary']
        self.body = project['body']
        self.margin_notes = loads(b64decode(project['margin_notes']))
        self.tags = loads(b64decode(project['tags']))
        self.refs = loads(b64decode(project['refs']))

    def to_dict(self):
        return vars(self)


class Review:
    def __init__(self, review):
        self.id = review['id']
        self.timestamp = datetime.strptime(review['timestamp'], '%Y-%m-%d %H:%M:%S')
        self.name = review['name']
        self.summary = review['summary']
        self.body = review['body']
        self.rating = review['rating']
        self.notes = review['notes']
        self.margin_notes = loads(b64decode(review['margin_notes']))
        self.tags = loads(b64decode(review['tags']))
        self.refs = loads(b64decode(review['refs']))
        self.link = review['link']

    def to_dict(self):
        return vars(self)
