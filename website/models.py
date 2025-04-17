from django.db import models

# Create your models here.
import mongoengine as me


class Project(me.Document):
    name = me.StringField(required=True)
    image_url = me.URLField()
    broucher_url = me.URLField()
