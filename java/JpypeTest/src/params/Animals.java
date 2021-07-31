package params;

public class Animals {

    private String name="";
    private int age=0;
    private String alias="";

    public Animals(String name, int age, String alias) {
        this.name = name;
        this.age = age;
        this.alias = alias;
    }

    public String sayHello(){
        return "你好!我是" + this.name + ",今年" + this.age + "岁, 人们通常叫我"+ this.alias;
    }
}
