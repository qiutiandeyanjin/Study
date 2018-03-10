package com.study.game;

/**
 * @author xukui
 *
 * 格子类 （或者可以理解成表示蛇的一块身体的类）
 *
 */

public class SnakePos {

    // 定义蛇身体的位置坐标
    public int col;
    public int row;

    /**
     * 行列构造器，表示这一块身体在游戏盘中所在的行列
     *
     * @param row
     *         所在的行
     * @param col
     *         所在的列
     */
    SnakePos(int row, int col) {
        this.row = row;
        this.col = col;
    }

    /**
     * 留下一个无参的构造器，不是为了调用，而是为了为Food类做方便
     */
    SnakePos() {
        col = 0;
        row = 0;
    }
}
