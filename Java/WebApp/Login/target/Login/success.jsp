<%--
  Created by IntelliJ IDEA.
  User: xukui
  Date: 2017/7/22
  Time: 21:50
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
    <title>登录成功</title>
</head>
<body>
<%
    String username = (String) session.getAttribute("username");
    String age = (String) session.getAttribute("age");
    String weight = (String) session.getAttribute("weight");
    String sex = (String) session.getAttribute("sex");
    System.out.println("性别：A" + sex + "A");
    if (sex.trim().equals("M")) {
        sex = "男";
    } else {
        sex = "女";
    }
%>
<div align="center">
    <%=username%>
    <p>欢迎您，登录成功！</p><br/>
    <label style="color: blue">登录用户信息：</label>
    <table border="1">
        <tr>
            <td>姓名：</td>
            <td> <%=username%> </td>
        </tr>
        <tr>
            <td>年龄：</td>
            <td> <%=age%> </td>
        </tr>
        <tr>
            <td>体重：</td>
            <td> <%=weight%> </td>
        </tr>
        <tr>
            <td>性别：</td>
            <td> <%=sex%> </td>
        </tr>
    </table>
    <a href="login.jsp">返回</a>
</div>
</body>
</html>
