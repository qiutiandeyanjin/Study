<%--
  Created by IntelliJ IDEA.
  User: xukui
  Date: 2017/7/22
  Time: 21:49
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" %>
<!DOCTYPE html>
<html lang="zh-cmn-Hans">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>用户登录</title>
</head>
<body>
<form action="LoginTestServlet" name="frmLogin" method="post">
    <h1 align="center">用户登录</h1>
    <div align="center">
        <table border="1">
            <tr>
                <td>用户名：</td>
                <td>
                    <label>
                        <input name="username" id="username" value="" size="20" maxlength="20" onfocus="if (this.value==='Your name') this.value='';"/>
                    </label>
                </td>
            </tr>
            <tr>
                <td>密 码：</td>
                <td>
                    <label>
                        <input type="password" name="password" id="password" value="" size="20" maxlength="20" onfocus="if (this.value==='Your Password') this.value='';" />
                    </label>
                </td>
            </tr>
        </table>
        <br/>
        <input type="submit" name="submit" value="Login" onclick="return validateLogin()">
        <input type="reset" name="reset" value="Clear" />
    </div>
</form>

<script type="text/javascript">
    function validateLogin() {
        var sUserName = document.frmLogin.username.value;
        var sPassWord = document.frmLogin.password.value;
        if(sUserName === "") {
            alert("请输入用户名！");
            return false;
        }

        if(sPassWord === "") {
            alert("请输入密码！");
            return false;
        }
    }
</script>
</body>
</html>
