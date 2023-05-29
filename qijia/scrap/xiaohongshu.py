from qijia.helper.xhs_helper import XhsHelper

PAGE_SIZE = 2000
COOKIE = None
xhs_helper = XhsHelper()


def save_cookie():
    cookie = xhs_helper.get_xhs_cookie()
    with open('cookie/xhs1.txt', 'w') as f:
        f.write(str(cookie))

def read_cookie():
    cookie_dict = {}
    with open('cookie/xhs1.txt', 'r') as f:
        cookie_str = f.read().strip()
        cookie_dict = eval(cookie_str)
    return cookie_dict


def get_accounts():
    # save_cookie()
    # cookie_dict = read_cookie()
    url = f"https://ad.xiaohongshu.com/api/leona/brand/shadow/list?page=1&page_size={PAGE_SIZE}"
    # cookie_dict = xhs_helper.get_xhs_cookie()
    data = xhs_helper.get_request_result(url=url)
    return data

if __name__ == '__main__':
    # save_cookie()
    get_accounts()











