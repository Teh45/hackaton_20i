from django.db import models


# Database storing all the different stacks (keywords-definition dictionaries
class Stacks_Database(models.Model):
    name = models.TextField()


# Database for one stack, storing all the keyword-definition combinations in this stack with their specific difficulty level
# For multi-table inheritance, see here: https://docs.djangoproject.com/en/3.2/topics/db/models/
class Keyword_Definition_Dictionary(Stacks_Database):
    keyword = models.TextField()
    definition = models.TextField()
    difficulty = models.TextField()

