#!/usr/bin/env python3
""" 
List all documents using python
"""

import pymongo


def list_all(mongo_collection):
    """ list_all impl. """
    docs = mongo_collection.find()
    return [x for x in docs]
