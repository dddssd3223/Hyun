# 이석준 쌤 캐릭터 일러스트 (SVG)
import sys
OUT = sys.argv[1]
SK, SKD = '#f7d7bd', '#e9b994'
HAIR = '#1f1f2b'
SUIT, SUITD = '#1d2a6b', '#141d4d'
L = '#22223a'


def teacher(pose='thumbs', mouth='grin'):
    o = []
    # 몸통(정장)
    o.append(f'<path d="M150,430 L150,330 Q150,268 205,256 L255,250 L305,256 Q360,268 360,330 L360,430 Z" fill="{SUIT}" stroke="{L}" stroke-width="3"/>')
    o.append('<path d="M228,252 L255,330 L282,252 Z" fill="#ffffff" stroke="#22223a" stroke-width="2.5"/>')
    o.append('<path d="M248,262 L255,256 L262,262 L259,318 L255,326 L251,318 Z" fill="#d6453d" stroke="#22223a" stroke-width="2"/>')
    o.append(f'<path d="M228,252 L215,300 L240,296 L255,330 Z M282,252 L295,300 L270,296 L255,330 Z" fill="{SUITD}" stroke="{L}" stroke-width="2.5"/>')
    o.append('<circle cx="305" cy="300" r="13" fill="#f2c94c" stroke="#22223a" stroke-width="2"/><text x="305" y="305" font-size="11" text-anchor="middle" font-weight="bold" fill="#1d2a6b" font-family="NanumGothic">SEL</text>')
    # 목
    o.append(f'<path d="M238,210 L238,252 L272,252 L272,210 Z" fill="{SKD}" stroke="{L}" stroke-width="2.5"/>')
    # 팔
    if pose == 'thumbs':
        # 오른팔(화면 오른쪽) 엄지척
        o.append(f'<path d="M345,285 Q400,300 410,250 L412,215" fill="none" stroke="{L}" stroke-width="44" stroke-linecap="round"/>')
        o.append(f'<path d="M345,285 Q400,300 410,250 L412,215" fill="none" stroke="{SUIT}" stroke-width="38" stroke-linecap="round"/>')
        o.append(f'<rect x="392" y="170" width="44" height="42" rx="14" fill="{SK}" stroke="{L}" stroke-width="3"/>')
        o.append(f'<path d="M402,174 Q398,140 412,132 Q424,134 420,172" fill="{SK}" stroke="{L}" stroke-width="3"/>')
        o.append(f'<path d="M398,186 L432,186 M398,198 L432,198" stroke="{L}" stroke-width="2"/>')
        # 왼팔 허리
        o.append(f'<path d="M165,285 Q120,330 160,385" fill="none" stroke="{L}" stroke-width="44" stroke-linecap="round"/>')
        o.append(f'<path d="M165,285 Q120,330 160,385" fill="none" stroke="{SUIT}" stroke-width="38" stroke-linecap="round"/>')
        o.append(f'<circle cx="168" cy="392" r="17" fill="{SK}" stroke="{L}" stroke-width="3"/>')
    else:  # pointer
        o.append(f'<path d="M345,285 Q395,270 420,215" fill="none" stroke="{L}" stroke-width="44" stroke-linecap="round"/>')
        o.append(f'<path d="M345,285 Q395,270 420,215" fill="none" stroke="{SUIT}" stroke-width="38" stroke-linecap="round"/>')
        o.append(f'<line x1="425" y1="205" x2="480" y2="110" stroke="#8a5a2b" stroke-width="6" stroke-linecap="round"/><circle cx="480" cy="110" r="6" fill="#d6453d"/>')
        o.append(f'<circle cx="423" cy="206" r="18" fill="{SK}" stroke="{L}" stroke-width="3"/>')
        o.append(f'<path d="M165,285 Q120,330 160,385" fill="none" stroke="{L}" stroke-width="44" stroke-linecap="round"/>')
        o.append(f'<path d="M165,285 Q120,330 160,385" fill="none" stroke="{SUIT}" stroke-width="38" stroke-linecap="round"/>')
        o.append(f'<circle cx="168" cy="392" r="17" fill="{SK}" stroke="{L}" stroke-width="3"/>')
    # 머리
    o.append(f'<ellipse cx="196" cy="150" rx="13" ry="20" fill="{SK}" stroke="{L}" stroke-width="3"/><ellipse cx="314" cy="150" rx="13" ry="20" fill="{SK}" stroke="{L}" stroke-width="3"/>')
    o.append(f'<path d="M200,120 Q200,60 255,58 Q310,60 310,120 L308,170 Q300,222 255,228 Q210,222 202,170 Z" fill="{SK}" stroke="{L}" stroke-width="3"/>')
    o.append(f'<path d="M194,140 Q186,52 255,40 Q328,46 318,140 L310,118 Q300,92 270,86 Q282,100 276,108 Q250,88 226,98 Q214,110 202,138 Z" fill="{HAIR}" stroke="{L}" stroke-width="3" stroke-linejoin="round"/>')
    o.append('<path d="M232,58 Q256,48 284,56" stroke="#ffffff" stroke-opacity="0.35" stroke-width="5" fill="none" stroke-linecap="round"/>')
    # 눈썹, 눈
    o.append(f'<path d="M218,126 Q232,116 246,124 M264,124 Q278,116 292,126" stroke="{HAIR}" stroke-width="5" fill="none" stroke-linecap="round"/>')
    if mouth == 'grin':
        o.append(f'<path d="M220,148 Q232,136 244,148 M266,148 Q278,136 290,148" stroke="{L}" stroke-width="4.5" fill="none" stroke-linecap="round"/>')
    else:
        o.append(f'<ellipse cx="232" cy="146" rx="6" ry="8" fill="{L}"/><ellipse cx="278" cy="146" rx="6" ry="8" fill="{L}"/><circle cx="234" cy="143" r="2" fill="#fff"/><circle cx="280" cy="143" r="2" fill="#fff"/>')
    o.append(f'<path d="M255,156 L250,175 L258,177" stroke="{SKD}" stroke-width="3" fill="none" stroke-linecap="round"/>')
    o.append('<path d="M228,188 Q255,214 282,188 Z" fill="#b8322b" stroke="#22223a" stroke-width="3" stroke-linejoin="round"/><path d="M233,190 L277,190 L274,197 L236,197 Z" fill="#ffffff"/>')
    o.append('<ellipse cx="218" cy="176" rx="11" ry="6" fill="#f29b8c" opacity="0.6"/><ellipse cx="292" cy="176" rx="11" ry="6" fill="#f29b8c" opacity="0.6"/>')
    return '\n'.join(o)


pose = sys.argv[2] if len(sys.argv) > 2 else 'thumbs'
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="110 20 400 420" width="400" height="420">{teacher(pose, "grin" if pose == "thumbs" else "open")}</svg>'
open(OUT, 'w', encoding='utf-8').write(svg)
