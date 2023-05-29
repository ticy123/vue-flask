from flask import jsonify



class ResUtil():

    @staticmethod
    def message(data: any = None, code: str = 0, description: str = 'success'):
        """
        标准API返回函数
        :param data: api回调数据
        :param code: code message  0 正常,0以外的异常码都会自动把错误信息添加到描述中
        :param message: 提示信息
        :return:
        """
        # 用enum实现
        # get_error_description = get_error_codes(code)
        #
        # if get_error_description:
        #     description = get_error_description[1]

        r = {
            'status': code,
            'description': description,
            'data': data if data else None
        }
        resp = jsonify(r)
        return resp
