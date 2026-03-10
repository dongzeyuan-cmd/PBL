import streamlit as st
import time

# ==========================================
# 0. 页面全局配置 (升级为宽屏模式容纳更多数据)
# ==========================================
st.set_page_config(page_title="AI 生涯规划专家 Pro版", page_icon="🎓", layout="wide")

# ==========================================
# 1. 商业防盗门 (保持不变)
# ==========================================
st.markdown("### 🔒 欢迎进入 AI 升学与生涯推演系统 (Pro版)")
access_code = st.text_input("请输入专属通行码解锁系统：", type="password")

if access_code != "VIP888":
    st.warning("⚠️ 密钥为空或不正确。获取测试密钥，请联系首席规划顾问。")
    st.stop()

st.success("✅ 密钥验证成功！系统已全面解锁。")
st.markdown("---")

# ==========================================
# 2. 核心大盘：四维数据采集矩阵 (UI 架构大升级)
# ==========================================
st.title("🎓 国际教育路径与生涯推演引擎")
st.write("请在左侧控制台精准输入测试者的底层参数，AI 将基于四维模型进行深度演算。")

st.sidebar.header("🎛️ 核心参数输入台")

# 维度一：八大智能 (多选框，因为人通常有 2-3 个优势智能)
with st.sidebar.expander("🧠 1. 多元智能评估 (选 2-3 项优势)"):
    intelligences = st.multiselect(
        "请选择最突出的智能维度：",
        ["言语/语言智能", "逻辑/数学智能", "视觉/空间智能", "身体/运动智能", 
         "音乐/节奏智能", "人际交往智能", "自我内省智能", "自然观察智能"],
        default=["逻辑/数学智能", "视觉/空间智能"] # 默认给你这个工科博士的配置
    )

# 维度二：八大感官雷达 (滑动条，1-10 细分颗粒度)
with st.sidebar.expander("👁️ 2. 感官雷达定位 (1=迟钝, 10=敏感/寻求)"):
    st.caption("请根据孩子的日常感官反应调整阈值：")
    visual = st.slider("👁️ 视觉敏感度", 1, 10, 5)
    auditory = st.slider("👂 听觉敏感度", 1, 10, 5)
    tactile = st.slider("🖐️ 触觉敏感度", 1, 10, 5)
    vestibular = st.slider("⚖️ 前庭觉 (运动与平衡)", 1, 10, 5)
    proprioceptive = st.slider("💪 本体觉 (身体力量与位置)", 1, 10, 5)
    olfactory = st.slider("👃 嗅觉敏感度", 1, 10, 5)
    gustatory = st.slider("👅 味觉敏感度", 1, 10, 5)
    interoception = st.slider("🫀 内感受觉 (情绪与生理感知)", 1, 10, 5)

# 维度三：MBTI 人格矩阵
with st.sidebar.expander("🎭 3. MBTI 心理类型"):
    mbti = st.selectbox(
        "请选择 MBTI 人格：",
        ["INTJ (建筑师)", "INTP (逻辑学家)", "ENTJ (指挥官)", "ENTP (辩论家)",
         "INFJ (提倡者)", "INFP (调停者)", "ENFJ (主人公)", "ENFP (竞选者)",
         "ISTJ (物流师)", "ISFJ (守卫者)", "ESTJ (总经理)", "ESFJ (执政官)",
         "ISTP (鉴赏家)", "ISFP (探险家)", "ESTP (企业家)", "ESFP (表演者)"]
    )

# 维度四：霍兰德职业基因
with st.sidebar.expander("🧬 4. 霍兰德职业兴趣 (RIASEC)"):
    holland = st.multiselect(
        "请选择 2-3 个职业兴趣代码：",
        ["R (实用型 - 喜欢动手/操作机器)", "I (研究型 - 喜欢思考/科学实验)", 
         "A (艺术型 - 喜欢创造/设计)", "S (社会型 - 喜欢助人/教育)", 
         "E (企业型 - 喜欢领导/影响他人)", "C (常规型 - 喜欢组织/数据处理)"]
    )

# ==========================================
# 3. 结果展示与私域收网模块
# ==========================================
st.markdown("### 📊 实时推演沙盘")

# 将所有的用户输入整合成一段提示词，让你看到未来 AI 会接收到什么
user_profile = f"""
**【当前载入的参数画像】**
* 优势智能：{', '.join(intelligences) if intelligences else '未选择'}
* MBTI 人格：{mbti}
* 霍兰德代码：{', '.join(holland) if holland else '未选择'}
* 特殊感官极值：前庭觉({vestibular})，本体觉({proprioceptive})，触觉({tactile})
"""
st.info(user_profile)

if st.button("🚀 启动大模型进行万字解析", type="primary"):
    
    # 模拟运算过程
    progress_text = "正在初始化分析引擎..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=f"正在调用全球顶尖名校录取数据库... {percent_complete+1}%")
    time.sleep(1)
    my_bar.empty()
    
    st.success("✅ 初步运算完成！根据四维数据模型，发现该学生具备强烈的非标特质。")
    
    # 模拟分栏展示结果 (让网页看起来极其专业)
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📚 国际课程体系建议")
        st.write("经算法评估，该感官配置与智能分布，最适配：**A-Level / AP 强理科组合**。")
        st.write("⚠️ **避坑预警**：由于内感受觉与语言智能非绝对主导，强烈建议**规避 IB 体系**，以防长篇论文 (EE/TOK) 引发情绪内耗与厌学。")
        
    with col2:
        st.subheader("🎯 本科专业锁定池")
        st.write("基于霍兰德与 MBTI 基因，推荐优先冲刺：")
        st.write("- 🤖 机器人工程 / 具身智能")
        st.write("- 📊 数据科学与商业分析")
        st.write("- ⚙️ 机械与精密仪器")
    
    # 私域引流
    st.markdown("---")
    st.error("🔒 **高级权限受限：** 当前网页仅提供 15% 的宏观结论。")
    st.markdown("""
    #### 👨‍🏫 获取【完整版万字定制规划书】包含：
    1.  **学科赋能点**：精准到高一、高二每学期的选课清单。
    2.  **感官代偿策略**：针对前庭觉/本体觉异常的学术干预方案。
    3.  **背景提升时间轴**：匹配其能力的国际竞赛与科研 PBL 项目推荐。
    """)
    st.write("👇 **请扫描下方二维码，添加首席规划专家微信，提交系统后台原始数据进行 1v1 解读：**")
    
    try:
        st.image("wechat.jpg", width=200)
    except:
        st.caption("[图片加载位置：请确保 GitHub 中存在 wechat.jpg]")
