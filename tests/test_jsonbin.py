import unittest
import uuid
from jsonbox import JsonBox

TEST_BOX_ID = str(uuid.uuid4()).replace("-", "_")
TEST_PRIVATE_BOX_ID = str(uuid.uuid4()).replace("-", "_")
TEST_PRIVATE_BOX_ID_FAIL = str(uuid.uuid4()).replace("-", "_")
TEST_COLLECTION_ID = "collection_427453"
TEST_RECORD_ID = "test_sjdgfygsf2347623564twfgyu"
TEST_DATA_KEY_1 = "gjsfdjghdjs"
TEST_DATA_VALUE_1 = "cbzmnxbc"
TEST_DATA_KEY_2 = "po[poiioip"
TEST_DATA_VALUE_2 = "yiyuynkjbb"


class TestJsonBox(unittest.TestCase):
    def setUp(self):
        self.jb = JsonBox()

    def test_get_record_id_list(self):
        data = [{"aaa": "bbb", self.jb.RECORD_ID_KEY: 1}, {"aaa": "bbb", self.jb.RECORD_ID_KEY: 2}]
        ids = self.jb.get_record_id(data)

        self.assertIsNotNone(ids)
        self.assertEqual(ids, [1, 2])

    def test_get_record_id_single(self):
        data = {"aaa": "bbb", self.jb.RECORD_ID_KEY: 1}
        ids = self.jb.get_record_id(data)

        self.assertIsNotNone(ids)
        self.assertEqual(ids, 1,)

    def test_read_record(self):
        data = {"name": "first", "age": 25}
        box_id = TEST_BOX_ID + "_query"
        result = self.jb.write(data, box_id)
        record_id = self.jb.get_record_id(result)

        json_data = self.jb.read(box_id, record_id)
        self.assertIsNotNone(json_data)
        self.assertFalse(isinstance(json_data, list))
        self.assertEqual(json_data["name"], data["name"])

    def test_read_box(self):
        json_data = self.jb.read(TEST_BOX_ID)
        self.assertIsNotNone(json_data)
        self.assertTrue(isinstance(json_data, list))

    def test_read_sort(self):
        data = [{"name": "first", "age": "25"}, {"name": "second", "age": "19"}]
        box_id = TEST_BOX_ID + "_sort"
        result = self.jb.write(data, box_id)
        record_ids = self.jb.get_record_id(result)

        json_data = self.jb.read(box_id, sort_by="age")
        self.assertIsNotNone(json_data)
        self.assertTrue(isinstance(json_data, list))
        self.assertEqual(json_data[0]["name"], "second")

        # cleanup
        for record_id in record_ids:
            self.jb.delete(box_id, record_id)

    def test_read_limit(self):
        data = [{"name": "first", "age": "25"}, {"name": "second", "age": "19"}]
        box_id = TEST_BOX_ID + "_limit"
        result = self.jb.write(data, box_id)
        record_ids = self.jb.get_record_id(result)

        json_data = self.jb.read(box_id, limit=1)
        self.assertIsNotNone(json_data)
        self.assertTrue(isinstance(json_data, list))
        self.assertEqual(len(json_data), 1)

        # cleanup
        for record_id in record_ids:
            self.jb.delete(box_id, record_id)

    def test_read_query(self):
        data = [{"name": "first", "age": 25}, {"name": "second", "age": 19}]
        box_id = TEST_BOX_ID + "_query"
        result = self.jb.write(data, box_id)
        record_ids = self.jb.get_record_id(result)

        json_data = self.jb.read(box_id, query="name:firs*")
        self.assertIsNotNone(json_data)
        self.assertTrue(isinstance(json_data, list))
        self.assertEqual(len(json_data), 1)
        self.assertEqual(json_data[0]["name"], "first")

        json_data = self.jb.read(box_id, query="age:=19")
        self.assertIsNotNone(json_data)
        self.assertTrue(isinstance(json_data, list))
        self.assertEqual(len(json_data), 1)
        self.assertEqual(json_data[0]["name"], "second")

        # cleanup
        for record_id in record_ids:
            self.jb.delete(box_id, record_id)

    def test_write_box(self):
        data = {
            TEST_DATA_KEY_1: TEST_DATA_VALUE_1
        }
        json_data = self.jb.write(data, TEST_BOX_ID)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

    def test_write_box_api_key(self):
        data = {
            TEST_DATA_KEY_1: TEST_DATA_VALUE_1
        }
        api_key = self.jb.get_new_api_key()
        json_data = self.jb.write(data, TEST_PRIVATE_BOX_ID, api_key=api_key)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

        record_id = self.jb.get_record_id(json_data)

        json_data = self.jb.read(TEST_PRIVATE_BOX_ID, record_id)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

        data = {
            TEST_DATA_KEY_2: TEST_DATA_VALUE_2
        }
        self.jb.update(data, TEST_PRIVATE_BOX_ID, record_id, api_key=api_key)

        json_data = self.jb.read(TEST_PRIVATE_BOX_ID, record_id)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_2], TEST_DATA_VALUE_2)

        json_data = self.jb.delete(TEST_PRIVATE_BOX_ID, record_id, api_key=api_key)
        self.assertIsNotNone(json_data)

        self.assertRaises(ValueError, self.jb.read, TEST_PRIVATE_BOX_ID, record_id)

    def test_write_box_api_key_fail(self):
        data = {
            TEST_DATA_KEY_1: TEST_DATA_VALUE_1
        }
        api_key = self.jb.get_new_api_key()
        json_data = self.jb.write(data, TEST_PRIVATE_BOX_ID_FAIL, api_key=api_key)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

        record_id = self.jb.get_record_id(json_data)

        json_data = self.jb.read(TEST_PRIVATE_BOX_ID_FAIL, record_id)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

        data = {
            TEST_DATA_KEY_2: TEST_DATA_VALUE_2
        }
        self.assertRaises(ValueError, self.jb.update, data, TEST_PRIVATE_BOX_ID_FAIL, record_id)

        self.assertRaises(ValueError, self.jb.delete, TEST_PRIVATE_BOX_ID_FAIL, record_id)


    def test_write_box_collection(self):
        data = {
            TEST_DATA_KEY_1: TEST_DATA_VALUE_1
        }
        json_data = self.jb.write(data, TEST_BOX_ID, TEST_COLLECTION_ID)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

    def test_update(self):
        data = {
            TEST_DATA_KEY_1: TEST_DATA_VALUE_1
        }
        json_data = self.jb.write(data, TEST_BOX_ID)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

        record_id = self.jb.get_record_id(json_data)

        json_data = self.jb.read(TEST_BOX_ID, record_id)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

        data = {
            TEST_DATA_KEY_2: TEST_DATA_VALUE_2
        }
        self.jb.update(data, TEST_BOX_ID, record_id)

        json_data = self.jb.read(TEST_BOX_ID, record_id)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_2], TEST_DATA_VALUE_2)

    def test_delete(self):
        data = {
            TEST_DATA_KEY_1: TEST_DATA_VALUE_1
        }
        json_data = self.jb.write(data, TEST_BOX_ID)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

        record_id = self.jb.get_record_id(json_data)

        json_data = self.jb.delete(TEST_BOX_ID, record_id)
        self.assertIsNotNone(json_data)

        self.assertRaises(ValueError, self.jb.read, TEST_BOX_ID, record_id )

    def test_delete_list(self):
        data = [{TEST_DATA_KEY_1: TEST_DATA_VALUE_1}, {TEST_DATA_KEY_2: TEST_DATA_VALUE_2}]
        json_data = self.jb.write(data, TEST_BOX_ID)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[0][TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

        record_ids = self.jb.get_record_id(json_data)

        json_data = self.jb.delete(TEST_BOX_ID, record_ids)
        self.assertIsNotNone(json_data)

        self.assertRaises(ValueError, self.jb.read, TEST_BOX_ID, record_ids[0])

    def test_delete_query(self):
        data = [{TEST_DATA_KEY_1: TEST_DATA_VALUE_1}, {TEST_DATA_KEY_2: TEST_DATA_VALUE_2}]
        json_data = self.jb.write(data, TEST_BOX_ID)
        self.assertIsNotNone(json_data)
        self.assertEqual(len([record for record in json_data if TEST_DATA_KEY_1 in record and record[TEST_DATA_KEY_1] == TEST_DATA_VALUE_1]), 1)
        self.assertEqual(len([record for record in json_data if TEST_DATA_KEY_2 in record and record[TEST_DATA_KEY_2] == TEST_DATA_VALUE_2]), 1)

        json_data = self.jb.read(TEST_BOX_ID)
        self.assertEqual(len([record for record in json_data if TEST_DATA_KEY_1 in record and record[TEST_DATA_KEY_1] == TEST_DATA_VALUE_1]), 1)
        self.assertEqual(len([record for record in json_data if TEST_DATA_KEY_2 in record and record[TEST_DATA_KEY_2] == TEST_DATA_VALUE_2]), 1)

        query = "{0}:{1}".format(TEST_DATA_KEY_2, TEST_DATA_VALUE_2[:4] + "*")

        json_data = self.jb.delete(TEST_BOX_ID, query=query)
        self.assertIsNotNone(json_data)

        json_data = self.jb.read(TEST_BOX_ID)
        self.assertEqual(len([record for record in json_data if TEST_DATA_KEY_1 in record and record[TEST_DATA_KEY_1] == TEST_DATA_VALUE_1]), 1)
        self.assertEqual(len([record for record in json_data if TEST_DATA_KEY_2 in record and record[TEST_DATA_KEY_2] == TEST_DATA_VALUE_2]), 0)


if __name__ == '__main__':
    unittest.main()
