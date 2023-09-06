from base64 import b64encode, b64decode
from hashlib import sha256
from time import time
from urllib import parse
from hmac import HMAC

def generate_sas_token(uri, key, policy_name=None, expiry=3600 * 24 * 365 * 10):
    ttl = time() + expiry
    sign_key = "%s\n%d" % ((parse.quote_plus(uri)), int(ttl))
    print(sign_key)
    signature = b64encode(HMAC(b64decode(key), sign_key.encode('utf-8'), sha256).digest())

    rawtoken = {
        'sr' :  uri,
        'sig': signature,
        'se' : str(int(ttl))
    }

    if policy_name is not None:
        rawtoken['skn'] = policy_name

    return 'SharedAccessSignature ' + parse.urlencode(rawtoken)

if __name__ == '__main__':
    uri = "WTBLHub.azure-devices.cn/WDLC295385WG583-1"
    key = "y7xudrVhee6InidGLBzr+ICq29EhKSTz0pP0MR26CNE="

    print(generate_sas_token(uri, key))