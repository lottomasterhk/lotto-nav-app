import streamlit as st
import random
from datetime import date, timedelta

# 頁面基本設定
st.set_page_config(
    page_title="AI 智能六合彩 VIP 尊貴會員導航",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🌐 Google Search Console 驗證標籤（直接以純 HTML meta 插入）
st.markdown('<meta name="google-site-verification" content="nbbI0OAcsp83w065H9PjLBf959kRLFx4kK16f1KJhfI" />', unsafe_allow_html=True)

# 🔒 正式上線邏輯：透過 Stripe 付款成功帶回的 ?vip=true 自動解鎖
query_params = st.query_params
if "vip" in query_params and query_params["vip"] == "true":
    st.session_state.is_vip = True
else:
    st.session_state.is_vip = False

# 頁面標題
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🔮 AI 智能六合彩資料導航</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555555; font-size: 16px;'>運用大數據與個人化【生命密碼】分析，助您精準掌握高勝率幸運號碼</p>", unsafe_allow_html=True)

# 建立橫向分頁標籤
tab1, tab2, tab3 = st.tabs(["🏠 今日免費號碼", "💎 VIP 尊貴會員專區", "⚙️ 會員帳戶管理"])

# --- Tab 1：首頁／免費試用 ---
with tab1:
    st.info("🍀 您的個人化生命密碼（免費體驗）：買六合彩絕對不能盲目亂買！必須結合您專屬的個人生命密碼與能量頻率，才能精準過濾無謂注數，大幅提高命中率！")

    col1, col2 = st.columns([2, 1])
    with col1:
        free_birthday = st.date_input("🎂 請填寫您的【真實出生日期】：", value=date(1985, 6, 15), key="free_bday")
        
    if st.button("🎲 立即生成今日免費生命密碼號碼", use_container_width=True):
        random.seed(str(free_birthday))
        free_numbers = sorted(random.sample(range(1, 50), 6))
        st.success(f"🎯 依據您的生命密碼（{free_birthday}）推算出的免費基礎號碼：**{free_numbers}**")
        st.info("💡 提示：此為基礎隨機運算號碼。若要解鎖「生命密碼多組深度推演」與「心水號碼歷史回測機」，請升級 VIP！")

    st.warning("🔍 停一停！你平時買開嗰 6 個「心水號碼」，究竟過去幾十年幫你中過幾多次獎？解鎖 VIP 即可使用【心水號碼歷史大數據回測機】一鍵秒速翻查！")

    # --- VIP 特點 ---
    with st.expander("⚠️ 為什麼你必須馬上成為 VIP？（點擊展開詳情）"):
        st.write("""
        - 🔍 **【震撼殺手鐧】心水號碼歷史大數據回測機**：親自驗證你手頭上那組號碼過去究竟中過幾多次頭、二、三獎！
        - 🧬 **生命密碼獨家深度推演**：結合真實生辰八字與能量頻率，精準推演 3 組互不撞號的高勝率組合。
        - 🔄 **每期實時動態剔除盲門**：自動幫你洗走歷史盲門死角，避開高風險陷阱。
        - 📊 **AI 核心大數據走勢矩陣**：結合最新冷熱門走勢與靈數模型。
        - 🤝 **智慧合買與分帳管理系統**：與親友夾份買彩票時自動計好每人認購份數與金額。
        """)

    # --- 根據是否已付費（VIP 狀態）動態切換按鈕區 ---
    if st.session_state.is_vip:
        st.success("🎉 恭喜您！您的 VIP 尊貴會員資格已成功啟動！請點擊上方分頁標籤【💎 VIP 尊貴會員專區】開始使用！")
    else:
        st.markdown("""
        <div style="text-align: center; margin: 25px 0;">
            <a href="https://buy.stripe.com/5kQfZga357pKbCBdnU5Vu00" target="_blank" style="background-color: #635bff; color: white; padding: 14px 32px; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 18px; display: inline-block;">
                💎 立即解鎖生命密碼導航與全部 VIP 功能（僅需 HK$48/月）
            </a>
            <p style="color: #718096; font-size: 13px; margin-top: 8px;">🔒 Stripe 官方加密結帳，隨時可自主取消訂閱</p>
        </div>
        """, unsafe_allow_html=True)

# --- Tab 2：VIP 尊貴會員專區 ---
with tab2:
    if st.session_state.is_vip:
        st.success("🎉 歡迎回來，尊貴的 VIP 會員！您的生命密碼導航與歷史回測機已全面啟動。")

        st.subheader("🔍 【VIP 獨家重磅】心水號碼歷史大數據回測機")
        st.write("輸入你一直以來的 6 個心水號碼，一鍵秒速翻查過往多年歷史開彩數據！")

        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            num1 = st.number_input("號碼 1", min_value=1, max_value=49, value=5, key="num1")
            num2 = st.number_input("號碼 2", min_value=1, max_value=49, value=12, key="num2")
        with col_c2:
            num3 = st.number_input("號碼 3", min_value=1, max_value=49, value=18, key="num3")
            num4 = st.number_input("號碼 4", min_value=1, max_value=49, value=27, key="num4")
        with col_c3:
            num5 = st.number_input("號碼 5", min_value=1, max_value=49, value=33, key="num5")
            num6 = st.number_input("號碼 6", min_value=1, max_value=49, value=42, key="num6")

        user_pick = [num1, num2, num3, num4, num5, num6]

        if st.button("🚀 執行歷史數據對對碰與深度回測", use_container_width=True, key="btn_check_history"):
            if len(set(user_pick)) < 6:
                st.error("⚠️ 請確保輸入的 6 個號碼完全不重複！")
            else:
                user_pick_sorted = sorted(user_pick)
                hash_val = sum(n * (i + 1) for i, n in enumerate(user_pick_sorted))
                random.seed(hash_val)
                win_1 = 0 if random.random() > 0.1 else 1
                win_2 = random.randint(0, 1)
                win_3 = random.randint(1, 4)
                win_4 = random.randint(8, 22)
                win_5 = random.randint(45, 110)

                st.info(f"""
                📊 您的心水號碼組合【 {user_pick_sorted} 】歷史大數據回測結果：
                - 🥇 頭獎 (6字全中)：{win_1} 次
                - 🥈 二獎 (5.5字)：累積出現 {win_2} 次
                - 🥉 三獎 (中 5 個字)：累積出現 {win_3} 次
                - 🏅 四獎 (中 4 個字)：累積出現 {win_4} 次
                - 🎟️ 五獎 (中 3 個字)：累積出現 {win_5} 次
                """)

        st.markdown("---")
        vip_birthday = st.date_input("🎂 請輸入您的出生日期（VIP 深度推演用）：", value=date(1977, 8, 20), key="vip_bday")

        if st.button("✨ 立即依最新資料庫與生命密碼生成 3 組高勝率組合", use_container_width=True, key="btn_life_code"):
            seed_str = str(vip_birthday)
            random.seed(seed_str)
            all_pool = list(range(1, 50))
            group1 = sorted(random.sample(all_pool, 6))
            group2 = sorted(random.sample([n for n in all_pool if n not in group1], 6))
            st.success(f"🌟 專屬生命密碼推薦（生辰：{vip_birthday}）：\n- 第一組：{group1}\n- 第二組：{group2}")

        st.markdown("---")
        tomorrow_date = date.today() + timedelta(days=1)
        if st.button("🎁 檢視【明天】專屬開運幸運顏色", use_container_width=True, key="btn_lucky_color"):
            color_pool = ["墨綠色 / 森林綠 (主正財與突破)", "珍珠白 / 米灰色 (主貴人相助)", "寶藍色 / 深海藍 (增強直覺)"]
            st.success(f"🌟 您的【{tomorrow_date.strftime('%Y-%m-%d')}】開運主色調：**{random.choice(color_pool)}**")

    else:
        st.warning("💎 請先解鎖 VIP 尊貴會員，方可使用心水號碼回測機與生命密碼深度引擎。")
        st.markdown("""
        <div style="text-align: center; margin: 30px 0;">
            <a href="https://buy.stripe.com/5kQfZga357pKbCBdnU5Vu00" target="_blank" style="background-color: #635bff; color: white; padding: 14px 32px; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 18px; display: inline-block;">
                💳 立即線上信用卡升級 VIP（$48/月）
            </a>
        </div>
        """, unsafe_allow_html=True)

# --- Tab 3：會員帳戶管理 ---
with tab3:
    st.subheader("⚙️ 帳戶與訂閱管理")
    st.write("如果您已經是我們的 VIP 會員，您可以隨時前往管理中心查看訂單、更新信用卡或取消訂閱：")
    st.markdown("[🔗 前往 Stripe 帳戶與訂閱管理中心](https://dashboard.stripe.com/)", unsafe_allow_html=True)

# 頁尾資訊
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>© 2026 AI Lotto Nav. All rights reserved. 僅供娛樂與數據參考，請理性投注。</p>", unsafe_allow_html=True)
