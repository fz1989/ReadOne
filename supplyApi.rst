获取阅读条目
------------
post:
    UserID

get:
    a list (ItemID,PicIndex,TitleName,Abstract)

url:
    /recommend/

param:
    usr_id

dataType:
    [{'item_id':1, 'pic_idx': 1, 'title':'a', 'abstract':'b'}]

最新动态
-------
post:
    UserID

get:
    a list (ItemID,PicIndex,TitleName,Abstract)

url:
    /cate/sub/cate_id

param:
    None

dateType:
    [{'item_id':1, 'pic_idx':1,'title':'a', 'abstract':'b'}]

问答
----
post:
    UserID

get:
    ProblemID,ProContent

url:
    /competition/

param:
    usr_id

dateTpye:
    {'prob_id':1, 'text':'sdasdasd', 'question':{'a':1,'b':2,'c':3}, 'answer':'a'}

挑战
----

成就  top10
-----------
post:
    UserID

get:
    a list PicIndex,ProfileName,AchiPoints

成就 all friends
----------------
post:
    UserID

get:
    PicIndex,ProfileName



点击阅读条目和HubTile
---------------------
post:
    UserID,ItemID

get:
    PicUrl,TitleName,SubTitleName,Time,Content

编辑条目
--------
post:
    UserID,ItemID

get:
    None

点击人名
--------
post:
    UserID

get:
    AchiDetailsItem,ItemPoints
