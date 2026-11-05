from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_BREAK
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'documents';OUT.mkdir(exist_ok=True)
BLUE=RGBColor(43,112,180); DARK=RGBColor(19,41,63); GREY=RGBColor(91,107,123)

def para(doc,text='',style=None):
    p=doc.add_paragraph(style=style);p.add_run(text);return p

def heading(doc,text):doc.add_heading(text,level=2)
def bullet(doc,text):doc.add_paragraph(text,style='List Bullet')

def setup(title,subtitle):
    d=Document(); sec=d.sections[0];sec.page_height=Cm(29.7);sec.page_width=Cm(21.0);sec.top_margin=Cm(2.15);sec.bottom_margin=Cm(1.8);sec.left_margin=Cm(2.35);sec.right_margin=Cm(2.35)
    styles=d.styles;norm=styles['Normal'];norm.font.name='Noto Sans CJK KR';norm.font.size=Pt(9.5);norm.font.color.rgb=DARK;norm.paragraph_format.space_after=Pt(6);norm.paragraph_format.line_spacing=1.34
    for sn in ('Title','Heading 1','Heading 2'):
        s=styles[sn];s.font.name='Noto Sans CJK KR';s.font.color.rgb=DARK;s.font.bold=True
    styles['Title'].font.size=Pt(25);styles['Heading 2'].font.size=Pt(12);styles['Heading 2'].font.color.rgb=BLUE;styles['Heading 2'].paragraph_format.space_before=Pt(15);styles['Heading 2'].paragraph_format.space_after=Pt(6)
    lst=styles['List Bullet'];lst.font.name='Noto Sans CJK KR';lst.font.size=Pt(9.5);lst.paragraph_format.space_after=Pt(4)
    d.add_heading(title,0);p=d.add_paragraph();r=p.add_run(subtitle);r.font.color.rgb=GREY;r.font.size=Pt(9)
    sec.header_distance=Cm(.8);head=sec.header.paragraphs[0];head.alignment=WD_ALIGN_PARAGRAPH.RIGHT;r=head.add_run('BR-A  /  PUBLIC CAREER DOCUMENT');r.font.name='Noto Sans CJK KR';r.font.size=Pt(7);r.font.color.rgb=GREY
    foot=sec.footer.paragraphs[0];foot.alignment=WD_ALIGN_PARAGRAPH.RIGHT;r=foot.add_run('김준홍  ·  공개용 요약본  ·  2026.11.04');r.font.name='Noto Sans CJK KR';r.font.size=Pt(7.5);r.font.color.rgb=GREY
    return d

d=setup('김준홍 | 이력서','지원 방향  System / Infrastructure Engineer  ·  Linux & Service Operations')
heading(d,'프로필')
para(d,'네트워크·보안 장비 구축 및 유지보수 경험 약 1년 3개월을 바탕으로 Linux 서버와 서비스 인프라 운영 역량을 확장하고 있습니다. 장비·서비스 설정을 실제 동작 결과로 재검증하는 접근을 중시합니다.')
para(d,'공개 포트폴리오  https://kjhnet.vercel.app  |  GitHub  https://github.com/wnsghd1802')
heading(d,'경력')
para(d,'2024.07.26 — 2025.10.31  |  네트워크 인프라 구축·보안 장비 유지보수 (기업명 비공개)')
bullet(d,'스위치 및 방화벽 장비 설치·교체·유지보수, 설정 비교와 연결 상태 점검을 수행했습니다.')
bullet(d,'장비 교체 후 VLAN 누락을 발견하고 하위 L2 스위치에 필요한 설정을 반영했습니다. 상위 L3 장비 작업은 선배 담당, 최종 통신 복구는 협업 결과입니다.')
bullet(d,'물리 결선 및 통신 경로 확인, 장애 시 현장 설정 비교·재검증을 수행했습니다.')
heading(d,'교육과 기술 실습')
para(d,'2026.08 — 2026.11  |  SKT ALEPH AI+정보보안 교육 과정')
bullet(d,'Ubuntu·Rocky Linux에서 웹, DB, DNS, 파일 공유 서비스 설치 및 기초 설정 실습')
bullet(d,'rsyslog·LogAnalyzer, Wazuh, Zabbix 등 로그 수집·모니터링 및 에이전트 점검')
bullet(d,'GNS3·pfSense·Snort/Suricata 기반 가상 네트워크·IPS 구성 및 차단 검증')
heading(d,'대표 프로젝트')
bullet(d,'PixelGate / Operation Respawn — 4인 팀 가상 기업 인프라 프로젝트, 시스템 보안 담당. Samba 그룹별 읽기·쓰기 권한 검증, Wazuh 로그 연계, DNS 및 서버 하드닝 수행.')
bullet(d,'OISECURE CTF — 웹페이지 구성·아이디어 설계에 참여. 구현 코드 작업에는 AI 보조를 활용.')
heading(d,'학력 · 자격')
para(d,'2023  |  대구과학대학교 응용소프트웨어학과 졸업')
para(d,'정보보안산업기사(2024.10)  ·  리눅스마스터 2급(2024.06)  ·  네트워크관리사 2급(2024.04)')
heading(d,'경력 구분 안내')
para(d,'상기 상용 근무 경력은 네트워크·보안 장비 분야입니다. Linux·DB·로그 시스템은 교육 및 팀 프로젝트 실습으로 구분하며, 단독 상용 Linux 운영 경력으로 기재하지 않습니다.')
d.save(OUT/'BR-A_이력서.docx')

d=setup('김준홍 | 자기소개서','주제  경험을 해석하는 태도 · 협업 · 기술 방향 전환')
heading(d,'1. 결과보다 먼저 확인할 것')
para(d,'처음부터 모든 일을 잘했던 것은 아닙니다. 네트워크 장비를 다루는 현장에서도 실수를 했고, 낯선 상황에서 무엇부터 확인해야 하는지 몰라 시간이 걸리는 일이 있었습니다. 다만 해결 여부를 막연하게 표현하는 대신, 실제로 변경한 설정과 통신 결과를 확인하는 습관을 익히려 했습니다.')
heading(d,'2. 함께 복구한 VLAN 장애 경험')
para(d,'장비 교체 이후 한 구간에서 통신이 이뤄지지 않았던 현장에서 기존 설정과 신규 설정을 비교하다 VLAN 누락을 발견한 적이 있습니다. 저는 담당한 하위 L2 스위치에 필요한 VLAN을 설정했고, 선배는 상위 L3 장비를 조정했습니다. 각자의 작업 후 통신이 정상화됐습니다. 이 경험에서 중요한 것은 혼자서 전부 해결했다는 이야기가 아니라, 제가 확인한 사실을 전달하고 맡은 구간을 정확히 처리해야 팀 전체의 결과가 만들어진다는 점입니다.')
heading(d,'3. 퇴사 이후 다시 시작한 학습')
para(d,'2025년 10월 첫 직장을 마치고 제가 계속 일하고 싶은 분야와 부족한 역량을 돌아봤습니다. 2026년 8월 시작한 정보보안 교육과정에서는 네트워크 경로뿐 아니라 Linux 웹·DB·DNS 서비스, 로그 수집과 접근 권한을 살피기 시작했습니다. 설정 파일이 맞게 보이는 것과 실제 클라이언트에서 접근이 되는 것을 구분해 확인하려고 노력했습니다.')
heading(d,'4. 실패를 지우지 않는 기록')
para(d,'2026년 9월 18일 리추얼 기록에는 복잡한 실습을 완료하지 못했다고 남겼습니다. 9월 21일에는 이전보다 진행했다고 적었습니다. 그 사이에 모든 것이 해결됐다는 뜻이 아니라, 미완료를 인정하고 다시 시도했다는 기록입니다. 확인되지 않은 완성도를 주장하지 않는 태도는 실무에서도 중요하다고 생각합니다.')
heading(d,'5. 앞으로의 방향')
para(d,'현재 목표는 System / Infrastructure Engineer입니다. 기존 네트워크·보안 장비 경험을 기반으로 Linux 서버와 서비스 인프라 구성, 모니터링과 장애 분석 역량을 넓히고 있습니다. 모르는 부분은 질문하고, 담당 범위를 분명히 하고, 조치 이후에는 결과로 검증하는 엔지니어가 되겠습니다.')
para(d,'본 문서는 BR-A 자전적 서사를 취업용 자기소개로 압축한 공개용 요약본입니다. 구체적인 사실관계는 경력기술서와 포트폴리오에 구분해 작성했습니다.')
d.save(OUT/'BR-A_자기소개서.docx')

d=setup('김준홍 | 경력기술서','지원 직무  System / Infrastructure Engineer  ·  근무 경력과 교육 실습 구분')
heading(d,'경력 개요')
para(d,'2024.07.26 — 2025.10.31  |  네트워크·보안 장비 구축 및 유지보수 실무 (기업명·고객사명 비공개)')
para(d,'스위치/방화벽 설치·교체, 운영 중인 장비의 설정 비교, 물리 및 논리 경로 점검, 현장 연결 검증 등 수행. Linux 서버 운영 실무 경력과는 별개입니다.')
heading(d,'주요 경험 01 · VLAN 설정 누락 확인 및 협업 복구')
para(d,'상황  장비 교체 후 특정 구간에서 통신 불가')
para(d,'확인  기존 장비와 신규 장비의 VLAN 설정 차이를 비교해 누락 확인')
para(d,'본인 조치  담당한 하위 L2 스위치 VLAN 구성 수정')
para(d,'협업  상위 L3 장비 설정 보완은 선배가 수행')
para(d,'결과  담당 구간 조치와 선배 작업을 마친 뒤 통신 정상화. 단독 복구로 표현하지 않음.')
heading(d,'주요 경험 02 · 현장 물리 연결 점검')
para(d,'통신 장애 원인 파악 과정에서 물리 결선과 연결 상태 확인을 수행했습니다. 110블록 결선 작업을 스스로 해결한 경험이 있으며, 물리 계층 확인의 중요성을 배웠습니다.')
heading(d,'교육·팀 프로젝트 실습 01 · Linux / Samba 접근 제어')
para(d,'Rocky Linux 9에서 공유 폴더를 구성하고 사용자 그룹별 읽기/쓰기 권한을 분리했습니다. Linux smbclient와 Windows 공유 드라이브 테스트를 통해 관리자 읽기·쓰기 성공, 일반 사용자 읽기 성공·쓰기 거부를 확인했습니다. 교육 팀 프로젝트 작업입니다.')
heading(d,'교육·팀 프로젝트 실습 02 · 로그·서비스·가상망')
bullet(d,'Wazuh Manager / Agent 구성 및 SSH 실패·파일 무결성·SMB 접근과 같은 로그 정책 검토')
bullet(d,'Ubuntu·Rocky Linux 웹·DB·DNS 서버 구성과 시스템 서비스 동작 확인')
bullet(d,'pfSense·Snort/Suricata IPS, GNS3 가상 네트워크 구성 및 DROP 로그와 실제 차단 결과 구분')
heading(d,'강점 · 확인 기준')
bullet(d,'장애가 발생한 위치뿐 아니라 통신 경로의 상·하위 계층과 변경 설정을 비교합니다.')
bullet(d,'협업에서 본인이 수행한 조치와 타인이 담당한 조치를 명확히 구분합니다.')
bullet(d,'로그·설정 상태와 실제 동작 결과를 함께 점검합니다.')
d.save(OUT/'BR-A_경력기술서.docx')
print('Created 3 DOCX documents')