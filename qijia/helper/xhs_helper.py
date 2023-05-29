from qijia.helper.base_helper import BaseHelper
import requests

login_url ="https://customer.xiaohongshu.com/api/cas/loginWithAccount"
login_data = {
  "account": "qitiantian@qeeka.com",
  "password": "Qiyixhs@2108",
  "service": "https://ad.xiaohongshu.com"
}

header_info = {
    # "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    # "Content-Type":"application/json;charset=UTF-8",
    # "Accept":"application/json, text/plain, */*",
    # "Accept-Encoding":"gzip, deflate, br",
    # "Accept-Language":"zh-CN,zh;q=0.9",
    # "Connection":"keep-alive",
    "UserName":"xhui@qeeka.com",
    "AccessToken":"f9218b083ec642959f24c4df5f3f8e87"
}

class XhsHelper(BaseHelper):


    def get_xhs_cookie(self):
        return self.get_cookie(login_url, payload=login_data)


    def test_token(self):
        url = "https://ad.xiaohongshu.com/api/leona/finance/trade_detail?page=1&pageSize=20&startTime=2023-04-01&endTime=2023-05-01&tradeType=0&type=0"
        data = requests.get(url,headers=header_info).json()
        return data

if __name__ == '__main__':
    xhs_helper = XhsHelper()
    # xhs_helper.get_xhs_cookie()
    xhs_helper.test_token()



