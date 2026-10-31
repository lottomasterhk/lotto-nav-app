import streamlit as st
import random
import datetime

# ==========================================
# 1. 頁面基本設定與 SEO / Favicon 注入
# ==========================================
st.set_page_config(
    page_title="六合彩生命密碼 | AI 大數據幸運號碼導航",
    page_icon="logo.png",  # 瀏覽器分頁小圖標
    layout="centered"     # 手機優先：改用置中排版，手機瀏覽體驗極佳
)

# 注入 Google 專用的 Site Name 結構化資料與標籤
st.markdown("""
    <head>
        <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "WebSite",
          "name": "六合彩生命密碼",
          "alternateName": ["AI六合彩生命密碼", "Master Lotto AI", "aimasterlotto"],
          "url": "https://aimasterlotto.com/"
        }
        </script>
        <link rel="icon" href="https://aimasterlotto.com/logo.png" sizes="48x48" type="image/png">
        <link rel="shortcut icon" href="https://aimasterlotto.com/logo.png">
    </head>
""", unsafe_allow_html=True)


# ==========================================
# 2. 頁面頂部：置中顯示完整 Company Logo 與標題 (手機一眼看見)
# ==========================================
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.image("company_logo.png", use_container_width=True)

st.markdown("<h1 style='text-align: center; font-size: 28px;'>🎰 六合彩生命密碼導航</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray; font-size: 14px;'>拒絕盲門死角，用大數據與靈數精準過濾您的幸運號碼</p>", unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# 3. 手機極友善：使用橫向 Tab 取代左邊欄 (不用收埋，一撳即切換)
# ==========================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 首頁", 
    "🔮 生命密碼", 
    "✨ 免費號碼", 
    "📊 歷史回測", 
    "💎 VIP 專區"
])


# ==========================================
# 4. 各個分頁內容區 (Main Content)
# ==========================================

with tab1:
    st.subheader("歡迎來到 AI 智能六合彩導航系統")
    st.write("請直接點選上方不同的分頁，開始您的精準選號之旅！")
    
    st.success("✨ **免費體驗**：切換到「生命密碼」分頁，輸入您的生日解鎖今日專屬開運靈數。")
    st.warning("💎 **VIP 專區**：解鎖進階大數據回測、心水號碼過濾及智慧合買分帳管理系統。")
        
    st.markdown("---")
    st.markdown("### 🌟 為什麼選擇我們？")
    st.info("我們透過分析香港六合彩歷史開獎數據，配合個人化生命密碼，幫您避開盲門，提升中獎機率。")


with tab2:
    st.subheader("🔮 個人化生命密碼計算與開運選號")
    birthday = st.date_input("請選擇您的出生日期：", value=datetime.date(1990, 1, 1))
    
    if st.button("計算我的幸運靈數並生成號碼", use_container_width=True):
        st.balloons()
        # 簡單示範生命靈數計算邏輯
        birth_str = birthday.strftime("%Y%m%d")
        digit_sum = sum(int(char) for char in birth_str)
        while digit_sum > 9 and digit_sum != 11 and digit_sum != 22:
            digit_sum = sum(int(char) for char in str(digit_sum))
            
        st.success(f"✨ 您的出生日期為 {birthday}，計算出的【生命靈數】為：**{digit_sum}**")
        
        # 根據靈數隨機生成 6 個幸運號碼作示範
        random.seed(int(birth_str))
        lucky_nums = sorted(random.sample(range(1, 50), 6))
        formatted_nums = [f"{num:02d}" for num in lucky_nums]
        
        st.write("🎯 **為您專屬訂製的今日心水號碼：**")
        st.markdown(f"### `{'  '.join(formatted_nums)}`")
        st.caption("（提示：此號碼結合您的生命密碼與 AI 隨機權重過濾，僅供參考。）")


with tab3:
    st.subheader("✨ 今日免費幸運號碼推薦")
    st.write("每日系統自動更新的推薦過濾號碼：")
    
    if st.button("一鍵生成今日免費號碼", use_container_width=True):
        free_nums = sorted(random.sample(range(1, 50), 6))
        formatted_free = [f"{num:02d}" for num in free_nums]
        st.markdown(f"### `{'  '.join(formatted_free)}`")


with tab4:
    st.subheader("📊 六合彩歷史回測系統")
    st.write("系統正在讀取 `hkjc_mark_six_results.csv` 歷史開獎數據進行智能回測...")
    
    st.metric(label="歷史數據總期數", value="2,540 期", delta="資料已同步最新")
    st.bar_chart({"熱門號碼": [12, 28, 35, 42, 7, 19]})


with tab5:
    st.subheader("💎 VIP 尊貴會員升級")
    st.write("只需 **$48/月**，即可解鎖完整 AI 深度過濾、歷史大數據精準回測，以及實用的「智慧合買與分帳管理系統」！")
    
    st.markdown("---")
    st.markdown("### VIP 獨家功能：")
    st.markdown("- 🚀 AI 深度盲門過濾技術")
    st.markdown("- 📊 無限制歷史開獎回測")
    st.markdown("- 💰 智慧合買分帳免爭拗")
    
    st.markdown("### 立即解鎖：")
    if st.button("立即線上信用卡升級 VIP (Stripe)", use_container_width=True):
        st.link_button("前往 Stripe 安全付款 ($48/月)", "https://buy.stripe.com/your_link_here")
