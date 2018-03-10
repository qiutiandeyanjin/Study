package com.ken;

import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.*;
import java.util.concurrent.TimeUnit;

/**
 * @Description testng+selenium+IDEA自动化测试示例
 * @author xukui
 * @date 2017-8-12 15:21:49
 */

public class script {

    private WebDriver driver = new ChromeDriver();

    @BeforeTest
    public void launchapp() throws Exception {
        System.out.println("第1条用例执行开始...");
        driver.get("http://www.baidu.com");
        driver.manage().window().setSize(new Dimension(800,600));
        String title = driver.getTitle();
        Assert.assertEquals(title, "百度一下，你就知道");
        System.out.println(title);
    }

    @Test
    public void action() throws Exception {
        // 等待3秒
        TimeUnit.SECONDS.sleep(3);
        driver.findElement(By.id("kw")).sendKeys("selenium");
        driver.findElement(By.id("su")).click();
        // 执行JS，并接受alert
        TimeUnit.SECONDS.sleep(3);
        String js = "alert(window.document.title)";
        ((JavascriptExecutor) driver).executeScript(js);
        driver.switchTo().alert().accept();
        // 执行JS
        TimeUnit.SECONDS.sleep(3);
        String js1 = "window.scrollTo(100,450)";
        ((JavascriptExecutor) driver).executeScript(js1);
        TimeUnit.SECONDS.sleep(3);
    }

    @AfterTest
    public void terminatetest() {
        System.out.println("第1条用例执行完成");
        driver.close();
    }
}
