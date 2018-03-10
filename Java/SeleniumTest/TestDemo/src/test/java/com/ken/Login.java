package com.ken;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

class Login {

    void login(WebDriver driver) {
        driver.findElement(By.id("account")).clear();
        driver.findElement(By.id("account")).sendKeys("xwx406368");
        driver.findElement(By.name("password")).clear();
        driver.findElement(By.name("password")).sendKeys("tiyudesi123");
        driver.findElement(By.id("submit")).click();
    }

    void logout(WebDriver driver) {
        driver.findElement(By.linkText("退出")).click();
    }
}
