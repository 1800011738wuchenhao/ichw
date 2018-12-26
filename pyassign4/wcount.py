#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Wuchenhao"
__pkuid__  = "1800011738"
__email__  = "wuchenhao@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import string
import urllib


def wcount(lines, topn = 10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    count_dict = {}
    
    for k in string.punctuation:
        lines = lines.replace(k , ' ')    #去掉了标点
    
    for i in lines.split():    #分成单词
        if not(i in count_dict):
            count_dict[i] = 1
        else:
            count_dict[i] += 1    #用字典统计次数
    
    count_list = [u for u in count_dict.items()]
    for j in range(len(count_list)):
        count_list[j] = list(count_list[j])
        count_list[j].reverse()
    count_list.sort()
    count_list.reverse()    #按次数倒序放入列表
    
    n = 1
    while n <= topn:
        print(str(count_list[n-1][1]) + ':' + str(count_list[n-1][0]))
        n += 1    #输出前topn的单词


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    else:
        url = sys.argv[1]    #获得输入的网址
        if len(sys.argv) >= 3 and type(eval(sys.argv[2])) == int:
            topn = int(sys.argv[2])   #获得topn
            if topn <= 0:
                print('输入的topn必须是正整数，不能是{}'.format(sys.argv[2]))
                topn = 0    #给topn<=0时
        elif len(sys.argv) == 2:
            topn = 10    #未给定topn时
        elif type(eval(sys.argv[2])) != int:
            print('输入的topn必须是正整数，不能是{}'.format(sys.argv[2]))    #给定非法topn时
            
        try:
            txt = urlopen(url)    #打开网页获得txt文件
            txt_bytes = txt.read()    #得到字节流形式文本
            txt.close()    #关掉网页
            txt_str = txt_bytes.decode('UTF-8','strict')    #字节流解码为字符串形式
            txt_lower = txt_str.lower()    #都换为小写以方便统计
            wcount(txt_lower,topn)    #统计次数输出前topn

        except urllib.error.HTTPError:    
            print(sys.exc_info()[1])    

        except urllib.error.URLError:    
            print(sys.exc_info()[1])
            
        except ValueError:
            print('输入的网址格式不正确')    #处理了一部分错误
