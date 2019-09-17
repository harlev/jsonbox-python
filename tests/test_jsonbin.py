import unittest
from jsonbox import JsonBox

TEST_BOX_ID = "test_gywvcu8ew7t7gascbascbuwd"
TEST_COLLECTION_ID = "collection_427453"
TEST_RECORD_ID = "test_sjdgfygsf2347623564twfgyu"
TEST_DATA_KEY_1 = "aaa"
TEST_DATA_VALUE_1 = "bbb"
TEST_DATA_KEY_2 = "ccc"
TEST_DATA_VALUE_2 = "ddd"


class TestJsonBox(unittest.TestCase):
    def setUp(self):
        self.jb = JsonBox()

    def test_read_record(self):
        json_data = self.jb.read(TEST_BOX_ID, "5d80031fca4f06001791fb28")
        self.assertIsNotNone(json_data)
        self.assertFalse(isinstance(json_data, list))
        print(json_data)

    def test_read_box(self):
        json_data = self.jb.read(TEST_BOX_ID)
        self.assertIsNotNone(json_data)
        self.assertTrue(isinstance(json_data, list))

        print(json_data)

    def test_write_box(self):
        data = {
            TEST_DATA_KEY_1: TEST_DATA_VALUE_1
        }
        json_data = self.jb.write(data, TEST_BOX_ID)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

        print(json_data)

    def test_write_box_collection(self):
        data = {
            TEST_DATA_KEY_1: TEST_DATA_VALUE_1
        }
        json_data = self.jb.write(data, TEST_BOX_ID, TEST_COLLECTION_ID)
        self.assertIsNotNone(json_data)
        self.assertEqual(json_data[TEST_DATA_KEY_1], TEST_DATA_VALUE_1)

        print(json_data)

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

        print(json_data)

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

        reuslt = self.jb.read(TEST_BOX_ID, record_id)
        self.assertFalse(reuslt)

        print(json_data)


if __name__ == '__main__':
    unittest.main()
