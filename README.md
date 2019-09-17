# jsonbox-python
Python wrapper for https://jsonbox.io

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

data = {"name": "David"}

# write data
result = jb.write(data, MY_BOX_ID)

# get record id of written data
record_id = jb.get_record_id(result)

# read data
print(jb.read(MY_BOX_ID, record_id))

# update data
data = {"name": "Bob"}
jb.update(data, MY_BOX_ID, record_id)

# read data
print(jb.read(MY_BOX_ID, record_id))
```


## License
MIT
