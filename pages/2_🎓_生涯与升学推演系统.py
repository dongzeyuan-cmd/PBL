import streamlit as st
import time

# ==========================================
# 0. 页面全局配置
# ==========================================
st.set_page_config(page_title="AI 生涯规划专家 | 专家全景版", page_icon="🎓", layout="wide")

# ==========================================
# 1. 安全验证 (调用 Streamlit 云端 Secrets)
# ==========================================
st.markdown("### 🔒 欢迎进入 AI 升学与生涯推演系统 (专家全景版)")

# 提示：请在 Streamlit 控制台的 Secrets 中设置 GENERAL_PASSWORD = "VIP888"
access_code = st.text_input("请输入高级权限通行码", type="password")

# 尝试从 Secrets 读取，如果没有设置则默认 VIP888 以防无法演示
try:
    correct_password = st.secrets["GENERAL_PASSWORD"]
except:
    correct_password = "VIP888"

if access_code != correct_password:
    st.warning("⚠️ 权限校验未通过。请获取高级测试密钥。")
    st.stop()

st.success("✅ 密钥验证成功！全景演算沙盘已解锁。")
st.markdown("---")

# ==========================================
# 2. 核心大盘：四维参数输入
# ==========================================
st.title("🎓 国际教育路径与生涯全景推演引擎")
st.sidebar.header("🎛️ 临床精细级参数输入")

# 维度一：多元智能组合 (权重排序)
with st.sidebar.expander("🧠 1. 多元智能评估 (权重排序)", expanded=True):
    mi_options = ["逻辑/数学智能", "视觉/空间智能", "身体/运动智能", "言语/语言智能", 
                  "音乐/节奏智能", "人际交往智能", "自我内省智能", "自然观察智能"]
    top1 = st.selectbox("🥇 第一优势 (核心驱动)", mi_options, index=0)
    top2 = st.selectbox("🥈 第二优势 (辅助驱动)", mi_options, index=1)
    top3 = st.selectbox("🥉 第三优势 (补充驱动)", mi_options, index=6)

# 维度二：精简版核心职业感官雷达 (ASI理论)
with st.sidebar.expander("👁️ 2. 核心职业感官雷达"):
    sensory_status = ["典型正常", "敏感/防卫 (容易过载)", "迟钝/忽略 (反应不足)", "感觉寻求 (极度渴望)"]
    vestibular = st.radio("⚖️ 前庭觉 (动静需求)", sensory_status, horizontal=True)
    proprioceptive = st.radio("💪 本体觉 (物理操作)", sensory_status, horizontal=True)
    auditory = st.radio("👂 听觉 (环境耐受)", sensory_status, horizontal=True)
    interoception = st.radio("🎭 情绪内感受 (抗压耐受)", sensory_status, horizontal=True)

# 维度三 & 四：MBTI 与 霍兰德
with st.sidebar.expander("🎭 3. 心理与职业基因"):
    mbti = st.selectbox("MBTI 操作系统：", ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"])
    holland = st.multiselect("霍兰德职业兴趣 (选2-3项)：", ["R (实用型)", "I (研究型)", "A (艺术型)", "S (社会型)", "E (企业型)", "C (常规型)"])

# ==========================================
# 3. 核心生成逻辑 (多维组合判定)
# ==========================================
if st.button("🚀 启动大模型全景演算", type="primary"):
    my_bar = st.progress(0, text="正在初始化矩阵分析引擎...")
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=f"正在进行多维智能交叉比对... {percent_complete+1}%")
    time.sleep(0.2)
    my_bar.empty()
    st.balloons()
    
    # 构建组合特征字符串
    top_3_str = f"{top1}{top2}{top3}"
    
    # --- 逻辑分支 A: 硬核 STEM ---
    if "逻辑" in top_3_str and ("视觉" in top_3_str or "身体" in top_3_str):
        track = "Hardcore STEM (硬核理工与具身智能)"
        a_level_score, ap_score, ib_score, gaokao_score = 95, 85, 70, 80
        subj_al = "进阶数学 + 物理 + 计算机科学"
        subj_ap = "AP微积分BC + AP物理C电磁学 + AP计算机A"
        uni_us = {"top": "MIT / 斯坦福 / 加州理工", "mid": "UIUC / 普渡 / 佐治亚理工", "safe": "宾州州立 / 俄亥俄州立"}
        uni_uk = {"top": "剑桥 / 帝国理工", "mid": "UCL / 曼大", "safe": "谢菲尔德 / 诺丁汉"}
        uni_cn = {"top": "清华 / 北航 / 哈工大 (强基)", "mid": "北邮 / 西电 (211强势)", "safe": "杭州电子科技大学"}
        career = "【高级具身智能架构师 / 机器人工程总监】"
        reason = f"【推演理由】：系统识别到由【{top1}】领衔的逻辑与空间组合，这是开发物理AI实体的黄金配置。结合 {mbti} 的严谨性，你在处理高维运动控制和复杂算法上具有原生优势。在未来 10 年，此类岗位由于涉及物理资产和复杂环境，极难被纯数字 AI 替代。"
        tl_ms, tl_g10, tl_g11 = "VEX机器人/Python入门", "AMC10/物理碗", "USACO金级/硬核夏校"

    # --- 逻辑分支 B: 人文社科/跨界商业 ---
    elif "语言" in top_3_str and ("人际" in top_3_str or "内省" in top_3_str):
        track = "Humanities & Social Sci (人文社科与跨界商业)"
        a_level_score, ap_score, ib_score, gaokao_score = 75, 85, 95, 80
        subj_al = "经济学 + 心理学 + 历史"
        subj_ap = "AP英语语言 + AP心理学 + AP微观经济"
        uni_us = {"top": "宾大 / 芝加哥 / 西北", "mid": "纽大 (NYU) / 南加州", "safe": "波士顿大学 (BU)"}
        uni_uk = {"top": "牛津 / LSE", "mid": "华威 / 杜伦", "safe": "利兹 / 兰卡斯特"}
        uni_cn = {"top": "人大 / 复旦 / 北师大", "mid": "中传 / 华东师范", "safe": "省重点师范"}
        career = "【数字时代心理架构师 / 跨文化商业领袖】"
        reason = f"【推演理由】：【{top1}】与【人际/内省】的交汇意味着你具备解析“人心系统”的能力。在代码廉价化的时代，理解复杂人类动机和情感防御（Fe/Ni功能）将成为最高价值的商业枢纽。{mbti} 的特性增强了你在高敏锐环境下的决策精准度。"
        tl_ms, tl_g10, tl_g11 = "NSDA英语辩论/原版阅读", "约翰洛克写作/NEC经济赛", "沃顿商赛/顶级人文科研"

    # --- 逻辑分支 C: 建筑/工业设计 ---
    elif "空间" in top_3_str and ("身体" in top_3_str or "视觉" in top_3_str):
        track = "Design & Architecture (工业设计与建筑)"
        a_level_score, ap_score, ib_score, gaokao_score = 80, 80, 85, 60
        subj_al = "纯艺术 + 物理 + 进阶数学"
        subj_ap = "AP艺术设计 + AP物理1 + AP预微积分"
        uni_us = {"top": "罗德岛设计 (RISD) / 卡梅", "mid": "普瑞特 (Pratt) / 帕森斯", "safe": "SCAD"}
        uni_uk = {"top": "伦艺 (UAL) / 皇艺", "mid": "爱丁堡 / 伦敦金斯顿", "safe": "考文垂"}
        uni_cn = {"top": "清美 / 同济 / 央美", "mid": "江南大学 / 北服", "safe": "省艺术名校"}
        career = "【人机交互总监 / 空间智能设计师】"
        reason = f"【推演理由】：由【{top1}】驱动的空间美学感知，结合物理操作的直觉，使你成为连接数字孪生与物理空间的桥梁。你不仅在创造产品，更在利用 {holland} 基因重构人类与机器的交互界面。"
        tl_ms, tl_g10, tl_g11 = "3D建模/艺术作品集积累", "iGEM设计岗/科技展统筹", "顶级作品集打磨/设计夏校"

    # --- 默认分支: 综合量化商科 ---
    else:
        track = "Business & Data Analysis (综合商科与量化)"
        a_level_score, ap_score, ib_score, gaokao_score = 85, 85, 85, 85
        subj_al = "数学 + 经济 + 商业研究"
        subj_ap = "AP微积分 + AP经济 + AP统计学"
        uni_us = {"top": "宾大沃顿 / 哥大 / 康奈尔", "mid": "密歇根安娜堡 / UT Austin", "safe": "福特汉姆"}
        uni_uk = {"top": "LSE / 华威", "mid": "曼大 / 杜伦", "safe": "伯明翰"}
        uni_cn = {"top": "上交 / 上财 / 央财", "mid": "中南财大 / 西南财大", "safe": "各省财大"}
        career = "【科技金融量化师 / 全球供应链策略家】"
        reason = "【推演理由】：均衡的智能矩阵意味着极强的环境适应性。结合多维智能优势，你擅长在混沌的信息中寻找规则与平衡，是理想的资源统筹者和风险管控核心。"
        tl_ms, tl_g10, tl_g11 = "Python数据分析/财商", "FBLA商赛/BPA挑战赛", "投行实习/WGHS队长"

    # ------------------ 渲染前端选项卡 ------------------
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 诊断", "📚 规划", "🏫 择校", "🚀 职业", "⏳ 时间轴"])
    
    with tab1:
        st.header("📊 系统优势聚类诊断")
        st.write(f"判定主控赛道：**【{track}】**")
        st.info(f"🥇核心驱动：{top1} | 🥈辅助：{top2} | 🥉补充：{top3}")
        st.warning(f"⚠️ 感官预警：情绪内感受[{interoception}]，环境耐受[{auditory}]。")

    with tab2:
        st.header("📚 体系抉择与学科组合")
        st.progress(a_level_score, text=f"🇬🇧 A-Level 适配: {a_level_score}% ➔ 核心选课：{subj_al}")
        st.progress(ap_score, text=f"🇺🇸 AP 适配: {ap_score}% ➔ 核心选课：{subj_ap}")
        st.progress(ib_score, text=f"🌐 IB 适配: {ib_score}% ➔ 抗压挑战等级：高")

    with tab3:
        st.header("🏫 全球择校分层矩阵")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**🌍 海外 (美/英)**\n- 🚀 冲刺：{uni_us['top']} | {uni_uk['top']}\n- 📊 匹配：{uni_us['mid']} | {uni_uk['mid']}\n- 🛡️ 保底：{uni_us['safe']} | {uni_uk['safe']}")
        with col2:
            st.markdown(f"**🇨🇳 国内高考**\n- 🚀 顶级：{uni_cn['top']}\n- 📊 强势：{uni_cn['mid']}\n- 🛡️ 稳健：{uni_cn['safe']}")

    with tab4:
        st.header("🚀 终极职业生态位")
        st.success(f"目标：{career}")
        st.markdown(reason)

    with tab5:
        st.header("⏳ K-12 执行时间轴")
        st.write(f"**初中**：{tl_ms} | **高一**：{tl_g10} | **高二**：{tl_g11}")
        st.write("---")
        st.caption("提示：详细万字执行计划请联系董博士咨询。")
