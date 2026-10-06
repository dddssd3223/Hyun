# SEL입시연구소 2026 2학기 중간고사 적중 PR 자료 (사회·수학, 10쪽)
import os, shutil
D = os.path.dirname(os.path.abspath(__file__))
OUT = '/home/user/Hyun/exam/pr'
os.makedirs(OUT + '/img', exist_ok=True)
for sub in ('act', 'cap'):
    for f in os.listdir(f'{D}/{sub}'):
        shutil.copy(f'{D}/{sub}/{f}', f'{OUT}/img/{f}')
for f in ('t1.svg', 't2.svg'):
    shutil.copy(f'{D}/{f}', f'{OUT}/img/{f}')

STU = '우○준'
SOC = [  # 번호, 배점, 내용, SEL 자료, 적중
    (1, 3, '사회화의 의미(자아)', '교과서 문제집 빈칸 2 · 예상 시험지 1', '동일'), (2, 4, '사회화의 두 측면 사례', '예상 시험지 10', '개념'),
    (3, 3, '문화의 특수성(민속춤)', '예상 시험지 11', '동일'), (4, 4, '사회적 지위 &lt;보기&gt;', '예상 시험지 4', '유형'),
    (5, 4, '도윤의 사회적 지위', '예상 시험지 4 · 모의고사 1회 3', '동일'), (6, 3, '사회화 기관(가정)', '예상 시험지 2 · 모의고사 1회 2', '유형'),
    (7, 3, '역할 갈등', '교과서 문제집 빈칸 11', '유형'), (8, 4, '역할 갈등의 해결', '모의고사 1회 4 · 예상 시험지 5', '유형'),
    (9, 3, '성차별(채용 공고)', '교과서 문제집 111 · 모의고사 1회 5', '동일'), (10, 4, '차별에 대처하는 시민 의식', '모의고사 1회 6', '동일'),
    (11, 4, '갈등 해결을 위한 제도', '모의고사 2회 4', '유형'), (12, 4, '문화의 전체성', '교과서 문제집 126', '동일'),
    (13, 4, '맞춤형 서비스와 편향', '예상 시험지 14', '개념'), (14, 4, '미디어 리터러시', '모의고사 2회 12', '동일'),
    (15, 4, '자문화 중심주의·문화 상대주의', '모의고사 1회 17', '유형'), (16, 4, '자문화 중심주의', '모의고사 1회 16', '유형'),
    (17, 3, '문화 사대주의', '교과서 문제집 140 · 모의고사 2회 14', '동일'), (18, 4, '넓은 의미의 정치', '예상 시험지 20', '유형'),
    (19, 4, '정치의 기능', '모의고사 2회 18', '유형'), (20, 3, '4·19 혁명', '모의고사 1회 24', '동일'),
    (21, 4, '현대 민주 정치의 과제', '예상 시험지 28', '유형'), (22, 4, '민주주의의 발전 과정', '모의고사 1회 21', '유형'),
    (23, 4, '민주주의의 의미', '예상 시험지 22', '유형'), (24, 3, '국민 주권·입헌주의', '모의고사 1회 27 · 예상 시험지 26', '동일'),
    (25, 4, '입헌주의', '모의고사 2회 25', '개념'), (26, 4, '자유와 평등', '모의고사 2회 24 · 예상 시험지 25', '동일'),
    (27, 4, '국민 투표·발안·청원', '예상 시험지 27 · 모의고사 2회 28', '동일')]
MATH = [
    (1, 4, '사분면과 부호', '예상 시험지 1', '유형'), (2, 4, '물통의 높이 그래프', '예상 시험지 13', '개념'),
    (3, 5, '좌표로 구하는 사각형 넓이', '예상 시험지 9', '유형'), (4, 4, '드론 고도 그래프 해석', '예상 시험지 13', '유형'),
    (5, 4, '정비례 관계 찾기', '예상 시험지 3·4', '개념'), (6, 4, '정비례 그래프와 점', '예상 시험지 3', '유형'),
    (7, 4, '반비례 관계 표', '예상 시험지 4', '유형'), (8, 4, '반비례 그래프의 성질', '예상 시험지 12', '유형'),
    (9, 5, '정비례·반비례 그래프와 넓이', '예상 시험지 23', '유형'), (10, 4, '직선·반직선·선분', '예상 시험지 5', '개념'),
    (11, 4, '잘린 정육면체', '예상 시험지 8', '개념'), (12, 4, '한 직선 위의 점과 길이의 비', '예상 시험지 27', '유형'),
    (13, 4, '사각형의 넓이와 거리', '-', '-'), (14, 4, '맞꼭지각', '예상 시험지 6', '유형'),
    (15, 4, '삼각뿔의 위치 관계', '예상 시험지 19', '유형'), (16, 4, '공간에서의 위치 관계', '예상 시험지 19', '개념'),
    (17, 4, '꼬인 위치의 모서리', '예상 시험지 19 · 8', '유형'), (18, 5, '동위각·엇각의 개수', '예상 시험지 14', '개념'),
    (19, 4, '평행선 사이 꺾인 선의 각', '예상 시험지 14', '유형'), (20, 4, '종이 접기와 각', '예상 시험지 14', '개념'),
    (21, 4, '삼각형의 작도 순서', '예상 시험지 17', '개념'), (22, 5, '삼각형이 되는 조건', '예상 시험지 16', '개념'),
    (23, 4, '삼각형의 합동 조건', '예상 시험지 18', '유형'), (24, 4, '합동을 이용한 길이·각', '예상 시험지 25 · 28', '개념')]

# 크게 싣는 적중 쌍: (실제 이미지, 실제 표기, SEL 이미지, SEL 표기, 적중, 포인트)
SOC_SAME = [
    ('S26', '26번 (4점)', 'S_2회_24', '파이널 모의고사 2회 24번', '동일', '체포 시 권리 고지·장애인 의무 고용 <b>자료가 같고</b>, 정답 "자유 / 평등"까지 일치'),
    ('S27', '27번 (4점)', 'S_시험지_27', 'SEL 예상 시험지 27번', '동일', '국민 투표·국민 발안·청원의 <b>정의 문장이 거의 그대로</b> 출제'),
    ('S3', '3번 (3점)', 'S_시험지_11', 'SEL 예상 시험지 11번', '동일', '강강술래·티니클링·플라멩코 <b>같은 자료</b>. SEL 정답 선지가 실제 지문 문장'),
    ('S5', '5번 (4점)', 'S_시험지_4', 'SEL 예상 시험지 4번', '동일', '도윤·라윤 가족 만화, <b>"오빠는 성취 지위" 함정</b>까지 동일'),
    ('S20', '20번 (3점)', 'S_1회_24', '파이널 모의고사 1회 24번', '동일', '4·19 혁명 설명 <b>문장 그대로</b>, 선지 5개 중 4개 일치'),
    ('S14', '14번 (4점)', 'S_2회_12', '파이널 모의고사 2회 12번', '동일', '미디어 정보 확인 방법, <b>선지 4개가 1:1로 대응</b>'),
    ('S10', '10번 (4점)', 'S_1회_6', '파이널 모의고사 1회 6번', '동일', '"차별을 찾아내고 문제를 제기하는 <b>시민 의식</b>" 보기 문장 그대로'),
    ('S9', '9번 (3점)', 'S_문제집_111', '교과서 문제집 111번', '동일', '채용 공고 성차별 사진(키 172cm·훈훈한 외모) <b>같은 사진</b>'),
    ('S17', '17번 (3점)', 'S_문제집_140', '교과서 문제집 140번', '동일', '"간판에 외국어를 쓴 가게가 세련되어 보이고…" <b>발언 그대로</b>'),
    ('S12', '12번 (4점)', 'S_문제집_126', '교과서 문제집 126번', '동일', '인터넷 시대의 새 인사말 <b>같은 그림·같은 문장</b> → 문화의 전체성'),
    ('S24', '24번 (3점)', 'S_1회_27', '파이널 모의고사 1회 27번', '동일', '"주권이 국민에게 있다는 원리" <b>정의 그대로</b>'),
    ('S1', '1번 (3점)', 'S_문제집_2', '교과서 문제집 빈칸 2번', '동일', '"개성과 ( 자아 )을/를 형성" <b>빈칸 문장 그대로</b>'),
]
SOC_TYPE = [
    ('S21', '21번 (4점)', 'S_시험지_28', 'SEL 예상 시험지 28번', '유형', '"복지 요구 증가 → <b>입법부/행정부</b>" 함정 그대로'),
    ('S18', '18번 (4점)', 'S_시험지_20', 'SEL 예상 시험지 20번', '유형', '가족 여행지·반 티셔츠 색 정하기 <b>같은 사례</b>로 넓은 의미의 정치'),
    ('S8', '8번 (4점)', 'S_1회_4', '파이널 모의고사 1회 4번', '유형', '역할 갈등 해결: <b>원인 명확화 + 우선순위</b>, 개인 노력 vs 제도 함정'),
]
MATH_HIT = [
    ('M23', '23번 (4점)', 'M_18', 'SEL 예상 시험지 18번', '유형', 'AB=DE에서 출발, <b>SSA(∠B=∠E, AC=DF) 함정</b>까지 같은 구조'),
    ('M19', '19번 (4점)', 'M_14', 'SEL 예상 시험지 14번', '유형', '평행선 사이 <b>꺾인 선(지그재그)</b>의 각, 같은 그림 유형'),
    ('M9', '9번 (5점·고난도)', 'M_23', 'SEL 예상 시험지 23번', '유형', 'y=ax와 반비례 그래프의 <b>교점 → 도형의 넓이</b>'),
    ('M4', '4번 (4점)', 'M_13', 'SEL 예상 시험지 13번', '유형', '구간별 그래프: <b>변화 없는 시간의 합</b>과 기울기 비교'),
    ('M12', '12번 (4점)', 'M_27', 'SEL 예상 시험지 27번', '유형', '한 직선 위 <b>다섯 점, 중점과 길이의 비</b>'),
    ('M3', '3번 (5점·고난도)', 'M_9', 'SEL 예상 시험지 9번', '유형', '좌표로 주어진 꼭짓점 → <b>다각형의 넓이</b>'),
]


def pair(a, alab, s, slab, kind, pt, subj):
    return (f'<div class="pair"><div class="phd"><span class="bd {"same" if kind=="동일" else "type"}">{kind} 적중</span>'
            f'<span class="t">목일중 {subj} <b>{alab}</b></span><span class="eq">=</span><span class="t">{slab}</span></div>'
            f'<div class="pbd"><figure class="act"><figcaption>실제 시험 · 10월 6일</figcaption><img src="img/{a}.png"></figure>'
            f'<figure class="sel"><figcaption>SEL 자료 · 시험 전 배포</figcaption><img src="img/{s}.png"></figure></div>'
            f'<div class="ppt">✔ {pt}</div></div>')


def page(n, body, cls=''):
    foot = f'<div class="pf"><span>SEL입시연구소 · 2026 2학기 중간고사 적중 리포트</span><span>{n} / 10</span></div>' if n > 1 else ''
    return f'<section class="page {cls}">{body}{foot}</section>'


def head(kicker, title, sub=''):
    return f'<div class="hd"><div class="kk">{kicker}</div><h2>{title}</h2>{f"<div class=sub>{sub}</div>" if sub else ""}</div>'


cnt = lambda L, k: sum(1 for x in L if x[4] == k)
sS, sT, sC = cnt(SOC, '동일'), cnt(SOC, '유형'), cnt(SOC, '개념')
mS, mT, mC = cnt(MATH, '동일'), cnt(MATH, '유형'), cnt(MATH, '개념')
pages = []

# 1. 표지
pages.append(page(1, f'''
<div class="cv-top">
  <div class="brand">SEL입시연구소</div>
  <div class="cv-k">2026학년도 2학기 중간고사 적중 리포트</div>
  <h1>해냈다!</h1>
  <div class="cv-s">목일중학교 1학년 <b>사회 · 수학</b></div>
  <div class="cv-q">"예상문제가 그대로 시험지에 나왔습니다."</div>
  <img class="cv-t" src="img/t1.svg">
  <div class="cv-name">이석준 쌤</div>
</div>
<div class="cv-bot">
  <div class="medal"><div class="mk">사회</div><div class="mv">96<small>점</small></div></div>
  <div class="medal"><div class="mk">수학</div><div class="mv">95<small>점</small></div></div>
  <div class="cv-txt"><b>{STU} 학생</b> · 목일중 1학년<br>2026. 10. 6. 실제 중간고사 결과
  <div class="cv-hit">사회 <b>{sS+sT}/27</b> 문항 동일·유형 적중<br>수학 <b>{mS+mT}/24</b> 문항 유형 적중</div></div>
</div>''', 'cover'))

# 2. 한눈에
def bar(L, N):
    seg = ''.join(f'<span class="sg {c}" style="width:{cnt(L,k)/N*100}%">{k} {cnt(L,k)}</span>' for k, c in (('동일', 'same'), ('유형', 'type'), ('개념', 'conc')) if cnt(L, k))
    return f'<div class="sbar">{seg}</div>'
pages.append(page(2, head('RESULT', '숫자로 보는 2학기 중간고사', '실제 시험지 문항을 SEL 자료와 한 문항씩 대조했습니다.') + f'''
<div class="kpis">
  <div class="kpi"><div class="kl">사회 동일 적중</div><div class="kv">{sS}<small>문항</small></div><div class="kn">자료·문장이 같은 문항</div></div>
  <div class="kpi"><div class="kl">사회 동일+유형</div><div class="kv">{round((sS+sT)/27*100)}<small>%</small></div><div class="kn">27문항 중 {sS+sT}문항</div></div>
  <div class="kpi"><div class="kl">수학 유형 적중</div><div class="kv">{mT}<small>문항</small></div><div class="kn">24문항 중, 5점 2문항 포함</div></div>
  <div class="kpi"><div class="kl">개념까지 포함</div><div class="kv">{round((sS+sT+sC+mS+mT+mC)/51*100)}<small>%</small></div><div class="kn">51문항 중 {sS+sT+sC+mS+mT+mC}문항</div></div>
</div>
<h3>과목별 적중 구성</h3>
<div class="brow"><span class="bl">사회 27문항</span>{bar(SOC, 27)}</div>
<div class="brow"><span class="bl">수학 24문항</span>{bar(MATH, 24)}<span class="none">미적중 1</span></div>
<div class="legend"><span class="sg same">동일</span> 같은 자료·문장·사진 <span class="sg type">유형</span> 같은 유형·같은 함정 <span class="sg conc">개념</span> 같은 개념</div>
<div class="two">
  <div class="card"><h3>학생 성적</h3>
    <div class="sc"><span>사회</span><b>96점</b><em>27문항 중 26문항 정답</em></div>
    <div class="sc"><span>수학</span><b>95점</b><em>24문항 중 23문항 정답</em></div>
    <div class="note">{STU} 학생 · 목일중학교 1학년</div></div>
  <div class="card"><h3>SEL이 시험 전에 준비한 자료</h3>
    <ul><li><b>사회</b> 예상 시험지 30문항 · 파이널 모의고사 2회 60문항</li><li><b>사회</b> 교과서 문제집 (빈칸·OX 100문항 + 교과서 자료 69문항)</li>
    <li><b>수학</b> 예상 시험지 29문항 + 학생별 정오표</li><li><b>공통</b> 개인 성적표와 맞춤 처방</li></ul></div>
</div>
<div class="tq"><img src="img/t2.svg"><div class="bub">교과서 자료 한 장, 선지 한 줄까지 <b>실제 시험 기준</b>으로 만들었습니다.<br>그 결과가 바로 이 리포트입니다!<span>- 이석준 쌤</span></div></div>
'''))

# 3~6. 사회 동일 적중
for i in range(4):
    chunk = SOC_SAME[i * 3:(i + 1) * 3]
    pages.append(page(3 + i, head('SOCIAL · 동일 적중', f'사회 동일 적중 ({i+1}/4)', '왼쪽은 실제 시험지, 오른쪽은 SEL이 시험 전에 나눠 준 자료입니다.') + ''.join(pair(*x, '사회') for x in chunk)))
# 7. 사회 유형 적중
pages.append(page(7, head('SOCIAL · 유형 적중', '사회 유형 적중', '보기 문장과 함정까지 같은 유형으로 미리 연습했습니다.') + ''.join(pair(*x, '사회') for x in SOC_TYPE)))
# 8~9. 수학
for i in range(2):
    pages.append(page(8 + i, head('MATH · 유형 적중', f'수학 유형 적중 ({i+1}/2)', '숫자는 달라도 풀이 구조와 함정이 같은 문항입니다.') + ''.join(pair(*x, '수학') for x in MATH_HIT[i * 3:(i + 1) * 3])))

# 10. 전체 적중표 + 메시지
def table(L, subj):
    rows = ''.join(f'<tr><td>{n}</td><td>{p}</td><td class="l">{t}</td><td class="l">{r}</td><td><span class="tg {dict(동일="same",유형="type",개념="conc").get(k,"no")}">{k if k!="-" else "–"}</span></td></tr>' for n, p, t, r, k in L)
    return f'<table class="all"><tr><th>번호</th><th>배점</th><th>{subj} 문항 내용</th><th>SEL 매칭 자료</th><th>적중</th></tr>{rows}</table>'
pages.append(page(10, head('ALL', '전체 문항 적중표', '사회 27문항 · 수학 24문항 전체') + f'''
<div class="tables">{table(SOC, '사회')}{table(MATH, '수학')}</div>
<div class="end"><img src="img/t1.svg"><div class="msg"><b>해냈다!</b> 사회 96점, 수학 95점.<br>시험지 위에서 다시 만난 SEL의 문제들이 그 증거입니다.
기말고사도 같은 방식으로, 교과서 한 장 한 장 끝까지 함께하겠습니다.<span>- SEL입시연구소 이석준</span></div>
<div class="cta">2학기 기말고사 대비<br><b>상담 접수 중</b></div></div>'''))

css = open(f'{D}/pr.css', encoding='utf-8').read()
html = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>SEL입시연구소 2026 2학기 중간고사 적중 리포트</title><style>{css}</style></head><body>{"".join(pages)}</body></html>'
open(f'{OUT}/SEL_2학기중간_적중리포트.html', 'w', encoding='utf-8').write(html)
print('ok', sS, sT, sC, mS, mT, mC)
