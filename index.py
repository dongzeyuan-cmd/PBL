import streamlit as st
import pandas as pd

# ==========================================
# 0. 页面全局配置
# ==========================================
st.set_page_config(page_title="Dr. 董 | 国际STEM教育架构师", page_icon="👩‍🔬", layout="wide")

# ==========================================
# 1. 英雄看板 (Hero Section)
# ==========================================
col_img, col_text = st.columns([1, 4])

with col_img:
    # 这里未来可以替换成你极其干练的高级职业照
    st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=Felix&style=circle&backgroundColor=e2e8f0", width=180)

with col_text:
    st.title("Dr. Dong 董博士")
    st.markdown("### 👩‍🔬 国际 STEM 教育架构师 | AI 智能硬件全栈开发者 | 精密仪器博士")
    st.write("📍 **位置**：北京 (Beijing, China)   |   📧 **邮箱**：director.dong@stem-edu.com")
    st.markdown("""
    > **“我不教学生死记硬背枯燥的语法。在 AGI (通用人工智能) 时代，我教他们如何作为‘系统架构师’，**
    > **利用大模型算力、硬件工程与数据科学，构建解决物理世界真实问题的顶尖科技产品。”**
    """)

st.divider()

# ==========================================
# 2. 核心战斗力指标 (Metrics Board)
# ==========================================
st.markdown("### ⚡ 核心算力矩阵 (Core Metrics)")
m1, m2, m3, m4 = st.columns(4)
m1.metric(label="最高学历", value="Ph.D.", delta="双一流高校 精密仪器")
m2.metric(label="独立研发 PBL 旗舰项目", value="2 套", delta="硬件/软件双轨并发")
m3.metric(label="底层架构能力", value="硬核跨界", delta="AI视觉 + 机械控制 + 数据交互")
m4.metric(label="MBTI 底层操作系统", value="INFJ", delta="极强共情力与教育洞察")

st.divider()

# ==========================================
# 3. 技能树与教育理念 (双栏展示)
# ==========================================
col_skills, col_edu = st.columns([1, 1])

with col_skills:
    st.markdown("### 🛠️ 跨维技术栈 (Tech Arsenal)")
    
    # 用多维表格展示技能，显得极其极客
    skills_data = {
        "技术领域 (Domain)": ["AI 敏捷开发 (Vibe Coding)", "硬件工程与结构设计", "数据可视化与 SaaS 开发", "系统集成测试"],
        "核心工具链 (Tools)": ["OpenAI API, Prompt Engineering", "SolidWorks, 树莓派, 3D打印", "Python, Streamlit, Pandas", "机器视觉 (OpenCV), 传感器网络"],
        "熟练度": ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐"]
    }
    df_skills = pd.DataFrame(skills_data)
    st.dataframe(df_skills, use_container_width=True, hide_index=True)

with col_edu:
    st.markdown("### 💡 顶层教育理念 (Philosophy)")
    st.info("""
    **1. 降维打击的 PBL 闭环：** 从学术界的“高光谱图像解析”中抽离底层逻辑，将复杂的工程问题降维拆解为高中生可落地执行的 PBL（项目式学习）微模块。
    """)
    st.success("""
    **2. 神经多样性与感统干预：**
    基于前沿感统心理学（ASI）与内感受觉分离理论，精准识别不同感官特质（如前庭觉寻求、高敏体质）的学生，提供定制化科技活动干预方案。
    """)
    st.warning("""
    **3. 跨越代码的系统思维：**
    拒绝“背诵式”编程教育。引导学生掌握顶层的 Prompt Architecture（提示词架构），像科技公司 CEO 一样调用工具，直达成果。
    """)

st.divider()

# ==========================================
# 4. 旗舰级 PBL 课程展示 (选项卡)
# ==========================================
st.markdown("### 🚀 独立研发旗舰 PBL 课程 (Portfolio)")
st.write("👈 *请点击左侧导航栏 (Pages) 体验真实的 SaaS 级互动 Demo。以下为课程大纲速览：*")

tab1, tab2 = st.tabs(["🤖 项目 A：AI 视觉 6 轴机械臂系统 (硬件级)", "🎓 项目 B：AI 生涯推演全景系统 (软件级)"])

with tab1:
    st.markdown("#### 《具身智能：基于机器视觉的智能制造产线开发》")
    st.markdown("""
    * **核心学科赋能**：物理（运动学/力学）、计算机科学（Python/机器视觉）、工程学（3D建模）。
    * **适用国际体系**：A-Level (Physics/CS), AP (Physics C / CS A), IB (Physics/CS HL)
    * **项目产出**：学生将从 0 到 1 用 SolidWorks 建模，3D 打印机械件，并利用大模型辅助编写 OpenCV 视觉代码，完成“特定颜色物体自动抓取”的工业级微缩模型。
    * **藤校竞争力**：展现极强的动手能力、三维空间重构能力及软硬件协同调试能力。
    """)

with tab2:
    st.markdown("#### 《数据科学：Kelly Mahler内感受分离模型下的AI智能体应用》")
    st.markdown("""
    * **核心学科赋能**：心理学、统计学、计算机科学。
    * **适用国际体系**：A-Level (Psychology), AP (Psychology / Capstone), IB (Psychology HL / EE)
    * **项目产出**：学生将学习如何将人类生理/情绪的非标特质（如八大智能、感官雷达）进行量化建模，并调用大语言模型 API，用 Streamlit 极速部署一款具备商业级 UI 的 Web 应用。
    * **藤校竞争力**：展现深厚的人文关怀、社会洞察力及跨界数据科学能力。
    """)

st.divider()

# ==========================================
# 5. 学术与科研背景 (折叠面板)
# ==========================================
st.markdown("### 📚 学术基因 (Academic Background)")

with st.expander("查看详细科研履历 (Ph.D. Research Details)", expanded=False):
    st.markdown("""
    #### 🎓 双一流大学 | 精密仪器与微机电系统 博士学位 (Ph.D.)
    * **研究核心**：高光谱图像采集与精密数据解析。
    * **科研素养**：习惯处理极其庞大、多维度的噪音数据，具备顶级的数据降噪、模型重构与系统验证能力。这段极度枯燥且硬核的科研经历，铸就了如今在面对任何复杂教育路径或技术难题时，都能一眼看穿系统 Bug 的敏锐直觉。
    """)

# ==========================================
# 6. 联系方式底部
# ==========================================
st.markdown("<div style='text-align: center; color: gray; padding-top: 50px;'>© 2024 Crafted with ❤️ & AI by Dr. Dong. <br>System Running on Streamlit Cloud.</div>", unsafe_allow_html=True)
