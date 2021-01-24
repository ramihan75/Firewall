import re
from textwrap import wrap

def insert_zero_per_hextet(var):
    list_split = var.split(':')
    s = '' 
    for i in list_split:
        if i == '':
           s += '::' #  восстанавливаем '::', если он был
        else:
           s += i.rjust(4, '0') # заполняем нолями каждый хекстет, если битов меньше, чем 4
           #    print(s)
    if var.find('::') != -1: # вызывает функцию, если находит соответствие '::'
        return insert_zero_between_hextet(s)
    else:
        return s
    
def insert_zero_between_hextet(var):
    list_split = var.split('::')
    #   half1 = re.findall(r'\w+',list_split[0])
    #   half2 = re.findall(r'\w+',list_split[1])
    half1 = ''.join(list_split[0])
    half2 = ''.join(list_split[1])
    remain = 32 - len(half1) - len(half2)
    return half1 + '0' * remain + half2
   

def insert_zero_result(var):
    if len(var) < 39:
        return insert_zero_per_hextet(var) # вызывает функцию, если длина адреса ipv6 меньше 39
    else:
        return var.replace(':', '')
    
result_hex = insert_zero_result('fff0:20:1:ffff:0100::1') # подаем ipv6 адрес с любыми формами сокращенного вида   
print(result_hex)    

result_bin = (bin(int('1'+result_hex, 16))[3:])
#print(result_bin)
result_bin_wrap = ':'.join(wrap(result_bin, width=16))
print(result_bin_wrap) # печать ipv6 адреса в двоичной форме с разделителем :


config = '10.10.10.1/32'
config = re.sub(r"([0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3})(\/32)", r"\1 255.255.255.255", config)
print(config)




