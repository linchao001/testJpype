package com.linchao;


import params.Animals;
import params.testEnum;
import params.testInterface;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class myJpypeTest {

    public int test_byte(byte param){
        int res =  param + 1;
        return res;
    }

    public String test_short(short param){
        int res = param + 1;
        return param + "+" + "1" + "=" + res;
    }

    public String test_int(int param){
        int res = param + 1;
        return param + "+" + "1" + "=" + res;
    }

    public String test_long(long param){
        long res = param + 1;
        return param + "+" + "1" + "=" + res;
    }

    public String test_float(float param){
        float res = param + 1;
        return param + "+" + "1" + "=" + res;
    }

    public String test_double(double param){
        double res = param + 1;
        return param + "+" + "1" + "=" + res;
    }

    public String test_boolean(boolean param){
        if(param == true){
            return "param is true";
        }
        else {
            return "param is false";
        }
    }

    public String test_char(char param){
        int a = param;
        return "ascii: " + param + "->" + a;
    }

    public String test_String(String param){
        return "Hello! " + param ;
    }

    public int test_Array(int[] param){
        int sum = 0;
        for(int i : param){
            sum = sum + i;
        }
        return sum;
    }

    public String test_Array(String[] param){
        String sum = "";
        for(String i : param){
            sum = sum + i;
        }
        return sum;
    }

//  遍历Animals数组，调用每个动物的sayHello接口，将其自我介绍打包到一个序列里并返回。
    public List<String> test_Array(Animals[] params){

        List<String> res = new ArrayList();
        for(Animals animal: params){
            res.add(animal.sayHello());
        }
        return res;
    }
    
    public String test_class(Animals animals){
        return animals.sayHello();
    }

    public String test_List(List<String> params){
        String res = "";
        for(String param : params){
            res = res + param;
        }
        return res;
    }

    public String test_Map(HashMap<String, Integer> params){
        int age = params.get("age");
        int rmb = params.get("RMB");
        return "age:"+age+" rmb:"+rmb;
    }

    public String test_Enum(testEnum testenum){
        return testenum.getColor();
    }

    public int test_Exception(int a, int b){
        if(b == 0){
            throw new ArithmeticException("异常：除数不能为0");
        }
        return a/b;
    }

    public int test_recall(int a, testInterface a_interface_obj){
        int b = a_interface_obj.testMethod();
        return a+b;
    }


    public static void main(String[] args){
        System.out.println("Jpype Test...");
    }
}
