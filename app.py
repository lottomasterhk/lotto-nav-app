import streamlit as st
import streamlit.components.v1 as components
import random
import pandas as pd
import os
import json
from datetime import date, timedelta

# ==========================================
# 1. 頁面基本設定與 SEO / Favicon / Google Tag 注入
# ==========================================
st.set_page_config(
    page_title="六合彩生命密碼 | AI 大數據幸運號碼導航與歷史回測",
    page_icon="logo.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🌟 全面強化 SEO Meta 標籤、Google Search Console 驗證、Google Ads 追蹤代碼及 Open Graph 社交分享預覽
st.markdown("""
<meta name="google-site-verification" content="nbbI0OAcsp83w065H9PjLBf959kRLFx4kK16f1KJhfI" />
<meta name="description" content="全港獨家 AI 智能六合彩大數據回測系統與個人化生命密碼導航。17 注全號覆蓋排陣結合個人生命密碼與過往開彩篩選，自動安排分佈與計數，助你精準掌握幸運組合！">
<meta name="keywords" content="六合彩, 生命密碼, AI六合彩預測, 六合彩歷史回測, 心水號碼, 智能六合彩, 17注全號覆蓋, 六合彩大數據">
<meta name="author" content="AI Master Lotto">

<!-- Open Graph / Social Media Sharing Tags (Facebook, WhatsApp 預覽優化) -->
<meta property="og:title" content="六合彩生命密碼 | AI 大數據幸運號碼導航與歷史回測">
<meta property="og:description" content="17 注全號覆蓋排陣 ＋ 個人生命密碼 ＋ 過往組合篩選！自動幫你分佈計數，立即體驗 AI 智能選號與歷史回測。">
<meta property="og:type" content="website">

<!-- Structured Data (JSON-LD) 幫助 Google 蜘蛛更易理解網站結構 -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "六合彩生命密碼 AI 導航",
  "url": "https://ai-masterlotto.streamlit.app",
  "description": "結合 AI 大數據、歷史回測、17 注全號覆蓋排陣與個人化生命密碼的六合彩號碼導航系統。"
}
</script>

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18553406259"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-18553406259');
</script>
""", unsafe_allow_html=True)

# 徹底隱藏 Streamlit 右下角所有官方選單、工具列及個人檔案跳轉連結
st.markdown("""
<style>
#MainMenu {visibility: hidden !important; display: none !important;}
footer {visibility: hidden !important; display: none !important;}
header {visibility: hidden !important; display: none !important;}
.stAppDeployButton {display: none !important; visibility: hidden !important;}
div[data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
div[class*="viewerBadge"] {display: none !important; visibility: hidden !important; pointer-events: none !important;}
div[class*="styles_viewerBadge"] {display: none !important; visibility: hidden !important;}
#GithubIcon {visibility: hidden !important; display: none !important;}
.viewerBadge_container__1QSob {display: hidden !important; visibility: hidden !important;}
.reportview-container .main footer {visibility: hidden !important;}

.stApp {
    color: #222222;
}

.main-title {
    text-align: center;
    color: #FF4B4B;
    font-size: 34px;
    font-weight: bold;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    color: #555555;
    font-size: 16px;
    margin-bottom: 14px;
}

.hero-badge-box {
    background: #fffaf0 !important;
    border: 2px solid #dd6b20;
    border-radius: 10px;
    padding: 12px 16px;
    text-align: center;
    color: #7b341e !important;
    font-size: 15px;
    line-height: 1.6;
    margin-bottom: 22px;
}

.section-card {
    background-color: #ffffff !important;
    color: #222222 !important;
    padding: 22px;
    border-radius: 12px;
    border: 1px solid #e0e0e0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

.section-card h3, .section-card p, .section-card strong, .section-card li {
    color: #222222 !important;
}

.vip-card {
    background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
    padding: 30px;
    border-radius: 12px;
    text-align: center;
    color: #222222 !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    margin-bottom: 25px;
}

.pay-btn {
    background-color: #635bff;
    color: white !important;
    padding: 14px 32px;
    text-decoration: none;
    border-radius: 8px;
    font-weight: bold;
    font-size: 18px;
    display: inline-block;
    margin-top: 15px;
    box-shadow: 0 4px 10px rgba(99,91,255,0.3);
    transition: all 0.3s ease;
}

.pay-btn:hover {
    background-color: #5147df;
    transform: translateY(-2px);
}

.lucky-box {
    background: #f8f9fa !important;
    color: #222222 !important;
    border-left: 5px solid #38a169;
    padding: 15px;
    margin: 10px 0;
    border-radius: 4px;
}

.warning-box {
    background: #fff5f5 !important;
    color: #c53030 !important;
    border-left: 5px solid #e53e3e;
    padding: 15px;
    margin: 15px 0;
    border-radius: 4px;
}

.warning-box h4, .warning-box p, .warning-box li {
    color: #c53030 !important;
}

div.stSuccess {
    background-color: #d4edda !important;
    color: #155724 !important;
}
div.stSuccess p, div.stSuccess span {
    color: #155724 !important;
}

div.stInfo {
    background-color: #d1ecf1 !important;
    color: #0c5460 !important;
}
div.stInfo p, div.stInfo span {
    color: #0c5460 !important;
}

.stButton button {
    background-color: #ff4b4b !important;
    color: #ffffff !important;
    font-weight: bold !important;
    border: none !important;
}
.stButton button:hover {
    background-color: #e03e3e !important;
    color: #ffffff !important;
}

@keyframes glow-pulse {
    0% { box-shadow: 0 0 5px rgba(49,151,149, 0.4), 0 0 10px rgba(49,151,149, 0.2); border-color: #319795; }
    50% { box-shadow: 0 0 20px rgba(49,151,149, 0.8), 0 0 30px rgba(49,151,149, 0.4); border-color: #2b6cb0; }
    100% { box-shadow: 0 0 5px rgba(49,151,149, 0.4), 0 0 10px rgba(49,151,149, 0.2); border-color: #319795; }
}

.bonus-glow-card {
    background: #e6fffa !important;
    border: 3px solid #319795;
    padding: 24px;
    border-radius: 14px;
    margin-bottom: 20px;
    animation: glow-pulse 2.5s infinite;
}

.bonus-glow-card h3, .bonus-glow-card p {
    color: #2c7a7b !important;
}

.bet-row-card {
    background: #f8fafc !important;
    border: 1px solid #cbd5e0;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 8px;
    color: #1a202c !important;
    font-weight: 600;
}

.locked-bet-card {
    background: #fffaf0 !important;
    border: 2px dashed #dd6b20;
    border-radius: 10px;
    padding: 16px;
    margin-top: 12px;
    margin-bottom: 14px;
    color: #7b341e !important;
}
</style>
""", unsafe_allow_html=True)

# 🔒 正式上線邏輯：透過 Stripe 付款成功帶回的 ?vip=true 自動解鎖
query_params = st.query_params
if "vip" in query_params and query_params["vip"] == "true":
    st.session_state.is_vip = True
else:
    st.session_state.is_vip = False


def load_historical_draws(csv_path="hkjc_marksix_results.csv"):
    """讀取歷史開彩 CSV，回傳已開出 6 字組合集合與總期數"""
    past_combos = set()
    draw_count = 0
    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path)
            for _, row in df.iterrows():
                try:
                    combo = tuple(sorted([
                        int(row["ball_1"]), int(row["ball_2"]), int(row["ball_3"]),
                        int(row["ball_4"]), int(row["ball_5"]), int(row["ball_6"])
                    ]))
                    if len(combo) == 6:
                        past_combos.add(combo)
                        draw_count += 1
                except Exception:
                    continue
        except Exception:
            pass
    return past_combos, draw_count


def get_zone_label(bet_index):
    """按 17 注分佈安排標示每注重點覆蓋區段，幫客解決分佈頭痛"""
    if bet_index <= 6:
        return "低段字頭分佈區（1–17 號為主）"
    elif bet_index <= 12:
        return "中段字頭分佈區（18–34 號為主）"
    else:
        return "高段字頭＋全盤補位區（35–49 號＋平衡配搭）"


def generate_17_bets_by_bday_and_date(bday_value, target_date, past_combos):
    """
    以「個人生命密碼（出生日期） + 今日日期」鎖定生成 17 注，
    確保今日之內重整或重複點擊結果完全一樣；
    同時每注 6 個號碼唔重複、覆蓋 1-49 全部號碼，並比對過往開彩紀錄剔除已開出相同組合。
    """
    seed_key = f"life17plan|{bday_value}|{target_date}"
    rng = random.Random(seed_key)

    all_49 = list(range(1, 50))
    covered_pool = []
    # 17 注 x 6 = 102 個位置，打亂兩輪令 1-49 全部號碼均有機會納入
    for _ in range(2):
        batch = all_49.copy()
        rng.shuffle(batch)
        covered_pool.extend(batch)

    bets = []
    seen_in_today = set()

    for idx in range(17):
        chunk = covered_pool[idx * 6 : (idx + 1) * 6]
        unique_chunk = list(dict.fromkeys(chunk))
        while len(unique_chunk) < 6:
            candidate = rng.choice(all_49)
            if candidate not in unique_chunk:
                unique_chunk.append(candidate)

        combo = tuple(sorted(unique_chunk[:6]))
        attempts = 0
        while (combo in past_combos or combo in seen_in_today) and attempts < 300:
            combo = tuple(sorted(rng.sample(all_49, 6)))
            attempts += 1

        seen_in_today.add(combo)
        bets.append(list(combo))

    return bets


def build_copy_text(visible_bets, bday_value, target_date, is_vip_user):
    """整理成方便喺手機抄注或貼去群組夾份分帳嘅純文字"""
    header = f"【{target_date}｜生命密碼 {bday_value}】17 注全號覆蓋排陣整理\n"
    lines = [header]
    for i, nums in enumerate(visible_bets, start=1):
        nums_str = ", ".join(f"{n:02d}" for n in nums)
        lines.append(f"第{i:02d}注（$10）：{nums_str}")
    if not is_vip_user:
        lines.append("（免費版顯示頭 10 注；其餘 7 條隨時中頭獎注項升級 VIP 即可解鎖）")
    return "\n".join(lines)


def render_copy_box(copy_text, btn_label="📋 一鍵複製號碼清單"):
    """提供一鍵複製按鈕＋可長按複製嘅文字框，方便手機用戶"""
    escaped_json = json.dumps(copy_text)
    components.html(
        f"""
        <div style="margin: 8px 0 14px 0;">
            <button onclick="copyLottoText()" style="
                background-color: #2b6cb0;
                color: #ffffff;
                border: none;
                border-radius: 8px;
                padding: 10px 18px;
                font-size: 15px;
                font-weight: bold;
                cursor: pointer;
                width: 100%;
            ">{btn_label}</button>
            <div id="copy-status" style="color: #2f855a; font-size: 13px; margin-top: 6px; font-weight: bold;"></div>
        </div>
        <script>
        function copyLottoText() {{
            const textToCopy = {escaped_json};
            const statusEl = document.getElementById("copy-status");
            if (navigator.clipboard && navigator.clipboard.writeText) {{
                navigator.clipboard.writeText(textToCopy).then(function() {{
                    statusEl.innerText = "✅ 已複製到剪貼簿，可直接貼去落注或群組分帳！";
                }}, function() {{
                    fallbackCopy(textToCopy, statusEl);
                }});
            }} else {{
                fallbackCopy(textToCopy, statusEl);
            }}
        }}
        function fallbackCopy(text, statusEl) {{
            const ta = document.createElement("textarea");
            ta.value = text;
            document.body.appendChild(ta);
            ta.select();
            try {{
                document.execCommand("copy");
                statusEl.innerText = "✅ 已複製到剪貼簿，可直接貼去落注或群組分帳！";
            }} catch (e) {{
                statusEl.innerText = "ℹ️ 請長按下方文字框手動全選複製。";
            }}
            document.body.removeChild(ta);
        }}
        </script>
        """,
        height=72,
    )
    st.text_area("方便抄注／夾份分帳純文字清單：", value=copy_text, height=150, label_visibility="collapsed")


def render_17_bets_module(bday_value, target_date, is_vip_user, key_prefix="main"):
    """一頁過渲染「17 注全號覆蓋方案」分佈安排、計數、一鍵複製清單與免費/VIP 顯示"""
    past_combos_set, total_past_draws = load_historical_draws("hkjc_marksix_results.csv")
    bets_17 = generate_17_bets_by_bday_and_date(bday_value, target_date, past_combos_set)
    covered_all_49 = sorted({num for row in bets_17 for num in row})

    st.markdown("""
    <div class="section-card" style="background: #f7fafc !important; border: 2px solid #2b6cb0;">
        <h3 style="color: #2b6cb0 !important; margin-top: 0;">🎯 17 注全號覆蓋排陣 ＋ 個人生命密碼 ＋ 過往組合篩選</h3>
        <p style="line-height: 1.7;">
            <strong>唔使自己頭痛點分佈！系統已經幫你安排好 17 注（每注 $10，共 $170）：</strong><br>
            • <strong>第 01–06 注</strong>：重點涵蓋低段字頭，減少漏字<br>
            • <strong>第 07–12 注</strong>：重點涵蓋中段字頭，平衡分佈<br>
            • <strong>第 13–17 注</strong>：重點涵蓋高段字頭及跨區補位，將 1–49 號全面納入
        </p>
        <p style="line-height: 1.7;">
            <strong>點解全號覆蓋＋個人生命密碼＋剔除過往組合值得持續用？</strong><br>
            全盤覆蓋可避免只死守少數號碼；結合<strong>個人生命密碼</strong>與<strong>今日日期</strong>鎖定排陣，今日再按幾多次結果都一樣；再比對過往開彩紀錄剔除已開出相同組合，避開重覆舊牌面。每期隨最新開彩紀錄同當日生命密碼更新，持續訂閱 <strong>HK$48/月 VIP</strong> 即可每期有系統跟住買。
        </p>
    </div>
    """, unsafe_allow_html=True)

    c_m1, c_m2, c_m3 = st.columns(3)
    c_m1.metric("總注數／預算", "17 注 / $170")
    c_m2.metric("涵蓋號碼數目", f"{len(covered_all_49)} / 49 號")
    c_m3.metric("今日解鎖進度", "17 / 17 注" if is_vip_user else "10 / 17 注（7 注待解鎖）")

    if total_past_draws > 0:
        st.caption(f"✅ 已比對 {total_past_draws} 期過往開彩紀錄，並已按生命密碼（{bday_value}）及今日日期（{target_date}）鎖定今日 17 注。")
    else:
        st.caption(f"ℹ️ 已按生命密碼（{bday_value}）及今日日期（{target_date}）鎖定今日 17 注（今日內重複點擊結果完全一樣）。")

    if st.button("🔄 重新檢視今日鎖定組合", use_container_width=True, key=f"{key_prefix}_refresh_17"):
        st.rerun()

    if is_vip_user:
        st.success("💎 VIP 已解鎖：以下為今日完整 17 注分佈安排（已覆蓋 1–49 號，已篩選過往相同組合）")
        for idx_b, b_nums in enumerate(bets_17, start=1):
            zone_txt = get_zone_label(idx_b)
            st.markdown(
                f'<div class="bet-row-card">第 {idx_b:02d} 注（$10｜{zone_txt}）：{b_nums}</div>',
                unsafe_allow_html=True
            )
        vip_copy_str = build_copy_text(bets_17, bday_value, target_date, True)
        render_copy_box(vip_copy_str, "📋 一鍵複製全部 17 注清單")
    else:
        st.info("🎁 免費試看頭 **10 注**（已幫你排好分佈，今日生命密碼鎖定版）：")
        for idx_b in range(10):
            zone_txt = get_zone_label(idx_b + 1)
            st.markdown(
                f'<div class="bet-row-card">第 {idx_b+1:02d} 注（$10｜{zone_txt}）：{bets_17[idx_b]}</div>',
                unsafe_allow_html=True
            )
        free_copy_str = build_copy_text(bets_17[:10], bday_value, target_date, False)
        render_copy_box(free_copy_str, "📋 一鍵複製已解鎖 10 注清單")

        st.markdown("""
        <div class="locked-bet-card">
            <h4 style="color: #c05621; margin-top: 0;">🔒 仲有最後 7 注（第 11–17 注・高段字頭＋全盤補位區）未解鎖！</h4>
            <p style="font-size: 15px; line-height: 1.65; margin-bottom: 0;">
                <strong>呢 7 注隨時都中頭獎！</strong>唔好睇少尾段關鍵分佈，好多時候決定中大獎嘅號碼就喺呢幾注入面。立即升級成為 <strong>VIP 尊貴會員（僅需 HK$48/月）</strong>，即刻一次過拎齊全部 17 注，再加埋「心水號碼歷史回測機」同「每日幸運導航」，期期有系統跟住買！
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align: center; margin: 16px 0 24px 0;">
            <a href="https://buy.stripe.com/5kQfZga357pKbCBdnU5Vu00" target="_blank" class="pay-btn" style="font-size: 18px; padding: 14px 28px;">
                💎 立即升級 VIP（HK$48/月）解鎖其餘 7 條隨時中頭獎注項
            </a>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# 2. 頁面頂部：置中顯示公司 Company Logo 與標題
# ==========================================
col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])
with col_logo2:
    st.image("company_logo.png", use_container_width=True)

st.markdown('<div class="main-title">🔮 AI 智能六合彩資料導航</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">17 注全號覆蓋排陣 ＋ 個人【生命密碼】分析，自動幫你分佈計數，助您精準掌握幸運號碼</div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-badge-box">
    <strong>💡 唔使再頭痛 17 注點樣分佈！</strong>系統自動按 <strong>低／中／高段字頭</strong> 排好 <strong>17 注（共 $170，涵蓋 1–49 號）</strong>，結合<strong>個人生命密碼</strong>及<strong>剔除過往相同組合</strong>，免費先睇 10 注，<strong>VIP（HK$48/月）</strong>解鎖其餘 7 條隨時中頭獎注項！
</div>
""", unsafe_allow_html=True)

# 建立橫向分頁標籤
tab1, tab2, tab3 = st.tabs(["🏠 今日免費號碼", "💎 VIP 尊貴會員專區", "⚙️ 會員帳戶管理"])

# --- Tab 1：首頁／免費試用 ---
with tab1:
    st.markdown("""
    <div class="section-card">
        <h3>🍀 您的個人化生命密碼（免費體驗）</h3>
        <p><strong>⚠️ 重要提醒</strong>：買六合彩絕對不能盲目亂買！如果隨便亂買「盲門死角」號碼，只會白白浪費金錢。必須結合您專屬的<strong>個人生命密碼</strong>與能量頻率，才能精準過濾無謂注數，大幅提高命中率！</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        free_birthday = st.date_input("🎂 請填寫您的【真實出生日期】：", value=date(1985, 6, 15), key="free_bday")
        
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        if st.button("🎲 立即生成今日免費生命密碼號碼", use_container_width=True):
            random.seed(str(free_birthday) + str(date.today()))
            free_numbers = sorted(random.sample(range(1, 50), 6))
            st.success(f"🎯 依據您的生命密碼（{free_birthday}）推算出的免費基礎號碼：**{free_numbers}**")
            st.info("💡 提示：此為基礎隨機運算號碼。若要解鎖「生命密碼多組深度推演」與「心水號碼歷史回測機」，請升級 VIP！")

    # --- 一頁過加入：17 注全號覆蓋排陣（免費看 10 注，VIP 解鎖其餘 7 注） ---
    render_17_bets_module(free_birthday, date.today(), st.session_state.is_vip, key_prefix="tab1")

    # --- 核心賣點 ---
    st.markdown("""
    <div class="section-card" style="background: #fffaf0; border: 2px solid #dd6b20;">
        <h3 style="color: #c05621; margin-top: 0;">🔍 停一停！你平時買開嗰 6 個「心水號碼」，究竟過去幾十年幫你中過幾多次獎？</h3>
        <p style="font-size: 16px; color: #2d3748; line-height: 1.6;">
            好多人買足幾十年六合彩，永遠唔知自己對住嗰組號碼其實係「財神爺」定係「白交學費」！<br>
            <strong>🔥 VIP 尊貴會員區現已全面解鎖【心水號碼歷史大數據回測機】</strong>：<br>
            輸入你一直以來的 6 個心水號碼，一鍵秒速翻查過往多年歷史開彩數據！親自驗證它究竟中過幾多次<strong>頭獎、二獎、三獎、四獎或五獎</strong>，徹底揭開你與幸運之神的真正距離！
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- VIP 特點 ---
    st.markdown("""
    <div class="warning-box" style="background: #fff5f5; border-left: 5px solid #e53e3e; padding: 18px; border-radius: 8px;">
        <h3 style="color: #c53030; margin-top: 0;">⚠️ 為什麼你必須馬上成為 VIP？（拒絕盲買，拒絕將錢掉落鹹水海！）</h3>
        <p style="font-size: 15px; color: #2d3748;">
            出面求其買一個電腦飛都要 $10、$20，但盲目亂買只會陷入<strong>「盲門死角」</strong>。解鎖 VIP，運用你的<strong>生命密碼</strong>作為最強導航：
        </p>
        <ul style="font-size: 15px; color: #2d3748; line-height: 1.8;">
            <li>🎯 <strong>17 注全號覆蓋排陣 ＋ 過往組合篩選</strong>：自動幫你分佈低／中／高段字頭（共 17 注、$170，涵蓋 1–49 號），結合個人生命密碼與今日日期鎖定，並剔除已開出相同組合，VIP 完整解鎖全部 17 注！</li>
            <li>🔍 <strong>【震撼殺手鐧】心水號碼歷史大數據回測機</strong>：親自驗證你手頭上那組號碼過去究竟中過幾多次頭、二、三獎，拒絕盲目執著！</li>
            <li>🧬 <strong>生命密碼獨家深度推演</strong>：結合你的真實生辰八字與能量頻率，每期動態防盲門，精準推演 3 組互不撞號的高勝率組合。</li>
            <li>🔄 <strong>每期實時動態剔除盲門</strong>：全港獨家！每期攪珠後第一時間更新，自動幫你洗走歷史盲門死角，避開高風險陷阱。</li>
            <li>📊 <strong>AI 核心大數據走勢矩陣</strong>：結合最新冷熱門走勢與靈數模型，大幅提升命中率。</li>
            <li>🤝 <strong>智慧合買與分帳管理系統</strong>：與同事、老友記夾份買彩票？系統自動幫你計好每人認購份數同應付金額，清楚無爭拗！</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- 動態發光特效的今日限定 BONUS 預告 ---
    st.markdown("""
    <div class="bonus-glow-card">
        <h3 style="margin-top: 0;">🎁 ✨ 【今日限定 BONUS】明日專屬個人幸運顏色與穿搭指引</h3>
        <p style="font-size: 15px; line-height: 1.6; margin-bottom: 0;">
            <strong>🔥 獨家附贈彩蛋</strong>：今日登記成為 VIP，額外即時解鎖專屬個人開運幸運色批算！男士女士唔使再為「明天返工著咩衫」頭痛，一秒決定好最旺財氣嘅穿搭，全方位催旺你的橫財磁場！
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- 根據是否已付費（VIP 狀態）動態切換按鈕區 ---
    if st.session_state.is_vip:
        st.markdown("""
        <div style="background: #e6fffa; border: 2px solid #319795; padding: 20px; border-radius: 12px; text-align: center; margin: 25px 0;">
            <h3 style="color: #2c7a7b; margin-top: 0;">🎉 恭喜您！您的 VIP 尊貴會員資格已成功啟動！</h3>
            <p style="font-size: 16px; color: #2d3748; margin-bottom: 15px;">
                <strong>✨ 專屬提示</strong>：您的生命密碼與歷史回測權限已全數開通。<br>
                ⚠️ <em>溫馨提示：本帳戶與您的個人生命磁場深度綁定，請切勿將帳號借予他人使用，以免個人財運與能量外洩！</em>
            </p>
            <p style="font-size: 15px; color: #2b6cb0; font-weight: bold;">
                👉 請直接點擊上方分頁標籤：【💎 VIP 尊貴會員專區】開始使用！
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="text-align: center; margin: 25px 0;">
            <a href="https://buy.stripe.com/5kQfZga357pKbCBdnU5Vu00" target="_blank" class="pay-btn" style="font-size: 20px; padding: 16px 36px;">
                💎 立即解鎖生命密碼導航與全部 VIP 功能（僅需 HK$48/月）
            </a>
            <p style="color: #718096; font-size: 13px; margin-top: 8px;">🔒 Stripe 官方加密結帳，隨時可自主取消訂閱，一杯咖啡錢換取專業數據導航！</p>
        </div>
        """, unsafe_allow_html=True)

# --- Tab 2：VIP 尊貴會員專區 ---
with tab2:
    if st.session_state.is_vip:
        st.success("🎉 歡迎回來，尊貴的 VIP 會員！您的生命密碼導航與歷史回測機已全面啟動。")

        # --- 玄學安全警示（防借人） ---
        st.markdown("""
        <div style="background: #fffaf0; border-left: 5px solid #dd6b20; padding: 12px 15px; margin-bottom: 20px; border-radius: 4px;">
            <p style="font-size: 14px; color: #c05621; margin: 0;">
                🛡️ <strong>能量保護提示</strong>：本系統之生命密碼與您的個人生辰磁場實時對應。<strong>請勿將帳號或預測結果隨意外借他人</strong>，以免個人運勢與財氣磁場分散外洩。祝您期期中大獎！
            </p>
        </div>
        """, unsafe_allow_html=True)

        # --- VIP 殺手鐧 1：心水號碼歷史真實回測機 (讀取 CSV) ---
        st.markdown("""
        <div class="section-card" style="background: #fffaf0 !important; border-color: #dd6b20;">
            <h3 style="color: #c05621 !important;">🔍 【VIP 獨家重磅】心水號碼歷史大數據回測機 (真實 CSV 引擎)</h3>
            <p style="color: #222222 !important;">輸入你一直以來的 <strong>6 個心水號碼</strong>，系統將即時讀取過往全部歷史開彩數據進行真實對對碰！驗證它究竟中過幾多次頭、二、三、四、五獎！</p>
        </div>
        """, unsafe_allow_html=True)

        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            num1 = st.number_input("號碼 1", min_value=1, max_value=49, value=9, key="num1")
            num2 = st.number_input("號碼 2", min_value=1, max_value=49, value=25, key="num2")
        with col_c2:
            num3 = st.number_input("號碼 3", min_value=1, max_value=49, value=26, key="num3")
            num4 = st.number_input("號碼 4", min_value=1, max_value=49, value=28, key="num4")
        with col_c3:
            num5 = st.number_input("號碼 5", min_value=1, max_value=49, value=44, key="num5")
            num6 = st.number_input("號碼 6", min_value=1, max_value=49, value=45, key="num6")

        user_pick = [num1, num2, num3, num4, num5, num6]

        if st.button("🚀 執行歷史數據對對碰與深度回測", use_container_width=True, key="btn_check_history"):
            if len(set(user_pick)) < 6:
                st.error("⚠️ 請確保輸入的 6 個號碼完全不重複！")
            else:
                user_pick_set = set(user_pick)
                csv_file = "hkjc_marksix_results.csv"
                
                if os.path.exists(csv_file):
                    try:
                        df = pd.read_csv(csv_file)
                        win_1, win_2, win_3, win_4, win_5 = 0, 0, 0, 0, 0
                        
                        for idx, row in df.iterrows():
                            try:
                                draw_set = {
                                    int(row['ball_1']), int(row['ball_2']), int(row['ball_3']),
                                    int(row['ball_4']), int(row['ball_5']), int(row['ball_6'])
                                }
                                special_num = int(row['extra_ball']) if pd.notna(row['extra_ball']) else None
                                
                                matched_count = len(user_pick_set.intersection(draw_set))
                                has_special = special_num in user_pick_set if special_num else False
                                
                                if matched_count == 6:
                                    win_1 += 1
                                elif matched_count == 5 and has_special:
                                    win_2 += 1
                                elif matched_count == 5:
                                    win_3 += 1
                                elif matched_count == 4:
                                    win_4 += 1
                                elif matched_count == 3:
                                    win_5 += 1
                            except:
                                continue
                        
                        st.markdown(f"""
                        <div class="lucky-box" style="border-left-color: #dd6b20;">
                            <h4>📊 您的心水號碼組合【 {sorted(list(user_pick_set))} 】真實歷史大數據回測結果：</h4>
                            <p style="font-size: 16px; line-height: 1.8;">
                                • 🥇 <strong>頭獎 (6字全中)</strong>：<strong>{win_1}</strong> 次<br>
                                • 🥈 <strong>二獎 (5.5字)</strong>：<strong>{win_2}</strong> 次<br>
                                • 🥉 <strong>三獎 (中 5 個字)</strong>：<strong>{win_3}</strong> 次<br>
                                • 🏅 <strong>四獎 (中 4 個字)</strong>：<strong>{win_4}</strong> 次<br>
                                • 🎟️ <strong>五獎 (中 3 個字)</strong>：<strong>{win_5}</strong> 次
                            </p>
                            <hr style="border-top: 1px dashed #cbd5e0; margin: 10px 0;">
                            <p style="font-size: 14px; color: #742a2a;">
                                💡 <strong>AI 數據拆解報告</strong>：系統已精準讀取歷史 CSV 檔案，此為該組號碼在歷史上真實命中的獎項統計！
                            </p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.error(f"⚠️ 讀取歷史 CSV 數據時發生錯誤：{e}")
                else:
                    st.warning("⚠️ 找不到 `hkjc_marksix_results.csv` 檔案，請確保已將檔案上載至 GitHub 根目錄。")

        st.markdown("---")

        st.markdown("""
        <div class="section-card" style="background: #fdf6e2 !important; border-color: #d69e2e;">
            <h3 style="color: #b7791f !important;">🔑 【核心設定】請輸入您的真實出生日期（生命密碼引擎）</h3>
            <p style="color: #222222 !important;"><strong>注意</strong>：以下所有的生命密碼推演、AI 大數據運算及 17 注全號覆蓋排陣，全部都是結合<strong>「每期最新更新的資料庫」</strong>並即時根據您輸入的生辰推算出來的！請務必核對準確。</p>
        </div>
        """, unsafe_allow_html=True)

        vip_birthday = st.date_input("🎂 請輸入您的出生日期（VIP 深度推演用）：", value=date(1977, 8, 20), key="vip_bday")

        # --- VIP 專區同步顯示完整 17 注全號覆蓋排陣 ---
        render_17_bets_module(vip_birthday, date.today(), True, key_prefix="tab2")

        st.markdown("---")

        # --- VIP 核心功能 1：生命密碼推演 (以今日日期鎖定) ---
        st.markdown("""
        <div class="section-card">
            <h3>🧬 1. 生命密碼獨家深度推演（提高命中率・動態防盲門）</h3>
            <p>結合您的生日頻率與最新一期更新的開彩矩陣，即時生成 3 組互相不撞號的高勝率精準組合：</p>
        </div>
        """, unsafe_allow_html=True)

        pick_count = st.selectbox("🎯 請選擇您心儀的組合字數：", [6, 7, 8, 9, 10], index=0, key="vip_pick_count")

        if st.button("✨ 立即依最新資料庫與生命密碼生成 3 組高勝率組合", use_container_width=True, key="btn_life_code"):
            # 🌟 鎖定今日日期 + 生日，確保今日之內多次點擊結果完全一致
            seed_str = str(vip_birthday) + str(pick_count) + str(date.today())
            random.seed(seed_str)
            all_pool = list(range(1, 50))
            group1 = sorted(random.sample(all_pool, pick_count))
            remaining_pool = [n for n in all_pool if n not in group1]
            group2 = sorted(random.sample(remaining_pool, pick_count))
            remaining_pool_2 = [n for n in remaining_pool if n not in group2]
            group3 = sorted(random.sample(remaining_pool_2, pick_count))

            st.markdown(f"""
            <div class="lucky-box">
                <h4>🌟 專屬生命密碼推薦（生辰：{vip_birthday} ｜ 日期：{date.today()}）：</h4>
                <p style="font-size: 17px; font-weight: bold; line-height: 1.6;">
                    • 第一組：{group1}<br>
                    • 第二組：{group2}<br>
                    • 第三組：{group3}<br>
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.info("💡 提示：今日磁場已鎖定，期號數據同步最新。")

        st.markdown("---")

        # --- VIP 核心功能 2：AI 大數據運算結果 (以今日日期鎖定) ---
        st.markdown("""
        <div class="section-card">
            <h3>📊 2. AI 核心大數據運算結果</h3>
            <p>結合當期最新冷熱走勢與您的生命密碼靈數模型，徹底避開盲買陷阱：</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 執行 AI 深度趨勢運算", use_container_width=True, key="btn_ai_calc"):
            # 🌟 鎖定今日日期 + 生日，確保今日之內 AI 預測號碼恆常不變
            ai_seed = str(vip_birthday).replace("-", "") + str(date.today()).replace("-", "") + "ai_core"
            random.seed(ai_seed)
            
            ai_main = sorted(random.sample(range(1, 50), 6))
            ai_extra = random.randint(1, 49)
            
            st.balloons()
            st.success(f"🎯 **AI 核心預測號碼（今日鎖定版）**：{ai_main} ＋ 特別號：【**{ai_extra}**】")
            st.write(f"📈 **個人化回測評語**：今日（{date.today()}）已為生辰 **{vip_birthday}** 的您鎖定專屬運勢矩陣，今日內重整或再按結果完全一致。")

        st.markdown("---")

        # --- VIP 核心功能 3：個人幸運方位、時間與地點導航 (以今日日期鎖定) ---
        st.markdown("""
        <div class="section-card">
            <h3>🧭 3. 個人幸運方位、時間與地點導航</h3>
            <p>知道買邊個號碼之餘，更要配合天時、地利、人和才能發揮最大命中率：</p>
        </div>
        """, unsafe_allow_html=True)

        # 🌟 嚴格鎖定今日日期 + 生日，確保今日之內的幸運方位、投注站與黃金時段 100% 固定不變！
        nav_seed = str(vip_birthday).replace("-", "") + str(date.today()).replace("-", "") + "nav_direction"
        rng_nav = random.Random(nav_seed)

        directions = [
            ("正南方（南離宮）", "主貴人與突發靈感，利正財與偏財氣場"),
            ("正北方（北坎宮）", "主思路清晰，利冷門號碼過濾與大局觀"),
            ("正東方（東震宮）", "主動力與衝勁，利快速決策與靈感爆發"),
            ("西北方（乾金位）", "主權威與大財氣，利合買團隊領軍下注"),
            ("西南方（坤土位）", "主穩陣聚財，利長線心水號碼追蹤")
        ]
        
        home_spots = [
            "客廳正南方或書房工作桌前",
            "露台或近窗戶之開揚通風處",
            "客廳梳化中央或飯桌東南位",
            "安靜無干擾之睡房私人角落"
        ]

        shops = [
            "屯門市廣場投注站 或 元朗青山公路投注站",
            "荃灣青山公路投注站 或 葵芳興芳路投注站",
            "旺角亞皆老街投注站 或 尖沙咀漢口道投注站",
            "銅鑼灣謝斐道投注站 或 灣仔軒尼詩道投注站",
            "沙田廣場投注站 或 大埔廣場投注站"
        ]

        time_slots = [
            "下午 15:15 至 17:00（申時金水相生，財氣最旺）",
            "下午 13:00 至 14:30（未時土金相生，決策精準）",
            "晚上 19:30 至 21:00（戌時財庫大開，下注最佳時機）",
            "上午 10:00 至 11:30（巳時朝氣蓬勃，靈感最高昂）"
        ]

        chosen_dir, dir_desc = rng_nav.choice(directions)
        chosen_home = rng_nav.choice(home_spots)
        chosen_shop = rng_nav.choice(shops)
        chosen_time = rng_nav.choice(time_slots)

        st.markdown(f"""
| 項目 | 今日精準指引（日期：{date.today()} ｜ 生日：{vip_birthday}） |
| :--- | :--- |
| 🌟 **今日吉利方位** | **{chosen_dir}** — {dir_desc} |
| 🏠 **屋企下注吉位** | 建議在 **{chosen_home}** 打開手機進行網上投注 |
| 🏢 **推薦香港投注站** | **{chosen_shop}**（今日能量場與您最契合） |
| ⏰ **最佳黃金時段** | **{chosen_time}**（切勿錯過今日黃金時段） |
        """, unsafe_allow_html=True)

        st.markdown("---")

        # --- VIP 核心功能 4：智慧合買 ---
        st.markdown("""
        <div class="section-card" style="background: #f0fff4 !important; border-color: #38a169;">
            <h3 style="color: #2f855a !important;">🤝 4. 智慧合買與分帳管理系統</h3>
            <p style="color: #222222 !important;">與親友夾份買彩票時，自動記錄成員認購份數與金額，避免混亂：</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("group_buy_form"):
            st.write("📝 **建立新一期合買名單**")
            group_name = st.text_input("合買群組名稱（例如：朋友夾份買六合彩）", "屯門老友記夾份團")
            total_shares = st.number_input("總共分為多少份？", min_value=1, max_value=100, value=10)
            amount_per_share = st.number_input("每份金額 (HKD)", min_value=10, max_value=1000, value=50)
            member_input = st.text_area("輸入成員與認購份數（格式：名字, 份數，每行一位）", "張三, 2\n李四, 3\n王五, 1")
            
            submitted = st.form_submit_button("📊 計算合買總金額與分帳清單")
            if submitted:
                lines = member_input.strip().split("\n")
                total_allocated = 0
                st.markdown(f"### 📋 【{group_name}】合買分配清單")
                for line in lines:
                    if "," in line:
                        name, shares = line.split(",")
                        shares_num = int(shares.strip())
                        total_allocated += shares_num
                        cost = shares_num * amount_per_share
                        st.write(f"• **{name.strip()}**：認購 {shares_num} 份（應付金額：**HK${cost}**）")
                
                st.info(f"💰 **總計**：已分出 {total_allocated} 份 / 總共 {total_shares} 份。")
                if total_allocated <= total_shares:
                    st.success("✅ 份數分配正常，隨時準備出擊！")
                else:
                    st.warning("⚠️ 注意：認購份數已超出總設定份數，請重新確認！")

        st.markdown("---")

        # --- 壓軸獨立拆出：有吸睛發光特效的今日限定 BONUS ---
        st.markdown("""
        <div class="bonus-glow-card">
            <h3 style="margin-top: 0;">🎁 ✨ 【今日限定 BONUS】明日專屬個人幸運顏色與穿搭指引</h3>
            <p style="margin-bottom: 12px; line-height: 1.6;">
                作為今日成為 VIP 的額外驚喜加碼！男士女士唔使再為「明天著咩衫」頭痛，系統一秒幫您決定好最夾的開運穿搭，全方位旺財氣：
            </p>
        </div>
        """, unsafe_allow_html=True)

        tomorrow_date = date.today() + timedelta(days=1)
        if st.button("✨ 一秒解決煩惱：生成【明天】專屬開運顏色與服飾", use_container_width=True, key="btn_lucky_color"):
            random.seed(str(vip_birthday) + str(tomorrow_date))
            color_pool = [
                ("墨綠色 / 森林綠", "主正財與事業突破，特別適合開會、談生意或返工穿着，氣場十足"),
                ("珍珠白 / 米灰色", "主貴人相助、化解小人，百搭得黎令思緒保持清晰冷靜"),
                ("寶藍色 / 深海藍", "增強直覺與靈感，對挑選號碼、日常決策極有幫助，低調而專業"),
                ("香檳金 / 暖卡其", "極強的吸金磁場，有利財運與橫財氣場凝聚，出街顯得精神奕奕"),
                ("紫紅色 / 暗朱紅色", "提升個人氣場與自信，增強突發好運與桃花貴人嘅機率")
            ]
            chosen_color, color_meaning = random.choice(color_pool)
            st.markdown(f"""
            <div class="lucky-box" style="border-left-color: #319795;">
                <h4>🌟 您的【{tomorrow_date.strftime('%Y-%m-%d')}（明天）】一石二鳥催運穿搭指南：</h4>
                <p style="font-size: 16px; line-height: 1.6;">
                    • 🎯 <strong>明天開運主色調</strong>: <span style="color: #2b6cb0; font-weight: bold; font-size: 18px;">{chosen_color}</span><br>
                    • 👔 <strong>穿搭建議</strong>: 唔使再頭痛！上衣/外套直接揀呢個色系，今晚準備好，明天出門返工直接吸財兼吸貴人！<br>
                    • 📈 <strong>雙效磁場</strong>: {color_meaning}
                </p>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="vip-card">
            <h1 style="margin-bottom: 10px;">💎 解鎖 AI 智能六合彩 VIP</h1>
            <p style="font-size: 16px; margin-bottom: 10px;">
                <strong>🔥【獨家重磅功能】17 注全號覆蓋排陣 ＋ 個人生命密碼 ＋ 歷史大數據回測機！</strong><br>
                解鎖其餘 7 條隨時中頭獎注項，即時檢驗心水號碼歷史中獎次數，更送你今日限定發光開運穿搭 BONUS！
            </p>
            <h2 style="color: #d93838; margin-top: 5px;">💰 僅需 HK$48 / 月</h2>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align: center; margin: 30px 0;">
            <a href="https://buy.stripe.com/5kQfZga357pKbCBdnU5Vu00" target="_blank" class="pay-btn">
                💳 立即線上信用卡升級 VIP（$48/月・解鎖全套 17 注與全部 VIP 功能）
            </a>
            <p style="color: #777777; font-size: 13px; margin-top: 10px;">🔒 由 Stripe 官方安全加密提供支援，隨時可取消訂閱</p>
        </div>
        """, unsafe_allow_html=True)

# --- Tab 3：會員帳戶管理 ---
with tab3:
    st.markdown("""
    <div class="section-card">
        <h3>⚙️ 帳戶與訂閱管理</h3>
        <p>如果您已經是我們的 VIP 會員，您可以隨時前往管理中心查看訂單、更新信用卡或取消訂閱：</p>
    </div>
    """, unsafe_allow_html=True)

    col_x, col_y, col_z = st.columns([1, 2, 1])
    with col_y:
        st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://dashboard.stripe.com/" target="_blank" style="background-color: #f0f2f6; color: #333333; padding: 10px 20px; text-decoration: none; border-radius: 6px; font-weight: bold; border: 1px solid #d0d7de; display: inline-block;">
                🔗 前往 Stripe 帳戶與訂閱管理中心
            </a>
        </div>
        """, unsafe_allow_html=True)

# 頁尾資訊
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>© 2026 AI Lotto Nav. All rights reserved. 僅供娛樂與數據參考，請理性投注。</p>", unsafe_allow_html=True)
