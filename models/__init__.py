#!/usr/bin/python3
"""
create a unique FileStorage for AirBnB application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
