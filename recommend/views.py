# Create your views here.
import json
import math

'''
@author: fz1989
'''


def search_cate_items(cate_id):
    if cate_id == '1':
        return [1, 2, 3, 4, 5, 6]
    elif cate_id == '2':
        return [7, 8, 9, 10, 11, 12]
    else:
        return [13, 14, 15, 16, 17, 18]


def get_all_usr_info():
    return json.dumps({
                    'fz': {'usr_name': 'fz', 'cate_vector': { '1': 0, '2': 0, '3': 0 }, 'items': []},
                    'dc': {'usr_name': 'dc', 'cate_vector': { '1': 2, '2': 3, '3': 1 }, 'items': [1, 2, 7, 8, 9, 13]},
                  'zmy': {'usr_name': 'zmy', 'cate_vector': { '1': 3, '3': 3, '2': 0 }, 'items': [4, 5, 6, 10, 11, 12]}
                     })


def get_usr_info(usr_id):
    if usr_id == 'fz':
        return json.dumps( {'usr_name': 'fz', 'cate_vector': { '1': 0, '2': 0, '3': 0 }, 'items': []} )
    else:
        return json.dumps( {'usr_name': 'dc', 'cate_vector': { '1': 2, '2': 3, '3': 1 }, 'items': [1, 2, 7, 8, 9, 13]})

class recommend:
    def __init__(self, usr_id):
        '''
        init need recommend info with usr_id
        @param usr_id: user's name
        @type usr_id: string
        '''
        self.usr_id = usr_id
        self.all_usr_info = json.loads(get_all_usr_info())
        self.usr_info = json.loads(get_usr_info(self.usr_id))


    def calc_usr_dist(self, usr_a, usr_b):
        '''
        @brief: calculate the difference between two usr's cate_vector
        @param usr_a: usr_a usr_a's cate_vector
        @type usr_a: dict
        @param usr_b: usr_b's cate_vector
        @type usr_b: dict
        @return: the difference between two vector
        @rtype: double
        '''

        vector_mul_sum = 0
        length_vector_a = 0
        length_vector_b = 0
        for key_a in usr_a:
            key_b = key_a
            vector_mul_sum += usr_a[key_a] * usr_b[key_b]
            length_vector_a += usr_a[key_a] * usr_a[key_a]
            length_vector_b += usr_b[key_b] * usr_b[key_b]
        if length_vector_a == 0 or length_vector_b == 0:
            return 0
        return  vector_mul_sum / math.sqrt(length_vector_a) / math.sqrt(length_vector_b)


    def get_items_by_cate_vector(self, cate_vector):
        '''
        @brief: calc the item with the greedy algotithm,first choose the max value 
        int the vector and find the recommend items which the usr hadn't read before.
        if the num of items reachs the number of we expect,we will stop.Otherwise, we find
        the next bigger value to do the samething above untill we get expect items or there is no avaliable items.
        @param cate_vector
        @return: a list,with all the items
        '''
        sorted_cate_vector =  sorted(cate_vector.items(), key=lambda cate_vector: cate_vector[1])
        sorted_cate_vector.reverse()
        ret_items = []
        for (cate_id, cate_value) in sorted_cate_vector:
            list_read_items = list(set(search_cate_items(cate_id)).difference(set(self.usr_info['items'])))
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
        tot_usr_num = len(self.all_usr_info)
        cate_vector = self.usr_info['cate_vector']
        for other_usr in self.all_usr_info:
            if other_usr != self.usr_info['usr_name']:
                for cate_id in self.all_usr_info[other_usr]['cate_vector']:
                    cate_vector[cate_id] = cate_vector[cate_id] + self.all_usr_info[other_usr]['cate_vector'][cate_id]
        for cate_id in cate_vector:
            cate_vector[cate_id] /= (tot_usr_num - 1.0)
        return self.get_items_by_cate_vector(cate_vector)


    def get_recommend_by_usrCF(self):
        '''
        @brief: use userCF rules to recommend
        @return: a list, which contains the recommend items id.
        '''
        usr_dist_list = {}
        for other_usr in self.all_usr_info:
            if other_usr != self.usr_info['usr_name']:
                dist = self.calc_usr_dist(self.usr_info['cate_vector'], self.all_usr_info[other_usr]['cate_vector'])
                usr_dist_list[other_usr] = dist

        sorted_dist_list = sorted(usr_dist_list.items(), key=lambda usr_dist_list: usr_dist_list[1])
        sorted_dist_list.reverse()
        if len(usr_dist_list) > 10:
            sorted_dist_list = sorted(usr_dist_list.items(), key=lambda usr_dist_list: usr_dist_list[1])[0:10]
        '''
        @note: get top 10 usr,to calc the cate_vector with their dist and then call get_items_by_cate_vector
        '''
        tot_usr_cnt = 0
        tot_usr_sum = 1
        cate_vector = self.usr_info['cate_vector']
        sorted_dist_list.reverse
        for top_usr_name, top_usr_dist in sorted_dist_list:
            if tot_usr_cnt == 10:
                break
            for cate_id in self.all_usr_info[top_usr_name]['cate_vector']:
                cate_vector[cate_id] = cate_vector[cate_id] + (top_usr_dist) * self.all_usr_info[top_usr_name]['cate_vector'][cate_id]
                tot_usr_sum = tot_usr_sum + top_usr_dist
                tot_usr_cnt = tot_usr_cnt + 1

        for cate_id in cate_vector:
            cate_vector[cate_id] /= tot_usr_sum
        print cate_vector
        return self.get_items_by_cate_vector(cate_vector)


    def get_recommend_items(self):
        '''
        @brief: get recommend items by usr_id. if the usr is his first time to use our software we use the
                average recommendation,othewise,we will use the usr_CF to do the recommendation.
        @param usr_id: a usr's regist id
        @return: the list of recommend items
        '''
        all_zero = True
        for key in self.usr_info['cate_vector']:
            if self.usr_info['cate_vector'][key] != 0:
                all_zero = False
                break
        if all_zero == True:
            return self.get_recommend_by_average()
        else:
            return self.get_recommend_by_usrCF()
