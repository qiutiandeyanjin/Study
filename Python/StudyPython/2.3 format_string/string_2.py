# coding=utf-8

format = "Pi with three decimals: %.3f"
from math import pi

print format % pi

# -----模板字符串-----
from string import Template

s = Template('$x, glorious $x!')
s.substitute(x='slurm')
