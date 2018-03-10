package com.study.game;

import java.util.LinkedList;

/**
 * @author xukui
 *
 * 食物类
 */

class Food extends SnakePos {

    // 定义食物所在的行列
    public int row;
    public int col;

    // 从Configure文件中读取的游戏行列
    private static final int Row = Configure.ROW;
    private static final int Column = Configure.COL;

    Food() {
        // 随机设置这个对象的行列变量
        randomPos();
    }

    /**
     * 获取蛇的snakeBody链表，让蛇身不与食物重叠
     *
     * @param snakeBody
     *         表示蛇身体的链表
     *
     * @return 返回这个类实例化对象的本身
     */
    public Food getSnake(LinkedList<SnakePos> snakeBody) {
        // 如果发现食物的位置和蛇身体重叠，则重新随机食物的位置
        while (checkSame(snakeBody))
            randomPos();
        // 返回这个对象本身，为创建实例时带来方便
        return this;
    }

    /**
     * 检查蛇身体链表中是否有一块与当前食物坐标相同
     *
     * @param snakeBody
     *         表示蛇身体的链表
     *
     * @return 如果有重复返回true
     */
    private boolean checkSame(LinkedList<SnakePos> snakeBody) {
        for (SnakePos sp : snakeBody)
            if (sp.row == this.row && sp.col == this.col)
                return true;
        // 循环遍历是否有重复
        return false;
    }

    /**
     * 随机该对象的行和列变量
     */
    private void randomPos() {
        this.row = (int) (Math.random() * Row);
        this.col = (int) (Math.random() * Column);
    }
}
