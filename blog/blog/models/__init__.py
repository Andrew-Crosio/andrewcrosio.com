"""Transparent Django models
By importing in this way, we create a virtual module that allows us to separate models into
different files without distributing Django
"""
from blog.models.article import Article
from blog.models.like import Like
