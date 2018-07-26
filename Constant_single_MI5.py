#coding:utf-8
#MI5
#小米5的设备id
device_id = 'c84e662d'
size = '1920x1080'

#ver2 jpg位置


#组队按钮的阈值
team_win_mark_box_threshold = (0.6890,0.0001)
team_start_fighting_threshold = (1.0742,0.0001)
team_win_mark_drum_threshold = (0.8954,0.0001)

#单人操作的阈值
single_win_mark_box_threshold = (1.4,0.1)
single_failure_threshold = (1.4,0.3)
single_challenge_btn_threshold = (0.9,0.1)

#其他阈值
net_lost_threshold = (0.9,0.1)

net_lost = {
    'y1':601,
    'y2':666,
    'x1':870,
    'x2':1045
}


#单人胜利之后出现大鼓时候点击位置，防止时延影响点到不该点的位置
win_mark_drum_tap2 = {
    'y1':275,
    'y2':723,
    'x1':200,
    'x2':290
}

#胜利之后出现宝箱之后，点击位置，防止时延影响点到不该点的位置
win_mark_box_tap2={
     'y1':275,
    'y2':723,
    'x1':200,
    'x2':290
}

single_failure_tap2={
     'y1':275,
    'y2':723,
    'x1':200,
    'x2':290
}

#组队开始按钮
team_start_fighting2 = {
    'y1':867,
    'y2':934,
    'x1':1445,
    'x2':1684
}


#组队失败之后的位置坐标
team_failure2 = {
    'y1':125,
    'y2':264,
    'x1':617,
    'x2':792
}

#组队胜利之后的大鼓的位置坐标
team_win_mark_drum2 = {
    'y1':155,
    'y2':274,
    'x1':633,
    'x2':804
}

#胜利之后的宝箱的下半部分坐标
team_win_mark_box2={
    'y1':879,
    'y2':936,
    'x1':804,
    'x2':1085
}






#ver 1 png

#胜利之后的大鼓的位置坐标
win_mark_drum = {
    'y1':149,
    'y2':286,
    'x1':632,
    'x2':826
}
#胜利之后的宝箱的下半部分坐标
win_mark_box={
    'y1':796,
    'y2':905,
    'x1':794,
    'x2':1093
}
#单人挑战按钮位置坐标
challenge_btn = {
    'y1':703,
    'y2':780,
    'x1':1335,
    'x2':1518
}
#单人失败之后的大鼓的位置坐标
single_failure = {
    'y1':195,
    'y2':423,
    'x1':604,
    'x2':872
}


#单人胜利之后出现大鼓时候点击位置，防止时延影响点到不该点的位置
win_mark_drum_tap = {
    'y1':87,
    'y2':953,
    'x1':180,
    'x2':330
}

#胜利之后出现宝箱之后，点击位置，防止时延影响点到不该点的位置
win_mark_box_tap={
    'y1':87,
    'y2':953,
    'x1':180,
    'x2':330
}

#胜利之后出现宝箱之后，点击位置，防止时延影响点到不该点的位置
single_failure_tap={
    'y1':87,
    'y2':953,
    'x1':180,
    'x2':330
}

#组队开始按钮
team_start_fighting = {
    'y1':862,
    'y2':933,
    'x1':1432,
    'x2':1685
}


#组队失败之后的位置坐标
team_failure = {
    'y1':107,
    'y2':303,
    'x1':603,
    'x2':802
}

#组队胜利之后的大鼓的位置坐标
team_win_mark_drum = {
    'y1':123,
    'y2':310,
    'x1':627,
    'x2':815
}

#组队胜利之后的宝箱的下半部分坐标
team_win_mark_box={
    'y1':881,
    'y2':943,
    'x1':783,
    'x2':1103
}
