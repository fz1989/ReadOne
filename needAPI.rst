Server need api
===============
需要的一些个api，这个只是个大概，还有就是\ **看着不合理的可以直接改了**\，目测后续还得加。。。P.S:偶就是不一次弄完，啦啦啦啦啦啦啦~

userCtl
-------

* regist_usr_account(usr_name, usr_pwd):
    注册用户，写入数据库

* check_usr_pwd(usr_name, usr_pwd):
    大概就是给用户usr_name和usr_pwd,看能不能成功登陆，返回个bool吧~

* check_usr_exist(usr_name):
    检测用户是不是存在

* get_all_usr_info():
    获取所有用户的信息

* search_usr_info(usr_name):
    获得指定用户usr_name的的信息
    这里需要的信息都有什么？关注列表？目录权值？

itemCtl
-------

* get_all_category():
    获取所有的分类的信息

* search_cate_items(cate_id):
    获取指定cate_id的所有item

* usr_get_item(item_id):
    获得指定item的的内容

* update_usr_behavior(usr_name, cate_id, offset):
    指定用户的cate_id上的权值变化个offset
    权值初始怎么设定？

* get_item_cate(item_id):
    获得指定item的cate_id

* get_problem_by_item(item_id):
    或得指定item_id的相关问题信息

* get_problem_by_cate(cate_id):
    获得指定cate_id的相关问题信息

* get_problem_ralation_info(prob_id):
    获得指定prob_id的item_id和cate_id

friendCtl
---------

* update_follow(usr_name, friends_name):
    更新usr关注了friend

* follow_find(usr_name, friends_name):
    看usr是不是关注了friend
