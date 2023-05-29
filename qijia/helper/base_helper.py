import json
import requests
from requests.utils import cookiejar_from_dict

# header_info = {
#     "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
#     "Content-Type":"application/json;charset=UTF-8",
#     "Cookie":"customerBeakerSessionId=875c3afaedfa0ac2035370d0cee24635ce3f60f2gAJ9cQAoWBAAAABjdXN0b21lclVzZXJUeXBlcQFLA1gOAAAAX2NyZWF0aW9uX3RpbWVxAkdB2RTit6szM1gJAAAAYXV0aFRva2VucQNYQQAAADZjODQzNTVlNzI3MTRkY2RiNDMyMmIwZWI2MTM4NzI1LTQ4ZDhmYThkNTcyOTQ0ODVhYmMzNjcyZTQ5ODI3ZmMzcQRYAwAAAF9pZHEFWCAAAAA5OGM0N2U1Mjk2Yjk0Y2ZlODc1ZWU2MzIzNTU5NzRmM3EGWA4AAABfYWNjZXNzZWRfdGltZXEHR0HZFOK3qzMzWAYAAAB1c2VySWRxCFgYAAAANWQ2N2E3NWI4ZTRmNDUxNzE5YzY5NzkxcQlYAwAAAHNpZHEKWBgAAAA2NDUzOGFkZTJiZDEzMDAwMDE1MWQzZmNxC3Uu; customerClientId=972551437233839; x-user-id-ad.xiaohongshu.com=5d67a75b8e4f451719c69791; ares.beaker.session.id=1683196639156052482917"
#
# }

header_info = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    "Content-Type":"application/json;charset=UTF-8",
    "Referer":"https://ad.xiaohongshu.com/aurora/ad/account/subAccountManage",
    "Accept":"application/json, text/plain, */*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cookie":"customerBeakerSessionId=3ca8cb5e75db6ffa08bd4629d9dbe7966d7d6c63gAJ9cQAoWBAAAABjdXN0b21lclVzZXJUeXBlcQFLA1gOAAAAX2NyZWF0aW9uX3RpbWVxAkdB2RTlftcaoFgJAAAAYXV0aFRva2VucQNYQQAAADZjODQzNTVlNzI3MTRkY2RiNDMyMmIwZWI2MTM4NzI1LTQ4ZDhmYThkNTcyOTQ0ODVhYmMzNjcyZTQ5ODI3ZmMzcQRYAwAAAF9pZHEFWCAAAAAwMTMxN2UwM2VhNzM0NDA2OWU4ZWYyODlmODk2ZmI2MXEGWA4AAABfYWNjZXNzZWRfdGltZXEHR0HZFOV+1xqgWAYAAAB1c2VySWRxCFgYAAAANWQ2N2E3NWI4ZTRmNDUxNzE5YzY5NzkxcQlYAwAAAHNpZHEKWBgAAAA2NDUzOTVmYjc4YzIxMTAwMDFiZTYwZWFxC3Uu; Max-Age=604800; Expires=Thu, 11-May-2023 11:24:43 GMT; Domain=.xiaohongshu.com; Path=/; HttpOnly, customerClientId=041334663773716; Max-Age=157680000; Expires=Tue, 02-May-2028 11:24:43 GMT; Domain=.xiaohongshu.com; Path=/; Secure; HttpOnly, x-user-id-ad.xiaohongshu.com=5d67a75b8e4f451719c69791; Max-Age=157680000; Expires=Tue, 02-May-2028 11:24:43 GMT; Domain=.xiaohongshu.com; Path=/; HttpOnly",
    "Connection":"keep-alive",
    # "x-s"
}


class BaseHelper(object):

    @staticmethod
    def get_request_result(url=None,cookies=None):
        with requests.get(url, headers=header_info,cookies=cookies) as r:
             res = r.json()
        return res

    @staticmethod
    def get_cookie(url=None, payload=None):
        data = json.dumps(payload)
        response = requests.post(url, headers=header_info, data=data)
        cookie = response.headers.get('Set-Cookie')

        # cookie = response.cookies
        return cookie



