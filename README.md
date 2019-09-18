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

data = [{"name": "first", "age": 25}, {"name": "second", "age": 19}]

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

# read records in box with sort matching query (see documentation for syntax)
print(jb.read(MY_BOX_ID, query="name:firs*"))
print(jb.read(MY_BOX_ID, query="age:=19"))

# read records with limit
print(jb.read(MY_BOX_ID, limit=1))

# read records with skip
print(jb.read(MY_BOX_ID, skip=1))

# update data
data = {"name": "Bob", "age": "25"}
jb.update(data, MY_BOX_ID, record_ids[0])

# read updated data
print(jb.read(MY_BOX_ID, record_ids[0]))

# delete records
jb.delete(MY_BOX_ID, record_ids)
```

## Query Params
As supported (and documented) by https://github.com/vasanthv/jsonbox

You can query by constructing a query string and passing it to the `query` parameter:
```
name:arya%20stark,age:>13
```
The above sample will look for the name `arya stark` and age greater than 13. 

You can filter on `Number`, `String` & `Boolean` values only.

#### Filters for Numeric values.

|                                                                      | Sample                       |
|----------------------------------------------------------------------|------------------------------|
| To filter values greater than or less than a specific value          | `q=age:>10` or `q=age:<10`   |
| To filter values greater (or less) than or equal to a specific value | `q=age:>=10` or `q=age:<=10` |
| To filter values that match a specific value.                        | `q=age:=10`                  |

#### Filters for String values.

|                                                                    | Sample              |
|--------------------------------------------------------------------|---------------------|
| Filter values that start with a specific string                    | `q=name:arya*`      |
| Filter values that end with a specific string                      | `q=name:*stark`     |
| Filter values where a specific string appears anywhere in a string | `q=name:*ya*`       |
| Filter values that match a specific string                         | `q=name:arya%20stark` |

You can combine multiple fields by separating them with commas as shown below:
```
name:arya%20stark,age:>13,isalive:true
```


## License
MIT
