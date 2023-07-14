import unittest
import json
import os

from main import sniff_json_schema

class JsonSchemaTestCase(unittest.TestCase):
    def setUp(self):
        # Create a temporary test directory
        self.test_dir = 'C:/Users/HP/OneDrive/Desktop/Data_science/Python_engineer_assessment/python_engineer_experienced_professional/test_data'
        os.makedirs(self.test_dir, exist_ok=True)

        # Create sample JSON files for testing
        self.simple_json = {
            "attributes": {
            "appName": "ABCDEFGHIJKLMNOPQRSTUVW",
            "eventType": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "subEventType": "ABCDEFGHIJKLMNO",
            "sensitive": False
            },
            "message": {
            "user": {
                "id": "ABCDEFGHIJKLMNOP",
                "nickname": "ABCD",
                "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZABC",
                "accountType": "ABCDEFGHIJKLMNOPQRSTUVWX",
                "countryCode": "ABCDEFGHIJKLMNOPQRSTUVWX",
                "orientation": "ABCDEFGHIJKLMNOPQRSTU"
            },
            "time": 890,
            "acl": [],
            "publicFeed": False,
            "internationalCountries": [
                "ABCDEFGHIJKLMNOPQRSTUVWXYZA",
                "ABCDEFGHIJKLMNOPQ",
                "ABCDEFGHIJKLMNOPQRSTUVW",
                "ABCDEFGHIJKLMNOPQRSTUVWXY",
                "ABCDEFGHIJK",
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "ABCDEFGHIJKLMNOPQR",
                "ABCDEFG",
                "ABCDEFGHIJKLM"
            ],
            "topTraderFeed": True
            }
        }

        with open(os.path.join(self.test_dir, 'simple.json'), 'w') as file:
            json.dump(self.simple_json, file)

    def tearDown(self):
        # Clean up the temporary test directory
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            os.remove(file_path)
        os.rmdir(self.test_dir)

    def test_simple_json_schema(self):
        schema = sniff_json_schema(self.simple_json)
        expected_schema = {
            "user": {
                "id": {
                    "type": "str",
                    "tag": "",
                    "description": "",
                    "required": False
                },
                "nickname": {
                    "type": "str",
                    "tag": "",
                    "description": "",
                    "required": False
                },
                "title": {
                    "type": "str",
                    "tag": "",
                    "description": "",
                    "required": False
                },
                "accountType": {
                    "type": "str",
                    "tag": "",
                    "description": "",
                    "required": False
                },
                "countryCode": {
                    "type": "str",
                    "tag": "",
                    "description": "",
                    "required": False
                },
                "orientation": {
                    "type": "str",
                    "tag": "",
                    "description": "",
                    "required": False
                }
            },
            "time": None,
            "acl": None,
            "publicFeed": None,
            "internationalCountries": None,
            "topTraderFeed": None
        }
        self.assertEqual(schema, expected_schema)

if __name__ == '__main__':
    unittest.main()
