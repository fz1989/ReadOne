获取阅读条目
------------
post: 
  (UserID)

get: 
  a list (ItemID,PicIndex,TitleName,Abstract)

最新动态
-------
post:
  (UserID)

get: 
  (ItemID,PicIndex,TitleName,Abstract)

问答
----
post:
  (UserID)

get: 
  (ProblemID,ProContent)

挑战
----




成就  top10
-----------
post: 
  (UserID)

get: 
  a list (PicIndex,ProfileName,AchiPoints)

成就 all friends
----------------
post: 
  (UserID)

get: 
  (PicIndex,ProfileName)

点击阅读条目和HubTile
---------------------
post: 
  (UserID,ItemID)

get:
  (PicUrl,TitleName,SubTitleName,Time,Content)

编辑条目
--------
post: 
  (UserID,ItemID)

get: 
  None

点击人名
--------
post: 
  (UserID)

get: 
  (AchiDetailsItem,ItemPoints)
