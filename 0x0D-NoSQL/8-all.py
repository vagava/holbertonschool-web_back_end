#!/usr/bin/env python3
"""
List all documents in Python
"""


def list_all(mongo_collection):
    """
    Write a Python function that lists all documents in a collection
    """
    return ([*mongo_collection.find()]
            if mongo_collection.find().count() > 0
            else [])
