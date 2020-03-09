import requests
import uuid
from six.moves.urllib import parse


class JsonBox:
    RECORD_ID_KEY = "_id"

    def __init__(self, service_host="https://jsonbox.io"):
        self.service_host = service_host

    def _get_url(self,
                 box_id,
                 collection_or_record=None,
                 sort_by=None,
                 skip=None,
                 limit=None,
                 query=None):
        url = "{0}/{1}".format(self.service_host, box_id)

        if collection_or_record:
            url = "{0}/{1}".format(url, collection_or_record)

        params = {}
        if sort_by:
            params["sort"] = sort_by

        if skip:
            params["skip"] = skip

        if limit:
            params["limit"] = limit

        if query:
            params["q"] = query

        if len(params.keys()) > 0:
            param_str = parse.urlencode(params)
            url = "{0}?{1}".format(url, param_str)

        return url

    def get_record_id(self, data):
        if isinstance(data, list):
            return [item[self.RECORD_ID_KEY] for item in data]
        else:
            return data[self.RECORD_ID_KEY]

    @staticmethod
    def get_new_api_key():
        return str(uuid.uuid4())

    def read(self,
             box_id,
             collection_or_record=None,
             sort_by=None,
             skip=None,
             limit=None,
             query=None):
        url = self._get_url(box_id, collection_or_record, sort_by, skip, limit, query)

        response = requests.get(url)
        return self._check_response(response)

    def write(self, data, box_id, collection=None, api_key=None):
        url = self._get_url(box_id, collection)

        headers = self._get_headers(api_key)

        response = requests.post(url, json=data, headers=headers)
        return self._check_response(response)

    def _get_headers(self, api_key):
        headers = None
        if api_key:
            headers = {"x-api-key": api_key}
        return headers

    def update(self, data, box_id, record_id, api_key=None):
        url = self._get_url(box_id, record_id)
        headers = self._get_headers(api_key)

        response = requests.put(url, json=data, headers=headers)
        return self._check_response(response)

    def delete(self, box_id, record_ids=None, query=None, api_key=None):
        if record_ids:
            if isinstance(record_ids, list):
                result = []
                for record_id in record_ids:
                    result.append(self._delete_one(box_id, record_id))
                return result
            else:
                return self._delete_one(box_id, record_ids, api_key=api_key)
        elif query:
            return self._delete_query(box_id, query, api_key=api_key)

    def _delete_query(self, box_id, query, api_key=None):
        url = self._get_url(box_id, query=query)
        headers = self._get_headers(api_key)

        response = requests.delete(url, headers=headers)
        return self._check_response(response)

    def _delete_one(self, box_id, record_id, api_key=None):
        url = self._get_url(box_id, record_id)
        headers = self._get_headers(api_key)

        response = requests.delete(url, headers=headers)
        return self._check_response(response)

    def _check_response(self, response):
        if response.ok:
            json_data = response.json()
            return json_data
        else:
            raise ValueError(str(response.text))
