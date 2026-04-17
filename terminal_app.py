import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime
import os

# 1. 암호 보안 설정 (암호: 1353)
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"]:
        return True

    # 암호 입력 화면 UI
    st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>🔐 Anti-Gravity Private Terminal</h1>", unsafe_allow_html=True)
    password = st.text_input("Access Code를 입력하십시오.", type="password")
    if st.button("Unlock"):
        if password == "1353":
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("❌ Access Denied. 코드가 일치하지 않습니다.")
    return False

if check_password():
    # 사이드바 레이아웃 및 페이지 네비게이션
    st.sidebar.title("💎 Master Menu")
    page = st.sidebar.radio("Go to", ["1. 주도주 타점 스캐너", "2. 차트 열공실", "3. Pradeep Bonde", "4. William O'Neil", "5. Mark Minervini"])

    # 공통 스타일 설정 (흰색 굵은 글씨 및 다크마크 친화적 카드)
    st.markdown("""
        <style>
        .main { background-color: #0e1117; }
        .stMarkdown, .stText, p, h1, h2, h3, span, td, th { color: #FFFFFF !important; font-weight: bold !important; }
        .stTable { background-color: #262730; border-radius: 10px; }
        div[data-testid="stTabs"] button { font-weight: 800 !important; font-size: 18px !important; color: #FFFFFF !important; }
        div[data-testid="stMetricValue"] { color: #FFFFFF !important; font-weight: 900 !important; }
        </style>
    """, unsafe_allow_html=True)

    # --- 페이지 1: 주도주 타점 스캐너 ---
    if page == "1. 주도주 타점 스캐너":
        st.header("🎯 MAGNA-PRO: 본데의 3대 핵심 타점 스캐너")
        
        # 시장 상황 필터 연동 (신호등)
        st.markdown("---")
        col1, col2 = st.columns([1, 4])
        with col1:
            st.markdown("<div style='text-align:center;'><h3 style='margin-bottom:0;'>🚦 시장 신호등</h3><div style='font-size:70px; margin-top:-10px;'>🟢</div></div>", unsafe_allow_html=True)
        with col2:
            st.write("### 현재 시장 상황 (Situational Awareness) : 위험 회피 해제")
            st.write("현재 미 증시에서 **4% 이상 돌파(Breakout) 종목 수가 50개를 초과**했습니다. 이는 시장의 폭발적인 매수세가 살아있음을 의미합니다.")
            st.error("👉 **본데의 디렉션:** 돌파 매매(MB)와 에피소딕 피봇(EP)을 공격적으로 노려야 할 시기입니다. 웅크리지 마십시오!")
        st.markdown("---")

        # 원클릭 프리셋 버튼 탭
        tab1, tab2, tab3 = st.tabs(["🔥 1. 모멘텀 버스트 (MB)", "🚀 2. 실적 홈런주 (EP)", "🤫 3. 조용한 눌림목 (Anticipation)"])

        with tab1:
            st.subheader("🔥 모멘텀 버스트 (Momentum Burst) 타점")
            st.caption("조건: 당일 4% 이상 상승 | 거래량 10만주 이상 증가 | TI65 지표 1.05+ | 최근 3일 연속 상승 제외 | 종가가 고점 근처 30% 이내")
            
            # 파이썬 데이터 프레임 시뮬레이션
            mb_data = {
                "분류": ["🔥미국", "🔥미국", "🔥미국", "🔥미국", "🔥미국", "🔥국내", "🔥국내", "🔥국내", "🔥국내", "🔥국내"],
                "종목명": ["SMCI", "CELH", "PLTR", "HOOD", "CRWD", "알테오젠", "한미반도체", "피에스케이홀딩스", "삼양식품", "제룡전기"],
                "현재가": ["$912.0", "$68.5", "$24.1", "$18.5", "$320.4", "185,200원", "142,000원", "45,300원", "320,500원", "48,200원"],
                "상승률": ["+6.2%", "+4.8%", "+5.1%", "+7.2%", "+4.1%", "+8.5%", "+5.2%", "+6.8%", "+4.5%", "+7.1%"],
                "거래량수준": ["1.5배", "1.8배", "2.1배", "1.4배", "1.6배", "3.2배", "1.5배", "2.4배", "1.8배", "4.1배"],
                "TI65 (추세)": ["1.12", "1.06", "1.08", "1.15", "1.05", "1.25", "1.10", "1.18", "1.08", "1.32"],
                "종가위치": ["고가대비 -5%", "종가=고가", "고가대비 -15%", "고가대비 -10%", "고가대비 -28%", "종가=고가", "고가대비 -5%", "고가대비 -8%", "고가대비 -12%", "종가=고가"]
            }
            st.table(pd.DataFrame(mb_data))

        with tab2:
            st.subheader("🚀 에피소딕 피봇 (Episodic Pivot) 타점")
            st.caption("조건: 전일비 4~10% 이상 상승 갭 | 당일 거래량 900만주 이상 (또는 평균3배) | 시총 100억$ 미만 중소형주")
            
            ep_data = {
                "분류": ["🚀미국", "🚀미국", "🚀미국", "🚀미국", "🚀미국", "🚀국내", "🚀국내", "🚀국내", "🚀국내", "🚀국내"],
                "종목명": ["ALAB", "SYM", "RXRX", "IOT", "MNDY", "HD현대일렉트릭", "실리콘투", "브이티", "클리오", "우진엔텍"],
                "현재가": ["$65.2", "$45.1", "$12.8", "$28.4", "$230.5", "254,000원", "18,400원", "24,500원", "35,100원", "19,800원"],
                "상승갭(Gap)": ["+8.5%", "+6.2%", "+9.1%", "+4.5%", "+5.8%", "+12.5%", "+8.4%", "+15.2%", "+6.1%", "+7.5%"],
                "당일거래량": ["1,200만 주", "평소 5배", "1,500만 주", "평소 4배", "950만 주", "300만 주", "1,200만 주", "850만 주", "210만 주", "540만 주"],
                "시가총액": ["$3.5B", "$2.8B", "$1.2B", "$4.1B", "$9.5B", "9.1조", "1.1조", "8,500억", "6,200억", "1,800억"],
                "촉매(뉴스)": ["어닝 서프라이즈", "신제품 발표", "FDA 승인", "가이던스 상향", "흑자 전환", "슈퍼 사이클 수주", "아마존 입점 대박", "일본 매출 폭발", "분기 최대 실적", "신규 원전 수주"]
            }
            st.table(pd.DataFrame(ep_data))

        with tab3:
            st.subheader("🤫 예측 매매 (Anticipation / Coiling) 타점")
            st.caption("조건: 최근 10일 변동폭 10% 이내 축소 | 당일 변동률 -1~1% 보합 | 거래량 50일 평균 이하 매마름 | TI65 1.05+ 유지")
            
            coiling_data = {
                "분류": ["🤫미국", "🤫미국", "🤫미국", "🤫미국", "🤫미국", "🤫국내", "🤫국내", "🤫국내", "🤫국내", "🤫국내"],
                "종목명": ["NVDA", "META", "UBER", "SHOP", "SPOT", "에코프로머티", "ISC", "두산테스나", "주성엔지니어링", "유한양행"],
                "현재가": ["$870.52", "$510.2", "$75.4", "$82.1", "$310.5", "125,000원", "95,400원", "51,200원", "34,800원", "72,100원"],
                "당일변동률": ["+0.2%", "-0.1%", "+0.5%", "-0.8%", "+0.1%", "-0.4%", "+0.2%", "-0.5%", "+0.8%", "0.0%"],
                "10일변동폭(Coiling)": ["4.5%(완료)", "3.2%(강력)", "6.1%", "5.5%", "2.8%(강력)", "3.5%(강력)", "4.1%(완료)", "5.8%", "3.9%(강력)", "2.5%(강력)"],
                "거래량상태(Dry-up)": ["평소 40%", "평소 45%", "평소 30%", "평소 60%", "평소 50%", "평소 25%", "평소 35%", "평소 40%", "평소 30%", "평소 20%"],
                "TI65 (추세)": ["1.15", "1.10", "1.08", "1.06", "1.09", "1.08", "1.12", "1.05", "1.07", "1.14"]
            }
            st.table(pd.DataFrame(coiling_data))

    # --- 페이지 2: 차트 열공실 ---
    elif page == "2. 차트 열공실":
        st.header("📈 VCP 파동 및 EP 돌파 원리 학습")
        st.subheader("1. VCP (변동성 축소 패턴)")
        st.write("주가가 왼쪽에서 오른쪽으로 갈수록 파동의 크기가 줄어드는 현상입니다. (예: 25% -> 12% -> 6% -> 3%)")
        st.subheader("2. 9M EP (900만 주 에피소딕 피봇)")
        st.write("강력한 뉴스와 함께 거래량이 폭발하며 갭상승하는 지점입니다. 기관 유입의 증거입니다.")

    # --- 페이지 3: 본데는 누구인가? ---
    elif page == "3. Pradeep Bonde":
        st.header("🚀 1억 달러 트레이더들의 스승, 프라딥 본데 (Pradeep Bonde, a.k.a StockBee)")
        st.markdown("---")
        
        st.subheader("👤 인물 소개: 월가의 전설적인 스윙 트레이더")
        st.write("프라딥 본데(Pradeep Bonde)는 온라인에서 **'스탁비(StockBee)'**라는 필명으로 더 잘 알려진 25년 경력의 전업 트레이더이자, 월가에서 가장 성공적인 트레이더들을 배출한 멘토입니다. 단돈 수천 달러를 1억 달러(약 1,300억 원) 이상으로 불린 크리스찬 쿨라매기(Kristjan Kullamägi)를 비롯해, 그의 매매법을 배워 7자리에서 9자리의 수익을 달성한 수많은 트레이더들이 그를 '스승'으로 부르며 존경을 표합니다. 화려한 마케팅이나 과장 광고 없이 오직 실력과 입소문만으로 수백, 수천 명의 제자들을 양성해 온 그는 현재 시장에서 가장 큰 영향력을 미치는 실전 트레이더 중 한 명입니다.")
        
        st.subheader("🛤️ 트레이딩 여정: 물류 마케터에서 트레이딩 팩토리의 수장으로")
        st.write("인도에서 DHL과 FedEx 프랜차이즈의 마케팅 책임자로 일했던 프라딥 본데는 1990년대 후반 닷컴 버블 시기에 미국으로 건너와 주식 시장에 입문했습니다. 초기에는 그 역시 큰 수익과 뼈아픈 손실을 반복하는 전형적인 초보 트레이더의 롤러코스터를 겪었습니다. 이 과정에서 그는 과거 비즈니스와 물류 분야에서 쌓았던 '효율성과 시스템화'의 경험을 트레이딩에 접목했습니다. 트레이딩을 단순한 도박이 아닌, 철저한 프로세스 기반의 비즈니스로 재설계한 것입니다. 그는 열정만으로는 돈을 벌 수 없으며, 흔들리지 않는 규율과 시스템만이 성공을 만든다고 굳게 믿습니다.")
        
        st.subheader("🧠 스탁비의 3대 핵심 트레이딩 철학")
        st.write("**1. 허황된 꿈을 버리고 안타(Singles)를 쳐라**")
        st.write("많은 트레이더들이 열대의 섬이나 럭셔리 카를 꿈꾸는 이른바 '섬의 환상(Island Mentality)'에 빠져 일확천금을 노리다 파산합니다. 프라딥 본데는 홈런 한 방을 노리기보다 작고 확실한 수익(Singles)을 지속적으로 누적하여 복리로 굴리는, 지루하지만 필수적인 과정을 마스터하라고 강조합니다.")
        st.write("**2. 절차적 기억(Procedural Memory)과 딥 다이브(Deep Dive)**")
        st.write("그는 훌륭한 트레이더는 장중에 머리로 고민하지 않고, 자전거를 타듯 몸이 반사적으로 반응하는 '절차적 기억'을 통해 매매해야 한다고 말합니다. 이를 위해 수천 개의 과거 폭등 차트와 매매 패턴을 집중적으로 분석하고 뇌에 각인시키는 '딥 다이브(Deep Dive)' 훈련을 매일/매주 끊임없이 반복할 것을 제자들에게 가르칩니다.")
        st.write("**3. 셀프 리더십(Self-Leadership)**")
        st.write("트레이딩은 본인이 스스로 코치가 되어 문제를 해결하고 피드백을 주어야 하는 고독한 직업입니다. 손실이 나더라도 스스로 동기를 부여하고, 매매 일지를 통해 문제점을 찾아내 교정하는 '셀프 리더십'이야말로 성공한 트레이더와 실패한 트레이더를 가르는 가장 결정적인 차이입니다.")
        
        st.subheader("📈 핵심 매매 전략")
        st.write("- **에피소딕 피벗 (Episodic Pivots, EP):** 깜짝 실적, 신약 승인, 새로운 테마 등 기업의 근본적인 이야기를 바꾸는 '강력한 촉매제(Catalyst)'가 발생했을 때 진입하는 전략입니다. 시장이 새로운 가치를 반영하기 위해 갭상승과 엄청난 거래량(예: 900만 주 이상)을 동반할 때, 그 폭발적인 상승의 초입에 탑승해 수익을 극대화합니다.")
        st.write("- **모멘텀 버스트 (Momentum Bursts):** 강한 상승 추세에 있는 주식이 짧고 좁은 조정을 거친 후, 하루에 4% 이상 급등하며 폭발할 때 진입합니다. 3~5일이라는 짧은 기간 동안 단기 수익을 챙기고 나오는 스탁비의 주력 '안타' 기법입니다.")
        st.write("- **완벽한 종목 선정 필터 (MAGNA 53+ CAP 10x10):** 폭발적으로 성장할 주식을 찾기 위해 매출 급성장(M, A), 갭상승(G), 기관의 무관심(N), 애널리스트 상향(A)의 조건을 따지며, 특히 시가총액 100억 달러 미만이면서 상장 10년 이내인 기업에 집중합니다.")
        st.write("- **상황 인식 (Situational Awareness):** 아무리 훌륭한 셋업도 시장 환경이 나쁘면 실패합니다. 매일 시장 전체 종목의 상승/하락 비율(Market Breadth)을 모니터링하여 '오늘 돌파 매매가 통하는 장인가?' 판단하고 매매 비중을 조절하는 신호등 역할을 합니다.")
        
        st.subheader("🤝 멘토링 커뮤니티, StockBee")
        st.write("프라딥 본데는 2005년 무렵부터 블로그를 통해 자신의 기법을 공유하기 시작했고, 'StockBee(stockbee.biz)'라는 유료 커뮤니티를 설립했습니다. 그 어떤 과장 광고 없이, 초보자부터 수백억을 굴리는 베테랑 트레이더들까지 매일 줌(Zoom) 미팅을 통해 시장을 분석하고 토론하며 성장하는 '트레이딩 팩토리'로 기능하고 있습니다.")

    # --- 페이지 4, 5 ---
    elif page == "4. William O'Neil":
        st.header("🦅 William O'Neil (CAN SLIM)")
        st.markdown("<h3 style='color: #FFFFFF; font-weight: bold;'>성장주 투자의 전설이자 IBD의 창립자, CAN SLIM 전략의 창시자</h3>", unsafe_allow_html=True)
        st.markdown("---")

        st.subheader("1. 그는 누구인가?")
        st.write("**윌리엄 오닐(1932~2023)**은 월스트리트에서 가장 존경받는 투자 전략가 중 한 명으로, 30세의 젊은 나이에 뉴욕증권거래소(NYSE) 의석을 최연소로 매입한 인물입니다. 단순한 직관이 아닌 과거 100년간 대폭등한 주식들의 공통점을 통계적으로 분석하여 CAN SLIM이라는 필승 공식을 정립했습니다.")

        st.subheader("2. 핵심 투자 철학: CAN SLIM 전략")
        st.write("오닐은 주가가 폭발하기 직전의 성장주가 갖춰야 할 7가지 조건을 제시했습니다.")
        st.write("- **C (Current Earnings):** 현재 분기 주당순이익(EPS)이 전년 대비 최소 25% 이상 급증.")
        st.write("- **A (Annual Earnings):** 연간 이익 성장률이 최근 3년간 가속화(ROE 17% 이상 선호).")
        st.write("- **N (New):** 신제품, 경영진 교체, 혹은 신고가(New High) 돌파 등의 새로운 촉매제.")
        st.write("- **S (Supply and Demand):** 공급보다 수요가 강한 주식(유통 주식수가 적거나 대량 거래 동반).")
        st.write("- **L (Leader or Laggard):** 업종 내 1등주(Relative Strength 점수 80~90점 이상).")
        st.write("- **I (Institutional Sponsorship):** 우량 기관 투자자들의 매집 흔적.")
        st.write("- **M (Market Direction):** 시장 전체의 추세(강세장 확인 필수).")

        st.subheader("3. 전매특허 타점: 컵 앤 핸들 (Cup and Handle)")
        st.write("오닐은 주가가 바닥권을 다지고 '컵' 모양의 조정을 거친 뒤, 손잡이(Handle) 부분에서 거래량을 동반하며 전고점을 돌파하는 순간을 가장 완벽한 매수 타이밍으로 봅니다.")

        st.subheader("4. 시장 진단의 기준: 팔로우스루 데이 (FTD)")
        st.write("하락장 끝에서 시장이 다시 상승 추세로 돌아섰음을 알리는 '팔로우스루 데이(Follow-Through Day)' 개념을 창시하여, 거북이투자전문가님의 시스템에서도 가장 중요한 시장 신호등 역할을 하고 있습니다.")

        st.subheader("🎙️ 오닐의 명언 (Master's Advice)")
        st.error('"주식 투자에서 가장 큰 실수는 하락 중인 주식을 물타기 하는 것이다. 오르는 주식을 사고, 떨어지는 주식은 기계적으로 손절하라."\n\n"RS 점수가 90점 미만인 잡주에는 눈길도 주지 마십시오. 시장보다 강하게 튀어 오르는 대장주만이 당신을 부자로 만들어 줄 것입니다."')

    elif page == "5. Mark Minervini":
        st.header("🧮 Mark Minervini (SEPA)")
        st.markdown("<h3 style='color: #FFFFFF; font-weight: bold;'>현대판 제시 리버모어, 변동성 축소 패턴(VCP)의 창시자이자 미국 투자 챔피언</h3>", unsafe_allow_html=True)
        st.markdown("---")

        st.subheader("1. 그는 누구인가?")
        st.write("마크 미너비니는 30년 이상의 경력을 가진 월스트리트의 전설적인 트레이더입니다. 1997년 미국 투자 챔피언십(USIC)에 자기 자본으로 참가하여 연간 155%라는 경이로운 수익률로 우승하며 이름을 알렸습니다. 수만 권의 차트를 분석하여 주가가 폭발하기 직전의 공통적인 기술적 특징을 정립한 SEPA(특수 진입점 분석) 전략의 창시자이기도 합니다.")

        st.subheader("2. 핵심 투자 철학: VCP 패턴 (Volatility Contraction Pattern)")
        st.write("미너비니 투자의 정수는 **'변동성의 축소'**에 있습니다.")
        st.write("- **파동의 원리:** 주가가 상승하기 직전에는 매도세가 소진되면서 주가의 흔들림(파동)이 점점 좁아집니다. (예: 20% 흔들림 → 10% → 5% → 2%)")
        st.write("- **치트 에어리어(Cheat Area):** 파동이 극도로 작아져 거래량이 먼지처럼 말라붙은 지점을 '치트 에어리어'라고 부르며, 이곳이 바로 리스크는 가장 작고 보상은 가장 큰 최적의 매수 타점입니다.")

        st.subheader("3. SEPA 전략의 5가지 요소")
        st.write("그는 단순히 차트만 보지 않고 아래 5가지가 일치할 때만 총을 쏩니다.")
        st.write("- **추세(Trend):** 반드시 2단계 상승 추세에 있는 종목일 것.")
        st.write("- **펀더멘털(Fundamentals):** 순이익, 매출, 이익률의 폭발적 성장.")
        st.write("- **촉매제(Catalyst):** 주가를 밀어 올릴 강력한 재료(신제품, 뉴스 등).")
        st.write("- **진입점(Entry Point):** 저항이 적은 지점에서의 VCP 돌파.")
        st.write("- **퇴장점(Exit Point):** 손실을 제한하는 기계적 손절매.")

        st.subheader("4. 위험 관리의 대가")
        st.write("미너비니는 \"나는 수익을 관리하지 않는다. 오직 **위험(Risk)**만 관리한다. 수익은 알아서 따라오는 것이다\"라고 강조합니다. 그는 평균적으로 -5% 내외의 매우 타이트한 손절선을 유지하며, 승률보다 **수익/손실 비율(Risk/Reward Ratio)**을 극대화하는 전략을 구사합니다.")

        st.subheader("🎙️ 미너비니의 명언 (Master's Advice)")
        st.error('"당신이 틀렸을 때 가장 적게 잃는 법을 배우십시오. 그것이 주식 시장에서 살아남는 유일한 방법입니다."\n\n"테니스공처럼 튀어 오르는 주식을 사십시오. 바닥에서 바들바들 떠는 달걀 같은 주식은 쳐다보지도 마십시오."')

    # 하단 고정 테마 (AI 생성 이미지 연동)
    st.sidebar.markdown("---")
    st.sidebar.write("거북이투자전문가 전용 터미널")
    
    # 앰버서더 이미지 로드 시도
    if os.path.exists("bull_market_ambassador.png"):
        st.sidebar.image("bull_market_ambassador.png", width=150)
    else:
        st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzI5yZq00eP8vE8XG9-L_9u_vB_W_K7uB6A&s", width=150)
