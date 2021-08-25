from enum import Enum
from types import DynamicClassAttribute


class TypeFieldEnum(Enum):
    """类型字段枚举类
    示例：
        class XXXEnum(TypeFieldEnum):
            xxx1 = (1, '展示内容1')
            xxx2 = (2, '展示内容2')
            ...
    """

    @classmethod
    def to_tuple(cls):
        """转为元组"""
        return tuple(item.value for item in cls)

    @DynamicClassAttribute
    def val(self):
        """值"""
        return self.value[0]

    @DynamicClassAttribute
    def desc(self):
        """描述"""
        return self.value[1]
