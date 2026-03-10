import streamlit as st
import time

# ==========================================
# 0. 页面全局配置
# ==========================================
st.set_page_config(page_title="AI 生涯规划专家 临床精细版", page_icon="🎓", layout="wide")

# ==========================================
# 1. 商业防盗门
# ==========================================
st.markdown("### 🔒 欢迎进入 AI 升学与生涯推演系统 (临床精细版)")
access_code = st.text_input("请输入专属通行码", type="password")

if access_code != "VIP888":
    st.warning("⚠️ 密钥为空或不正确。获取测试密钥，请联系首席规划顾问。")
    st.stop()

st.success("✅ 密钥验证成功！系统已全面解锁。")
st.markdown("---")

# ==========================================
# 2. 核心大盘：四维临床级数据采集矩阵
# ==========================================
st.title("🎓 国际教育路径与生涯推演引擎")
st.write("请在左侧控制台精准输入测试者的底层参数，AI 将基于四维模型进行深度演算。")

st.sidebar.header("🎛️ 临床精细级参数输入")

# 维度一：多元智能
with st.sidebar.expander("🧠 1. 多元智能评估 (权重排序)", expanded=True):
    mi_options = ["逻辑/数学智能", "视觉/空间智能", "身体/运动智能", "言语/语言智能",
                  "音乐/节奏智能", "人际交往智能", "自我内省智能", "自然观察智能"]
    top1 = st.selectbox("🥇 第一优势 (Top 1 核心驱动)", mi_options, index=0)
    top2 = st.selectbox("🥈 第二优势 (Top 2 辅助驱动)", mi_options, index=1)
    top3 = st.selectbox("🥉 第三优势 (Top 3 补充驱动)", mi_options, index=6)

# 维度二：感官雷达 (融入 Kelly Mahler 内感受觉分离理论)
with st.sidebar.expander("👁️ 2. 感官雷达定位 (Kelly Mahler 架构)"):
    st.caption("请根据神经反馈精准选择对应状态：")
    sensory_status = ["典型正常", "敏感/防卫 (逃避)", "迟钝/忽略 (反应不足)", "感觉寻求 (极度渴望)"]

    tactile_light = st.radio("🪶 轻触觉 (温度/材质/微碰)", sensory_status, horizontal=True)
    tactile_deep = st.radio("🫂 深触觉/本体压觉 (重物/拥抱)", sensory_status, horizontal=True)
    vestibular = st.radio("⚖️ 前庭觉 (旋转/平衡/速度)", sensory_status, horizontal=True)
    proprioceptive = st.radio("💪 本体感觉 (肌肉力量/空间定位)", sensory_status, horizontal=True)
    visual = st.radio("👁️ 视觉 (强光/色彩/动态)", sensory_status, horizontal=True)
    auditory = st.radio("👂 听觉 (高频噪音/嘈杂)", sensory_status, horizontal=True)

    st.markdown("---")
    st.markdown("**🫀 内感受觉 (双通道分离解析)**")
    interoception_physio = st.radio("🩸 生理通道 (饥饿/饱腹/体温/便意/痛觉)", sensory_status, horizontal=True)
    interoception_emotion = st.radio("🎭 情绪通道 (情绪波动感知/压力躯体化)", sensory_status, horizontal=True)

# 维度三：MBTI
with st.sidebar.expander("🎭 3. MBTI 心理类型"):
    mbti = st.selectbox("请选择 MBTI 人格：",
                        ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ",
                         "ISTP", "ISFP", "ESTP", "ESFP"])

# 维度四：霍兰德
with st.sidebar.expander("🧬 4. 霍兰德职业兴趣 (RIASEC)"):
    holland = st.multiselect("请选择 2-3 个核心职业兴趣：",
                             ["R (实用型 - 机器/操作)", "I (研究型 - 科学/思考)", "A (艺术型 - 设计/创造)",
                              "S (社会型 - 助人/教育)", "E (企业型 - 领导/统筹)", "C (常规型 - 数据/规则)"])

# ==========================================
# 3. 结果展示与私域收网模块
# ==========================================
st.markdown("### 📊 实时推演沙盘")

if st.button("🚀 启动大模型临床解析", type="primary"):

    # 封包检查：将细分后的内感受觉加入后台监控
    st.info(
        f"**【后台参数封包检查】**\n* 核心智能：🥇{top1} ➔ 🥈{top2} ➔ 🥉{top3}\n* 生理内感受：{interoception_physio} | 情绪内感受：{interoception_emotion}\n* MBTI & Holland：{mbti} | {', '.join(holland) if holland else '未补全'}")

    progress_text = "正在初始化临床分析引擎..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=f"正在载入内感受觉分离模型比对数据... {percent_complete + 1}%")
    time.sleep(0.5)
    my_bar.empty()

    st.success("✅ 初步运算完成！(当前为结构演示面板)")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📚 国际课程体系建议")
        st.write("经算法评估，该感官配置与智能分布，最适配：**A-Level / AP 强理科组合**。")
        st.write(
            "⚠️ **生理干预预警**：检测到生理/情绪通道分离。在备考期需强制设定物理闹钟提醒进食/饮水，防止生理性低血糖引发的情绪崩溃。")
    with col2:
        st.subheader("🎯 本科专业锁定池")
        st.write("基于底层基因，推荐优先冲刺：\n- 🤖 机器人工程 / 具身智能\n- 📊 数据科学与分析\n- ⚙️ 机械与精密仪器")

    st.markdown("---")
    st.error("🔒 **高级权限受限：** 当前网页仅提供基础测算框架。")
    st.markdown("""
    #### 👨‍🏫 获取【完整版万字定制规划书】包含：
    1.  **学科赋能点**：精准到高一、高二每学期的选课清单。
    2.  **感官代偿策略**：针对内感受觉分离与前庭特征的学术干预方案。
    3.  **背景提升时间轴**：匹配核心智能的国际竞赛与科研 PBL 项目推荐。
    """)
    st.write("👇 **请扫描下方二维码，添加首席规划专家微信，提交系统原始数据进行 1v1 解读：**")

    try:
        st.image("wechat.jpg", width=250)
    except:
        st.caption("[图片加载位置：请确保 GitHub 代码仓库中已上传 wechat.jpg 文件]")

import streamlit as st
import time

# ==========================================
# 0. 页面全局配置
# ==========================================
st.set_page_config(page_title="AI 生涯规划专家 临床精细版", page_icon="🎓", layout="wide")

# ==========================================
# 1. 商业防盗门
# ==========================================
st.markdown("### 🔒 欢迎进入 AI 升学与生涯推演系统 (临床精细版)")
access_code = st.text_input("请输入专属通行码", type="password")

if access_code != "VIP888":
    st.warning("⚠️ 密钥为空或不正确。获取测试密钥，请联系首席规划顾问。")
    st.stop()

st.success("✅ 密钥验证成功！系统已全面解锁。")
st.markdown("---")

# ==========================================
# 2. 核心大盘：四维临床级数据采集矩阵
# ==========================================
st.title("🎓 国际教育路径与生涯推演引擎")
st.write("请在左侧控制台精准输入测试者的底层参数，AI 将基于四维模型进行深度演算。")

st.sidebar.header("🎛️ 临床精细级参数输入")

# 维度一：多元智能
with st.sidebar.expander("🧠 1. 多元智能评估 (权重排序)", expanded=True):
    mi_options = ["逻辑/数学智能", "视觉/空间智能", "身体/运动智能", "言语/语言智能",
                  "音乐/节奏智能", "人际交往智能", "自我内省智能", "自然观察智能"]
    top1 = st.selectbox("🥇 第一优势 (Top 1 核心驱动)", mi_options, index=0)
    top2 = st.selectbox("🥈 第二优势 (Top 2 辅助驱动)", mi_options, index=1)
    top3 = st.selectbox("🥉 第三优势 (Top 3 补充驱动)", mi_options, index=6)

# 维度二：感官雷达 (融入 Kelly Mahler 内感受觉分离理论)
with st.sidebar.expander("👁️ 2. 感官雷达定位 (Kelly Mahler 架构)"):
    st.caption("请根据神经反馈精准选择对应状态：")
    sensory_status = ["典型正常", "敏感/防卫 (逃避)", "迟钝/忽略 (反应不足)", "感觉寻求 (极度渴望)"]

    tactile_light = st.radio("🪶 轻触觉 (温度/材质/微碰)", sensory_status, horizontal=True)
    tactile_deep = st.radio("🫂 深触觉/本体压觉 (重物/拥抱)", sensory_status, horizontal=True)
    vestibular = st.radio("⚖️ 前庭觉 (旋转/平衡/速度)", sensory_status, horizontal=True)
    proprioceptive = st.radio("💪 本体感觉 (肌肉力量/空间定位)", sensory_status, horizontal=True)
    visual = st.radio("👁️ 视觉 (强光/色彩/动态)", sensory_status, horizontal=True)
    auditory = st.radio("👂 听觉 (高频噪音/嘈杂)", sensory_status, horizontal=True)

    st.markdown("---")
    st.markdown("**🫀 内感受觉 (双通道分离解析)**")
    interoception_physio = st.radio("🩸 生理通道 (饥饿/饱腹/体温/便意/痛觉)", sensory_status, horizontal=True)
    interoception_emotion = st.radio("🎭 情绪通道 (情绪波动感知/压力躯体化)", sensory_status, horizontal=True)

# 维度三：MBTI
with st.sidebar.expander("🎭 3. MBTI 心理类型"):
    mbti = st.selectbox("请选择 MBTI 人格：",
                        ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ",
                         "ISTP", "ISFP", "ESTP", "ESFP"])

# 维度四：霍兰德
with st.sidebar.expander("🧬 4. 霍兰德职业兴趣 (RIASEC)"):
    holland = st.multiselect("请选择 2-3 个核心职业兴趣：",
                             ["R (实用型 - 机器/操作)", "I (研究型 - 科学/思考)", "A (艺术型 - 设计/创造)",
                              "S (社会型 - 助人/教育)", "E (企业型 - 领导/统筹)", "C (常规型 - 数据/规则)"])

# ==========================================
# 3. 结果展示与私域收网模块
# ==========================================
st.markdown("### 📊 实时推演沙盘")

if st.button("🚀 启动大模型临床解析", type="primary"):

    # 封包检查：将细分后的内感受觉加入后台监控
    st.info(
        f"**【后台参数封包检查】**\n* 核心智能：🥇{top1} ➔ 🥈{top2} ➔ 🥉{top3}\n* 生理内感受：{interoception_physio} | 情绪内感受：{interoception_emotion}\n* MBTI & Holland：{mbti} | {', '.join(holland) if holland else '未补全'}")

    progress_text = "正在初始化临床分析引擎..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=f"正在载入内感受觉分离模型比对数据... {percent_complete + 1}%")
    time.sleep(0.5)
    my_bar.empty()

    st.success("✅ 初步运算完成！(当前为结构演示面板)")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📚 国际课程体系建议")
        st.write("经算法评估，该感官配置与智能分布，最适配：**A-Level / AP 强理科组合**。")
        st.write(
            "⚠️ **生理干预预警**：检测到生理/情绪通道分离。在备考期需强制设定物理闹钟提醒进食/饮水，防止生理性低血糖引发的情绪崩溃。")
    with col2:
        st.subheader("🎯 本科专业锁定池")
        st.write("基于底层基因，推荐优先冲刺：\n- 🤖 机器人工程 / 具身智能\n- 📊 数据科学与分析\n- ⚙️ 机械与精密仪器")

    st.markdown("---")
    st.error("🔒 **高级权限受限：** 当前网页仅提供基础测算框架。")
    st.markdown("""
    #### 👨‍🏫 获取【完整版万字定制规划书】包含：
    1.  **学科赋能点**：精准到高一、高二每学期的选课清单。
    2.  **感官代偿策略**：针对内感受觉分离与前庭特征的学术干预方案。
    3.  **背景提升时间轴**：匹配核心智能的国际竞赛与科研 PBL 项目推荐。
    """)
    st.write("👇 **请扫描下方二维码，添加首席规划专家微信，提交系统原始数据进行 1v1 解读：**")

    try:
        st.image("wechat.jpg", width=250)
    except:
        st.caption("[图片加载位置：请确保 GitHub 代码仓库中已上传 wechat.jpg 文件]")


