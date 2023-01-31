from django.db import models

# We've created a new database model called post which has the database field text.
# We've also specified the type of content it will hold, "TextField()"
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
