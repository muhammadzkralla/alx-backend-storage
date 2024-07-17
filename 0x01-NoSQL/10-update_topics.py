#!/usr/bin/env python3
"""
Update topics with python
"""


def update_topics(mongo_collection, name, topics):
    """ update_topics impl. """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)
