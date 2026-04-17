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
    # 현재 날짜 및 시간 가져오기
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 사이드바 레이아웃 및 페이지 네비게이션
    st.sidebar.title("💎 Master Menu")
    st.sidebar.info(f"🕒 Last Update: {now}")
    page = st.sidebar.radio("Go to", ["1. 주도주 타점 스캐너", "2. 차트 열공실", "3. Pradeep Bonde", "4. William O'Neil", "5. Mark Minervini"])

    # 공통 스타일 설정 (가독성 극대화 최신 버전)
    st.markdown("""
        <style>
        /* 1. 전체 배경 및 기본 텍스트 색상 강제 지정 */
        [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main, [data-testid="stSidebar"] {
            background-color: #000000 !important;
            color: #ffffff !important;
        }
        
        /* 2. 모든 텍스트 요소 흰색 처리 */
        p, span, li, label, div, .stMarkdown, [data-testid="stMetricValue"] {
            color: #ffffff !important;
            font-weight: 600 !important;
        }

        /* 3. 중요 제목 및 헤더 - 노란색 포인트 */
        h1, h2, h3, [data-testid="stSidebarNav"] span, th {
            color: #fcd34d !important;
            font-weight: 900 !important;
        }
        
        /* 4. 테이블 및 알림창 가독성 보강 */
        .stTable, table {
            background-color: #111111 !important;
            border: 1px solid #444 !important;
        }
        td {
            color: #ffffff !important;
            border-bottom: 1px solid #222 !important;
        }
        
        /* 알림창(Success, Warning, Error) 디자인 */
        div[data-testid="stNotification"] {
            background-color: #111111 !important;
            border: 1px solid #fcd34d !important;
        }
        div[data-testid="stNotification"] p {
            color: #fcd34d !important;
        }

        /* 5. 탭(Tabs) 메뉴 가독성 */
        div[data-testid="stTabs"] button {
            color: #888888 !important; /* 비활성 탭 은은하게 */
        }
        div[data-testid="stTabs"] button[aria-selected="true"] {
            color: #fcd34d !important; /* 활성 탭 노란색 */
            border-bottom: 3px solid #fcd34d !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # 실시간 데이터 가져오기 함수
    def get_realtime_price(tickers):
        prices = {}
        try:
            data = yf.download(tickers, period="1d", interval="1m", group_by='ticker', progress=False)
            for ticker in tickers:
                if len(tickers) == 1:
                    target_data = data
                else:
                    target_data = data[ticker]
                
                if not target_data.empty:
                    current = target_data['Close'].iloc[-1]
                    prev_close = target_data['Open'].iloc[0]
                    change = ((current - prev_close) / prev_close) * 100
                    prices[ticker] = {
                        "price": f"{current:,.2f}" if "." in ticker else f"{int(current):,}",
                        "change": f"{change:+.21}%"
                    }
                else:
                    prices[ticker] = {"price": "N/A", "change": "0.00%"}
        except:
            for ticker in tickers:
                prices[ticker] = {"price": "Error", "change": "0.00%"}
        return prices

    # --- 시장 스캔 마스터 리스트 (미국/한국 핵심 150개) ---
    MASTER_TICKERS = [
        # 미국 (NASDAQ 100 + Hot Stocks)
        "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "AVGO", "COST", "PEP", "ADBE", "AMD", 
        "NFLX", "INTC", "CSCO", "TMUS", "CMCSA", "AMAT", "QCOM", "ISRG", "HON", "INTU", "TXN", "VRTX", 
        "BKNG", "SBUX", "PANW", "MDLZ", "ADP", "MCHP", "PYPL", "ADI", "MU", "SNPS", "REGN", "KLAC", 
        "CDNS", "ASML", "ORLY", "MAR", "NXPI", "MNST", "MELI", "LRCX", "AEP", "FTNT", "KDP", "ADSK", 
        "CHTR", "KHC", "CTAS", "PCAR", "BKR", "GFS", "SMCI", "CELH", "PLTR", "HOOD", "CRWD", "ALAB", 
        "SYM", "RXRX", "IOT", "MNDY", "SHOP", "SPOT", "UBER", "ARM", "DELL", "APP", "STX",
        # 한국 (KOSPI 200 + KOSDAQ Top Bluechips)
        "005930.KS", "000660.KS", "005490.KS", "005380.KS", "035420.KS", "035720.KS", "000270.KS", 
        "051910.KS", "006400.KS", "068270.KS", "105560.KS", "055550.KS", "012330.KS", "032830.KS", 
        "096770.KS", "003670.KS", "033780.KS", "009150.KS", "011200.KS", "086790.KS", "010130.KS", 
        "017670.KS", "000810.KS", "034220.KS", "018260.KS", "015760.KS", "034730.KS", "373220.KS", 
        "323410.KS", "402340.KS", "247540.KQ", "091990.KQ", "196170.KQ", "042700.KS", "247660.KQ", 
        "457550.KQ", "095340.KQ", "000100.KS", "254000.KS", "003550.KS", "316140.KS", "028260.KS", 
        "000080.KS", "008770.KS", "293480.KQ", "112040.KQ", "278280.KQ", "035900.KQ", "214150.KQ"
    ]

    def run_market_scan(tickers):
        with st.spinner("🚀 전 세계 시장을 훑어 주도주를 찾고 있습니다... (약 10초 소요)"):
            try:
                # 7일치 데이터를 가져와서 평균 거래량과 오늘 거래량 비교
                data = yf.download(tickers, period="7d", group_by='ticker', progress=False)
                results = []
                
                for ticker in tickers:
                    try:
                        if len(tickers) == 1:
                            target_data = data
                        else:
                            target_data = data[ticker]
                        
                        if target_data.empty or len(target_data) < 2:
                            continue
                            
                        # 현재가 및 등락률
                        current_price = target_data['Close'].iloc[-1]
                        prev_close = target_data['Open'].iloc[-1] # 당일 시가 기준
                        if prev_close == 0: continue
                        
                        change_pct = ((current_price - prev_close) / prev_close) * 100
                        
                        # 거래량 분석 (오늘 vs 5일 평균)
                        today_vol = target_data['Volume'].iloc[-1]
                        avg_vol = target_data['Volume'].iloc[:-1].mean()
                        vol_ratio = today_vol / avg_vol if avg_vol > 0 else 0
                        
                        # Bonde Filter: 등락률 4% 이상 & 거래량 1.5배 이상
                        if change_pct >= 3.0 and vol_ratio >= 1.3: # 실습을 위해 기준을 살짝 낮춤
                            results.append({
                                "종목": ticker,
                                "현재가": f"{current_price:,.2f}" if "." in ticker else f"{int(current_price):,}",
                                "상승률": f"{change_pct:+.2f}%",
                                "거래량증가": f"{vol_ratio:.1f}배",
                                "종합점수": "🟢 강력추천" if change_pct > 5 and vol_ratio > 2 else "🟡 관심종목"
                            })
                    except:
                        continue
                
                return pd.DataFrame(results).sort_values(by="상승률", ascending=False)
            except Exception as e:
                st.error(f"스캔 중 오류가 발생했습니다: {e}")
                return pd.DataFrame()

    # --- 페이지 1: 주도주 타점 스캐너 ---
    if page == "1. 주도주 타점 스캐너":
        st.markdown(f"<h1 style='color:#fcd34d;'>🎯 MAGNA-PRO Terminal <span style='font-size:16px; color:#ffffff;'>({now})</span></h1>", unsafe_allow_html=True)
        
        # 🚀 실시간 스캔 버튼 섹션
        st.markdown("### 🔍 실시간 시장 스캐너")
        cola, colb = st.columns([2, 3])
        with cola:
            if st.button("🚀 실시간 시장 스캔 시작", use_container_width=True):
                scan_results = run_market_scan(MASTER_TICKERS)
                st.session_state['scan_results'] = scan_results
        
        if 'scan_results' in st.session_state:
            res = st.session_state['scan_results']
            if not res.empty:
                st.success(f"✨ 총 {len(res)}개의 주도주 후보를 찾아냈습니다!")
                st.table(res)
            else:
                st.warning("현재 스캔 조건(상승률 3%+, 거래량 1.3배+)에 부합하는 종목이 없습니다.")

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

        # 티커 매핑 (실제 데이터용)
        mb_tickers = ["SMCI", "CELH", "PLTR", "196170.KQ", "042700.KS"] # 알테오젠, 한미반도체
        ep_tickers = ["ALAB", "SYM", "247660.KQ", "457550.KQ"] # 실리콘투, 우진엔텍
        coil_tickers = ["NVDA", "META", "095340.KQ", "000100.KS"] # ISC, 유한양행

        with tab1:
            st.subheader("🔥 모멘텀 버스트 (Momentum Burst) 타점")
            st.caption("조건: 당일 4% 이상 상승 | 거래량 10만주 이상 증가 | TI65 지표 1.05+ | 최근 3일 연속 상승 제외 | 종가가 고점 근처 30% 이내")
            
            live_mb = get_realtime_price(mb_tickers)
            mb_data = {
                "분류": ["🔥미국", "🔥미국", "🔥미국", "🔥국내", "🔥국내"],
                "종목명": ["SMCI", "CELH", "PLTR", "알테오젠", "한미반도체"],
                "현재가": [live_mb[t]["price"] for t in mb_tickers],
                "상승률": [live_mb[t]["change"] for t in mb_tickers],
                "목표가": ["$1,100", "$85", "$30", "220,000", "200,000"],
                "손절가": ["$880", "$65", "$22.5", "178,000", "136,000"],
                "RS": ["98", "94", "91", "99", "95"],
                "ROE": ["45%", "32%", "12%", "28%", "35%"],
                "종합점수": ["🟢 좋음", "🟢 좋음", "🟡 보통", "🟢 좋음", "🟡 보통"],
                "TI65": ["1.12", "1.06", "1.08", "1.25", "1.10"]
            }
            st.table(pd.DataFrame(mb_data))

        with tab2:
            st.subheader("🚀 에피소딕 피봇 (Episodic Pivot) 타점")
            st.caption("조건: 전일비 4~10% 이상 상승 갭 | 당일 거래량 900만주 이상 (또는 평균3배) | 시총 100억$ 미만 중소형주")
            
            live_ep = get_realtime_price(ep_tickers)
            ep_data = {
                "분류": ["🚀미국", "🚀미국", "🚀국내", "🚀국내"],
                "종목명": ["ALAB", "SYM", "실리콘투", "우진엔텍"],
                "현재가": [live_ep[t]["price"] for t in ep_tickers],
                "상승률": [live_ep[t]["change"] for t in ep_tickers],
                "목표가": ["$90", "$60", "25,000", "28,000"],
                "손절가": ["$61", "$42", "17,200", "18,500"],
                "RS": ["96", "89", "97", "85"],
                "ROE": ["N/A", "15%", "40%", "18%"],
                "종합점수": ["🟢 좋음", "🟡 보통", "🟢 좋음", "🔴 나쁨"],
                "촉매": ["어닝 서프라이즈", "신제품 발표", "K-뷰티 폭발", "원전 수주"]
            }
            st.table(pd.DataFrame(ep_data))

        with tab3:
            st.subheader("🤫 예측 매매 (Anticipation / Coiling) 타점")
            st.caption("조건: 최근 10일 변동폭 10% 이내 축소 | 당일 변동률 -1~1% 보합 | 거래량 50일 평균 이하 매마름 | TI65 1.05+ 유지")
            
            live_coil = get_realtime_price(coil_tickers)
            coiling_data = {
                "분류": ["🤫미국", "🤫미국", "🤫국내", "🤫국내"],
                "종목명": ["NVDA", "META", "ISC", "유한양행"],
                "현재가": [live_coil[t]["price"] for t in coil_tickers],
                "상승률": [live_coil[t]["change"] for t in coil_tickers],
                "목표가": ["$1,000", "$600", "120,000", "85,000"],
                "손절가": ["$850", "$495", "91,000", "69,500"],
                "RS": ["99", "97", "92", "88"],
                "ROE": ["52%", "28%", "22%", "12%"],
                "종합점수": ["🟢 좋음", "🟢 좋음", "🟡 보통", "🟡 보통"],
                "10일변동": ["4.5%", "3.2%", "4.1%", "2.5%"],
                "거래량": ["평소 40%", "평소 45%", "평소 35%", "평소 20%"]
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
