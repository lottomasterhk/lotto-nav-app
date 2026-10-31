import streamlit as st
import random
import datetime

# ==========================================
# 1. 頁面基本設定與 SEO / Favicon 注入
# ==========================================
st.set_page_config(
    page_title="六合彩生命密碼 | AI 大數據幸運號碼導航",
    page_icon="logo.png",  # 瀏覽器分頁小圖標
    layout="wide"
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
# 2. 側邊欄 (Sidebar) 設置 Company Logo 與導航
# ==========================================
with st.sidebar:
    # 顯示完整的 Company Logo（包含圖標與中英文字）
    st.image("company_logo.png", use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 🧭 導航選單")
    menu = st.radio(
        "選擇功能",
        [
            "🏠 首頁導航", 
            "🔮 個人化生命密碼選號", 
            "✨ 今日免費開運號碼", 
            "📊 歷史回測與大數據分析", 
            "💎 VIP 尊貴會員專區"
        ]
    )
    
    st.markdown("---")
    st.markdown("### 💡 網站提示")
    st.info("結合個人化生命密碼與 AI 數據的幸運導航工具，拒絕盲門死角。")


# ==========================================
# 3. 網頁主要內容區 (Main Content)
# ==========================================

# 在首頁正上方居中放一次完整 Company Logo 作為大 Banner
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("company_logo.png", use_container_width=True)

st.markdown("<h1 style='text-align: center;'>🎰 六合彩生命密碼導航</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>拒絕盲門死角，用大數據與靈數精準過濾您的幸運號碼</p>", unsafe_allow_html=True)

st.markdown("---")

# 根據側邊欄選單顯示對應內容
if menu == "🏠 首頁導航":
    st.subheader("歡迎來到 AI 智能六合彩導航系統")
    st.write("請從左側側邊欄選擇您想要使用的功能，開始您的精準選號之旅！")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.success("✨ **免費體驗**：輸入您的生日，解鎖今日專屬開運靈數與推薦號碼。")
    with col_b:
        st.warning("💎 **VIP 專區**：解鎖進階大數據回測、心水號碼過濾及智慧合買分帳管理系統。")
        
    st.markdown("---")
    st.markdown("### 🌟 為什麼選擇我們？")
    st.info("我們透過分析香港六合彩歷史開獎數據，配合個人化生命密碼，幫您避開盲門，提升中獎機率。")

elif menu == "🔮 個人化生命密碼選號":
    st.subheader("🔮 個人化生命密碼計算與開運選號")
    birthday = st.date_input("請選擇您的出生日期：", value=datetime.date(1990, 1, 1))
    
    if st.button("計算我的幸運靈數並生成號碼"):
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

elif menu == "✨ 今日免費開運號碼":
    st.subheader("✨ 今日免費幸運號碼推薦")
    st.write("每日系統自動更新的推薦過濾號碼：")
    
    if st.button("一鍵生成今日免費號碼"):
        free_nums = sorted(random.sample(range(1, 50), 6))
        formatted_free = [f"{num:02d}" for num in free_nums]
        st.markdown(f"### `{'  '.join(formatted_free)}`")

elif menu == "📊 歷史回測與大數據分析":
    st.subheader("📊 六合彩歷史回測系統")
    st.write("系統正在讀取 `hkjc_mark_six_results.csv` 歷史開獎數據進行智能回測...")
    
    # 模擬歷史回測展示
    st.metric(label="歷史數據總期數", value="2,540 期", delta="資料已同步最新")
    st.bar_chart({"熱門號碼": [12, 28, 35, 42, 7, 19]})

elif menu == "💎 VIP 尊貴會員專區":
    st.subheader("💎 VIP 尊貴會員升級")
    st.write("只需 **$48/月**，即可解鎖完整 AI 深度過濾、歷史大數據精準回測，以及實用的「智慧合買與分帳管理系統」！")
    
    st.markdown("---")
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.markdown("### VIP 獨家功能：")
        st.markdown("- 🚀 AI 深度盲門過濾技術")
        st.markdown("- 📊 無限制歷史開獎回測")
        st.markdown("- 💰 智慧合買分帳免爭拗")
    with col_v2:
        st.markdown("### 立即解鎖：")
        if st.button("立即線上信用卡升級 VIP (Stripe)"):
            st.link_button("前往 Stripe 安全付款 ($48/月)", "https://buy.stripe.com/your_link_here")
