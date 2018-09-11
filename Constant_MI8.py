#coding:utf-8
#MI8

device_id = '61e08bf1'
size = '2248x1080'

team_start_fighting_threshold = (1.2,0.1)
team_win_mark_drum_threshold = (0.9,0.4)
team_win_mark_box_threshold = (1,0.4)
reward_threshold = (1, 0.5)
later_btn_threshold = (1, 0.5)
damo_threshold = (2, 1)



#组队胜利之后出现大鼓时候点击位置，防止时延影响点到不该点的位置
team_win_mark_drum_tap = {
    'y1':346,
    'y2':740,
    'x1':300,
    'x2':350
}

#组队胜利之后出现宝箱之后，点击位置，防止时延影响点到不该点的位置
team_win_mark_box_tap={
    'y1':346,
    'y2':740,
    'x1':300,
    'x2':350
}

#组队胜利之后出现宝箱之后，点击位置，防止时延影响点到不该点的位置
team_single_failure_tap={
      'y1':346,
    'y2':740,
    'x1':300,
    'x2':350
}


#组队开始按钮
team_start_fighting = {
    'y1':870,
    'y2':929,
    'x1':1670,
    'x2':1896
}

#组队失败之后的位置坐标
team_failure = {
    'y1':139,
    'y2':248,
    'x1':836,
    'x2':995
}

#组队胜利之后的大鼓的位置坐标
team_win_mark_drum = {
    'y1':156,
    'y2':271,
    'x1':850,
    'x2':1030
}

#胜利之后的宝箱的下半部分坐标
team_win_mark_box={
    'y1':870,
    'y2':923,
    'x1':1020,
    'x2':1323
}

reward={
    'y1':241,
    'y2':289,
    'x1':1064,
    'x2':1362
}

reward_tap={
    'y1':751,
    'y2':817,
    'x1':1467,
    'x2':1513
}

later_btn={
    'y1':597,
    'y2':672,
    'x1':826,
    'x2':1005
}

later_btn_tap={
     'y1':597,
    'y2':672,
    'x1':826,
    'x2':1005
}

team_damo = {
    'y1': 434,
    'y2': 667,
    'x1': 1057,
    'x2': 1294
}

team_damo_tap = {
    'y1': 434,
    'y2': 667,
    'x1': 1057,
    'x2': 1294
}

