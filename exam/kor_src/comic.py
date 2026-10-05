# 만화 「동메달이 행복한 까닭은?」 장면을 직접 그린 SVG 삽화로 생성
OUT = '/home/user/Hyun/exam/img/kor/'
SKIN = '#f8dcc4'
FONT = "font-family=\"NanumGothic, 'Nanum Gothic', Gulim, sans-serif\""
W = 600


def person(cx, by, s=1.0, hair='#2b2b2b', hstyle='short', shirt='#f4a6b6', inner=None, mouth='smile',
           eyes='open', glasses=False, back=False, arm='down', extra=''):
    r = 40 * s
    hy = by - 165 * s
    o = []
    # 뒷머리
    if not back and hstyle == 'bob':
        o.append(f'<path d="M{cx-r-9*s},{hy+r*0.9} Q{cx-r-12*s},{hy-r-14*s} {cx},{hy-r-12*s} Q{cx+r+12*s},{hy-r-14*s} {cx+r+9*s},{hy+r*0.9} Z" fill="{hair}"/>')
    if not back and hstyle == 'long':
        o.append(f'<path d="M{cx-r-8*s},{by-95*s} Q{cx-r-14*s},{hy-r-14*s} {cx},{hy-r-12*s} Q{cx+r+14*s},{hy-r-14*s} {cx+r+8*s},{by-95*s} Z" fill="{hair}"/>')
    # 몸통
    o.append(f'<path d="M{cx-58*s},{by} L{cx-58*s},{by-82*s} Q{cx-58*s},{by-118*s} {cx-24*s},{by-121*s} L{cx+24*s},{by-121*s} Q{cx+58*s},{by-118*s} {cx+58*s},{by-82*s} L{cx+58*s},{by} Z" fill="{shirt}" stroke="#333" stroke-width="{1.6*s}"/>')
    if inner and not back:
        o.append(f'<path d="M{cx-20*s},{by} L{cx-20*s},{by-118*s} L{cx+20*s},{by-118*s} L{cx+20*s},{by} Z" fill="{inner}" stroke="#333" stroke-width="{1.2*s}"/>')
    o.append(f'<rect x="{cx-10*s}" y="{hy+r-8*s}" width="{20*s}" height="{22*s}" fill="{SKIN}"/>')
    o.append(extra)
    # 팔
    sh_l, sh_r = (cx - 48 * s, by - 105 * s), (cx + 48 * s, by - 105 * s)
    arms = {
        'down': [(sh_l, (cx - 66 * s, by - 20 * s)), (sh_r, (cx + 66 * s, by - 20 * s))],
        'point': [(sh_l, (cx - 66 * s, by - 20 * s)), (sh_r, (cx + 82 * s, hy + 30 * s))],
        'pointl': [(sh_r, (cx + 66 * s, by - 20 * s)), (sh_l, (cx - 82 * s, hy + 30 * s))],
        'mic': [(sh_l, (cx - 66 * s, by - 20 * s)), (sh_r, (cx + 22 * s, hy + 52 * s))],
        'micg': [(sh_l, (cx - 78 * s, by - 50 * s)), (sh_r, (cx + 22 * s, hy + 52 * s))],
        'raise': [(sh_l, (cx - 66 * s, by - 20 * s)), (sh_r, (cx + 55 * s, hy - 75 * s))],
        'chin': [(sh_l, (cx - 66 * s, by - 20 * s)), (sh_r, (cx + 6 * s, hy + r + 4 * s))],
        'head': [(sh_l, (cx - 66 * s, by - 20 * s)), (sh_r, (cx + r + 6 * s, hy - 8 * s))],
        'yawn': [(sh_l, (cx - 66 * s, by - 20 * s)), (sh_r, (cx + 4 * s, hy + 22 * s))],
        'desk': [(sh_l, (cx - 30 * s, by - 30 * s)), (sh_r, (cx + 30 * s, by - 30 * s))],
        'cross': [],
    }[arm]
    for (a, b) in arms:
        o.append(f'<path d="M{a[0]},{a[1]} L{b[0]},{b[1]}" stroke="#333" stroke-width="{24*s}" stroke-linecap="round"/>')
        o.append(f'<path d="M{a[0]},{a[1]} L{b[0]},{b[1]}" stroke="{shirt}" stroke-width="{21*s}" stroke-linecap="round"/>')
        o.append(f'<circle cx="{b[0]}" cy="{b[1]}" r="{10*s}" fill="{SKIN}" stroke="#333" stroke-width="{1.2*s}"/>')
    if arm == 'cross':
        o.append(f'<rect x="{cx-52*s}" y="{by-78*s}" width="{104*s}" height="{26*s}" rx="{13*s}" fill="{shirt}" stroke="#333" stroke-width="{1.6*s}"/>')
        o.append(f'<circle cx="{cx-40*s}" cy="{by-65*s}" r="{9*s}" fill="{SKIN}" stroke="#333" stroke-width="1"/><circle cx="{cx+40*s}" cy="{by-65*s}" r="{9*s}" fill="{SKIN}" stroke="#333" stroke-width="1"/>')
    if arm in ('mic', 'micg'):
        o.append(f'<rect x="{cx+18*s}" y="{hy+30*s}" width="{8*s}" height="{24*s}" fill="#222"/><circle cx="{cx+22*s}" cy="{hy+28*s}" r="{8*s}" fill="#333"/>')
    # 머리
    if back:
        o.append(f'<circle cx="{cx}" cy="{hy}" r="{r}" fill="{hair}" stroke="#222" stroke-width="{1.2*s}"/>')
        if hstyle == 'bob':
            o.append(f'<path d="M{cx-r-6*s},{hy} L{cx-r-6*s},{hy+r+4*s} L{cx+r+6*s},{hy+r+4*s} L{cx+r+6*s},{hy} Z" fill="{hair}"/>')
        return '\n'.join(o)
    o.append(f'<circle cx="{cx}" cy="{hy}" r="{r}" fill="{SKIN}" stroke="#333" stroke-width="{1.4*s}"/>')
    o.append(f'<path d="M{cx-r-3*s},{hy+4*s} Q{cx-r-5*s},{hy-r-12*s} {cx},{hy-r-9*s} Q{cx+r+5*s},{hy-r-12*s} {cx+r+3*s},{hy+4*s} Q{cx+r-6*s},{hy-16*s} {cx+12*s},{hy-20*s} Q{cx-10*s},{hy-12*s} {cx-r+2*s},{hy-6*s} Z" fill="{hair}"/>')
    # 얼굴
    ey = hy + 4 * s
    for dx in (-14, 14):
        if eyes == 'open':
            o.append(f'<ellipse cx="{cx+dx*s}" cy="{ey}" rx="{3.8*s}" ry="{5.5*s}" fill="#222"/><circle cx="{cx+dx*s+1.3*s}" cy="{ey-2*s}" r="{1.4*s}" fill="#fff"/>')
        elif eyes == 'closed':
            o.append(f'<path d="M{cx+dx*s-5*s},{ey} Q{cx+dx*s},{ey+4*s} {cx+dx*s+5*s},{ey}" stroke="#222" stroke-width="{2*s}" fill="none"/>')
        elif eyes == 'happy':
            o.append(f'<path d="M{cx+dx*s-5*s},{ey+2*s} Q{cx+dx*s},{ey-5*s} {cx+dx*s+5*s},{ey+2*s}" stroke="#222" stroke-width="{2.2*s}" fill="none"/>')
        elif eyes == 'down':
            o.append(f'<path d="M{cx+dx*s-5*s},{ey+1*s} L{cx+dx*s+5*s},{ey+1*s}" stroke="#222" stroke-width="{2.2*s}"/>')
    if eyes == 'angry':
        for dx in (-14, 14):
            o.append(f'<ellipse cx="{cx+dx*s}" cy="{ey+1*s}" rx="{3.6*s}" ry="{4.5*s}" fill="#222"/>')
        o.append(f'<path d="M{cx-21*s},{ey-12*s} L{cx-8*s},{ey-8*s} M{cx+21*s},{ey-12*s} L{cx+8*s},{ey-8*s}" stroke="#222" stroke-width="{2.4*s}"/>')
    elif eyes == 'sad':
        o.append(f'<path d="M{cx-21*s},{ey-8*s} L{cx-8*s},{ey-12*s} M{cx+21*s},{ey-8*s} L{cx+8*s},{ey-12*s}" stroke="#222" stroke-width="{2.2*s}"/>')
    if glasses:
        o.append(f'<circle cx="{cx-14*s}" cy="{ey}" r="{10*s}" fill="none" stroke="#555" stroke-width="{1.8*s}"/><circle cx="{cx+14*s}" cy="{ey}" r="{10*s}" fill="none" stroke="#555" stroke-width="{1.8*s}"/><path d="M{cx-4*s},{ey} L{cx+4*s},{ey}" stroke="#555" stroke-width="{1.8*s}"/>')
    my = hy + 22 * s
    m = {
        'smile': f'<path d="M{cx-9*s},{my} Q{cx},{my+9*s} {cx+9*s},{my}" stroke="#a33" stroke-width="{2.2*s}" fill="none"/>',
        'grin': f'<path d="M{cx-11*s},{my-2*s} Q{cx},{my+14*s} {cx+11*s},{my-2*s} Z" fill="#c44" stroke="#822" stroke-width="{1.2*s}"/>',
        'open': f'<ellipse cx="{cx}" cy="{my+2*s}" rx="{6*s}" ry="{5*s}" fill="#b33"/>',
        'flat': f'<path d="M{cx-8*s},{my+2*s} L{cx+8*s},{my+2*s}" stroke="#a33" stroke-width="{2.2*s}"/>',
        'frown': f'<path d="M{cx-9*s},{my+5*s} Q{cx},{my-3*s} {cx+9*s},{my+5*s}" stroke="#a33" stroke-width="{2.2*s}" fill="none"/>',
        'yawn': f'<ellipse cx="{cx}" cy="{my+3*s}" rx="{8*s}" ry="{10*s}" fill="#b33"/>',
        'o': f'<ellipse cx="{cx}" cy="{my+2*s}" rx="{4*s}" ry="{5*s}" fill="#b33"/>',
    }[mouth]
    o.append(m)
    o.append(f'<ellipse cx="{cx-24*s}" cy="{hy+16*s}" rx="{6*s}" ry="{3.5*s}" fill="#f4a6a6" opacity="0.7"/><ellipse cx="{cx+24*s}" cy="{hy+16*s}" rx="{6*s}" ry="{3.5*s}" fill="#f4a6a6" opacity="0.7"/>')
    if arm == 'yawn':
        o.append(f'<circle cx="{cx+4*s}" cy="{hy+22*s}" r="{10*s}" fill="{SKIN}" stroke="#333" stroke-width="{1.2*s}"/>')
    return '\n'.join(o)


def text(x, y, lines, fs=21, anchor='middle', weight='normal', fill='#111', lh=1.32):
    t = f'<text x="{x}" y="{y}" font-size="{fs}" text-anchor="{anchor}" font-weight="{weight}" fill="{fill}" {FONT}>'
    for i, l in enumerate(lines):
        t += f'<tspan x="{x}" dy="{0 if i == 0 else fs*lh}">{l}</tspan>'
    return t + '</text>'


def bubble(x, y, w, lines, tail, fs=21):
    h = len(lines) * fs * 1.32 + fs * 0.9
    tx, ty = tail
    bx = min(max(tx, x + 30), x + w - 30)
    by = y + h if ty > y + h / 2 else y
    o = f'<path d="M{bx-14},{by} L{tx},{ty} L{bx+14},{by} Z" fill="#fff" stroke="#222" stroke-width="2.2"/>'
    o += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{min(h/2, 30)}" fill="#fff" stroke="#222" stroke-width="2.2"/>'
    o += f'<path d="M{bx-12},{by} L{bx+12},{by}" stroke="#fff" stroke-width="4"/>'
    o += text(x + w / 2, y + fs * 1.2, lines, fs)
    return o


def narr(x, y, w, lines, fs=20):
    h = len(lines) * fs * 1.34 + fs * 0.8
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fffdf2" stroke="#222" stroke-width="2"/>' + text(x + w / 2, y + fs * 1.15, lines, fs)


def panel(x, y, w, h, bg, body, pid):
    return (f'<clipPath id="{pid}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>'
            f'<g clip-path="url(#{pid})"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg}"/>{body}</g>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#111" stroke-width="3"/>')


def svg(h, body, name):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}">{body}</svg>'
    open(OUT + name + '.svg', 'w', encoding='utf-8').write(s)


PINK, YEL, WHITE = '#f4a6b6', '#f6d76b', '#ffffff'
SJ = dict(hair='#222', hstyle='short', shirt=PINK, inner='#fbe3e8')
EJ = dict(hair='#6b4226', hstyle='bob', shirt=YEL, inner=WHITE)
LEC = dict(hair='#5a3d2b', hstyle='long', shirt='#c9b496', inner='#f5f0e6', glasses=True)

# ---- 1. 약속 장면 ----
B = 25  # 말풍선 글자 크기
N = 24  # 해설 상자 글자 크기
H = 480
p1 = ('<rect x="150" y="70" width="120" height="410" fill="#cfe6ee" stroke="#9bb" stroke-width="2"/>'
      '<rect x="18" y="14" width="112" height="44" rx="6" fill="#333"/>' + text(74, 47, ['4:20'], 30, weight='bold', fill='#ff4b4b') +
      person(78, H, 0.8, arm='cross', mouth='flat', eyes='angry', **SJ) +
      person(222, H, 0.8, arm='pointl', mouth='open', **EJ) +
      bubble(6, 70, 190, ['야, 최은주!', '지금 몇 시야?'], (75, 280), B) +
      bubble(152, 188, 138, ['지금?', '4시 20분.'], (222, 296), B))
p2 = (person(392, H, 0.8, arm='down', mouth='frown', eyes='angry', **SJ) +
      person(532, H, 0.8, arm='head', mouth='grin', eyes='happy', **EJ) +
      bubble(308, 6, 260, ['내가 지금 몇 시인지', '궁금해서 물어본 게', '아니잖아. 우리', '4시에 만나기로', '했잖아.'], (385, 296), B) +
      bubble(412, 212, 182, ['아, 미안해.', '빨리 들어가자.'], (505, 300), B))
svg(H, panel(0, 0, 296, H, '#dff0f7', p1, 'c1') + panel(304, 0, 296, H, '#fbeee0', p2, 'c2'), 'comic1')

# ---- 2. 도서관 장면 ----
H = 300
clock = lambda x, y: f'<circle cx="{x}" cy="{y}" r="22" fill="#fff" stroke="#333" stroke-width="3"/><path d="M{x},{y} L{x},{y-15} M{x},{y} L{x+10},{y+6}" stroke="#333" stroke-width="3"/>'
p3 = (clock(40, 36) + clock(150, 36) + clock(258, 36) +
      person(80, H, 0.72, arm='desk', mouth='flat', eyes='down', **SJ) +
      person(215, H, 0.72, arm='yawn', mouth='yawn', eyes='closed', **EJ) +
      f'<rect x="0" y="{H-40}" width="296" height="40" fill="#e3c08f" stroke="#a07c4c" stroke-width="2"/>' +
      f'<rect x="45" y="{H-48}" width="70" height="14" fill="#fff" stroke="#555"/><rect x="180" y="{H-48}" width="70" height="14" fill="#fff" stroke="#555"/>' +
      text(255, 105, ['하암~'], 26, weight='bold', fill='#444') + text(80, 105, ['?'], 34, weight='bold', fill='#c33'))
p4 = (f'<rect x="320" y="30" width="95" height="{H-30}" fill="#e9f3f7" stroke="#9bb" stroke-width="2"/>' +
      person(368, H, 0.68, arm='down', mouth='open', **EJ) +
      person(520, H, 0.72, arm='desk', mouth='flat', eyes='down', **SJ) +
      f'<rect x="470" y="{H-68}" width="100" height="62" rx="6" fill="#333"/><rect x="476" y="{H-62}" width="88" height="50" fill="#7fb3d5"/>' +
      f'<rect x="420" y="{H-30}" width="180" height="30" fill="#e3c08f" stroke="#a07c4c" stroke-width="2"/>' +
      bubble(425, 14, 165, ['성재야,', '뭐 해?'], (385, 150), B))
svg(H, panel(0, 0, 296, H, '#eaf4ec', p3, 'c3') + panel(304, 0, 296, H, '#f3efe6', p4, 'c4'), 'comic2')

# ---- 3. 강연 1 ----
H = 330
p5 = (person(100, H, 0.92, arm='micg', mouth='open', **LEC) +
      narr(214, 16, 372, ['왜 이런 결과가 나왔을까요?', '메달이 확정된 뒤 은메달을', '딴 선수와 동메달을 딴', '선수가 자신에게 일어난', '일을 대하는 태도에', '차이가 있었기 때문입니다.'], N))
svg(H, panel(0, 0, 600, H, '#e5eef2', p5, 'c5'), 'comic3')

# ---- 4. 두 선수 ----
H = 520
medal = lambda x, y, c: f'<path d="M{x-14},{y-50} L{x},{y-8} L{x+14},{y-50}" stroke="#3a6fb0" stroke-width="7" fill="none"/><circle cx="{x}" cy="{y}" r="14" fill="{c}" stroke="#555" stroke-width="2"/>'
p6 = (person(160, H, 0.92, arm='down', mouth='frown', eyes='sad', hair='#222', hstyle='short', shirt='#eef3f8', inner='#3a6fb0',
             extra=medal(160, H - 82, '#c8c8c8')) +
      person(440, H, 0.92, arm='raise', mouth='grin', eyes='happy', hair='#3a2a1a', hstyle='short', shirt='#eef3f8', inner='#3a6fb0',
             extra=medal(440, H - 82, '#c98a45')) +
      text(50, H - 150, ['은메달'], 22, weight='bold', fill='#555') + text(552, H - 150, ['동메달'], 22, weight='bold', fill='#8a5a2b') +
      narr(12, 10, 576, ['은메달을 딴 선수는 \'내가 실수만 하지', '않았더라면 금메달을 딸 수 있었을 텐데.\'', '라고 생각하여 은메달을 딴 것에 실망하는', '경우가 많았습니다.'], N) +
      narr(12, 168, 576, ['한편 동메달을 딴 선수는 \'내가 실수를', '했더라면 메달을 못 딸 뻔했다.\'라고 생각하여', '동메달을 딴 것에 대단히 만족하는', '경우가 많았답니다.'], N))
svg(H, panel(0, 0, 600, H, '#f6e9f0', p6, 'c6'), 'comic4')

# ---- 5. 강연 2 ----
H = 440
p7 = (f'<rect x="336" y="{H-170}" width="250" height="140" rx="6" fill="#1d3f7a" stroke="#333" stroke-width="3"/>' +
      text(461, H - 92, ['결과를 대하는 태도!'], 25, weight='bold', fill='#fff') +
      person(220, H, 0.92, arm='micg', mouth='open', **LEC) +
      narr(10, 10, 300, ['선수들의 만족감을', '결정한 것은 메달의', '색이 아니었습니다.', '결과보다는 결과를', '대하는 태도가 더 크게', '작용한 것이지요.'], N) +
      narr(318, 10, 272, ['은메달을 딴 선수보다', '동메달을 딴 선수가', '더 기뻐하는 까닭은', '바로 여기에', '있습니다.'], N))
svg(H, panel(0, 0, 600, H, '#e5eef2', p7, 'c7'), 'comic5')

# ---- 6. 대화 ----
H = 470
p8 = (person(78, H, 0.8, arm='chin', mouth='open', **EJ) +
      person(225, H, 0.8, arm='chin', mouth='flat', **SJ) +
      bubble(8, 8, 232, ['은메달을 딴', '선수보다 동메달을', '딴 선수가 더', '기뻐한다고?', '놀라운걸?'], (75, 290), B) +
      text(262, 250, ['음.'], 28, weight='bold'))
p9 = (person(390, H, 0.8, back=True, **SJ) + person(530, H, 0.8, back=True, **EJ) +
      bubble(308, 6, 270, ['단순히 그 사실을', '알려 주려는 것만은', '아닌 것 같아.', '강연자가 이 이야기를', '하는 의도가 따로', '있지 않을까?'], (385, 300), B) +
      bubble(452, 212, 142, ['그래?', '어떤 의도?'], (520, 318), B) +
      text(330, 300, ['?'], 34, weight='bold', fill='#3a9a4a'))
svg(H, panel(0, 0, 296, H, '#eef5e6', p8, 'c8') + panel(304, 0, 296, H, '#f7eadf', p9, 'c9'), 'comic6')
print('done')
