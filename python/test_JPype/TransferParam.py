# coding: utf-8

from jpype import *


def to_byte(param):
    return JByte(param)

def to_short(param):
    return JShort(param)

def to_int(param):
    return JInt(param)

def to_long(param):
    return JLong(param)

def to_float(param):
    return JFloat(param)

def to_double(param):
    return JDouble(param)

def to_boolean(param):
    return JBoolean(param)

def to_char(param):
    return JChar(param)

def to_String(param):
    return JString(param)

def to_int_array(param):
    return JArray(JInt)(param)

def to_String_array(param):
    return JArray(JString)(param)

def to_Animal_array(param, Animal):
    return JArray(Animal)(param)

def to_java_class(cls, param):
    # 获得java class
    java_class = JClass(cls)
    # 调用java class的构造函数示例化对象
    return java_class(*param)

def to_list(param):
    return java.util.ArrayList(param)

def to_HashMap(param):
    return java.util.HashMap(param)

def to_Enum(cls, param):
    # 获得枚举类
    java_class = JClass(cls)
    # 获取枚举对象中的成员
    return getattr(java_class, param)
