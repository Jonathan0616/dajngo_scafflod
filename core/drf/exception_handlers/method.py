from typing import Type

from django.http import JsonResponse
from rest_framework.exceptions import MethodNotAllowed

from core.drf.exception_handlers import BaseExcHandler
from core.error_code import ECEnum
from core.response import response_fail


class MethodExcHandler(BaseExcHandler):
    """请求方式异常处理"""

    def get_exception(self) -> Type[Exception]:
        return MethodNotAllowed

    def handler(self, exception: Exception, context: dict) -> JsonResponse:
        return response_fail(enum=ECEnum.MethodNotAllowed)
