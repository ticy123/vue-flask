from app import app
from applications.handler.response import ResUtil


@app.errorhandler(405)
def catch_405_error(e):
    """
    405 error

    """

    return ResUtil.message(data=None, code=405, description=str(e))


@app.errorhandler(404)
def catch_404_error(e):
    """
    404 error

    """
    return ResUtil.message(data=None, code=404, description=str(e))


@app.errorhandler(403)
def catch_403_error(e):
    """
    404 error

    """
    return ResUtil.message(data=None, code=403, description=str(e))


@app.errorhandler(401)
def catch_401_error(e):
    """
    404 error

    """
    return ResUtil.message(data=None, code=401, description=str(e))

@app.errorhandler(500)
def catch_500_error(e):
    """
    500 error
    """
    print('捕捉到了500异常')
    # return jsonify({"msg":'error'})
    return ResUtil.message(data=None, code=500, description=str(e))


@app.errorhandler(Exception)
def catch_other_error(e):
    """
    全局异常捕获,所有报错信息统一处理
    """
    print('捕捉到了自定义异常')
    return ResUtil.message(data='捕获到了自定义异常', code='1', description=str(e))
