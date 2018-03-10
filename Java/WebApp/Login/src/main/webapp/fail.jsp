<%--
  Created by IntelliJ IDEA.
  User: xukui
  Date: 2017/7/22
  Time: 21:50
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8"%>
<!DOCTYPE html>
<html lang="zh-cmn-Hans">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>登录失败</title>
</head>
<body>
<%
    String username = (String) session.getAttribute("username");
    String msg = (String) session.getAttribute("message");
%>
</body>
<div align="center">
    <%=username%>
    <p>对不起，登录失败！</p><br/>
    <label style="color: red">原因：</label>
    <%=msg%><br/>
    <br/>
    <p>5秒后将返回登录界面</p>
</div>

<%
    response.setHeader("Refresh", "5;URL=/login.jsp");
%>
</html>
