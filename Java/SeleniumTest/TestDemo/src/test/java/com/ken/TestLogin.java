package com.ken;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.util.concurrent.TimeUnit;
import org.testng.annotations.*;

/**
 * @Description 调用Login模块进行禅道登录登出测试
 * @author xukui
 * @date 2017-8-13 23:33:15
 */

public class TestLogin {

    private WebDriver driver = new ChromeDriver();

    @BeforeTest
    public void launchapp() throws Exception {
        System.out.println("第2条用例执行开始...");
        //Puts a Implicit wait, Will wait for 10 seconds before throwing exception
        driver.get("http://szxtsv0813.ken.com/zentaopms/www/index.php");
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    }

    @Test
    public void action() throws InterruptedException {
        // 调用登录模块
        Login test = new Login();
        test.login(driver);
        TimeUnit.SECONDS.sleep(3);
        test.logout(driver);
    }

    @AfterTest
    public void terminatetest() {
        System.out.println("第2条用例执行完成");
        driver.close();
    }
}
