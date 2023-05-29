from enum import Enum, unique
from typing import Optional


class BaseEnum(Enum):
    def get_code(self):
        """
        根据枚举名称取状态码code
        :return: 状态码code
        """
        return self.value[0]

    def get_msg(self):
        """
        根据枚举名称取状态说明message
        :return: 状态说明message
        """
        return self.value[1]

    @classmethod
    def get_msg_by_code(cls, code) -> Optional[str]:
        """根据状态码获取状态信息说明"""
        for name, member in cls.__members__.items():
            if code in member.value:
                return cls[name].get_msg()
        return None

    @classmethod
    def get_code_by_msg(cls, msg) -> Optional[str]:
        """根据状态信息获取状态码说明"""
        for name, member in cls.__members__.items():
            if msg in member.value:
                return cls[name].get_code()
        return None


@unique
class KPIStatus(BaseEnum):
    """客户kpi"""
    KPI_STATUS_DEFAULT = (0, "无")
    KPI_STATUS_SET = (1, "KPI未设置完")
    KPI_STATUS_UNCONFIRMED = (2, "KPI已设置完但未确认")
    KPI_STATUS_CONFIRMED = (3, "KPI已确认")


@unique
class CustomerStatus(BaseEnum):
    """客户状态"""
    CUSTOMER_STATUS_WORKING = (0, "正常运行")
    CUSTOMER_STATUS_PAUSE = (1, "停车检修")  # 不再使用
    CUSTOMER_STATUS_MISS = (2, "业务丢失")
    CUSTOMER_STATUS_DISCARD = (3, "客戶不在使用Insight")  # 不再使用
    CUSTOMER_STATUS_UNWANTED = (4, "客戶不需要服务")
