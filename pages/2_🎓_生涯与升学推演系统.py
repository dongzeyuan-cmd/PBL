import streamlit as st
import time

# ==========================================
# 0. 页面全局配置
# ==========================================
st.set_page_config(page_title="AI 生涯规划专家 | 专家全景版", page_icon="🎓", layout="wide")

st.markdown("### 🔒 欢迎进入 AI 升学与生涯推演系统 (专家全景版)")
access_code = st.text_input("请输入高级权限通行码", type="password")

access_code_secret = st.secrets["GENERAL_PASSWORD"] 
# 未来接入 DeepSeek/OpenAI 时使用：
# api_key = st.secrets["DEEPSEEK_API_KEY"]

if access_code != access_code_secret:
    st.warning("⚠️ 权限校验未通过。")
    st.stop()

st.success("✅ 密钥验证成功！全景演算沙盘已解锁。")
st.markdown("---")

st.title("🎓 国际教育路径与生涯全景推演引擎")
st.write("左侧录入核心底层参数，右侧生成多维战略蓝图及执行时间轴。")

st.sidebar.header("🎛️ 核心参数输入台")

# ==========================================
# 1. 多元智能组合 (权重排序)
# ==========================================
with st.sidebar.expander("🧠 1. 多元智能评估 (权重排序)", expanded=True):
    mi_options = ["逻辑/数学智能", "视觉/空间智能", "身体/运动智能", "言语/语言智能", 
                  "音乐/节奏智能", "人际交往智能", "自我内省智能", "自然观察智能"]
    top1 = st.selectbox("🥇 第一优势 (核心驱动)", mi_options, index=0)
    top2 = st.selectbox("🥈 第二优势 (辅助驱动)", mi_options, index=1)
    top3 = st.selectbox("🥉 第三优势 (补充驱动)", mi_options, index=6)

# ==========================================
# 2. 精简版核心职业感官雷达 (ASI理论)
# ==========================================
with st.sidebar.expander("👁️ 2. 核心职业感官雷达 (ASI理论)"):
    st.caption("提取对学业与职业环境最具影响力的四大体征：")
    sensory_status = ["典型正常", "敏感/防卫 (容易过载)", "迟钝/忽略 (反应不足)", "感觉寻求 (极度渴望)"]
    
    vestibular = st.radio("⚖️ 前庭觉 (动静与注意力需求)", sensory_status, horizontal=True)
    proprioceptive = st.radio("💪 本体与深触觉 (物理操作与空间感知)", sensory_status, horizontal=True)
    auditory = st.radio("👂 听觉与环境 (开放环境噪音频段容忍度)", sensory_status, horizontal=True)
    interoception = st.radio("🎭 情绪内感受 (高压环境躯体化反应)", sensory_status, horizontal=True)

# ==========================================
# 3. MBTI 与 霍兰德
# ==========================================
with st.sidebar.expander("🎭 3. 心理与职业基因"):
    mbti = st.selectbox("MBTI 操作系统：", ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"])
    holland = st.multiselect("霍兰德职业兴趣 (选2-3项)：", ["R (实用型-硬核操作)", "I (研究型-科学推演)", "A (艺术型-美学创造)", "S (社会型-人文共情)", "E (企业型-商业统筹)", "C (常规型-规则数据)"])

# ==========================================
# 核心生成逻辑
# ==========================================
if st.button("🚀 启动大模型全景演算", type="primary"):
    my_bar = st.progress(0, text="正在初始化矩阵分析引擎...")
    for percent_complete in range(100):
        time.sleep(0.015)
        my_bar.progress(percent_complete + 1, text=f"正在进行多维智能交叉比对与全球数据库检索... {percent_complete+1}%")
    time.sleep(0.2)
    my_bar.empty()
    st.balloons()
    
    # ------------------ 动态算法：前三大优势聚类 ------------------
    top_3_str = str(top1) + str(top2) + str(top3)
    
    if "逻辑" in top_3_str and "空间" in top_3_str:
        track = "Hardcore STEM (硬核理工与具身智能)"
        a_level_score, ap_score, ib_score, gaokao_score = 95, 85, 70, 80
        subj_al = "进阶数学 + 物理 + 计算机科学 (极客组合)"
        subj_ap = "AP微积分BC + AP物理C电磁学 + AP计算机A"
        subj_ib = "数学 AA HL + 物理 HL + 化学 SL"
        uni_us = {"top": "MIT / 斯坦福 / 加州理工", "mid": "UIUC / 普渡 / 佐治亚理工", "safe": "宾州州立 / 俄亥俄州立"}
        uni_uk = {"top": "剑桥 / 帝国理工", "mid": "UCL / 曼彻斯特", "safe": "谢菲尔德 / 诺丁汉"}
        uni_cn = {"top": "清华 / 北航 / 哈工大 (985强基)", "mid": "北邮 / 西电 (211强势)", "safe": "杭州电子科技大学"}
        career = "【高级具身智能架构师 / 机器人工程总监】"
        reason = f"【推演理由】：系统检测到你拥有罕见的【逻辑+空间】双高核驱动，结合 {mbti} 的架构特性，你具备极强的将抽象数据转化为三维物理实体的能力。在 AGI 时代，你是不可替代的物理世界底层奠基者。"
        tl_ms = "AMC8 数学竞赛、VEX IQ 机器人赛、Python 语法入门"
        tl_g10 = "AMC10、物理碗 (PhysicsBowl)、丘成桐中学科学奖组队"
        tl_g11 = "HiMCM 数模竞赛、USACO 计算机竞赛、顶级硬核夏校 (如ROSS, SSP)"
        
    elif "语言" in top_3_str and ("人际" in top_3_str or "内省" in top_3_str):
        track = "Humanities & Social Sci (人文社科与跨界商业)"
        a_level_score, ap_score, ib_score, gaokao_score = 75, 85, 95, 80
        subj_al = "经济学 + 心理学 + 历史/社会学"
        subj_ap = "AP英语语言 + AP心理学 + AP微观经济"
        subj_ib = "英语A HL + 心理学 HL + 经济学 HL"
        uni_us = {"top": "宾大 / 芝加哥 / 西北", "mid": "纽大 (NYU) / 南加州", "safe": "波士顿大学 (BU)"}
        uni_uk = {"top": "牛津 / LSE", "mid": "华威 / 杜伦", "safe": "利兹 / 兰卡斯特"}
        uni_cn = {"top": "人大 / 复旦 / 北师大", "mid": "中传 / 华东师范", "safe": "各省重点师范类/政法类"}
        career = "【数字时代心理干预专家 / 跨文化商业领袖】"
        reason = f"【推演理由】：【语言+人际/内省】的高维组合，叠加 {mbti} 的共情或领导特质，使你拥有极强的社会网络穿透力。当底层代码被 AI 取代后，处理复杂人际博弈、调动人类情绪将成为最高溢价能力。"
        tl_ms = "英文原版阅读积累、全英文辩论赛打底 (NSDA)"
        tl_g10 = "NEC全美经济学挑战赛、MUN模拟联合国、约翰洛克写作大赛"
        tl_g11 = "CTB全球青年研究创新论坛、沃顿商赛、发表独立社科调研论文 (EPQ/EE)"

    elif "空间" in top_3_str and "身体" in top_3_str:
        track = "Architecture & Industrial Design (建筑与工业设计)"
        a_level_score, ap_score, ib_score, gaokao_score = 80, 80, 85, 60
        subj_al = "纯艺术 (Fine Art) + 物理 + 设计与技术"
        subj_ap = "AP 2D艺术设计 + AP 艺术史 + AP 物理1"
        subj_ib = "视觉艺术 HL + 物理 SL + 设计技术 HL"
        uni_us = {"top": "罗德岛设计学院 / 卡梅", "mid": "普瑞特 (Pratt) / 帕森斯", "safe": "萨凡纳艺术设计学院 (SCAD)"}
        uni_uk = {"top": "伦艺 (UAL) / 皇家艺术学院", "mid": "爱丁堡 / 伦敦金斯顿", "safe": "考文垂 (汽车设计)"}
        uni_cn = {"top": "清华美院 / 同济", "mid": "央美 / 江南大学", "safe": "北京服装学院"}
        career = "【人机交互设计师 (HCI) / 智能硬件产品经理】"
        reason = f"【推演理由】：【空间+身体】的组合让你拥有无可挑剔的物理美学与动手直觉。结合极其落地的操作基因，你是最懂如何把冰冷科技转化为适宜人类感官的高级创作者。"
        tl_ms = "跨学科创客项目、积累基础素描/3D建模作品"
        tl_g10 = "参加科技展美工统筹、国际基因工程机器大赛 (iGEM) 设计岗"
        tl_g11 = "打磨极具个人化色彩的顶级作品集 (Portfolio)、申请顶级设计夏校"
        
    else:
        track = "Comprehensive Business & Data (综合商科与量化)"
        a_level_score, ap_score, ib_score, gaokao_score = 85, 85, 85, 85
        subj_al = "数学 + 经济学 + 商业研究"
        subj_ap = "AP微积分 + AP宏微观经济 + AP统计学"
        subj_ib = "数学 AI HL + 经济学 HL + 商业管理 HL"
        uni_us = {"top": "宾大沃顿 / 哥大 / 康奈尔", "mid": "密歇根安娜堡 / 德州奥斯汀", "safe": "福特汉姆大学"}
        uni_uk = {"top": "LSE / UCL", "mid": "曼大 / 华威商学院", "safe": "伯明翰 / 利物浦"}
        uni_cn = {"top": "上交 / 上财 / 央财", "mid": "西南财大 / 中南财大", "safe": "各省重点财经大学"}
        career = "【科技金融量化分析师 / 科技企业操盘手】"
        reason = f"【推演理由】：极其均衡的能力矩阵，让你在数据运算与资源统筹中游刃有余。结合 {mbti} 的底色，你善于制定规则、管理风险，是掌控商业资源流动的枢纽核心。"
        tl_ms = "财商启蒙、Python数据分析基础"
        tl_g10 = "FBLA 商业挑战赛、BPA 商业全能挑战赛"
        tl_g11 = "投行/咨询公司中学生实习项目、沃顿商赛 (WGHS) 队长"

    # ------------------ 渲染前端选项卡 ------------------
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 1. 优势聚类诊断", 
        "📚 2. 学科与体系规划", 
        "🏫 3. 全球择校矩阵", 
        "🚀 4. 终极职业推演",
        "⏳ 5. K-12 执行时间轴"
    ])
    
    with tab1:
        st.header("📊 系统架构与优势聚类诊断")
        st.write(f"系统将前三大优势进行交汇降维分析，判定主控赛道为：**【{track}】**")
        col1, col2 = st.columns(2)
        with col1:
            st.info("**💡 组合爆发点**")
            st.write(f"- 核心天赋上限由 **{top1}** 决定。")
            st.write(f"- 护城河壁垒由 **{top2}** 与 **{top3}** 构建，形成无法被单一 AI 取代的复合型能力。")
        with col2:
            st.warning("**⚠️ 环境与功耗预警**")
            st.write(f"- **高压防卫警告**：系统检测情绪内感受为[{interoception}]。如果此项为敏感/逃避，**强烈建议规避 IB 体系**及未来的高压金融投行岗位，防范躯体化断电。")
            st.write(f"- **空间物理干预**：听觉反馈为[{auditory}]，前庭觉为[{vestibular}]。如果偏向敏感，未来择校与就业必须选择“独立静音空间”，拒绝开放式打卡办公区。")

    with tab2:
        st.header("📚 国际体系抉择与学科排雷")
        st.write(f"针对 **【{track}】** 赛道，各体系的最优满配打法：")
        st.progress(a_level_score, text=f"🇬🇧 A-Level 适配度：{a_level_score}% (允许战略性偏科) ➔ 核心选课：{subj_al}")
        st.progress(ap_score, text=f"🇺🇸 AP 适配度：{ap_score}% (灵活变通，主线+副本) ➔ 核心选课：{subj_ap}")
        st.progress(ib_score, text=f"🌐 IB 适配度：{ib_score}% (全人教育，抗压极强) ➔ 核心选课：{subj_ib}")
        st.progress(gaokao_score, text=f"🇨🇳 国内高考体系：{gaokao_score}% (规则适应者，六边形战士)")
        st.write("---")
        st.markdown("**🎓 架构师铁律：** 国际高中的选课不是看孩子“喜欢”什么，而是用科目组合向顶尖大学证明你具备该赛道的**学术深度**。切忌文理盲目混搭导致画像崩塌。")

    with tab3:
        st.header("🏫 全球高教择校分层图谱")
        st.write("名校申请必须遵循“风险对冲策略”，AI 已基于您的能力矩阵生成精准的三级分层名单：")
        col_intl, col_dom = st.columns(2)
        with col_intl:
            st.subheader("🌍 海外顶尖名校 (美英双申)")
            st.markdown(f"""
            * **🎯 冲刺梯队 (Reach - 录取率极低)**：
              (美) {uni_us['top']}
              (英) {uni_uk['top']}
            * **📊 匹配梯队 (Match - 稳健发力区)**：
              (美) {uni_us['mid']}
              (英) {uni_uk['mid']}
            * **🛡️ 保底梯队 (Safety - 托底安全网)**：
              (美) {uni_us['safe']}
              (英) {uni_uk['safe']}
            """)
        with col_dom:
            st.subheader("🇨🇳 国内高考/强基体系")
            st.markdown(f"""
            * **🎯 顶级目标 (C9/顶级985)**：
              {uni_cn['top']}
            * **📊 中坚力量 (强势211/双一流)**：
              {uni_cn['mid']}
            * **🛡️ 省属重点 (稳健保底)**：
              {uni_cn['safe']}
            """)

    with tab4:
        st.header("🚀 10年期：职场生态终局推演")
        st.success(f"**终极目标生态位：{career}**")
        st.markdown(reason)
        st.write("> *在通用人工智能（AGI）全面落地的未来，我们不预测被淘汰的具体岗位，我们只锁定不可替代的生态位。您的底层架构注定您将成为系统规则的制定者。*")

    with tab5:
        st.header("⏳ 核心执行：K-12 逆向推演时间轴")
        st.write("战略已定，以下为各关键节点的战术动作拆解：")
        
        st.markdown("""
        ### 🌱 启蒙与探索期 (小学 G1-G6)
        * **核心任务**：保护系统算力（好奇心），修复底层硬件（感统代偿干预）。
        * **学科动作**：沉浸式英语阅读打底，切忌过早高压刷题引发“内感受觉情绪剥离”。
        """)
        
        st.markdown("""
        ---
        ### 🔍 定位与奠基期 (初中 G7-G9)
        * **学术准备**：GPA 稳定在 A 梯队，完成托福/雅思首考摸底。
        * **赛道试水**：开始参加初级赛事验证天赋组合。
        """)
        st.info(f"**🎯 专属动作**：{tl_ms}")

        st.markdown("""
        ---
        ### ⚔️ 冲刺与发力期 (高一 G10)
        * **系统切换**：确立 AP/A-Level/IB 体系，选定前文推演的核心科目。
        * **背景提升**：打磨深度 PBL 课外活动，进军高含金量赛事。
        """)
        st.info(f"**🎯 专属动作**：{tl_g10}")

        st.markdown("""
        ---
        ### 炼狱模式 (高二 G11) —— 申请前最关键战役
        * **硬核输出**：挑战最高难度学科，确保极高的预估分 (PG)；托福/SAT出分。
        * **定海神针**：产出顶级学术成果，冲击赛事金奖。
        """)
        st.info(f"**🎯 专属动作**：{tl_g11}")

        st.markdown("""
        ---
        ### 🎓 战略投递期 (高三 G12)
        * **上学期**：基于此报告的底层基因，撰写极其个人化的主文书 (Personal Statement)；完成早申 (ED/EA) 及牛剑面试准备。
        * **下学期**：维持最终大考成绩，防止 Offer 撤回，准备签证与行前过渡。
        """)
