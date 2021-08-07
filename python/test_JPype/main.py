# coding: utf-8

from jpype import JClass, java
import jpype
# from java_interface import java_interface
from java_interface import java_interface_1
from TransferParam import *

if __name__ == "__main__":
    # 启动jvm并加载jar包
    jpype.startJVM(classpath=r"D:\myProjects\java\JpypeTest\out\artifacts\JpypeTest_v0_1\JpypeTest_v0.1.jar")

    # 实例化myJpypeTest类
    myJpypeTest = JClass("com.linchao.myJpypeTest")()

    # 测试byte类型转换
    res = myJpypeTest.test_byte(to_byte(100))
    print(res)

    # 测试short类型转换
    res = myJpypeTest.test_short(to_short(100))
    print(res)

    # 测试int类型转换
    res = myJpypeTest.test_int(to_int(200))
    print(res)

    # 测试long类型转换
    res = myJpypeTest.test_long(to_long(300))
    print(res)

    # 测试float类型转换
    res = myJpypeTest.test_float(to_float(400.54))
    print(res)

    # 测试double类型转换
    res = myJpypeTest.test_double(to_double(520.54))
    print(res)

    # 测试boolean类型转换
    res = myJpypeTest.test_boolean(to_boolean(True))
    print(res)

    # 测试char类型转换
    res = myJpypeTest.test_char(to_char("a"))
    print(res)

    # 测试String类型转换
    res = myJpypeTest.test_String(to_String("Devin"))
    print(res)


    # 测试int[]类型转换
    # 传入的数组是[0,0,0,0,0]
    res = myJpypeTest.test_Array(to_int_array(5))
    print(res)

    # 传入的数组是[1,2,3,4,5]
    res = myJpypeTest.test_Array(to_int_array([1,2,3,4,5]))
    print(res)

    # 测试String[]类型转换
    res = myJpypeTest.test_Array(to_String_array(["我", "爱", "中", "国"]))
    print(res)

    # 测试自定义对象数组类型转换
    names = ["假老练", "风车车", "莽哥"]
    ages = [3,2,4]
    alias = ["猫儿", "耗子", "狗儿"]
    # 得到Animals类定义
    Animal = JClass("params.Animals")
    animals = []
    for i in range(3):
        # 初始化Animal，并将其加入到列表里。
        animals.append(Animal(to_String(names[i]), to_int(ages[i]), to_String(alias[i])))
    # 参数准备工作已经完成，调用java函数。
    res = myJpypeTest.test_Array(to_Animal_array(animals, Animal))
    for i in res:
        print(i)


    # 测试自定义类型转换
    res = myJpypeTest.test_class(to_java_class("params.Animals", [to_String("假老练"), to_int(3), to_String("猫儿")]))
    print(res)

    # 测试自List类型转换
    res = myJpypeTest.test_List(to_list(["新","年","快","乐"]))
    print(res)

    # 测试自HashMap类型转换
    res = myJpypeTest.test_Map(to_HashMap({to_String("age"):to_int(18), to_String("RMB"):to_int(999999)}))
    print(res)

    # 测试自Enum类型转换
    res = myJpypeTest.test_Enum(to_Enum("params.testEnum", "RED"))
    print(res)

    # 测试JPype异常机制
    try:
        res = myJpypeTest.test_Exception(2, 0)
    except JException as e:
        print("\n\n##############  print(e)  ######################")
        print(e)
        print("\n\n##############  print(e.message)  ######################")
        print(e.message)
        print("\n\n##############  print(e.stacktrace())  ######################")
        print(e.stacktrace())
    print(res)

    # 测试python实现java接口作为回调函数
    res = myJpypeTest.test_recall(to_int(1), JProxy("params.testInterface", inst=java_interface_1()))
    # res = myJpypeTest.test_recall(to_int(1), java_interface())
    print(res)







