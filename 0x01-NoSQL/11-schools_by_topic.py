#!/usr/bin/env python3
"""
Find topics with python
"""


def schools_by_topic(mongo_collection, topic):
    """ schools_by_topic impl. """
    return mongo_collection.find({"topics": topic})
