# coding=utf-8

# 以正确的宽度在居中的"盒子"内打印一个句子

# 注意，整数除法运算符（//）只能用在Python2.2以及后续的版本，在之前的版本中，只是使用普通除法

# He's a very naughty boy!
sentence = raw_input("Sentence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print
print '' * left_margin + '+' + '-' * (box_width-2) + '+'
print '' * (left_margin + 4) + '| ' + ' ' * text_width + '   |'
print '' * (left_margin + 4) + '| ' + sentence + '   |'
print '' * (left_margin + 4) + '| ' + ' ' * text_width + '   |'
print '' * left_margin + '+' + '-' * (box_width-2) + '+'
print
