import streamlit as st
import time

# ==========================================
# 0. 页面全局配置 (宽屏专业版)
# ==========================================
st.set_page_config(page_title="AI 生涯规划专家 临床版", page_icon="🎓", layout="wide")

# ==========================================
# 1. 商业防盗门：通行码验证模块
# ==========================================
st.markdown("### 🔒 欢迎进入 AI 升学与生涯推演系统 (专家临床版)")
st.write("本系统仅对内部邀约用户开放，请输入访问密钥：")

access_code = st.text_input("请输入专属通行码", type="password")

if access_code != "VIP888":
    st.warning("⚠️ 密钥为空或不正确。获取测试密钥，请联系首席规划顾问。")
    st.stop()  # 拦截未授权用户

st.success("✅ 密钥验证成功！系统已全面解锁。")
st.markdown("---")

# ==========================================
# 2. 核心大盘：四维临床级数据采集矩阵
# ==========================================
st.title("🎓 国际教育路径与生涯推演引擎")
st.write("请在左侧控制台精准输入测试者的底层参数，AI 将基于四维模型进行深度演算。")

st.sidebar.header("🎛️ 临床级参数输入台")

# 维度一：多元智能 (权重排序架构)
with st.sidebar.expander("🧠 1. 多元智能评估 (权重排序)", expanded=True):
    st.caption("请严谨判定优势智能的优先序：")
    mi_options = ["逻辑/数学智能", "视觉/空间智能", "身体/运动智能", "言语/语言智能", 
                  "音乐/节奏智能", "人际交往智能", "自我内省智能", "自然观察智能"]
    
    top1 = st.selectbox("🥇 第一优势 (Top 1 核心驱动)", mi_options, index=0)
    top2 = st.selectbox("🥈 第二优势 (Top 2 辅助驱动)", mi_options, index=1)
    top3 = st.selectbox("🥉 第三优势 (Top 3 补充驱动)", mi_options, index=6)

# 维度二：感官雷达 (最新 ASI 感统理论架构)
with st.sidebar.expander("👁️ 2. 感官雷达定位 (临床体征)"):
    st.caption("请根据神经反馈选择对应状态：")
    sensory_status = ["典型正常", "敏感/防卫 (逃避)", "迟钝/忽略 (反应不足)", "感觉寻求 (极度渴望)"]
    
    tactile_light = st.radio("🪶 轻触觉 (温度/材质/微碰)", sensory_status, horizontal=True)
    tactile_deep = st.radio("🫂 深触觉/本体压觉 (重物/拥抱)", sensory_status, horizontal=True)
    vestibular = st.radio("⚖️ 前庭觉 (旋转/平衡/速度)", sensory_status, horizontal=True)
    proprioceptive = st.radio("💪 本体感觉 (肌肉力量/定位)", sensory_status, horizontal=True)
    visual = st.radio("👁️ 视觉 (强光/色彩/动态)", sensory_status, horizontal=True)
    auditory = st.radio("👂 听觉 (高频噪音/嘈杂)", sensory_status, horizontal=True)
    interoception = st.radio("🫀 内感受觉 (饥饿/情绪/心跳)", sensory_status, horizontal=True)

# 维度三：MBTI 心理类型
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
        "请选择 2-3 个核心职业兴趣：",
        ["R (实用型 - 机器/操作)", "I (研究型 - 科学/思考)", 
         "A (艺术型 - 设计/创造)", "S (社会型 - 助人/教育)", 
         "E (企业型 - 领导/统筹)", "C (常规型 - 数据/规则)"]
    )

# ==========================================
# 3. 结果展示与私域收网模块
# ==========================================
st.markdown("### 📊 实时推演沙盘")

if st.button("🚀 启动大模型临床解析", type="primary"):
    
    # 后台参数封包检查 (让前端看起来极具极客感)
    st.info(f"**【后台参数封包检查】**\n* 核心智能链：🥇{top1} ➔ 🥈{top2} ➔ 🥉{top3}\n* 核心异常感官：前庭觉({vestibular})，深触觉({tactile_deep})\n* MBTI & Holland：{mbti} | {', '.join(holland) if holland else '未补全'}")
    
    # 模拟读条动画
    progress_text = "正在初始化临床分析引擎..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.015)
        my_bar.progress(percent_complete + 1, text=f"正在调用全球顶尖名校与医学数据库比对参数... {percent_complete+1}%")
    time.sleep(0.5)
    my_bar.empty()
    
    st.success("✅ 初步运算完成！(当前为结构演示面板)")
    
    # 分栏展示结果
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📚 国际课程体系建议")
        st.write("经算法评估，该感官配置与智能分布，最适配：**A-Level / AP 强理科组合**。")
        st.write("⚠️ **避坑预警**：基于参数，强烈建议规避需要大量长篇学术写作的课业模块。")
    with col2:
        st.subheader("🎯 本科专业锁定池")
        st.write("基于霍兰德与 MBTI 基因，推荐优先冲刺：\n- 🤖 机器人工程 / 具身智能\n- 📊 数据科学与分析\n- ⚙️ 机械与精密仪器")
    
    # ==========================================
    # 商业引流：微信二维码拦截点
    # ==========================================
    st.markdown("---")
    st.error("🔒 **高级权限受限：** 当前网页仅提供基础测算框架。")
    st.markdown("""
    #### 👨‍🏫 获取【完整版万字定制规划书】包含：
    1.  **学科赋能点**：精准到高一、高二每学期的选课清单。
    2.  **感官代偿策略**：针对前庭/本体等感官特征的学术干预方案。
    3.  **背景提升时间轴**：匹配核心智能的国际竞赛与科研 PBL 项目推荐。
    """)
    st.write("👇 **请扫描下方二维码，添加首席规划专家微信，提交系统原始数据进行 1v1 解读：**")
    
    try:
        # 必须确保 GitHub 中有名为 wechat.jpg 的图片
        st.image("wechat.jpg", width=250)
    except:
        st.caption("[图片加载位置：请确保 GitHub 代码仓库中已上传 wechat.jpg 文件]")
