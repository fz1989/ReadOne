Server need api
===============
需要的一些个api，这个只是个大概，还有就是\ **看着不合理的可以直接改了**\""，目测后续还得加。。。P.S:偶就是不一次弄完，啦啦啦啦啦啦啦~

* check_usr_pwd(usr_id, usr_pwd):
    大概就是给用户usr_id和usr_pwd,看能不能成功登陆，返回个bool吧~

* check_usr_exist(usr_id):
    检测用户是不是存在

* regist_usr_account(usr_id, usr_pwd):
    注册用户，写入数据库

* get_all_usr_info():
    获取所有用户的信息,

* search_usr_info(usr_id):
    或得指定用户usr_id的的信息

* get_all_category(start, end):
    获取所有的分类的信息。。。。

* search_cate_items(cate_id):
    获取指定cate_id的所有item。。。

* usr_get_item(item_id):
    获得指定item的的内容

* update_usr_behavior(usr_id, cate_id, offset):
    指定用户的cate_id上的权值变化个offset

* get_item_cate(item_id):
    获得指定item的的cate_id

* update_follow(usr_id, friends_id):
    更新usr关注了friend

* follow_find(usr_id, friends_id):
    看usr是不是关注了friend

* add_friends(usr_id, friends_id):
    添加usr_id和friends_id是好友

* get_problem_by_item(item_id):
    或得指定item_id的相关问题信息

* get_problem_by_cate(cate_id):
    获得指定cate_id的相关问题信息

* get_problem_ralation_info(prob_id):
    获得指定prob_id的item_id和cate_id
