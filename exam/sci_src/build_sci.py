import math, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, '../1학년_수학_시험지.html') if os.path.exists(os.path.join(HERE, '../1학년_수학_시험지.html')) else '/home/user/Hyun/exam/1학년_수학_시험지.html'
OUT = os.path.join(os.path.dirname(BASE), '1학년_과학_시험지.html')

def T(xx, yy, s, size=10.5, anchor='middle', extra=''):
    size = round(size*1.22, 1)
    return f'<text x="{xx:.1f}" y="{yy:.1f}" font-size="{size}" text-anchor="{anchor}"{extra}>{s}</text>'
def L(x1, y1, x2, y2, w=1.2, dash=False, col='#000'):
    d = ' stroke-dasharray="3,2"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}"{d}/>'
def P(pts, fill='none', w=1.2, dash=False, col='#000'):
    d = ' stroke-dasharray="3,2"' if dash else ''
    return f'<polyline points="{" ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)}" fill="{fill}" stroke="{col}" stroke-width="{w}"{d}/>'
def R(x, y, w, h, fill='none', sw=1.2):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" stroke="#000" stroke-width="{sw}"/>'
def C(x, y, r, fill='#555'):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="#000" stroke-width="0.6"/>'
def arrow(x1, y1, x2, y2, w=1.6):
    ang = math.atan2(y2 - y1, x2 - x1); h = 7
    p1 = (x2 - h*math.cos(ang - 0.4), y2 - h*math.sin(ang - 0.4)); p2 = (x2 - h*math.cos(ang + 0.4), y2 - h*math.sin(ang + 0.4))
    return L(x1, y1, x2, y2, w) + f'<polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"/>'
def spring(x, y1, y2, coils=10, wid=7):
    pts = [(x, y1)]; n = coils*2; seg = (y2 - y1 - 8) / n
    for i in range(n):
        pts.append((x + (wid if i % 2 == 0 else -wid), y1 + 4 + seg*(i + 0.5)))
    pts.append((x, y2))
    return P(pts, w=1.1)
def svg(w, h, body):
    mm = min(w*0.245, 72)
    return f'<div class="pic"><svg viewBox="0 0 {w} {h}" style="width:{mm:.1f}mm" font-family="Gulim, sans-serif">{body}</svg></div>'
def opts(items, cols=3):
    cls = {3: 'opts', 2: 'opts c2', 1: 'opts c1', 5: 'opts c5'}[cols]
    return f'<div class="{cls}">' + ''.join(f'<div>{"①②③④⑤"[i]} {t}</div>' for i, t in enumerate(items)) + '</div>'
def bogi(*lines):
    return '<div class="bogi">' + ''.join(f'<p>{l}</p>' for l in lines) + '</div>'
def tbl(head, rows):
    h = ''.join(f'<th>{x}</th>' for x in head)
    r = ''.join('<tr>' + ''.join(f'<td>{x}</td>' for x in row) + '</tr>' for row in rows)
    return f'<table class="dt"><tr>{h}</tr>{r}</table>'
def otbl(head, rows):
    h = '<th></th>' + ''.join(f'<th>{x}</th>' for x in head)
    r = ''.join(f'<tr><td>{"①②③④⑤"[i]}</td>' + ''.join(f'<td>{x}</td>' for x in row) + '</tr>' for i, row in enumerate(rows))
    return f'<table class="ot">{h}{r}</table>'
NOT = '<span class="u"><b>않은</b></span>'
ALL = '<span class="u"><b>모두</b></span>'

def curve(xs_ys, ox, oy, sx, sy):
    return [(ox + a*sx, oy - b*sy) for a, b in xs_ys]
def graph_axes(ox, oy, w, h, xl, yl):
    return (arrow(ox, oy, ox + w, oy, 1.1) + arrow(ox, oy, ox, oy - h, 1.1) +
            T(ox + w, oy + 30, xl, 9, 'end') + T(ox + 7, oy - h + 10, yl, 9, 'start') + T(ox - 6, oy + 12, '0', 9))

Q = []
def add(stem, pts, body=''):
    Q.append((stem, pts, body))

# 1
add('확산의 예로 옳지 ' + NOT + ' 것은?', 3, opts([
    '방 안에 뿌린 향수 냄새가 방 전체로 퍼진다.', '물에 떨어뜨린 잉크가 물 전체로 퍼져 나간다.',
    '빵집 앞을 지나가면 빵 굽는 냄새가 난다.', '햇볕이 좋은 날 젖은 빨래가 마른다.', '전자 모기향을 켜 두면 모기향 성분이 방 안에 퍼진다.'], 1))
# 2
add('물질의 세 가지 상태에 대한 설명으로 옳은 것은?', 3, opts([
    '고체는 담는 그릇에 따라 모양이 변한다.', '액체는 담는 그릇에 따라 부피가 변한다.',
    '기체는 입자 사이의 인력이 가장 강하다.', '액체는 기체보다 입자 사이의 거리가 멀다.', '기체는 담는 용기에 따라 모양과 부피가 모두 변한다.'], 1))
# 3
add('고체가 액체로 변하는 상태 변화는?', 3, opts(['융해', '응고', '기화', '액화', '승화']))
# 4
add('힘을 화살표로 나타낼 때, 화살표의 길이가 나타내는 것은?', 3, opts(['힘의 방향', '힘의 크기', '힘의 작용점', '물체의 질량', '물체의 속력'], 2))
# 5
add('&lt;보기&gt;에서 과학에서 말하는 힘이 작용한 경우의 개수는?', 3,
    bogi('ㄱ. 축구공을 발로 차서 멀리 보냈다.', 'ㄴ. 밤늦게까지 숙제를 하느라 힘이 들었다.', 'ㄷ. 찰흙을 손으로 눌러 모양을 바꾸었다.',
         'ㄹ. 친구에게 힘내라고 응원하였다.', 'ㅁ. 굴러오는 공을 손으로 잡아 멈추게 하였다.') +
    opts(['1개', '2개', '3개', '4개', '5개']))
# 6
add('지구에서 질량이 60 kg인 사람이 달에 갔을 때, 달에서 이 사람의 질량과 무게는? (단, 지구에서 질량이 1 kg인 물체의 무게는 9.8 N이고, 달의 중력은 지구의 <span class="fr"><span>1</span><span>6</span></span>이다.)', 3,
    otbl(['질량', '무게'], [['10 kg', '98 N'], ['60 kg', '98 N'], ['60 kg', '588 N'], ['10 kg', '588 N'], ['60 kg', '60 N']]))
# 7
add('증발에 대한 설명으로 옳은 것은?', 3, opts([
    '액체 표면에서 입자가 기체로 변하는 현상이다.', '액체 내부에서만 일어난다.', '온도가 낮을수록 잘 일어난다.',
    '바람이 불지 않을 때 더 잘 일어난다.', '입자가 운동하지 않을 때 일어난다.'], 1))
# 8 particle boxes
def box(x, kind):
    b = R(x, 10, 62, 62, sw=1.1); import random
    if kind == 's':
        for i in range(5):
            for j in range(5):
                b += C(x + 9 + i*11, 19 + j*11, 4)
    elif kind == 'l':
        pts = [(9, 50), (20, 56), (31, 52), (42, 57), (53, 50), (13, 40), (25, 43), (37, 40), (49, 44), (18, 30), (32, 31), (45, 30), (54, 38), (10, 60), (40, 62)]
        for p in pts: b += C(x + p[0], 10 + p[1], 4)
    else:
        for p in [(12, 14), (45, 20), (28, 38), (52, 50), (14, 54), (35, 12)]: b += C(x + p[0], 10 + p[1], 4)
    return b
body = box(8, 's') + box(90, 'l') + box(172, 'g') + T(39, 88, '(가)') + T(121, 88, '(나)') + T(203, 88, '(다)')
add('그림은 물질의 세 가지 상태를 입자 모형으로 나타낸 것이다. (가) → (나)로 변하는 상태 변화의 예는?', 3,
    svg(242, 96, body) + opts(['얼음이 녹아 물이 된다.', '주전자의 물이 끓는다.', '드라이아이스의 크기가 작아진다.', '새벽에 풀잎에 이슬이 맺힌다.', '촛농이 흘러내리다가 굳는다.'], 1))
# 9
add('물질의 상태가 변할 때 변하지 <span class="u"><b>않는</b></span> 것만을 &lt;보기&gt;에서 있는 대로 고른 것은?', 3,
    bogi('ㄱ. 입자의 종류', 'ㄴ. 입자의 개수', 'ㄷ. 입자의 배열', 'ㄹ. 물질의 질량', 'ㅁ. 물질의 부피') +
    opts(['ㄱ, ㄴ', 'ㄷ, ㅁ', 'ㄱ, ㄴ, ㄹ', 'ㄱ, ㄷ, ㄹ', 'ㄴ, ㄹ, ㅁ']))
# 10
add('마찰력을 크게 하여 이용하는 예만을 &lt;보기&gt;에서 있는 대로 고른 것은?', 3,
    bogi('ㄱ. 눈길에서 자동차 바퀴에 체인을 감는다.', 'ㄴ. 삐걱거리는 문의 경첩에 윤활유를 바른다.', 'ㄷ. 운동화 바닥에 울퉁불퉁한 홈을 만든다.',
         'ㄹ. 볼링장 레인에 기름을 칠한다.', 'ㅁ. 얼어붙은 길에 모래를 뿌린다.') +
    opts(['ㄱ, ㄴ', 'ㄱ, ㄷ, ㅁ', 'ㄴ, ㄹ', 'ㄴ, ㄷ, ㄹ', 'ㄷ, ㄹ, ㅁ']))
# 11
add('탄성력에 대한 설명으로 옳지 ' + NOT + ' 것은?', 3, opts([
    '변형된 물체가 원래 모양으로 되돌아가려는 힘이다.', '물체를 변형시킨 힘과 반대 방향으로 작용한다.',
    '물체가 많이 변형될수록 탄성력이 크다.', '활, 트램펄린, 장대높이뛰기 등에 이용된다.', '탄성력은 물체를 변형시킨 힘보다 항상 크다.'], 1))
# 12
add('중력에 대한 설명으로 옳은 것은?', 3, opts([
    '지구 중심 방향으로 작용한다.', '물체의 질량이 클수록 작아진다.', '달에서는 작용하지 않는다.',
    '중력의 크기를 나타내는 단위는 kg이다.', '물체가 공중에 떠 있을 때만 작용한다.'], 1))
# 13
add('열에너지를 <b>흡수</b>하는 상태 변화가 일어나는 현상만을 &lt;보기&gt;에서 있는 대로 고른 것은?', 4,
    bogi('ㄱ. 손에 든 아이스크림이 녹아 흘러내린다.', 'ㄴ. 추운 날 따뜻한 실내로 들어오면 안경이 뿌옇게 흐려진다.',
         'ㄷ. 소나기가 내리기 전에는 날씨가 후텁지근하다.', 'ㄹ. 더운 날 개가 혀를 내밀고 헐떡거린다.',
         'ㅁ. 휴대용 버너를 사용하고 난 뒤 부탄가스 통을 만져 보면 차갑다.') +
    opts(['ㄱ, ㄴ', 'ㄱ, ㄹ', 'ㄴ, ㅁ', 'ㄱ, ㄹ, ㅁ', 'ㄴ, ㄷ, ㄹ']))
# 14 triangle
Sx, Sy = 50, 120; Lx, Ly = 210, 120; Gx, Gy = 130, 25
def bub(x, y, t):
    return f'<circle cx="{x}" cy="{y}" r="19" fill="#eee" stroke="#000" stroke-width="1"/>' + T(x, y + 5, t, 10)
def off(p1, p2, d):
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]; n = math.hypot(dx, dy); ux, uy = dx/n, dy/n; nx, ny = -uy, ux
    a = (p1[0] + ux*24 + nx*d, p1[1] + uy*24 + ny*d); b = (p2[0] - ux*24 + nx*d, p2[1] - uy*24 + ny*d)
    return a, b, ((a[0] + b[0])/2 + nx*d*1.6, (a[1] + b[1])/2 + ny*d*1.6)
body = ''
for (p1, p2, lab) in [((Sx, Sy), (Lx, Ly), 'A'), ((Lx, Ly), (Sx, Sy), 'B'), ((Lx, Ly), (Gx, Gy), 'C'), ((Gx, Gy), (Lx, Ly), 'D'), ((Gx, Gy), (Sx, Sy), 'E'), ((Sx, Sy), (Gx, Gy), 'F')]:
    a, b, m = off(p1, p2, 6)
    body += arrow(*a, *b, 1.4) + T(m[0], m[1] + 5, lab, 10)
body += bub(Sx, Sy, '고체') + bub(Lx, Ly, '액체') + bub(Gx, Gy, '기체')
add('그림은 물질의 상태 변화를 나타낸 것이다. A~F에 해당하는 예로 옳지 ' + NOT + ' 것은?', 4,
    svg(260, 148, body) + opts(['A : 손에 든 아이스크림이 녹는다.', 'B : 흘러내린 촛농이 굳는다.', 'C : 젖은 머리카락이 마른다.',
                                 'D : 차가운 컵 표면에 물방울이 맺힌다.', 'E : 드라이아이스의 크기가 점점 작아진다.'], 1))
# 15
add('표는 1기압에서 물질 A~C의 녹는점과 끓는점을 나타낸 것이다. 이에 대한 설명으로 옳은 것만을 &lt;보기&gt;에서 있는 대로 고른 것은?', 4,
    tbl(['물질', '녹는점(℃)', '끓는점(℃)'], [['A', '−39', '357'], ['B', '80', '218'], ['C', '−117', '78']]) +
    bogi('ㄱ. 25 ℃에서 B는 고체 상태이다.', 'ㄴ. 25 ℃에서 액체 상태인 물질은 1가지이다.', 'ㄷ. 100 ℃에서 C는 기체 상태이다.', 'ㄹ. 어는점이 가장 낮은 물질은 A이다.') +
    opts(['ㄱ, ㄴ', 'ㄴ, ㄹ', 'ㄱ, ㄷ', 'ㄷ, ㄹ', 'ㄱ, ㄷ, ㄹ']))
# 16 forces on a box
body = (L(10, 70, 250, 70, 1.4) + R(100, 35, 60, 35, '#ddd') + arrow(160, 46, 220, 46) + T(232, 50, '8 N', 10, 'start') +
        arrow(160, 60, 197, 60) + T(208, 64, '5 N', 10, 'start') + arrow(100, 52, 75, 52) + T(66, 56, '3 N', 10, 'end'))
add('그림과 같이 수평면 위의 물체에 세 힘이 동시에 작용할 때, 물체에 작용하는 합력의 크기와 방향은?', 4,
    svg(260, 82, body) + opts(['0 N', '10 N, 오른쪽', '10 N, 왼쪽', '6 N, 오른쪽', '16 N, 오른쪽'], 2))
# 17 spring graph
ox, oy = 40, 130; sx, sy = 6, 9
body = graph_axes(ox, oy, 200, 125, '추의 무게(N)', '늘어난 길이(cm)')
body += P(curve([(0, 0), (30, 12)], ox, oy, sx, sy), w=1.5)
for wv, lv in [(10, 4), (20, 8)]:
    X, Y = ox + wv*sx, oy - lv*sy
    body += L(X, Y, X, oy, dash=True) + L(X, Y, ox, Y, dash=True) + T(X, oy + 13, str(wv), 9) + T(ox - 5, Y + 4, str(lv), 9, 'end')
add('그래프는 어떤 용수철에 매단 추의 무게에 따라 용수철이 늘어난 길이를 나타낸 것이다. 이 용수철의 원래 길이가 15 cm일 때, 무게가 25 N인 추를 매달았을 때 용수철의 전체 길이는?', 4,
    svg(260, 168, body) + opts(['10 cm', '15 cm', '20 cm', '25 cm', '30 cm']))
# 18 buoyancy
def scale(x, top, bot, inwater):
    s = L(x - 40, top, x + 40, top, 3) + spring(x, top, bot - 18, 9, 6) + R(x - 14, bot - 18, 28, 26, '#888')
    if inwater:
        s += P([(x - 34, bot - 46), (x - 34, bot + 22), (x + 34, bot + 22), (x + 34, bot - 46)], w=1.2)
        s += f'<rect x="{x - 33}" y="{bot - 34}" width="66" height="55" fill="#cfe3f5" opacity="0.7"/>'
    return s
body = scale(70, 12, 112, False) + scale(200, 12, 112, True) + T(70, 150, '공기 중: 50 N', 10) + T(200, 150, '물속: 32 N', 10)
add('그림과 같이 용수철저울에 물체를 매달아 공기 중과 물속에서 각각 무게를 측정하였다. 이에 대한 설명으로 옳은 것만을 &lt;보기&gt;에서 있는 대로 고른 것은? (단, 물체는 물에 완전히 잠겨 있다.)', 4,
    svg(270, 158, body) +
    bogi('ㄱ. 물체에 작용하는 부력의 크기는 18 N이다.', 'ㄴ. 부력은 중력과 반대 방향인 위쪽으로 작용한다.',
         'ㄷ. 물속에서 물체에 작용하는 중력의 크기는 32 N이다.', 'ㄹ. 물체를 완전히 잠긴 상태로 더 깊이 넣어도 부력의 크기는 같다.') +
    opts(['ㄱ, ㄴ', 'ㄱ, ㄷ', 'ㄴ, ㄷ, ㄹ', 'ㄱ, ㄴ, ㄹ', 'ㄱ, ㄴ, ㄷ, ㄹ']))
# 19
add('수평면 위에 놓인 상자를 오른쪽으로 20 N의 힘으로 밀었지만 상자는 움직이지 않았다. 이때 상자에 작용하는 알짜힘의 크기와 마찰력의 크기는?', 4,
    otbl(['알짜힘', '마찰력'], [['0 N', '0 N'], ['20 N', '0 N'], ['20 N', '20 N'], ['0 N', '10 N'], ['0 N', '20 N']]))
# 20
add('&lt;보기&gt;의 운동 중 속력과 운동 방향이 <b>모두</b> 변하는 운동만을 있는 대로 고른 것은?', 4,
    bogi('ㄱ. 일정한 빠르기로 도는 회전목마', 'ㄴ. 나무에서 똑바로 떨어지는 사과', 'ㄷ. 비스듬히 던져 올린 공',
         'ㄹ. 좌우로 흔들리는 그네', 'ㅁ. 곧은 비탈길을 미끄러져 내려가는 썰매') +
    opts(['ㄱ, ㄴ', 'ㄱ, ㄷ', 'ㄴ, ㅁ', 'ㄷ, ㄹ', 'ㄷ, ㄹ, ㅁ']))
# 21 cooling curve
ox, oy = 40, 135; sx, sy = 13, 1.25
body = graph_axes(ox, oy, 210, 125, '시간(분)', '온도(℃)')
pts = [(0, 70), (4, 30), (10, 30), (15, 5)]
body += P(curve(pts, ox, oy, sx, sy), w=1.5)
for t in (4, 10):
    X = ox + t*sx; body += L(X, oy - 30*sy, X, oy, dash=True)
body += L(ox, oy - 30*sy, ox + 4*sx, oy - 30*sy, dash=True) + T(ox - 5, oy - 30*sy + 4, '30', 9, 'end')
for (a, b, lab) in [(0, 4, '(가)'), (4, 10, '(나)'), (10, 15, '(다)')]:
    body += T(ox + (a + b)/2*sx, oy + 14, lab, 9)
add('그래프는 액체 상태의 어떤 물질을 냉각할 때 시간에 따른 온도 변화를 나타낸 것이다. 이에 대한 설명으로 옳은 것은?', 4,
    svg(260, 172, body) + opts(['(나) 구간에서는 열에너지를 흡수한다.', '(나) 구간에서는 물질의 온도가 계속 낮아진다.',
                                 '(나) 구간에서는 응고가 일어나며 액체와 고체가 함께 존재한다.', '(다) 구간에서 입자의 운동이 가장 활발하다.',
                                 '(가) 구간에서는 입자 사이의 거리가 점점 멀어진다.'], 1))
# 22
add('같은 양의 찬물과 뜨거운 물에 잉크를 한 방울씩 떨어뜨렸더니, 뜨거운 물에서 잉크가 더 빨리 퍼져 나갔다. 이에 대한 설명으로 옳은 것만을 &lt;보기&gt;에서 있는 대로 고른 것은?', 4,
    bogi('ㄱ. 이 현상은 확산의 예이다.', 'ㄴ. 온도가 높을수록 입자의 운동이 활발하다.', 'ㄷ. 찬물에서는 물 입자가 운동하지 않는다.',
         'ㄹ. 확산은 기체 상태보다 액체 상태에서 더 빠르게 일어난다.') +
    opts(['ㄱ, ㄴ', 'ㄱ, ㄷ', 'ㄴ, ㄷ', 'ㄱ, ㄴ, ㄷ', 'ㄴ, ㄷ, ㄹ']))
# 23
add('부력을 이용한 예에 대한 설명으로 옳은 것만을 &lt;보기&gt;에서 있는 대로 고른 것은?', 4,
    bogi('ㄱ. 구명조끼를 입으면 몸의 질량이 줄어들어 물에 쉽게 뜬다.', 'ㄴ. 열기구는 내부 공기를 가열하여 부력이 중력보다 커지면 위로 떠오른다.',
         'ㄷ. 잠수함이 떠오르려면 공기 탱크의 물을 밖으로 빼내어 중력을 부력보다 작게 해야 한다.',
         'ㄹ. 쇠로 만든 배는 내부를 빈 공간으로 만들어 물에 잠기는 부피를 크게 하므로 물에 뜬다.') +
    opts(['ㄱ, ㄴ', 'ㄷ, ㄹ', 'ㄱ, ㄴ, ㄷ', 'ㄴ, ㄷ, ㄹ', 'ㄱ, ㄴ, ㄷ, ㄹ']))
# 24 three springs
def hang(x, bot, lab, hand=None):
    s = L(x - 30, 12, x + 30, 12, 3) + spring(x, 12, bot - 13, 10, 6) + C(x, bot, 13, '#777') + T(x, 175, lab, 10)
    if hand == 'down': s += arrow(x + 22, bot - 6, x + 22, bot + 22, 1.3) + T(x + 30, bot + 16, '손', 9.5, 'start')
    if hand == 'up': s += arrow(x + 22, bot + 22, x + 22, bot - 6, 1.3) + T(x + 30, bot + 18, '손', 9.5, 'start')
    return s
body = hang(45, 105, '(가)') + hang(140, 135, '(나)', 'down') + hang(235, 62, '(다)', 'up')
add('천장에 고정된 용수철에 무게가 20 N인 추를 매달아 정지시킨 상태가 (가)이다. (나)는 손으로 추를 아래로 더 당겨 정지시킨 상태이고, (다)는 손으로 추를 위로 밀어 용수철이 원래 길이보다 짧게 압축된 상태로 정지시킨 것이다. 이에 대한 설명으로 옳은 것만을 &lt;보기&gt;에서 있는 대로 고른 것은?', 5,
    svg(285, 182, body) +
    bogi('ㄱ. (가)에서 추에 작용하는 탄성력은 위쪽 방향으로 20 N이다.', 'ㄴ. (나)에서 추에 작용하는 탄성력의 크기는 (가)일 때보다 크다.',
         'ㄷ. (다)에서 추에 작용하는 탄성력의 방향은 아래쪽이다.', 'ㄹ. (나)에서 손이 추에 작용하는 힘의 방향은 위쪽이다.') +
    opts(['ㄱ, ㄴ', 'ㄷ, ㄹ', 'ㄱ, ㄴ, ㄷ', 'ㄱ, ㄷ, ㄹ', 'ㄱ, ㄴ, ㄷ, ㄹ']))
# 25 box with forces, weight 50 N
body = (L(10, 80, 250, 80, 1.4) + R(100, 40, 60, 40, '#ddd') + T(130, 65, '50 N', 10) +
        arrow(160, 60, 220, 60) + T(230, 64, '30 N', 10, 'start') + arrow(100, 60, 80, 60) + T(72, 64, '10 N', 10, 'end'))
add('그림과 같이 수평면 위에 놓인 무게 50 N인 상자에 오른쪽으로 30 N, 왼쪽으로 10 N의 힘을 동시에 작용하였더니 상자가 움직이지 않았다. 이에 대한 설명으로 옳은 것만을 &lt;보기&gt;에서 있는 대로 고른 것은?', 5,
    svg(260, 90, body) +
    bogi('ㄱ. 상자에 작용하는 마찰력은 왼쪽 방향으로 20 N이다.', 'ㄴ. 상자에 작용하는 알짜힘은 0 N이다.',
         'ㄷ. 수평면이 상자를 떠받치는 힘은 위쪽 방향으로 50 N이다.', 'ㄹ. 상자에 작용하는 중력의 크기는 30 N이다.') +
    opts(['ㄱ, ㄴ', 'ㄱ, ㄴ, ㄷ', 'ㄱ, ㄷ, ㄹ', 'ㄴ, ㄷ, ㄹ', 'ㄱ, ㄴ, ㄷ, ㄹ']))
# 26
add('지구에서 어떤 용수철에 질량이 3 kg인 추를 매달았더니 용수철이 6 cm 늘어났다. 달에서 같은 용수철을 6 cm 늘어나게 하려면 질량이 몇 kg인 추를 매달아야 하는가? (단, 달의 중력은 지구의 <span class="fr"><span>1</span><span>6</span></span>이고, 용수철이 늘어난 길이는 매단 추의 무게에 비례한다.)', 5,
    opts(['0.5 kg', '3 kg', '6 kg', '12 kg', '18 kg']))
# 27 heating curve of water from ice
ox, oy = 40, 140; sx, sy = 9.0, 0.8
body = graph_axes(ox, oy, 225, 133, '가열 시간(분)', '온도(℃)')
base = 25
pts = [(0, -20), (2, 0), (7, 0), (12, 100), (21, 100), (24, 120)]
cp = [(ox + t*sx, oy - (v + base)*sy) for t, v in pts]
body += P(cp, w=1.5)
for t, v in [(2, 0), (7, 0), (12, 100), (21, 100)]:
    X, Y = ox + t*sx, oy - (v + base)*sy
    body += L(X, Y, X, oy, dash=True)
body += L(ox, oy - base*sy, ox + 2*sx, oy - base*sy, dash=True) + T(ox - 5, oy - base*sy + 4, '0', 9, 'end')
body += L(ox, oy - (100 + base)*sy, ox + 12*sx, oy - (100 + base)*sy, dash=True) + T(ox - 5, oy - (100 + base)*sy + 4, '100', 9, 'end')
for (a, b, lab) in [(0, 2, '(가)'), (2, 7, '(나)'), (7, 12, '(다)'), (12, 21, '(라)'), (21, 24, '(마)')]:
    body += T(ox + (a + b)/2*sx, oy + 14, lab, 9)
add('그래프는 1기압에서 −20 ℃의 얼음을 가열할 때 시간에 따른 온도 변화를 나타낸 것이다. 이에 대한 설명으로 옳은 것만을 &lt;보기&gt;에서 있는 대로 고른 것은?', 5,
    svg(275, 178, body) +
    bogi('ㄱ. (나) 구간에서는 고체와 액체가 함께 존재한다.', 'ㄴ. (라) 구간에서 흡수한 열에너지는 입자 사이의 거리를 멀게 하는 데 사용된다.',
         'ㄷ. 입자의 운동이 가장 활발한 구간은 (마)이다.', 'ㄹ. (다) 구간에서는 열에너지를 흡수해도 입자의 운동이 변하지 않는다.',
         'ㅁ. 입자의 배열이 가장 규칙적인 구간은 (가)이다.') +
    opts(['ㄱ, ㄴ', 'ㄷ, ㄹ', 'ㄱ, ㄴ, ㄷ', 'ㄱ, ㄷ, ㅁ', 'ㄱ, ㄴ, ㄷ, ㅁ']))

PTS = [3]*12 + [4]*11 + [5]*4
assert len(Q) == 27 and sum(PTS) == 100
html = ''.join(f'<div class="q">\n  <div class="stem"><b class="no">{i}.</b> {stem} <span class="pt">({PTS[i-1]}점)</span></div>\n  {body}\n</div>\n' for i, (stem, _, body) in enumerate(Q, 1))

src = open(BASE, encoding='utf-8').read()
a0 = src.index('<div id="pool">') + len('<div id="pool">'); b0 = src.index('<div class="end" id="endblock">')
s = src[:a0] + '\n' + html + '\n' + src[b0:]
s = s.replace('<title>1학년 수학 지필평가</title>', '<title>1학년 과학 지필평가</title>')
s = s.replace('<div class="title">수학과<br>', '<div class="title">과학과<br>')
s = s.replace('3일(토)&nbsp;&nbsp;&nbsp;2교시', '3일(토)&nbsp;&nbsp;&nbsp;3교시').replace('과목코드(04)', '과목코드(05)')
s = s.replace('<span class="l1">(1)학년 (수학)과목</span>', '<span class="l1">(1)학년 (과학)과목</span>')
s = s.replace('<td>8문항x3점</td><td>24점</td></tr><tr><td>14문항x4점</td><td>56점</td>', '<td>12문항x3점</td><td>36점</td></tr><tr><td>11문항x4점</td><td>44점</td>')
s = s.replace('<td>26문항</td><td>100점</td>', '<td>27문항</td><td>100점</td>')
s = s.replace('</style>', '  table.dt { margin: 1.4mm 0 2mm; }\n  table.dt th, table.dt td { padding: 0.5mm 2mm; }\n</style>', 1)
s = s.replace('const MAXQ = 2;', 'const MAXQ = 3;').replace('const FILL = 0.9;', 'const FILL = 1.0;').replace('.col > .q { margin-bottom: 14mm; }', '.col > .q { margin-bottom: 8mm; }').replace('font-size: 10.6pt; line-height: 1.72;', 'font-size: 9.8pt; line-height: 1.6;').replace('.end { margin-top: 85mm !important; }', '.end { margin-top: 30mm !important; }')
s = s.replace('for (const b of blocks) {', "for (const b of blocks) {\n    if (b.classList.contains('end') && ci === 0) ci = 1;", 1)
open(OUT, 'w', encoding='utf-8').write(s)
print('written', OUT)
