package com.ken;

import com.mysql.jdbc.Connection;
import com.mysql.jdbc.Statement;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.util.Objects;

/**
 * Servlet implementation class LoginTestServlet
 * java+mysql+tomcat实现登录
 * @author xukui
 * 2017-7-22 21:22:11
 */
@WebServlet("/LoginTestServlet")
public class LoginTestServlet extends HttpServlet{
    private static final long serialVersionUID = 1L;

    /**
     * @see HttpServlet#HttpServlet()
     */
    public LoginTestServlet() {
        super();
    }

    /**
     * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse respone)
     */
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        doPost(request, response);
    }

    /**
     * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
     */
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
        response.setContentType("text/html;charset=gb2312");
        request.setCharacterEncoding("gb2312");

        String result;

        String username = request.getParameter("username");
        String psw = request.getParameter("password");

        if (Objects.equals("", username) || username == null || username.length() > 20) {
            try {
                result = "请输入用户名（不能超过20个字符）";
                request.setAttribute("message", result);
                response.sendRedirect("login.jsp");
                return;
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        if (Objects.equals("", psw) || psw == null || psw.length() > 20) {
            try {
                result = "请输入密码（不能超过20个字符）";
                request.setAttribute("message", result);
                response.sendRedirect("login.jsp");
                return;
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        //登记JDBC驱动程序
        try {
            Class.forName("com.mysql.jdbc.Driver");
        } catch (Exception e) {
            System.out.print("Class Not Found Exception");
        }

        //链接URL
        String url = "jdbc:mysql://localhost:3306/study";
        Connection connection;
        Statement statement;
        ResultSet resultSet = null;

        try {
            connection = (Connection) DriverManager.getConnection(url, "root", "root123");
            statement = (Statement) connection.createStatement();

            String sql = "select * from userInfo where username = '"+username+"' and userpsw = '"+psw+"'";
            resultSet = statement.executeQuery(sql);
        } catch (Exception e) {
            e.printStackTrace();
        }

        HttpSession session = request.getSession();
        session.setAttribute("username", username);

        try {
            assert resultSet != null;
            if (resultSet.next()) {
                session.setAttribute("age", resultSet.getString("age"));
                session.setAttribute("sex", resultSet.getString("sex"));
                session.setAttribute("weight", resultSet.getString("weight"));
                response.sendRedirect("success.jsp");
            } else {
                session.setAttribute("message", "用户名或密码不匹配。");
                response.sendRedirect("fail.jsp");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
