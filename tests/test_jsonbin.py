import unittest
import uuid
from jsonbox import JsonBox

TEST_BOX_ID = str(uuid.uuid4()).replace("-", "_")
TEST_COLLECTION_ID = "collection_427453"
TEST_RECORD_ID = "test_sjdgfygsf2347623564twfgyu"
TEST_DATA_KEY_1 = "aaa"
TEST_DATA_VALUE_1 = "bbb"
TEST_DATA_KEY_2 = "ccc"
TEST_DATA_VALUE_2 = "ddd"


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
        json_data = self.jb.read(TEST_BOX_ID, "5d80031fca4f06001791fb28")
        self.assertIsNotNone(json_data)
        self.assertFalse(isinstance(json_data, list))
        print(json_data)

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

    def test_write_box(self):
        data = {
            TEST_DATA_KEY_1: TEST_DATA_VALUE_1
        }
        json_data = self.jb.write(data, TEST_BOX_ID)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

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

        result = self.jb.read(TEST_BOX_ID, record_id)
        self.assertFalse(result)

    def test_delete_list(self):
        data = [{TEST_DATA_KEY_1: TEST_DATA_VALUE_1}, {TEST_DATA_KEY_2: TEST_DATA_VALUE_2}]
        json_data = self.jb.write(data, TEST_BOX_ID)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[0][TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

        record_ids = self.jb.get_record_id(json_data)

        json_data = self.jb.delete(TEST_BOX_ID, record_ids)
        self.assertIsNotNone(json_data)

        result = self.jb.read(TEST_BOX_ID, record_ids[0])
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
