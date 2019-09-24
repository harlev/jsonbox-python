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
data = {"name": "Bob", "age": 23}
jb.update(data, MY_BOX_ID, record_ids[0])

# read updated data
print(jb.read(MY_BOX_ID))
print(jb.read(MY_BOX_ID, record_ids[0]))

# delete records matching to query
print(jb.delete(MY_BOX_ID, query="age:=23"))

# delete records
jb.delete(MY_BOX_ID, record_ids[1])


