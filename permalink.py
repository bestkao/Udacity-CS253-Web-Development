from handler import *
from post import *

# A permalink page for particular posts

class Permalink(Handler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent = blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        self.render('permalink.html', post = post)