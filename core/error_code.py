from libs.error_code.enum import BaseECEnum, ECData


class ECEnum(BaseECEnum):
    """错误码枚举类"""
    ServerError = ECData('500', '服务异常，请稍后重试')

    # 客户端错误
    MethodNotAllowed = ECData('405', '非法的请求方式')
    InvalidVersion = ECData('420', '无效的版本保')
    InvalidParameter = ECData('430', '请求参数无效')

    # 用户
    PermissionDenied = ECData('10001', '权限不够')
    UserPasswordErr = ECData('10002', '用户账号或密码错误')
    UserExist = ECData('10003', '已存在的用户')
    # 账单

