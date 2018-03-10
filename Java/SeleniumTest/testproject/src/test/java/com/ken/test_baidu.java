package com.ken;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;
import java.util.concurrent.TimeUnit;
import org.testng.annotations.*;
import org.testng.Assert;

/**
 * @Description 百度搜索测试类
 * @author xukui
 * @date 2017-8-17 23:53:55
 */

public class test_baidu {

    private WebDriver driver = new ChromeDriver();

    @BeforeTest
    public void setUp() throws InterruptedException {
        System.out.println("test_baidu start");
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.get("http://www.baidu.com");
    }

    @Test
    public void action() throws InterruptedException {
        driver.findElement(By.id("kw")).clear();
        driver.findElement(By.id("kw")).sendKeys("testng");
        driver.findElement(By.id("su")).click();
        TimeUnit.SECONDS.sleep(2);
        String title = driver.getTitle();
        Assert.assertEquals(title, "testng_百度搜索");
    }

    @AfterTest
    public void tearDown() {
        driver.quit();
        System.out.println("test_baidu end");
    }
}
