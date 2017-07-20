#!/bin/usr/env python3
# -*- coding:utf-8 -*-
# @function:random dictum
# @author:jiwenkangatech@foxmail.com
# @license:MIT License
import random
import os

maths=random.randrange(1,150,1)
os.system('mysql -h irabe.me -u article -p"article" -e "select article from article.article where id=%s" | sed -n "2p"' % (maths) )
exit(0)
