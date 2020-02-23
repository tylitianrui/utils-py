# -*- coding: UTF-8 -*-
# author: tyltr


# [{'age': 9, 'name': 'Homer'}, {'age': 10, 'name': 'Bart'}]
#  排序
#  默认升序
def sor_list_dict(obj,key,reverse=False):

    l =sorted(obj,key=lambda obj:obj[key],reverse = reverse)
    return  l



if __name__ == '__main__':
    l = [{'age': 9, 'name': 'Homer'}, {'age': 10, 'name': 'Bart'}]
    l = sor_list_dict(l,"age")
    print(l)