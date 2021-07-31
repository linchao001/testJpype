package params;

public enum testEnum {
    RED("红色"), GREEN("绿色"), BLANK("白色"), YELLO("黄色");

    private String color;
    testEnum(String color) {
        this.color = color;
    }

    public String getColor() {
        return color;
    }
}
