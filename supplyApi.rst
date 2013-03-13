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
    [{'item_id':1, 'item_pic_idx': 1, 'title':'a', 'abstract':'b'}]

status:
    done

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
    [{'item_id':1, 'item_pic_idx':1,'title':'a', 'abstract':'b'}]

status:
    done
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

status:
    done

挑战
----

成就  top10
-----------
post:
    UserID

get:
    a list PicIndex,ProfileName,AchiPoints

url:
    /rank/

param:
    usr_id

dataType:
    [{'usr_pic_idx':1, 'usr_id':'狄仁杰', 'score':15}]

status:
    done

成就 all friends
----------------
post:
    UserID

get:
    PicIndex,ProfileName

url:
    /friends/show

param:
    usr_id

dataType:
    [{'usr_pic_idx':1, 'usr_id':'狄仁杰'}]

status:
    done


点击阅读条目和HubTile
---------------------
post:
    UserID,ItemID

get:
    PicUrl,TitleName,SubTitleName,Time,Content

url:
    /item/

param:
    usr_id, item_id

dataType:
    {'item_id':1, 'pic_url':'www.duomaomao.com', 'title':'fz','sub_title':'duo','text':'nimeide',}

status:
    done

编辑条目
--------
post:
    UserID,ItemID

get:
    None

url:
    /item/edit

param:
    usr_id, item_id, text

status:
    done

点击人名
--------
post:
    UserID

get:
   a list AchiDetailsItem,ItemPoints

url:
    /rank/arch/

param:
    usr_id

dataType:
    [{'arch_id':'狄仁杰', 'arch_score':'30'}]
