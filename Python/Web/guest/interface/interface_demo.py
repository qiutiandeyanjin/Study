from zope.interface import Interface
from zope.interface.declarations import implementer


# 定义接口
class IHost(Interface):
    def goodmorning(self, host):
        """say good morning to host"""


@implementer(IHost)  # 继承接口
class Host:
    def goodmorning(self, guest):
        """say good morning to guest"""
        return "Good morning, %s" % guest


if __name__ == "__main__":
    p = Host()
    hi = p.goodmorning('Tom')
    print(hi)
