#!/usr/bin/env python3
# encoding: utf-8


class Const(object):

    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError("不能改变常量[{0}]的值".format(name))
        if not name.isupper():
            raise self.ConstCaseError("常量名[{0}]必须都是大写".format(name))
        self.__dict__[name] = value

const = Const()

const.UMENG = "umeng"
const.ANDROID = "android"
const.IOS_IPHONE = "iphone"


