#!/usr/bin/python3
"""filestorage to help store our info for app"""
from models.engine.file_storage import FileStorage as FS


storage = FS()
storage.reload()
