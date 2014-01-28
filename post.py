from handler import *

from google.appengine.ext import db

# Defines the value of the blog's parent

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

# Defines the properties of the datastore entity for posts

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True, indexed = False)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    # Renders the blog entry in html, while substituting newlines with line breaks
    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str('post.html', p = self)

    def as_dict(self):
        return {'subject': self.subject,
                'content': self.content,
                'created': self.created.strftime('%c'),
                'last_modified': self.last_modified.strftime('%c')}
