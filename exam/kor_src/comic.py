# 만화 「동메달이 행복한 까닭은?」 장면을 직접 그린 SVG 삽화로 생성
OUT = '/home/user/Hyun/exam/img/kor/'
SKIN = '#f8dcc4'
FONT = "font-family=\"NanumGothic, 'Nanum Gothic', Gulim, sans-serif\""
W = 600


def person(cx, by, s=1.0, hair='#2b2b2b', hstyle='short', shirt='#f4a6b6', inner=None, mouth='smile',
           eyes='open', glasses=False, back=False, arm='down', extra=''):
    """교과서 삽화풍 상반신 인물 (흑백 변환 전제)"""
    L = '#2a2a2a'
    sw = 1.5 * s
    hy = by - 172 * s          # 얼굴 중심
    rx, ry = 29 * s, 35 * s
    o = []
    P = lambda x, y: f'{cx + x * s:.1f},{by + y * s:.1f}' if False else f'{x:.1f},{y:.1f}'
    # 뒷머리
    if hstyle == 'bob':
        o.append(f'<path d="M{cx-40*s},{hy+34*s} Q{cx-44*s},{hy-50*s} {cx},{hy-46*s} Q{cx+44*s},{hy-50*s} {cx+40*s},{hy+34*s} Q{cx+30*s},{hy+40*s} {cx+22*s},{hy+32*s} L{cx-22*s},{hy+32*s} Q{cx-30*s},{hy+40*s} {cx-40*s},{hy+34*s} Z" fill="{hair}" stroke="{L}" stroke-width="{sw}"/>')
    if hstyle == 'long':
        o.append(f'<path d="M{cx-40*s},{by-92*s} Q{cx-46*s},{hy-50*s} {cx},{hy-46*s} Q{cx+46*s},{hy-50*s} {cx+40*s},{by-92*s} Q{cx},{by-80*s} {cx-40*s},{by-92*s} Z" fill="{hair}" stroke="{L}" stroke-width="{sw}"/>')
    # 몸통
    torso = f'M{cx-56*s},{by+2} L{cx-55*s},{by-92*s} Q{cx-53*s},{by-124*s} {cx-20*s},{by-130*s} L{cx+20*s},{by-130*s} Q{cx+53*s},{by-124*s} {cx+55*s},{by-92*s} L{cx+56*s},{by+2} Z'
    o.append(f'<path d="{torso}" fill="{shirt}" stroke="{L}" stroke-width="{sw}"/>')
    if not back:
        if inner:
            o.append(f'<path d="M{cx-14*s},{by-130*s} L{cx-22*s},{by+2} L{cx+22*s},{by+2} L{cx+14*s},{by-130*s} Z" fill="{inner}" stroke="{L}" stroke-width="{sw}"/>')
            o.append(f'<path d="M{cx-14*s},{by-130*s} L{cx-26*s},{by-96*s} L{cx-18*s},{by-90*s} M{cx+14*s},{by-130*s} L{cx+26*s},{by-96*s} L{cx+18*s},{by-90*s}" fill="none" stroke="{L}" stroke-width="{sw}"/>')
        o.append(f'<path d="M{cx-10*s},{by-131*s} Q{cx},{by-116*s} {cx+10*s},{by-131*s}" fill="none" stroke="{L}" stroke-width="{sw}"/>')
    o.append(f'<path d="M{cx+30*s},{by-125*s} Q{cx+52*s},{by-110*s} {cx+55*s},{by-60*s} L{cx+56*s},{by+2} L{cx+36*s},{by+2} Q{cx+40*s},{by-70*s} {cx+30*s},{by-125*s} Z" fill="#000" opacity="0.10"/>')
    o.append(f'<path d="M{cx-38*s},{by-40*s} Q{cx-30*s},{by-30*s} {cx-34*s},{by-12*s} M{cx+36*s},{by-50*s} Q{cx+28*s},{by-38*s} {cx+33*s},{by-20*s}" fill="none" stroke="{L}" stroke-width="{1*s}" opacity="0.6"/>')
    # 목
    o.append(f'<path d="M{cx-9*s},{hy+26*s} L{cx-10*s},{by-128*s} Q{cx},{by-120*s} {cx+10*s},{by-128*s} L{cx+9*s},{hy+26*s} Z" fill="{SKIN}" stroke="{L}" stroke-width="{sw}"/>')
    o.append(f'<path d="M{cx-9*s},{hy+30*s} Q{cx},{hy+40*s} {cx+9*s},{hy+30*s} L{cx+9*s},{hy+38*s} Q{cx},{hy+46*s} {cx-9*s},{hy+38*s} Z" fill="#000" opacity="0.12"/>')
    o.append(extra)
    # 팔 (어깨-팔꿈치-손)
    shL, shR = (cx - 46 * s, by - 116 * s), (cx + 46 * s, by - 116 * s)
    d = lambda x, y: (cx + x * s, by + y * s)
    h_ = lambda x, y: (cx + x * s, hy + y * s)
    poses = {
        'down': [(shL, d(-62, -70), d(-62, -14)), (shR, d(62, -70), d(62, -14))],
        'point': [(shL, d(-62, -70), d(-62, -14)), (shR, d(72, -92), h_(86, 26))],
        'pointl': [(shR, d(62, -70), d(62, -14)), (shL, d(-72, -92), h_(-86, 26))],
        'micg': [(shL, d(-74, -72), d(-98, -98)), (shR, d(48, -66), h_(16, 48))],
        'raise': [(shL, d(-62, -70), d(-62, -14)), (shR, h_(64, -6), h_(56, -78))],
        'chin': [(shL, d(-62, -70), d(-62, -14)), (shR, d(34, -62), h_(8, 40))],
        'head': [(shL, d(-62, -70), d(-62, -14)), (shR, h_(72, 22), h_(30, -24))],
        'yawn': [(shL, d(-62, -70), d(-62, -14)), (shR, d(36, -62), h_(6, 24))],
        'desk': [(shL, d(-58, -52), d(-26, -34)), (shR, d(58, -52), d(26, -34))],
        'cross': [(shL, d(-56, -66), d(30, -76)), (shR, d(56, -66), d(-30, -70))],
    }[arm]
    if back:
        poses = [(shL, d(-62, -70), d(-62, -14)), (shR, d(62, -70), d(62, -14))]
    for (a, e, h) in poses:
        pth = f'M{a[0]:.1f},{a[1]:.1f} L{e[0]:.1f},{e[1]:.1f} L{h[0]:.1f},{h[1]:.1f}'
        o.append(f'<path d="{pth}" fill="none" stroke="{L}" stroke-width="{21*s}" stroke-linecap="round" stroke-linejoin="round"/>')
        o.append(f'<path d="{pth}" fill="none" stroke="{shirt}" stroke-width="{18*s}" stroke-linecap="round" stroke-linejoin="round"/>')
        o.append(f'<path d="M{e[0]:.1f},{e[1]:.1f} L{(e[0]+h[0])/2:.1f},{(e[1]+h[1])/2:.1f}" stroke="#000" opacity="0.08" stroke-width="{8*s}" stroke-linecap="round"/>')
        o.append(f'<ellipse cx="{h[0]:.1f}" cy="{h[1]:.1f}" rx="{8*s}" ry="{9.5*s}" fill="{SKIN}" stroke="{L}" stroke-width="{sw}"/>')
    if arm == 'micg':
        o.append(f'<path d="M{cx+16*s},{hy+40*s} L{cx+13*s},{hy+62*s}" stroke="#222" stroke-width="{6*s}" stroke-linecap="round"/><ellipse cx="{cx+17*s}" cy="{hy+34*s}" rx="{6*s}" ry="{7*s}" fill="#444" stroke="#111" stroke-width="1"/>')
    # 머리
    if back:
        o.append(f'<ellipse cx="{cx}" cy="{hy-4*s}" rx="{rx+6*s}" ry="{ry+8*s}" fill="{hair}" stroke="{L}" stroke-width="{sw}"/>')
        if hstyle == 'bob':
            o.append(f'<path d="M{cx-37*s},{hy} L{cx-38*s},{hy+36*s} Q{cx},{hy+44*s} {cx+38*s},{hy+36*s} L{cx+37*s},{hy} Z" fill="{hair}" stroke="{L}" stroke-width="{sw}"/>')
        for k in (-16, -4, 8, 20):
            o.append(f'<path d="M{cx+k*s},{hy-38*s} Q{cx+(k+4)*s},{hy} {cx+(k-2)*s},{hy+30*s}" stroke="#fff" opacity="0.25" stroke-width="{1.4*s}" fill="none"/>')
        return '\n'.join(o)
    o.append(f'<ellipse cx="{cx-29*s}" cy="{hy+6*s}" rx="{5*s}" ry="{8*s}" fill="{SKIN}" stroke="{L}" stroke-width="{sw}"/><ellipse cx="{cx+29*s}" cy="{hy+6*s}" rx="{5*s}" ry="{8*s}" fill="{SKIN}" stroke="{L}" stroke-width="{sw}"/>')
    o.append(f'<path d="M{cx-rx},{hy-6*s} Q{cx-rx},{hy+24*s} {cx-12*s},{hy+33*s} Q{cx},{hy+38*s} {cx+12*s},{hy+33*s} Q{cx+rx},{hy+24*s} {cx+rx},{hy-6*s} Q{cx+rx},{hy-ry} {cx},{hy-ry} Q{cx-rx},{hy-ry} {cx-rx},{hy-6*s} Z" fill="{SKIN}" stroke="{L}" stroke-width="{sw}"/>')
    # 앞머리
    if hstyle == 'short':
        o.append(f'<path d="M{cx-31*s},{hy+4*s} Q{cx-36*s},{hy-46*s} {cx},{hy-45*s} Q{cx+36*s},{hy-46*s} {cx+31*s},{hy+4*s} L{cx+27*s},{hy-12*s} L{cx+17*s},{hy-20*s} L{cx+9*s},{hy-12*s} L{cx-2*s},{hy-22*s} L{cx-12*s},{hy-13*s} L{cx-22*s},{hy-20*s} L{cx-28*s},{hy-8*s} Z" fill="{hair}" stroke="{L}" stroke-width="{sw}" stroke-linejoin="round"/>')
    else:
        o.append(f'<path d="M{cx-33*s},{hy+12*s} Q{cx-38*s},{hy-48*s} {cx},{hy-46*s} Q{cx+38*s},{hy-48*s} {cx+33*s},{hy+12*s} Q{cx+26*s},{hy-14*s} {cx+4*s},{hy-18*s} Q{cx-16*s},{hy-14*s} {cx-24*s},{hy-4*s} Q{cx-28*s},{hy+4*s} {cx-33*s},{hy+12*s} Z" fill="{hair}" stroke="{L}" stroke-width="{sw}"/>')
    o.append(f'<path d="M{cx-14*s},{hy-38*s} Q{cx},{hy-42*s} {cx+14*s},{hy-37*s}" stroke="#fff" opacity="0.35" stroke-width="{3*s}" fill="none" stroke-linecap="round"/>')
    # 얼굴
    ey = hy + 4 * s
    for dx in (-12, 12):
        ex = cx + dx * s
        if eyes in ('open', 'angry', 'sad'):
            o.append(f'<ellipse cx="{ex}" cy="{ey}" rx="{5.2*s}" ry="{5.6*s}" fill="#fff" stroke="{L}" stroke-width="{0.8*s}"/>'
                     f'<circle cx="{ex}" cy="{ey+0.6*s}" r="{3.9*s}" fill="#333"/><circle cx="{ex+1.3*s}" cy="{ey-1.2*s}" r="{1.3*s}" fill="#fff"/>'
                     f'<path d="M{ex-6*s},{ey-3*s} Q{ex},{ey-8.5*s} {ex+6*s},{ey-3*s}" stroke="#111" stroke-width="{2*s}" fill="none"/>')
        elif eyes == 'closed':
            o.append(f'<path d="M{ex-6*s},{ey} Q{ex},{ey+4*s} {ex+6*s},{ey}" stroke="#222" stroke-width="{1.8*s}" fill="none"/>')
        elif eyes == 'happy':
            o.append(f'<path d="M{ex-6*s},{ey+2*s} Q{ex},{ey-5*s} {ex+6*s},{ey+2*s}" stroke="#222" stroke-width="{2*s}" fill="none"/>')
        elif eyes == 'down':
            o.append(f'<path d="M{ex-6*s},{ey} Q{ex},{ey+3*s} {ex+6*s},{ey}" stroke="#222" stroke-width="{2*s}" fill="none"/><path d="M{ex-6*s},{ey-1*s} L{ex+6*s},{ey-1*s}" stroke="#222" stroke-width="{1*s}"/>')
    if eyes == 'angry':
        o.append(f'<path d="M{cx-20*s},{ey-13*s} L{cx-6*s},{ey-9*s} M{cx+20*s},{ey-13*s} L{cx+6*s},{ey-9*s}" stroke="#222" stroke-width="{2.2*s}"/>')
    elif eyes == 'sad':
        o.append(f'<path d="M{cx-19*s},{ey-9*s} L{cx-6*s},{ey-14*s} M{cx+19*s},{ey-9*s} L{cx+6*s},{ey-14*s}" stroke="#222" stroke-width="{2*s}"/>')
    else:
        o.append(f'<path d="M{cx-18*s},{ey-12*s} Q{cx-12*s},{ey-15*s} {cx-6*s},{ey-12*s} M{cx+18*s},{ey-12*s} Q{cx+12*s},{ey-15*s} {cx+6*s},{ey-12*s}" stroke="#333" stroke-width="{1.6*s}" fill="none"/>')
    o.append(f'<path d="M{cx+1*s},{hy+10*s} L{cx-2*s},{hy+17*s} L{cx+2*s},{hy+18*s}" stroke="#555" stroke-width="{1.2*s}" fill="none"/>')
    if glasses:
        o.append(f'<rect x="{cx-21*s}" y="{ey-6*s}" width="{16*s}" height="{12*s}" rx="{4*s}" fill="none" stroke="#333" stroke-width="{1.5*s}"/><rect x="{cx+5*s}" y="{ey-6*s}" width="{16*s}" height="{12*s}" rx="{4*s}" fill="none" stroke="#333" stroke-width="{1.5*s}"/><path d="M{cx-5*s},{ey-1*s} L{cx+5*s},{ey-1*s}" stroke="#333" stroke-width="{1.5*s}"/>')
    my = hy + 25 * s
    m = {
        'smile': f'<path d="M{cx-7*s},{my} Q{cx},{my+6*s} {cx+7*s},{my}" stroke="#333" stroke-width="{1.6*s}" fill="none"/>',
        'grin': f'<path d="M{cx-9*s},{my-2*s} Q{cx},{my+11*s} {cx+9*s},{my-2*s} Z" fill="#555" stroke="#222" stroke-width="{1.2*s}"/><path d="M{cx-7*s},{my-1*s} L{cx+7*s},{my-1*s}" stroke="#fff" stroke-width="{2*s}"/>',
        'open': f'<ellipse cx="{cx}" cy="{my+1*s}" rx="{5*s}" ry="{4*s}" fill="#555" stroke="#222" stroke-width="{1*s}"/>',
        'flat': f'<path d="M{cx-6*s},{my+1*s} L{cx+6*s},{my+1*s}" stroke="#333" stroke-width="{1.8*s}"/>',
        'frown': f'<path d="M{cx-7*s},{my+4*s} Q{cx},{my-2*s} {cx+7*s},{my+4*s}" stroke="#333" stroke-width="{1.8*s}" fill="none"/>',
        'yawn': f'<ellipse cx="{cx}" cy="{my+2*s}" rx="{6*s}" ry="{8*s}" fill="#555" stroke="#222" stroke-width="{1*s}"/>',
        'o': f'<ellipse cx="{cx}" cy="{my+1*s}" rx="{3.5*s}" ry="{4*s}" fill="#555"/>',
    }[mouth]
    o.append(m)
    if arm == 'yawn':
        o.append(f'<ellipse cx="{cx+6*s}" cy="{hy+24*s}" rx="{8*s}" ry="{9.5*s}" fill="{SKIN}" stroke="{L}" stroke-width="{sw}"/>')
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
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#ffffff" stroke="#222" stroke-width="2"/>' + text(x + w / 2, y + fs * 1.15, lines, fs)


def panel(x, y, w, h, bg, body, pid):
    return (f'<clipPath id="{pid}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>'
            f'<g clip-path="url(#{pid})"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg}"/>{body}</g>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#111" stroke-width="3"/>')


def svg(h, body, name):
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}">'
         '<defs><filter id="gs"><feColorMatrix type="saturate" values="0"/></filter></defs>'
         f'<g filter="url(#gs)">{body}</g></svg>')
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
medal = lambda x, y, c: f'<path d="M{x-14},{y-50} L{x},{y-8} L{x+14},{y-50}" stroke="#222" stroke-width="6" fill="none"/><circle cx="{x}" cy="{y}" r="16" fill="{c}" stroke="#222" stroke-width="2"/><circle cx="{x}" cy="{y}" r="10" fill="none" stroke="#222" stroke-width="1"/>'
p6 = (person(160, H, 0.92, arm='down', mouth='frown', eyes='sad', hair='#222', hstyle='short', shirt='#eef3f8', inner='#b8c4d0',
             extra=medal(160, H - 82, '#eeeeee')) +
      person(440, H, 0.92, arm='raise', mouth='grin', eyes='happy', hair='#3a2a1a', hstyle='short', shirt='#eef3f8', inner='#b8c4d0',
             extra=medal(440, H - 82, '#8a6a4a')) +
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
