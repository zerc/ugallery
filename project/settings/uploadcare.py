""" Uploadcare related settings.
"""
import os

UPLOADCARE = {
    'pub_key': os.environ.get('UPLOADCARE_PUBLIC_KEY', 'demopublickey'),
    'secret': os.environ.get('UPLOADCARE_SECRET_KEY', 'demoprivatekey'),
}

FORBIDDEN_EXTENSIONS = ('.exe',)
