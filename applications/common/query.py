import datetime

from flask import request
from flask_sqlalchemy import BaseQuery
from flask_marshmallow import Marshmallow

class Query(BaseQuery):
    def soft_delete(self):
        return self.update({"is_deleted": 1})

    def logic_all(self):
        return self.filter_by(delete_at=None).all()

    def all_json(self, schema: Marshmallow().Schema):
        return schema(many=True).dump(self.all())

    def layui_paginate(self):
        return self.paginate(page=request.args.get('page', type=int),
                             per_page=request.args.get('limit', type=int),
                             error_out=False)

    def layui_paginate_json(self, schema: Marshmallow().Schema):
        """
        返回dict
        """
        _res = self.paginate(
            page=request.args.get('page', type=int),
            per_page=request.args.get('limit', type=int),
            error_out=False
        )
        return schema(many=True).dump(_res.items), _res.total, _res.page, _res.per_page

    def layui_paginate_db_json(self):
        """
        db.query(A.name).layui_paginate_db_json()
        """
        _res = self.paginate(page=request.args.get('page', type=int),
                             per_page=request.args.get('limit', type=int),
                             error_out=False)
        return [dict(i) for i in _res.items], _res.total