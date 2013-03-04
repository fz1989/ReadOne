# Create your views here.
import json
import math

def __init__(self, usr_id):
    '''
    init need recommend info with usr_id
    @param usr_id: user's name
    '''
    self.usr_id = usr_id
    self.all_usr_info = json.loads(get_all_usr_info())
    self.usr_info = json.loads(get_usr_info(usr_info))


def calc_usr_dist(usr_a, usr_b):
    '''
    @brief: calculate the difference between two usr's cate_vector
    @param usr_a: usr_a usr_a's cate_vector
    @param usr_b: usr_b's cate_vector
    @return: the difference between two vector
    '''

    vector_mul_sum = 0
    length_vector_a =  0
    length_vector_b = 0
    for value_a, value_b in usr_a, usr_b:
        vector_mul_sum += value_a * value_b
        length_vector_a += value_a * value_a
        length_vector_b += value_b * value_b
    return  vector_mul_sum / math.sqrt(length_vector_a) / math.sqrt(length_vector_b)

def get_recommend_by_average():
    '''
    @brief: when a user is a fresh man in use the system, use this to recommend items.
    @return: a list, which contains the recommend items id.
    '''
    tot_item_num = len(self.all_usr_info)
    ret_item = self.usr_info['cate_vector']
    return ret_item

def get_recommend_by_usrCF():
    ret_items = {}
    usr_dist_list = {}

    for other_usr in self.all_usr_info:
        if other_usr['usr_name'] != self.usr_info['usr_name']:
            dist = calc_usr_dist(self.usr_info['cate_vector'], other_usr['cate_vector'])
            usr_dist_list[other_usr['usr_name']] = dist

    sort(usr_dist_list.items(), key=lambda d: d[1])


def get_recommend_items():
    '''
    @brief: get recommend items by usr_id
    @param usr_id: a usr's regist id
    @return: the list of recommend items
    '''
    all_zero = True
    for key in self.usr_info['cate_vector']:
        if usr_info['cate_vector'][key] != 0:
            all_zero = False
            break

    if all_zero == True:
        return get_recommend_by_average()
    else:
        return get_recommend_by_usrCF()
