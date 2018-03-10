from pymysql import cursors, connect

# 连接数据库
conn = connect(host='127.0.0.1',
               user='root',
               password='root123',
               db='guest',
               charset='utf8mb4',
               cursorclass=cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        # 创建嘉宾数据
        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id, create_time)' \
              'VALUES' \
              '("andy", "13600110010", "andy@mail.com", 0, 1, NOW());'
        cursor.execute(sql)
        # 提交事物
        conn.commit()

    with conn.cursor() as cursor:
        # 查询添加的嘉宾
        sql = "SELECT realname, phone, email, sign FROM sign_guest WHERE phone=%s"
        cursor.execute(sql, ('13600110010',))
        result = cursor.fetchone()
        print(result)
finally:
    conn.close()
