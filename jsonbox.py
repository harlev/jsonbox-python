import requests


class JsonBox:
    RECORD_ID_KEY = "_id"

    def __init__(self, service_host="https://jsonbox.io"):
        self.service_host = service_host

    def _get_url(self, box_id, collection_or_record=None, sort_by=None):
        url = "{0}/{1}".format(self.service_host, box_id)

        if collection_or_record:
            url = "{0}/{1}".format(url, collection_or_record)

        if sort_by:
            url = "{0}?sort={1}".format(url, sort_by)

        return url

    def get_record_id(self, data):
        if isinstance(data, list):
            return [item[self.RECORD_ID_KEY] for item in data]
        else:
            return data[self.RECORD_ID_KEY]

    def read(self, box_id, collection_or_record=None, sort_by=None):
        url = self._get_url(box_id, collection_or_record, sort_by)

        response = requests.get(url)
        if response.ok:
            json_data = response.json()
            return json_data
        else:
            return False

    def write(self, data, box_id, collection=None):
        url = self._get_url(box_id, collection)

        response = requests.post(url, json=data)
        if response.ok:
            json_data = response.json()
            return json_data
        else:
            return False

    def update(self, data, box_id, record_id):
        url = self._get_url(box_id, record_id)

        response = requests.put(url, json=data)
        if response.ok:
            json_data = response.json()
            return json_data
        else:
            return False

    def delete(self, box_id, record_ids):
        if isinstance(record_ids, list):
            result = []
            for record_id in record_ids:
                result.append(self._delete_one(box_id, record_id))
            return result
        else:
            return self._delete_one(box_id, record_ids)

    def _delete_one(self, box_id, record_id):
        url = self._get_url(box_id, record_id)

        response = requests.delete(url)
        if response.ok:
            json_data = response.json()
            return json_data
        else:
            return False
