# -*- coding: utf-8 -*-
#设置中文字符编码
print None                      #变量是个空值，0是有意义的然而None是特殊空值
s = 8.0                         #把8.0置入变量“s”,8.0是浮点数
q = 9                           #把9置入变量“q”，9是整数
print s + q                     #变量“s”加上变量“q”，因为S是浮点数，所以结果也会是浮点数
print 9*7                       #打印出9*7的结果
w = "Hello"                     #把字符串“Hello”置入“w”中
r = '\n"Python"'                #“\n”是换行符
print w + r                     #变量“w”加上变量“r”
print s == q                    #布尔打印出变量s是否等于变量q，F否
print r"O(>.0)O"                #r" "是转义符，表示双引号里面的符号都默认不转义
print u"你要搞哪样？"           #u 是代表Unicode编码 这样才能正常显示汉字
txet = u"你好"
print "hello", txet or u"世界"  #打印出来的是hello 你好，左边的优先级大于右边
#↑↑↑数据类型与变量↑↑↑
eve = 50                        #把50置入变量“eve”中
if eve >= 40:                   #判断变量“eve”是否大于等于60
	print "pass"                #是大于等于60则打印“pass”
if not eve >= 40:               #eve不大于等于60
	print "no"                  #则打印“no”

ee = 60                         #变量“ee”中置入60
if ee >= 70:                    #判断“ee”是否大于等于70
	print "pass"                #判断为是，则打印“pass”
elif ee > 60:                   #则判断“ee”是否大于60
    print "haha"                #判断为是，则打印“haha”
else:                           #否则
	print "no"                  #打印“no”
#↑↑↑条件判断↑↑↑
t = (1,2,3,["laugh",87,"exe",90],5,)
print t
t[3][2] ='tell'
print t
#dict和set
d = {'A' : 50,'B' : 60,'C' : 80,'D' : 10}
print d['B']
d ['B'] = 70
print d
