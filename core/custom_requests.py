'''

'''

import requests
import json as complexjson
from common.custom_logger import CreateLogger

class CustomRequests:

    def __init__(self, url):
        self.api_root_url = url
        #能够跨请求地保持参数
        self.session = requests.sessions.Session

    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        logger = CreateLogger.get_logging().logger
        logger.info('接口请求地址：{}'.format(url))
        logger.info('接口请求方式：{}'.format(method))
        logger.info('接口请求头：{}'.format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info('接口请求params参数：{}'.format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        logger.info('接口请求体data参数：{}'.format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        logger.info('接口请求体json参数：{}'.format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        logger.info('接口上传附件files参数：{}'.format(files))
        logger.info('接口cookies参数：{}'.format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))

    def request(self, url, method, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        headers = dict(**kwargs).get('headers')
        params = dict(**kwargs).get('params')
        files = dict(**kwargs).get('params')
        cookies = dict(**kwargs).get('params')
        self.request_log(url, method, data, json, params, headers, files, cookies)
        if method == 'GET':
            return self.session.get(url, **kwargs)
        if method == 'POST':
            return requests.post(url, data, json, **kwargs)
        if method == 'PUT':
            if json:
                data = complexjson.dumps(json)
                return self.session.put(url, data, **kwargs)
        if method == 'DELETE':
            return self.session.delete(url, **kwargs)
        if method == 'PATCH':
            if json:
                data = complexjson.dumps(json)
                return self.session.patch(url, data, **kwargs)

    def get(self, url, **kwargs):
        return self.request(url, 'GET', **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, 'POST', data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, 'PUT', data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, 'DELETE', **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, 'PATCH', data, **kwargs)
