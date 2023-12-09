from models.engine.file_storage import FileStorage
from models.base_model import BaseModel as BM

# Create an instance of the FileStorage class
fs = FileStorage()

# Create two instances of the BaseModel class
bm1 = BM()
bm2 = BM()

# Add the two instances to the FileStorage object
fs.new(bm1)
fs.new(bm2)

# Save the FileStorage object to the JSON file
fs.save()

# Print the contents of the JSON file
with open("file.json", "r") as f:
    print(f.read())

# Reload the FileStorage object from the JSON file
fs.reload()

# Print the dictionary of objects in the FileStorage object
print(fs.all())
