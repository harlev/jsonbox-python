# jsonbox-python
Python wrapper for https://jsonbox.io

[![PyPI version](https://badge.fury.io/py/jsonbox.svg)](https://badge.fury.io/py/jsonbox)
<a href="https://github.com/harlev/jsonbox-python/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
</a>
[![Downloads](https://pepy.tech/badge/jsonbox)](https://pepy.tech/project/jsonbox)

## Installation
    pip install jsonbox
    
## Usage
```python
import uuid
from jsonbox import JsonBox

# generate unique box id
MY_BOX_ID = str(uuid.uuid4()).replace("-", "_")

# create instance
jb = JsonBox()

data = [{"name": "David", "age": "25"}, {"name": "Alice", "age": "19"}]

# write data
result = jb.write(data, MY_BOX_ID)

# get record id of written data
record_ids = jb.get_record_id(result)

# read record
print(jb.read(MY_BOX_ID, record_ids[0]))

# read all records in box
print(jb.read(MY_BOX_ID))

# read all records in box with sort
print(jb.read(MY_BOX_ID, sort_by="age"))

# update data
data = {"name": "Bob", "age": "25"}
jb.update(data, MY_BOX_ID, record_ids[0])

# read updated data
print(jb.read(MY_BOX_ID, record_ids[0]))

# delete records
jb.delete(MY_BOX_ID, record_ids)
```


## License
MIT
