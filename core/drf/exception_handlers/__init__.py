from typing import List
from django.http import JsonResponse


from .base import BaseExcHandler


# 异常处理实例列表
_EXC_HANDLER_LIST = List[BaseExcHandler] = sorted((
    # UnknownExcHandler(),
))