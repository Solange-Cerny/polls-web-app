"""
Settings for the polls application.

You can set values of REPOSITORY_NAME and REPOSITORY_SETTINGS in
environment variables, or set the default values in code here.
"""

from os import environ

REPOSITORY_NAME = environ.get('REPOSITORY_NAME', 'azuretablestorage')

if REPOSITORY_NAME == 'azuretablestorage':
    REPOSITORY_SETTINGS = {
        'STORAGE_NAME': environ.get('STORAGE_NAME', 'solarotablestorage'),
        'STORAGE_KEY': environ.get('STORAGE_KEY', 'yH2Zfz+ZUpbxe3QGc/titIuFFE0d+qp5Zz6B2GygG62iwzWYJnCJVt8MeyDGvf6V/yr8MsnTGNhdcyqPgmmPtw=='),
        'STORAGE_TABLE_POLL': environ.get('STORAGE_TABLE_POLL', 'polls'),
        'STORAGE_TABLE_CHOICE': environ.get('STORAGE_TABLE_CHOICE', 'choices'),
    }
elif REPOSITORY_NAME == 'mongodb':
    REPOSITORY_SETTINGS = {
        'MONGODB_HOST': environ.get('MONGODB_HOST', None),
        'MONGODB_DATABASE': environ.get('MONGODB_DATABASE', 'polls'),
        'MONGODB_COLLECTION': environ.get('MONGODB_COLLECTION', 'polls'),
    }
elif REPOSITORY_NAME == 'memory':
    REPOSITORY_SETTINGS = {}
else:
    raise ValueError('Unknown repository.')
