package com.ken;

import org.testng.annotations.*;
import org.testng.Assert;

/**
 * @Description 测试加法
 * @author xukui
 * @date 2017-8-15 22:17:48
 */

public class test {

    private calculator count = new calculator();

    @BeforeTest
    public void setUp() {
        System.out.println("test add start");
    }

    @Test
    public void test_add() {
        int j = count.add(2, 3);
        Assert.assertEquals(j, 5);
    }

    @Test
    public void test_add2() {
        int j = count.add(41, 76);
        Assert.assertEquals(j, 117);
    }

    @AfterTest
    public void tearDown() {
        System.out.println("test add end");
    }
}
