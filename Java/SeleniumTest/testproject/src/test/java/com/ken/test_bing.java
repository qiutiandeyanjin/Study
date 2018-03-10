package com.ken;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;
import java.util.concurrent.TimeUnit;
import org.testng.annotations.*;
import org.testng.Assert;

/**
 * @Description 必应搜索测试类
 * @author xukui
 * @date 2017-8-17 23:55:13
 */

public class test_bing {

    private WebDriver driver = new ChromeDriver();

    @BeforeTest
    public void setUp() throws InterruptedException {
        System.out.println("test_bing start");
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.get("http://cn.bing.com/");
    }

    @Test
    public void action() throws InterruptedException {
        driver.findElement(By.id("sb_form_q")).clear();
        driver.findElement(By.id("sb_form_q")).sendKeys("webdriver");
        driver.findElement(By.id("sb_form_go")).click();
        TimeUnit.SECONDS.sleep(2);
        String title = driver.getTitle();
        Assert.assertEquals(title, "webdriver - 国内版 Bing");
    }

    @AfterTest
    public void tearDown() {
        driver.quit();
        System.out.println("test_bing end");
    }
}
