#! /user/bin/env python
#coding=utf-8
import json
import math
from userCtl.models import *
from itemCtl.models import *
'''
@author: fz1989
'''


def search_cate_items(cate_id):
    return get_cate(cate_id)[1]


def get_all_user_info():
    ret = {}
    user_name_list = get_all_user_name()
    for user_name in user_name_list:
        user_info = get_user(user_name)
        ret[user_info[0]] = {'user_name': user_info[0], 'cate_vector': user_info[5], 'items': user_info[4]}
    return json.dumps(ret)


def get_user_info(user_id):
    user_info = get_user(user_id)
    return json.dumps( {'user_name': user_info[0], 'cate_vector': user_info[5], 'items': user_info[4]})

class recommend:
    def __init__(self, user_id):
        '''
        init need recommend info with user_id
        @param user_id: user's name
        @type user_id: string
        '''
        self.user_id = user_id
        self.all_user_info = json.loads(get_all_user_info())
        self.user_info = json.loads(get_user_info(self.user_id))


    def calc_user_dist(self, user_a, user_b):
        '''
        @brief: calculate the difference between two user's cate_vector
        @param user_a: user_a user_a's cate_vector
        @type user_a: dict
        @param user_b: user_b's cate_vector
        @type user_b: dict
        @return: the difference between two vector
        @rtype: double
        '''

        vector_mul_sum = 0
        length_vector_a = 0
        length_vector_b = 0
        for key_a in user_a:
            key_b = key_a
            vector_mul_sum += user_a[key_a] * user_b[key_b]
            length_vector_a += user_a[key_a] * user_a[key_a]
            length_vector_b += user_b[key_b] * user_b[key_b]
        if length_vector_a == 0 or length_vector_b == 0:
            return 0
        return  vector_mul_sum / math.sqrt(length_vector_a) / math.sqrt(length_vector_b)


    def get_items_by_cate_vector(self, cate_vector):
        '''
        @brief: calc the item with the greedy algotithm,first choose the max value 
        int the vector and find the recommend items which the user hadn't read before.
        if the num of items reachs the number of we expect,we will stop.Otherwise, we find
        the next bigger value to do the samething above untill we get expect items or there is no avaliable items.
        @param cate_vector
        @return: a list,with all the items
        '''
        sorted_cate_vector =  sorted(cate_vector.items(), key=lambda cate_vector: cate_vector[1])
        sorted_cate_vector.reverse()
        ret_items = []
        for (cate_id, cate_value) in sorted_cate_vector:
            list_read_items = list(set(search_cate_items(cate_id)).difference(set(self.user_info['items'])))
            ret_items.extend(list_read_items)
            ret_items.sort()
            if len(ret_items) > 10:
                ret_items = ret_items[0:10]
                break
        return ret_items;

    def get_recommend_by_average(self):
        '''
        @brief: when a user is a fresh man in using the system, use this to recommend items.
        @return: a list, which contains the recommend items id.
        '''
        tot_user_num = len(self.all_user_info)
        cate_vector = self.user_info['cate_vector']
        for other_user in self.all_user_info:
            if other_user != self.user_info['user_name']:
                for cate_id in self.all_user_info[other_user]['cate_vector']:
                    cate_vector[cate_id] = cate_vector[cate_id] + self.all_user_info[other_user]['cate_vector'][cate_id]
        for cate_id in cate_vector:
            cate_vector[cate_id] /= (tot_user_num - 1.0)
        return self.get_items_by_cate_vector(cate_vector)


    def get_recommend_by_userCF(self):
        '''
        @brief: use userCF rules to recommend
        @return: a list, which contains the recommend items id.
        '''
        user_dist_list = {}
        for other_user in self.all_user_info:
            if other_user != self.user_info['user_name']:
                dist = self.calc_user_dist(self.user_info['cate_vector'], self.all_user_info[other_user]['cate_vector'])
                user_dist_list[other_user] = dist

        sorted_dist_list = sorted(user_dist_list.items(), key=lambda user_dist_list: user_dist_list[1])
        sorted_dist_list.reverse()
        if len(user_dist_list) > 10:
            sorted_dist_list = sorted(user_dist_list.items(), key=lambda user_dist_list: user_dist_list[1])[0:10]
        '''
        @note: get top 10 user,to calc the cate_vector with their dist and then call get_items_by_cate_vector
        '''
        tot_user_cnt = 0
        tot_user_sum = 1
        cate_vector = self.user_info['cate_vector']
        sorted_dist_list.reverse
        for top_user_name, top_user_dist in sorted_dist_list:
            if tot_user_cnt == 10:
                break
            for cate_id in self.all_user_info[top_user_name]['cate_vector']:
                cate_vector[cate_id] = cate_vector[cate_id] + (top_user_dist) * self.all_user_info[top_user_name]['cate_vector'][cate_id]
                tot_user_sum = tot_user_sum + top_user_dist
                tot_user_cnt = tot_user_cnt + 1

        for cate_id in cate_vector:
            cate_vector[cate_id] /= tot_user_sum
        print cate_vector
        return self.get_items_by_cate_vector(cate_vector)


    def get_recommend_items(self):
        '''
        @brief: get recommend items by user_id. if the user is his first time to use our software we use the
                average recommendation,othewise,we will use the user_CF to do the recommendation.
        @param user_id: a user's regist id
        @return: the list of recommend items
        '''
        all_zero = True
        for key in self.user_info['cate_vector']:
            if self.user_info['cate_vector'][key] != 0:
                all_zero = False
                break
        if all_zero == True:
            return self.get_recommend_by_average()
        else:
            return self.get_recommend_by_userCF()
