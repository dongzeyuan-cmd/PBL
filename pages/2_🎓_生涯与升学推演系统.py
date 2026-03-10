import streamlit as st
import time

st.set_page_config(page_title="AI 生涯规划专家 | 专家全景版", page_icon="🎓", layout="wide")

st.markdown("### 🔒 欢迎进入 AI 升学与生涯推演系统 (专家全景版)")
access_code = st.text_input("请输入高级权限通行码", type="password")

if access_code != "VIP888":
    st.warning("⚠️ 密钥为空或不正确。获取高级测试密钥，请联系董主任。")
    st.stop()

st.success("✅ 密钥验证成功！全景演算沙盘已解锁。")
st.markdown("---")

st.title("🎓 国际教育路径与生涯全景推演引擎")

st.sidebar.header("🎛️ 临床精细级参数输入")

# 维度一：多元智能
with st.sidebar.expander("🧠 1. 多元智能评估 (权重排序)", expanded=True):
    mi_options = ["逻辑/数学智能", "视觉/空间智能", "身体/运动智能", "言语/语言智能", 
                  "音乐/节奏智能", "人际交往智能", "自我内省智能", "自然观察智能"]
    top1 = st.selectbox("🥇 第一优势 (核心驱动)", mi_options, index=0)
    top2 = st.selectbox("🥈 第二优势 (辅助驱动)", mi_options, index=1)
    top3 = st.selectbox("🥉 第三优势 (补充驱动)", mi_options, index=6)

# 维度二：感官雷达
with st.sidebar.expander("👁️ 2. 感官雷达定位 (临床体征)"):
    sensory_status = ["典型正常", "敏感/防卫 (逃避)", "迟钝/忽略 (反应不足)", "感觉寻求 (极度渴望)"]
    tactile_light = st.radio("🪶 轻触觉 (温度/材质)", sensory_status, horizontal=True)
    tactile_deep = st.radio("🫂 深触觉 (重物/拥抱)", sensory_status, horizontal=True)
    vestibular = st.radio("⚖️ 前庭觉 (旋转/平衡)", sensory_status, horizontal=True)
    interoception_emotion = st.radio("🎭 情绪内感受 (躯体化)", sensory_status, horizontal=True)

# 维度三 & 四：MBTI 与 霍兰德
with st.sidebar.expander("🎭 3. MBTI & 🧬 4. 霍兰德基因"):
    mbti = st.selectbox("MBTI 人格：", ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"])
    holland = st.multiselect("霍兰德职业兴趣：", ["R (实用型)", "I (研究型)", "A (艺术型)", "S (社会型)", "E (企业型)", "C (常规型)"])

if st.button("🚀 启动大模型全景演算", type="primary"):
    my_bar = st.progress(0, text="正在初始化矩阵分析引擎...")
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=f"正在进行多维智能交叉比对... {percent_complete+1}%")
    time.sleep(0.2)
    my_bar.empty()
    st.balloons()
    
    # ------------------ 核心动态算法：基于前三大优势的组合判定 ------------------
    top_3_str = str(top1) + str(top2) + str(top3)
    
    if "逻辑" in top_3_str and "空间" in top_3_str:
        track = "Hardcore STEM (硬核理工与工程)"
        a_level_score, ap_score, ib_score, gaokao_score = 95, 85, 75, 80
        subj_al = "进阶数学 + 物理 + 计算机科学 (放弃短板文科)"
        subj_ap = "AP微积分BC + AP物理C电磁学 + AP计算机A"
        subj_ib = "数学 AA HL + 物理 HL + 化学 SL"
        uni_us = {"top": "MIT / 斯坦福 / 加州理工", "mid": "UIUC / 普渡 / 佐治亚理工", "safe": "宾州州立 / 俄亥俄州立"}
        uni_uk = {"top": "剑桥 / 帝国理工", "mid": "UCL / 曼大", "safe": "谢菲尔德 / 诺丁汉"}
        uni_cn = {"top": "清华 / 北航 / 哈工大 (985强基)", "mid": "北邮 / 西电 (211强势)", "safe": "杭州电子科技大学等"}
        career = "【高级具身智能架构师 / 机器人工程总监】"
        reason = f"推演理由：系统检测到你拥有罕见的【逻辑+空间】双高核驱动，结合 {mbti} 的架构特性，你具备极强的将抽象数据转化为三维物理实体的能力，AI 时代不可替代的底层奠基者。"
        
    elif "语言" in top_3_str and ("人际" in top_3_str or "内省" in top_3_str):
        track = "Humanities & Social Sci (人文社科与传媒)"
        a_level_score, ap_score, ib_score, gaokao_score = 70, 85, 95, 75
        subj_al = "经济学 + 心理学 + 历史/社会学"
        subj_ap = "AP英语语言 + AP心理学 + AP微观经济"
        subj_ib = "英语A HL + 心理学 HL + 经济学 HL (完美驾驭大论文)"
        uni_us = {"top": "宾大 / 芝加哥 / 西北", "mid": "纽大 (NYU) / 南加州", "safe": "波士顿大学 (BU)"}
        uni_uk = {"top": "牛津 / LSE", "mid": "华威 / 杜伦", "safe": "利兹 / 兰卡斯特"}
        uni_cn = {"top": "人大 / 复旦 / 北师大", "mid": "中传 / 华东师范", "safe": "各省重点师范类/政法类"}
        career = "【数字时代心理干预专家 / 跨文化商业领袖】"
        reason = f"推演理由：【语言+人际/内省】的高维组合，叠加 {mbti} 的共情或领导特质，使你拥有极强的社会网络穿透力。在代码被 AI 取代后，处理复杂人际博弈和人文关怀将成为最高溢价能力。"

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
        reason = f"推演理由：【空间+身体】的组合让你拥有无可挑剔的物理美学与动手直觉。结合 {holland} 的实干与艺术基因，你是最懂如何把冰冷科技转化为适宜人类操作的高级创作者。"
        
    else:
        track = "Comprehensive Business & Data (综合商科与量化)"
        a_level_score, ap_score, ib_score, gaokao_score = 85, 85, 85, 85
        subj_al = "数学 + 经济学 + 商业研究"
        subj_ap = "AP微积分 + AP宏微观经济 + AP统计学"
        subj_ib = "数学 AI HL + 经济学 HL + 商业管理 HL"
        uni_us = {"top": "宾大沃顿 / 哥大", "mid": "密歇根安娜堡 / 德州奥斯汀", "safe": "福特汉姆大学"}
        uni_uk = {"top": "LSE / UCL", "mid": "曼大 / 华威商学院", "safe": "伯明翰 / 利物浦"}
        uni_cn = {"top": "上财 / 央财 / 贸大", "mid": "西南财大 / 中南财大", "safe": "各省财经大学"}
        career = "【科技金融量化分析师 / 科技企业操盘手】"
        reason = f"推演理由：极其均衡的能力矩阵，让你在数据运算与资源统筹中游刃有余。结合 {mbti} 和 {holland} 的底色，你善于制定规则、管理风险，是掌控商业资源流动的枢纽核心。"

    # ------------------ 渲染前端选项卡 ------------------
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 1. 优势聚类诊断", 
        "📚 2. 国际学科排雷", 
        "🏫 3. 全球择校梯队", 
        "🚀 4. 终极职业推演",
        "⏳ 5. K-12 时间轴"
    ])
    
    with tab1:
        st.header("📊 系统架构与优势聚类诊断")
        st.write(f"根据数据封包，系统将前三大优势进行交汇分析，判定你的主控赛道为：**【{track}】**")
        col1, col2 = st.columns(2)
        with col1:
            st.info("**💡 组合爆发点**")
            st.write(f"- 第一优势 **{top1}** 决定了你的天赋上限。")
            st.write(f"- 第二/三优势 **{top2}** 与 **{top3}** 为你构建了无法被单一维度取代的护城河。")
        with col2:
            st.warning("**⚠️ 功耗与系统预警**")
            st.write(f"感官过载警报：前庭觉[{vestibular}]，内感受[{interoception_emotion}]。在执行高压学术任务时需防范躯体化报错。")

    with tab2:
        st.header("📚 国际体系抉择与学科组合")
        st.write(f"针对 **【{track}】** 赛道，各体系的最优解如下：")
        st.write(f"👉 **英国 A-Level 路线**：{subj_al} *(适配度: {a_level_score}%)*")
        st.write(f"👉 **美国 AP 路线**：{subj_ap} *(适配度: {ap_score}%)*")
        st.write(f"👉 **国际 IB 路线**：{subj_ib} *(适配度: {ib_score}%)*")
        st.write("---")
        st.markdown("**架构师选课逻辑：** 国际高中的选课不是看你喜欢什么，而是为了向大学证明你具备该赛道的学术深度。切忌文理盲目混搭导致画像模糊。")

    with tab3:
        st.header("🏫 全球高教择校矩阵图谱")
        st.write("大学申请遵循“风险对冲策略”，系统已为您生成分层名单：")
        col_intl, col_dom = st.columns(2)
        with col_intl:
            st.subheader("🌍 海外顶尖名校体系")
            st.markdown(f"""
            * **🎯 冲刺梯队 (Reach - 录取率<10%)**：
              (美) {uni_us['top']}
              (英) {uni_uk['top']}
            * **📊 匹配梯队 (Match - 录取率15-30%)**：
              (美) {uni_us['mid']}
              (英) {uni_uk['mid']}
            * **🛡️ 保底梯队 (Safety - 录取率>40%)**：
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
        st.success(f"**核心锚点：{career}**")
        st.write(reason)
        st.write("在 AGI 时代，我们不预测具体的‘岗位’，而是预测你不可替代的‘生态位’。你的底层智能架构决定了你将作为系统规则的制定者，而非执行者。")

    with tab5:
        st.header("⏳ 核心执行：K-12 逆向推演时间轴")
        if "Hardcore STEM" in track:
            st.markdown("**(理科路线摘要)**\n* **初中**：AMC8 拿奖，熟练掌握 Python 语法。\n* **高一**：物理碗，丘成桐科学奖组队。\n* **高二**：AP物理/微积分双满分，冲刺硬核夏校 (如ROSS)。")
        elif "Humanities" in track:
            st.markdown("**(人文社科路线摘要)**\n* **初中**：全英文辩论赛打底，积累阅读量。\n* **高一**：NEC经济学挑战赛，约翰洛克写作大赛。\n* **高二**：发表独立社科调研论文 (EPQ/EE)，参与顶级人文夏校。")
        else:
            st.markdown("**(综合设计路线摘要)**\n* **初中**：跨学科创客项目，积累基础素描/3D建模作品。\n* **高一**：商业挑战赛 (FBLA) 或国际基因工程机器大赛 (iGEM) 美工岗。\n* **高二**：打磨极具个人化色彩的作品集 (Portfolio)。")
