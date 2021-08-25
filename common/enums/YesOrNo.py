from enum import Enum


class YesOrNo(Enum):
    NO = 0
    YES = 1

    @property
    def code(self):
        return self.value

    @property
    def msg(self):
        return self.name


