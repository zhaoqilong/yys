#coding:utf-8
#MI5
#小米5的设备id
device_id = 'c84e662d'
size = '1920x1080'

#ver2 jpg位置


#组队按钮的阈值
team_win_mark_box_threshold = (0.5,0.2)
team_start_fighting_threshold = (1.0,0.1)
team_win_mark_drum_threshold = (0.9,0.1)

# team_start_fighting_threshold = (1.0742,0.0001)
# team_win_mark_drum_threshold = (0.8954,0.0001)


#单人胜利之后出现大鼓时候点击位置，防止时延影响点到不该点的位置
team_win_mark_drum_tap = {
    'y1':275,
    'y2':723,
    'x1':200,
    'x2':290
}

#胜利之后出现宝箱之后，点击位置，防止时延影响点到不该点的位置
team_win_mark_box_tap={
     'y1':275,
    'y2':723,
    'x1':200,
    'x2':290
}

team_failure_tap={
     'y1':275,
    'y2':723,
    'x1':200,
    'x2':290
}

#组队开始按钮
team_start_fighting = {
    'y1':867,
    'y2':934,
    'x1':1445,
    'x2':1684
}


#组队失败之后的位置坐标
team_failure = {
    'y1':125,
    'y2':264,
    'x1':617,
    'x2':792
}

#组队胜利之后的大鼓的位置坐标
team_win_mark_drum = {
    'y1':155,
    'y2':274,
    'x1':633,
    'x2':804
}

#胜利之后的宝箱的下半部分坐标
team_win_mark_box={
    'y1':879,
    'y2':936,
    'x1':804,
    'x2':1085
}