import math, re
S = ''
BASE = '../1학년_사회_파이널모의고사_1회.html'
OUT = '../1학년_수학_시험지.html'

def v(s):  # italic variable
    return f'<i class="mv">{s}</i>'
def ov(s):
    return f'<span class="ov">{s}</span>'
def fr(a, b):
    return f'<span class="fr"><span>{a}</span><span>{b}</span></span>'
x, y, a, b, c = v('x'), v('y'), v('a'), v('b'), v('c')

def svg(w, h, body, width=None):
    mm = min(w*0.30, 78)
    return f'<div class="pic"><svg viewBox="0 0 {w} {h}" style="width:{mm:.1f}mm" font-family="Gulim, sans-serif">{body}</svg></div>'
def T(xx, yy, s, size=11, anchor='middle', it=False, extra=''):
    st = ' font-style="italic" font-family="Liberation Serif, serif" font-size-adjust="0.5"' if it else ''
    size = round(size*1.22, 1)
    return f'<text x="{xx:.1f}" y="{yy:.1f}" font-size="{size}" text-anchor="{anchor}"{st}{extra}>{s}</text>'
def L(x1, y1, x2, y2, w=1.2, dash=False, col='#000'):
    d = ' stroke-dasharray="3,2"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}"{d}/>'
def P(pts, fill='none', w=1.2, dash=False):
    d = ' stroke-dasharray="3,2"' if dash else ''
    return f'<polyline points="{" ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)}" fill="{fill}" stroke="#000" stroke-width="{w}"{d}/>'
def FR(xx, yy, num, den, size=10.5, lhs='y'):
    sz = round(size*1.22, 1); cw = sz*0.55
    out = (f'<text x="{xx:.1f}" y="{yy:.1f}" font-size="{sz}" font-style="italic" font-family="Liberation Serif, serif">{lhs}</text>'
           f'<text x="{xx+cw*1.1:.1f}" y="{yy:.1f}" font-size="{sz}" font-family="Liberation Serif, serif">=</text>')
    fx = xx + cw*2.6; w = max(len(num), len(den))*cw + 2
    def it(t): return f' font-style="italic"' if t.isalpha() else ''
    out += (f'<text x="{fx + w/2:.1f}" y="{yy - sz*0.55:.1f}" font-size="{sz*0.9:.1f}" text-anchor="middle" font-family="Liberation Serif, serif"{it(num)}>{num}</text>'
            f'<line x1="{fx:.1f}" y1="{yy - sz*0.33:.1f}" x2="{fx + w:.1f}" y2="{yy - sz*0.33:.1f}" stroke="#000" stroke-width="0.8"/>'
            f'<text x="{fx + w/2:.1f}" y="{yy + sz*0.55:.1f}" font-size="{sz*0.9:.1f}" text-anchor="middle" font-family="Liberation Serif, serif"{it(den)}>{den}</text>')
    return out
def dot(xx, yy, r=2):
    return f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="{r}" fill="#000"/>'
def arc(cx, cy, r, a1, a2):  # math degrees, svg y down
    x1, y1 = cx + r*math.cos(math.radians(a1)), cy - r*math.sin(math.radians(a1))
    x2, y2 = cx + r*math.cos(math.radians(a2)), cy - r*math.sin(math.radians(a2))
    large = 1 if (a2 - a1) % 360 > 180 else 0
    return f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 0 {x2:.1f},{y2:.1f}" fill="none" stroke="#000" stroke-width="0.9"/>'
def lab_at(cx, cy, r, ang, s, size=10.5, it=False):
    return T(cx + r*math.cos(math.radians(ang)), cy - r*math.sin(math.radians(ang)) + size*0.35, s, size, it=it)
def axes(ox, oy, x1, x2, y1, y2):
    return (L(x1, oy, x2, oy, 1) + L(ox, y1, ox, y2, 1) +
            f'<path d="M{x2},{oy} l-6,-3 v6 z M{ox},{y1} l-3,6 h6 z"/>' +
            T(x2 - 2, oy + 13, 'x', 11, it=True) + T(ox - 9, y1 + 8, 'y', 11, it=True) + T(ox - 8, oy + 12, 'O', 10))

def opts(items, cols=3):
    cls = {3: 'opts', 2: 'opts c2', 1: 'opts c1', 5: 'opts c5'}[cols]
    nums = '①②③④⑤'
    return f'<div class="{cls}">' + ''.join(f'<div>{nums[i]} {t}</div>' for i, t in enumerate(items)) + '</div>'

Q = []
def add(stem, pts, body=''):
    Q.append((stem, pts, body))

# ---------------- 1 ----------------
add(f'점 ({a}, {b})가 제2사분면 위의 점일 때, 점 ({a}{b}, {b}−{a})가 속하는 사분면은?', 3,
    opts(['제1사분면', '제2사분면', '제3사분면', '제4사분면', '어느 사분면에도 속하지 않는다.'], 2))
# ---------------- 2 ----------------
add(f'평면 위에 어느 세 점도 한 직선 위에 있지 않은 네 점 A, B, C, D가 있다. 이 중 두 점을 이어 만들 수 있는 서로 다른 직선의 개수를 {a}, 반직선의 개수를 {b}, 선분의 개수를 {c}라 할 때, {a}+{b}+{c}의 값은?', 3,
    opts(['18', '20', '24', '26', '28']))
# ---------------- 3 ----------------
cx, cy, R = 150, 75, 70
body = ''
for ang in (0, 100, 60):
    body += L(cx - R*1.25*math.cos(math.radians(ang)), cy + R*1.25*math.sin(math.radians(ang)) if False else cy + R*math.sin(math.radians(ang)),
              cx + R*math.cos(math.radians(ang)), cy - R*math.sin(math.radians(ang)))
body = (L(cx - 110, cy, cx + 110, cy) +
        L(cx - 70*math.cos(math.radians(100)), cy + 70*math.sin(math.radians(100)), cx + 70*math.cos(math.radians(100)), cy - 70*math.sin(math.radians(100))) +
        L(cx - 80*math.cos(math.radians(60)), cy + 80*math.sin(math.radians(60)), cx + 80*math.cos(math.radians(60)), cy - 80*math.sin(math.radians(60))) +
        arc(cx, cy, 20, 100, 180) + arc(cx, cy, 26, 60, 100) + arc(cx, cy, 20, 180, 240) +
        lab_at(cx, cy, 38, 145, '2<tspan font-style="italic">x</tspan>°') + lab_at(cx, cy, 42, 80, '40°') +
        lab_at(cx, cy, 46, 212, '(<tspan font-style="italic">x</tspan>+20)°') + T(cx + 8, cy + 14, 'O', 10))
add(f'다음 그림과 같이 세 직선이 한 점 O에서 만날 때, {x}의 값은?', 3, svg(300, 150, body, '85%') + opts(['40', '45', '50', '55', '60']))
# ---------------- 4 ----------------
s, dx, dy = 70, 30, -22
ox_, oy_ = 60, 112
A_ = (ox_, oy_ - s); B_ = (ox_ + s, oy_ - s); C_ = (ox_ + s + dx, oy_ - s + dy); D_ = (ox_ + dx, oy_ - s + dy)
E_ = (ox_, oy_); F_ = (ox_ + s, oy_); G_ = (ox_ + s + dx, oy_ + dy); H_ = (ox_ + dx, oy_ + dy)
body = (P([A_, B_, C_, D_, A_]) + P([A_, E_, F_, B_]) + P([F_, G_, C_]) + L(*E_, *H_, dash=True) + L(*H_, *G_, dash=True) + L(*H_, *D_, dash=True) +
        T(A_[0] - 8, A_[1] - 2, 'A') + T(B_[0] - 2, B_[1] + 13, 'B') + T(C_[0] + 8, C_[1], 'C') + T(D_[0] - 8, D_[1] - 2, 'D') +
        T(E_[0] - 8, E_[1] + 10, 'E') + T(F_[0], F_[1] + 13, 'F') + T(G_[0] + 9, G_[1] + 4, 'G') + T(H_[0] - 9, H_[1] + 2, 'H'))
add(f'다음 그림의 정육면체에서 모서리 AB와 꼬인 위치에 있는 모서리의 개수는?', 3, svg(200, 135, body) + opts(['0', '1', '2', '3', '4']))
# ---------------- 5 ----------------
add(f'점 A({a}+3, 2{a}−4)는 {x}축 위에 있고, 점 B({b}−1, {b}+5)는 {y}축 위에 있다. 이때 {a}{b}의 값은?', 4,
    opts(['1', '2', '3', '4', '5']))
# ---------------- 6 ----------------
add(f'좌표평면 위의 세 점 A(−3, 2), B(−1, −3), C(4, 1)을 꼭짓점으로 하는 삼각형 ABC의 넓이는?', 4,
    opts(['15', fr(31, 2), '16', fr(33, 2), '17']))
# ---------------- 7 ----------------
u = 9
ox_, oy_ = 110, 72
body = axes(ox_, oy_, 20, 200, 6, 165)
f7 = lambda t: -1.5*t
body += L(ox_ + (-5.5)*u, oy_ - f7(-5.5)*u, ox_ + 6.7*u, oy_ - f7(6.7)*u, 1.4)
px, py = ox_ - 4*u, oy_ - 6*u
body += dot(px, py) + L(px, py, px, oy_, dash=True) + L(px, py, ox_, py, dash=True) + T(px, oy_ + 12, '−4', 10) + T(ox_ + 10, py + 4, '6', 10)
qx, qy = ox_ + 6*u, oy_ + 9*u * 0.92
body += dot(ox_ + 6*u, oy_ - f7(6)*u) + L(ox_ + 6*u, oy_ - f7(6)*u, ox_ + 6*u, oy_, dash=True) + L(ox_ + 6*u, oy_ - f7(6)*u, ox_, oy_ - f7(6)*u, dash=True) + T(ox_ + 6*u, oy_ - 5, 'b', 10, it=True) + T(ox_ - 4, oy_ - f7(6)*u + 4, '−9', 10, 'end')
body += T(ox_ - 5.5*u - 4, oy_ - 8.25*u + 12, f'<tspan font-style="italic">y</tspan>=<tspan font-style="italic">ax</tspan>', 10)
add(f'정비례 관계 {y}={a}{x}의 그래프가 다음 그림과 같을 때, {a}{b}의 값은? (단, {a}는 상수)', 4,
    svg(230, 170, body, '68%') + opts(['−9', '−6', '−3', '6', '9']))
# ---------------- 8 ----------------
add(f'반비례 관계 {y}={fr(a, x)}의 그래프가 세 점 (3, −4), ({b}, 6), (−6, {c})를 지날 때, {a}+{b}+{c}의 값은? (단, {a}는 상수)', 4,
    opts(['−16', '−15', '−14', '−13', '−12']))
# ---------------- 9 ----------------
add(f'정비례 관계와 반비례 관계의 그래프에 대한 설명으로 옳지 <span class="u"><b>않은</b></span> 것은?', 4,
    opts([f'{y}=−2{x}의 그래프는 {x}의 값이 증가하면 {y}의 값은 감소한다.',
          f'{y}={fr(3, x)}의 그래프는 제1사분면과 제3사분면을 지난다.',
          f'{y}={a}{x}의 그래프는 {a}의 절댓값이 클수록 {y}축에 가깝다.',
          f'{y}=−{fr(6, x)}의 그래프는 점 (2, −3)을 지난다.',
          f'{y}={fr(a, x)}의 그래프는 원점을 지난다.'], 1))
# ---------------- 10 ----------------
ux, uy = 11, 1.6
ox_, oy_ = 30, 125
body = axes(ox_, oy_, 15, 270, 10, 135)
pts = [(0, 0), (4, 60), (10, 60), (12, 40), (15, 40), (16, 0), (18, 0), (20, 30)]
body += P([(ox_ + p[0]*ux, oy_ - p[1]*uy) for p in pts], w=1.5)
for xv in (4, 10, 12, 15, 16, 18, 20):
    yv = dict(pts)[xv]
    if yv: body += L(ox_ + xv*ux, oy_ - yv*uy, ox_ + xv*ux, oy_, dash=True)
    body += T(ox_ + xv*ux + (4 if xv in (16,) else (-4 if xv == 15 else 0)), oy_ + 12, str(xv), 9)
for yv in (30, 40, 60):
    body += T(ox_ - 4, oy_ - yv*uy + 3, str(yv), 9, 'end') + L(ox_, oy_ - yv*uy, ox_ + (4 if yv == 60 else (12 if yv == 40 else 20))*ux, oy_ - yv*uy, dash=True)
add(f'다음 그래프는 지호네 가족이 자동차를 타고 출발한 지 {x}분 후의 자동차의 속력을 시속 {y} km라 할 때, {x}와 {y} 사이의 관계를 나타낸 것이다. 출발 후 20분 동안 자동차가 <b>멈추지 않고 일정한 속력</b>으로 달린 시간의 합은?', 4,
    svg(285, 140, body, '96%') + opts(['9분', '10분', '11분', '12분', '13분']))
# ---------------- 11 ----------------
k = 1.7
def m(p): return (40 + p[0]*k, 190 - p[1]*k)
Pp = (0, 100); Qp = (43.3, 75); Rp = (1.6, 40); Sp = (35.2, 0)
body = (L(*m((-20, 100)), *m((110, 100))) + L(*m((-20, 0)), *m((110, 0))) +
        P([m(Pp), m(Qp), m(Rp), m(Sp)], w=1.4) +
        T(m((112, 100))[0] + 4, m((112, 100))[1] + 4, 'l', 12, 'start', True) + T(m((112, 0))[0] + 4, m((112, 0))[1] + 4, 'm', 12, 'start', True) +
        arc(*m(Pp), 20, -30, 0) + lab_at(*m(Pp), 32, -12, '30°', 10) +
        arc(*m(Qp), 14, 150, 220) + lab_at(*m(Qp), 24, 185, '<tspan font-style="italic">x</tspan>°', 11) +
        arc(*m(Rp), 14, -50, 40) + lab_at(*m(Rp), 26, -5, '90°', 10) +
        arc(*m(Sp), 18, 130, 180) + lab_at(*m(Sp), 30, 158, '50°', 10))
add(f'다음 그림에서 {v("l")} // {v("m")}일 때, ∠{x}의 크기는?', 4, svg(260, 210, body, '72%') +
    opts(['50°', '55°', '60°', '65°', '70°']))
# ---------------- 12 ----------------
add(f'다음 중 △ABC가 하나로 정해지지 <span class="u"><b>않는</b></span> 것은?', 4,
    opts([f'{ov("AB")}=5 cm, {ov("BC")}=7 cm, {ov("CA")}=10 cm',
          f'{ov("AB")}=4 cm, {ov("BC")}=6 cm, ∠B=50°',
          f'{ov("BC")}=8 cm, ∠B=40°, ∠C=70°',
          f'{ov("AB")}=7 cm, {ov("BC")}=8 cm, ∠C=60°',
          f'{ov("AB")}=7 cm, ∠A=50°, ∠B=60°'], 1))
# ---------------- 13 ----------------
add(f'세 변의 길이가 4 cm, 9 cm, {x} cm인 삼각형을 만들 수 있도록 하는 자연수 {x}의 값의 합은?', 4,
    opts(['63', '66', '70', '72', '75']))
# ---------------- 14 ----------------
add(f'작도에 대한 설명으로 옳은 것을 &lt;보기&gt;에서 <span class="u"><b>모두</b></span> 고른 것은?', 4,
    '<div class="bogi"><p>ㄱ. 작도할 때에는 눈금 없는 자와 컴퍼스만을 사용한다.</p>'
    '<p>ㄴ. 선분의 길이를 다른 직선 위로 옮길 때에는 눈금 없는 자를 사용한다.</p>'
    '<p>ㄷ. 두 점을 연결하는 선분을 그릴 때에는 눈금 없는 자를 사용한다.</p>'
    '<p>ㄹ. 크기가 같은 각의 작도를 이용하여 평행선을 작도할 수 있다.</p></div>' +
    opts(['ㄱ, ㄴ', 'ㄱ, ㄷ', 'ㄴ, ㄹ', 'ㄱ, ㄷ, ㄹ', 'ㄴ, ㄷ, ㄹ']))
# ---------------- 15 ----------------
add(f'△ABC와 △DEF에서 {ov("AB")}={ov("DE")}, ∠B=∠E일 때, 두 삼각형이 합동이 되기 위해 더 필요한 조건이 될 수 <span class="u"><b>없는</b></span> 것은?', 4,
    opts([f'{ov("BC")}={ov("EF")}', f'{ov("AC")}={ov("DF")}', '∠A=∠D', '∠C=∠F', '∠A=∠D, ∠C=∠F'], 2))
# ---------------- 16 ----------------
A_ = (50, 30); B_ = (25, 55); C_ = (120, 50)
D_ = (50, 120); E_ = (25, 145); F_ = (120, 140)
body = (P([A_, B_, C_, A_]) + L(*B_, *E_) + L(*C_, *F_) + P([E_, F_]) + L(*A_, *D_, dash=True) + L(*D_, *E_, dash=True) + L(*D_, *F_, dash=True) +
        T(A_[0], A_[1] - 5, 'A') + T(B_[0] - 9, B_[1] + 3, 'B') + T(C_[0] + 9, C_[1] + 3, 'C') +
        T(D_[0] + 4, D_[1] - 5, 'D') + T(E_[0] - 9, E_[1] + 4, 'E') + T(F_[0] + 9, F_[1] + 4, 'F'))
add(f'다음 그림의 삼각기둥에 대한 설명으로 옳은 것을 &lt;보기&gt;에서 <span class="u"><b>모두</b></span> 고른 것은? (단, 옆면은 모두 밑면에 수직이다.)', 4,
    svg(150, 160, body, '45%') +
    '<div class="bogi"><p>ㄱ. 모서리 AD와 꼬인 위치에 있는 모서리는 3개이다.</p>'
    '<p>ㄴ. 면 ABC와 평행한 모서리는 3개이다.</p>'
    '<p>ㄷ. 모서리 BE와 수직인 면은 2개이다.</p>'
    '<p>ㄹ. 모서리 AB와 평행한 면은 1개이다.</p></div>' +
    opts(['ㄱ, ㄴ', 'ㄴ, ㄷ', 'ㄱ, ㄷ, ㄹ', 'ㄴ, ㄷ, ㄹ', 'ㄱ, ㄴ, ㄷ, ㄹ']))
# ---------------- 17 ----------------
u = 13
ox_, oy_ = 115, 95
body = axes(ox_, oy_, 15, 215, 8, 182)
h1 = [(t, 12/t) for t in [0.9 + i*0.1 for i in range(0, 72)]]
body += P([(ox_ + p[0]*u, oy_ - p[1]*u) for p in h1 if p[1] <= 6.5], w=1.3)
body += P([(ox_ - p[0]*u, oy_ + p[1]*u) for p in h1 if p[1] <= 6.5], w=1.3)
pA = (ox_ + 3*u, oy_ - 4*u); pC = (ox_ - 3*u, oy_ + 4*u)
body += P([pA, (pA[0], pC[1]), pC, (pC[0], pA[1]), pA], w=1.1)
body += (dot(*pA) + dot(*pC) + T(pA[0] + 8, pA[1] - 4, 'A') + T(pA[0] + 8, pC[1] + 10, 'D') + T(pC[0] - 8, pC[1] + 10, 'C') + T(pC[0] - 8, pA[1] - 4, 'B') +
         FR(ox_ + 72, oy_ - 58, 'a', 'x'))
add(f'다음 그림은 반비례 관계 {y}={fr(a, x)}의 그래프이다. 그래프 위의 두 점 A, C는 원점에 대하여 대칭이고, 직사각형 ABCD의 넓이가 48이다. 이 그래프가 점 (2, {b})를 지날 때, {a}+{b}의 값은? (단, 직사각형의 모든 변은 좌표축에 평행하다.)', 4,
    svg(230, 190, body, '68%') + opts(['16', '18', '20', '22', '24']))
# ---------------- 18 ----------------
u = 18
ox_, oy_ = 25, 135
body = axes(ox_, oy_, 10, 175, 8, 145)
h2 = [(t, 12/t) for t in [1.6 + i*0.05 for i in range(0, 120)]]
body += P([(ox_ + p[0]*u, oy_ - p[1]*u) for p in h2 if p[0] <= 8.2], w=1.3)
body += L(ox_, oy_, ox_ + 4.6*u, oy_ - 4.6*4/3*u, 1.3)
pP = (ox_ + 3*u, oy_ - 4*u); pQ = (ox_ + 6*u, oy_ - 2*u)
body += (f'<polygon points="{ox_},{oy_} {pP[0]},{pP[1]} {pQ[0]},{pQ[1]}" fill="#ddd" stroke="#000" stroke-width="0.9"/>' +
         dot(*pP) + dot(*pQ) + T(pP[0] - 9, pP[1] - 3, 'P') + T(pQ[0] + 3, pQ[1] - 7, 'Q') +
         T(ox_ + 4.6*u + 2, oy_ - 4.6*4/3*u - 2, f'<tspan font-style="italic">y</tspan>=<tspan font-style="italic">ax</tspan>', 10, 'start') +
         FR(ox_ + 6.9*u, oy_ - 3.6*u, '12', 'x'))
add(f'다음 그림과 같이 정비례 관계 {y}={a}{x}의 그래프와 반비례 관계 {y}={fr(12, x)}의 그래프가 점 P({v("k")}, 4)에서 만난다. 점 Q는 {y}={fr(12, x)}의 그래프 위의 점이고 {x}좌표가 6일 때, △OPQ의 넓이는? (단, O는 원점)', 4,
    svg(185, 150, body, '62%') + opts(['6', '8', '9', '10', '12']))
# ---------------- 19 ----------------
k = 15
Bp = (0, 0); Cp = (5, 0); Ap = (2.5, 4.33); Dp = (9, 0); Ep = (9.5, 7.79)
def m2(p): return (25 + p[0]*k, 140 - p[1]*k)
body = (L(*m2((-0.5, 0)), *m2((10.5, 0))) + P([m2(Ap), m2(Bp), m2(Cp), m2(Ap)]) + P([m2(Ap), m2(Dp), m2(Ep), m2(Ap)]) +
        L(*m2(Cp), *m2(Ep), 1, dash=True) +
        T(m2(Ap)[0] - 6, m2(Ap)[1] - 5, 'A') + T(m2(Bp)[0], m2(Bp)[1] + 13, 'B') + T(m2(Cp)[0], m2(Cp)[1] + 13, 'C') +
        T(m2(Dp)[0], m2(Dp)[1] + 13, 'D') + T(m2(Ep)[0] + 8, m2(Ep)[1], 'E') + T(m2((7, 0))[0], m2((7, 0))[1] + 13, '4 cm', 9.5))
add(f'다음 그림에서 △ABC와 △ADE는 정삼각형이고, 세 점 B, C, D는 한 직선 위에 있다. △ABC의 둘레의 길이가 15 cm이고 {ov("CD")}=4 cm일 때, {ov("CE")}의 길이는?', 5,
    svg(200, 155, body, '70%') + opts(['6 cm', '7 cm', '8 cm', '9 cm', '10 cm']))
# ---------------- 20 ----------------
add(f'한 직선을 다음과 같은 규칙으로 회전시킨다.<div class="bx" style="margin-top:1.5mm"><p class="hang2">· 첫 번째에는 시계 방향으로 {x}°만큼 회전시킨다.</p><p class="hang2">· 두 번째에는 시계 반대 방향으로 3{x}°만큼 회전시킨다.</p><p class="hang2">· 세 번째에는 시계 방향으로 5{x}°, 네 번째에는 시계 반대 방향으로 7{x}°, …와 같이 방향을 번갈아 바꾸며 회전시킨다.</p></div>이와 같이 10번 회전시켰더니 처음 직선과 겹쳐졌다. 0&lt;{x}&lt;30일 때, {x}의 값은?', 5,
    opts(['12', '15', '18', '20', '24']))
# ---------------- 21 ----------------
body = (L(10, 30, 290, 30, 1.2) + '<path d="M290,30 l-6,-3 v6 z M10,30 l6,-3 v6 z"/>')
for xx_, nm in [(40, 'A'), (75, 'C'), (150, 'M'), (205, 'D'), (260, 'B')]:
    body += dot(xx_, 30, 2.4) + T(xx_, 48, nm, 11)
add(f'다음 그림과 같이 수직선 위에 다섯 개의 점 A, C, M, D, B가 있다. 두 점 A, B의 좌표는 각각 −6, 18이고, 점 M은 {ov("AB")}의 중점이다. {ov("AC")}={fr(1, 3)}{ov("AM")}, {ov("DB")}={fr(1, 4)}{ov("AB")}일 때, {ov("CD")}의 중점의 좌표는?', 5,
    svg(300, 58, body) + opts(['3', '4', '5', '6', '7']))
# ---------------- 22 ----------------
k = 13
Bq = (0, 0); Cq = (6, 0); Aq = (0, 6); Dq = (6, 6); Gq = (10, 0); Fq = (10, 4); Eq = (6, 4); Hq = (6.92, 4.62)
def m3(p): return (20 + p[0]*k, 105 - p[1]*k)
body = (P([m3(Aq), m3(Bq), m3(Gq), m3(Fq), m3(Eq)]) + P([m3(Aq), m3(Dq), m3(Cq)]) + L(*m3(Bq), *m3(Hq)) + L(*m3(Dq), *m3(Gq)) +
        T(m3(Aq)[0] - 8, m3(Aq)[1] + 3, 'A') + T(m3(Bq)[0] - 8, m3(Bq)[1] + 10, 'B') + T(m3(Cq)[0], m3(Cq)[1] + 12, 'C') +
        T(m3(Dq)[0], m3(Dq)[1] - 5, 'D') + T(m3(Eq)[0] - 9, m3(Eq)[1] + 4, 'E') + T(m3(Fq)[0] + 8, m3(Fq)[1], 'F') +
        T(m3(Gq)[0] + 2, m3(Gq)[1] + 12, 'G') + T(m3(Hq)[0] + 8, m3(Hq)[1] - 3, 'H') +
        arc(*m3(Gq), 14, 123.7, 180) + lab_at(*m3(Gq), 24, 152, '56°', 9.5))
add(f'다음 그림과 같이 정사각형 ABCD와 정사각형 ECGF에서 점 E는 {ov("CD")} 위에 있고, 세 점 B, C, G는 한 직선 위에 있다. {ov("BE")}의 연장선과 {ov("DG")}의 교점을 H라 하자. ∠CGD=56°일 때, ∠BHD의 크기는?', 5,
    svg(180, 125, body) + opts(['80°', '85°', '90°', '95°', '100°']))

# ---------------- 서답형 ----------------
SD = []
SD.append((f'톱니의 수가 30개인 톱니바퀴 A와 톱니의 수가 {x}개인 톱니바퀴 B가 서로 맞물려 돌고 있다. A가 4바퀴 회전하는 동안 B는 {y}바퀴 회전할 때, B의 톱니의 수가 24개이면 B가 회전하는 바퀴 수는?', 3, opts(['1바퀴', '2바퀴', '3바퀴', '4바퀴', '5바퀴'])))
SD.append((f'좌표평면 위의 세 점 A(−2, 4), B(−2, −2), C({a}, −2)를 꼭짓점으로 하는 삼각형 ABC의 넓이가 18일 때, {a}의 값은? (단, {a}&gt;0)', 4, opts(['2', '3', '4', '5', '6'])))
cx, cy = 150, 108
body = L(cx - 120, cy, cx + 120, cy, 1.3)
for ang, nm in [(140, 'C'), (80, 'D'), (40, 'E')]:
    body += L(cx, cy, cx + 85*math.cos(math.radians(ang)), cy - 85*math.sin(math.radians(ang)), 1.2) + T(cx + 95*math.cos(math.radians(ang)), cy - 95*math.sin(math.radians(ang)) + 4, nm, 11)
body += T(cx - 124, cy + 4, 'A', 11, 'end') + T(cx + 124, cy + 4, 'B', 11, 'start') + T(cx, cy + 14, 'O', 10)
SD.append((f'다음 그림에서 세 점 A, O, B는 한 직선 위에 있고, ∠AOC : ∠COD : ∠DOB = 2 : 3 : 4이다. 반직선 OE가 ∠DOB를 이등분할 때, ∠COE의 크기는?', 3, svg(300, 125, body) + opts(['100°', '105°', '110°', '115°', '120°'])))
k = 16
def m4(p): return (40 + p[0]*k, 130 - p[1]*k)
Ar = (0, 7); Br = (0, 0); Cr = (7, 0); Dr = (7, 7); Er = (3.5, 6.06)
body = (P([m4(Ar), m4(Br), m4(Cr), m4(Dr), m4(Ar)]) + P([m4(Br), m4(Er), m4(Cr)]) + P([m4(Ar), m4(Er), m4(Dr)], w=1) +
        T(m4(Ar)[0] - 8, m4(Ar)[1] - 2, 'A') + T(m4(Br)[0] - 8, m4(Br)[1] + 10, 'B') + T(m4(Cr)[0] + 8, m4(Cr)[1] + 10, 'C') +
        T(m4(Dr)[0] + 8, m4(Dr)[1] - 2, 'D') + T(m4(Er)[0], m4(Er)[1] + 16, 'E'))
SD.append((f'다음 그림과 같이 정사각형 ABCD의 내부에 △EBC가 정삼각형이 되도록 점 E를 잡았을 때, ∠AED의 크기는?', 4, svg(190, 150, body) + opts(['120°', '135°', '140°', '150°', '160°'])))

# ---------------- assemble ----------------
ORDER = ['Q1','Q5','Q7','S1','Q2','Q3','S3','Q4','Q6','S2','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','S4','Q17','Q18','Q19','Q20','Q21','Q22']
PTS = [3]*8 + [4]*14 + [5]*4
items = {f'Q{i}': q for i, q in enumerate(Q, 1)}
items.update({f'S{i}': q for i, q in enumerate(SD, 1)})
html = []
for i, key in enumerate(ORDER, 1):
    stem, _, body = items[key]
    html.append(f'<div class="q">\n  <div class="stem"><b class="no">{i}.</b> {stem} <span class="pt">({PTS[i-1]}점)</span></div>\n  {body}\n</div>\n')

src = open(BASE, encoding='utf-8').read()
a0 = src.index('<div id="pool">') + len('<div id="pool">'); b0 = src.index('<div class="end" id="endblock">')
s = src[:a0] + '\n' + ''.join(html) + '\n' + src[b0:]
s = s.replace('<title>1학년 사회 파이널 모의고사 1회</title>', '<title>1학년 수학 지필평가</title>')
s = s.replace('<div class="title">사회과<br><span class="t2">파이널 모의고사 1회</span></div>', '<div class="title">수학과<br><span class="t2">2학기&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;중간고사</span></div>')
s = s.replace('3일(토)&nbsp;&nbsp;&nbsp;1교시', '3일(토)&nbsp;&nbsp;&nbsp;2교시')
s = s.replace('과목코드(03)', '과목코드(04)').replace('const MAXQ = 3;', 'const MAXQ = 2;').replace('const FILL = 1.0;', 'const FILL = 0.9;').replace('.col > .q { margin-bottom: 7mm; }', '.col > .q { margin-bottom: 14mm; }').replace("font-size: 10pt; line-height: 1.62;", "font-size: 10.6pt; line-height: 1.72;")
s = s.replace('<span class="l1">(1)학년 (사회)과목</span>', '<span class="l1">(1)학년 (수학)과목</span>')
old_tbl = re.search(r'<table class="score">.*?</table>', s, re.S).group(0)
s = s.replace(old_tbl, '<table class="score"><tr><td>문항 유형</td><td>문항 수x배점</td><td>점수(점)</td></tr>'
    '<tr><td rowspan="3">선택형</td><td>8문항x3점</td><td>24점</td></tr><tr><td>14문항x4점</td><td>56점</td></tr><tr><td>4문항x5점</td><td>20점</td></tr>'
    '<tr><td>계</td><td>26문항</td><td>100점</td></tr></table>')
s = s.replace('※&nbsp; 다음 문제를 읽고 정답을 OMR카드에 정확히 표기하시오.', '※&nbsp; 다음 문제를 읽고 정답을 OMR카드에 정확히 표기하시오.')
css = '''
  i.mv { font-family: 'Liberation Serif', 'Times New Roman', serif; font-size: 1.12em; }
  .ov { text-decoration: overline; text-decoration-thickness: 1px; }
  .fr { display: inline-flex; flex-direction: column; vertical-align: middle; text-align: center; font-size: 0.85em; line-height: 1.1; margin: 0 1px; }
  .fr, .fr > span { text-indent: 0; padding-left: 0; }
  .fr > span:first-child { border-bottom: 1px solid #000; padding: 0 2px; }
  .q.sd .sdh { font-weight: 800; margin-bottom: 1mm; }
  .abox { border: 1px solid #000; height: 34mm; margin-top: 2mm; }
'''
s = s.replace('</style>', css + '</style>', 1)
s = s.replace("document.getElementById('pool').remove();", """document.querySelectorAll('.col').forEach(col => {
    const qs = Array.from(col.querySelectorAll(':scope > .q, :scope > .end'));
    if (!qs.length || !col.lastElementChild) return;
    const used = col.lastElementChild.getBoundingClientRect().bottom - col.getBoundingClientRect().top;
    const free = col.clientHeight - used;
    const rest = qs.filter(q => q.classList.contains('q')).slice(1);
    if (!rest.length) return;
    const g = Math.max(0, Math.min(free / (rest.length + 1.2), 105));
    rest.forEach(q => { q.style.marginTop = (parseFloat(getComputedStyle(q).marginTop) + g) + 'px'; });
  });
  document.getElementById('pool').remove();""")
open(OUT, 'w', encoding='utf-8').write(s)
print('written', len(Q), len(SD))
