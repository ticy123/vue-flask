import jpush
import logging
logger = logging.getLogger('jpush')
_jpush = jpush.JPush('c9234fd2de8f177fe07ef501', '652ce8134de37ad7d8085ff6')

def test_push():
    push = _jpush.create_push()
    # if you set the logging level to "DEBUG",it will show the debug logging.
    _jpush.set_logging("DEBUG")
    push.audience = jpush.alias("test_alias@veolia.com")
    # push.audience = jpush.registration_id("18071adc0215d1d5979")
    alert = "Praxair (Shanghai ZJ) Semiconductor Gase_Online - Cooling Copper Corrosion rate数值高于InSight设置报警上限(HH)，现值0.21，前值0.168, 0.172, 0.167，请及时登录InSight查看详细数据情况 https://insight.watertechs.cn/"
    push.notification = jpush.notification(ios=jpush.ios(alert=alert),android=jpush.android(alert=alert,big_text=alert,title="水质报告报警",style=1))
    # push.message = jpush.message(msg_content=alert,title="水质报告报警",content_type="text",extras={"key": "value"})
    push.platform = jpush.all_
    response=push.send()

def test_device():
    device = _jpush.create_device()
    # if you set the logging level to "DEBUG",it will show the debug logging.
    _jpush.set_logging("DEBUG")
    # get device info from registration_id
    response=device.get_deviceinfo("18071adc0215d1d5979")
    logger.info(response)
    #set alias through registration_id
    # response=device.set_deviceinfo("18071adc0215d1d5979",{'alias':"test_alias@veolia.com"})
    # logger.info(response)

if __name__ == '__main__':
    # test_device()
    test_push()
