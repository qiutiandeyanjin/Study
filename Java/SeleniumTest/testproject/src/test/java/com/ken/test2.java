package com.ken;

import org.testng.annotations.*;
import org.testng.Assert;

/**
 * @Description 测试减法
 * @author xukui
 * @date 2017-8-15 22:18:29
 */

public class test2 {

    private calculator count = new calculator();

    @BeforeTest
    public void setUp() {
        System.out.println("test sub start");
    }

    @Test
    public void test_sub() {
        int j = count.sub(2, 3);
        Assert.assertEquals(j, -1);
    }

    @Test
    public void test_sub2() {
        int j = count.sub(71, 46);
        Assert.assertEquals(j, 25);
    }

    @AfterTest
    public void tearDown() {
        System.out.println("test sub end");
    }
}
