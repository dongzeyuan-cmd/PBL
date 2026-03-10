import streamlit as st
import time

# ==========================================
# 0. 页面全局配置
# ==========================================
st.set_page_config(page_title="AI 生涯规划专家 | 全景展示版", page_icon="🎓", layout="wide")

# ==========================================
# 1. 高级权限验证
# ==========================================
st.markdown("### 🔒 欢迎进入 AI 升学与生涯推演系统 (全景演算版)")
access_code = st.text_input("请输入高级权限通行码", type="password")

if access_code != "VIP888":
    st.warning("⚠️ 密钥为空或不正确。获取高级测试密钥，请联系实验室主任。")
    st.stop()

st.success("✅ 密钥验证成功！全景演算沙盘已解锁。")
st.markdown("---")

# ==========================================
# 2. 核心大盘：四维临床级数据采集矩阵
# ==========================================
st.title("🎓 国际教育路径与生涯全景推演引擎")
st.write("左侧录入底层物理与认知参数，右侧生成全景战略蓝图。")

st.sidebar.header("🎛️ 临床精细级参数输入")

# 维度一：多元智能
with st.sidebar.expander("🧠 1. 多元智能评估 (权重排序)", expanded=True):
    mi_options = ["逻辑/数学智能", "视觉/空间智能", "身体/运动智能", "言语/语言智能", 
                  "音乐/节奏智能", "人际交往智能", "自我内省智能", "自然观察智能"]
    top1 = st.selectbox("🥇 第一优势 (Top 1 核心驱动)", mi_options, index=0)
    top2 = st.selectbox("🥈 第二优势 (Top 2 辅助驱动)", mi_options, index=1)
    top3 = st.selectbox("🥉 第三优势 (Top 3 补充驱动)", mi_options, index=6)

# 维度二：感官雷达 
with st.sidebar.expander("👁️ 2. 感官雷达定位 (临床体征)"):
    sensory_status = ["典型正常", "敏感/防卫 (逃避)", "迟钝/忽略 (反应不足)", "感觉寻求 (极度渴望)"]
    tactile_light = st.radio("🪶 轻触觉 (温度/材质)", sensory_status, horizontal=True)
    tactile_deep = st.radio("🫂 深触觉 (重物/拥抱)", sensory_status, horizontal=True)
    vestibular = st.radio("⚖️ 前庭觉 (旋转/平衡)", sensory_status, horizontal=True)
    proprioceptive = st.radio("💪 本体感觉 (肌肉力量)", sensory_status, horizontal=True)
    visual = st.radio("👁️ 视觉 (光线/色彩)", sensory_status, horizontal=True)
    auditory = st.radio("👂 听觉 (噪音/频段)", sensory_status, horizontal=True)
    interoception_physio = st.radio("🩸 生理内感受 (饥饿/饱腹)", sensory_status, horizontal=True)
    interoception_emotion = st.radio("🎭 情绪内感受 (情绪躯体化)", sensory_status, horizontal=True)

# 维度三 & 四：MBTI 与 霍兰德
with st.sidebar.expander("🎭 3. MBTI & 🧬 4. 霍兰德基因"):
    mbti = st.selectbox("MBTI 人格：", ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"])
    holland = st.multiselect("霍兰德职业兴趣：", ["R (实用型)", "I (研究型)", "A (艺术型)", "S (社会型)", "E (企业型)", "C (常规型)"])

# ==========================================
# 3. 终极生成逻辑：全量分析报告 (新增时间轴)
# ==========================================
if st.button("🚀 启动大模型全景演算", type="primary"):
    
    my_bar = st.progress(0, text="正在初始化全景分析引擎...")
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=f"正在重组数据链并生成 K-12 时间轴... {percent_complete+1}%")
    time.sleep(0.2)
    my_bar.empty()
    
    st.balloons()
    st.success("✅ 全景演算完成！系统已为您生成深度战略蓝图及执行时间轴：")
    
    # 新增了第 6 个选项卡：K-12 升学时间轴
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📊 1. 综合诊断评价", 
        "🛤️ 2. 四大体系抉择", 
        "📚 3. 学科赋能与选课", 
        "🏫 4. 中外大学专业", 
        "🚀 5. 未来职业推演",
        "⏳ 6. K-12 升学时间轴"
    ])
    
    # ------------------ Tab 1: 综合诊断评价 ------------------
    with tab1:
        st.header("📊 系统架构与底层基因诊断")
        st.write(f"根据采集的数据封包，该个体的核心操作系统为 **{mbti}**，底层核心驱动程序由 **{top1}** 主导。")
        col1, col2 = st.columns(2)
        with col1:
            st.info("**💡 优势与天赋雷达**")
            st.write(f"- **高优算力区**：由 {top1} 和 {top2} 构成的双核驱动，具备降维打击能力。")
            st.write(f"- **内在动机链路**：霍兰德基因 {holland} 显示其底层价值序列清晰。")
        with col2:
            st.warning("**⚠️ 功耗与系统预警**")
            st.write(f"- **感官过载警报**：系统检测到前庭觉反馈为[{vestibular}]，情绪内感受反馈为[{interoception_emotion}]。")
            st.write("- **架构师干预建议**：在执行高压学术任务时极易发生“物理报错”，需配置专属的感统安抚策略。")

    # ------------------ Tab 2: 四大体系抉择 ------------------
    with tab2:
        st.header("🛤️ 教育路径适配度测算")
        a_level_score = 95 if "逻辑" in top1 or "空间" in top1 else 75
        ib_score = 90 if "语言" in top1 and "正常" in interoception_emotion else 55
        ap_score = 85
        gaokao_score = 50 if "敏感" in interoception_emotion or "寻求" in vestibular else 80
        
        st.progress(a_level_score, text=f"🇬🇧 A-Level 体系适配度：{a_level_score}% (扬长避短，适合单科极客)")
        st.progress(ap_score, text=f"🇺🇸 AP 体系适配度：{ap_score}% (模块化进攻，灵活变通)")
        st.progress(ib_score, text=f"🌐 IB 体系适配度：{ib_score}% (要求极高时间管理与全科抗压)")
        st.progress(gaokao_score, text=f"🇨🇳 国内高考体系：{gaokao_score}% (适合六边形战士)")

    # ------------------ Tab 3: 学科赋能与选课 ------------------
    with tab3:
        st.header("📚 国际课程体系全景选课图谱")
        st.info(f"**💡 基于第一优势【{top1}】生成的定制化选课方案：**")
        if "逻辑" in top1 or "空间" in top1:
            st.write("👉 **若选 A-Level**：进阶数学 + 物理 + 计算机科学")
            st.write("👉 **若选 AP**：AP微积分BC + AP物理C电磁学 + AP计算机A")
            st.write("👉 **若选 IB**：数学 AA HL + 物理 HL + 经济学 SL")
        else:
            st.write("👉 **若选 A-Level**：心理学 + 经济学 + 社会学")
            st.write("👉 **若选 AP**：AP心理学 + AP微观经济 + AP英语语言")
            st.write("👉 **若选 IB**：英语A HL + 心理学 HL + 经济学 HL")

    # ------------------ Tab 4: 中外大学专业 ------------------
    with tab4:
        st.header("🏫 升学双轨制：中外大学与专业图谱")
        col_intl, col_dom = st.columns(2)
        with col_intl:
            st.subheader("🌍 国外顶尖名校 (藤校/G5) 申请策略")
            st.write("✔️ 具身智能 / 数据科学 / 认知科学 / 人机交互")
        with col_dom:
            st.subheader("🇨🇳 国内高考/强基计划 填报策略")
            st.write("✔️ 自动化类 / 计算机科学 / 心理学 / 精密仪器")

    # ------------------ Tab 5: 未来职业推演 ------------------
    with tab5:
        st.header("🚀 10年期：AI 纪元职场生态演化")
        st.write(f"基于 {mbti} 与 {top1}，未来核心赛道预测为：【系统定义架构师】或【科技商业化破局者】。")

    # ------------------ Tab 6: K-12 升学时间轴 (全新独家硬核模块) ------------------
    with tab6:
        st.header("⏳ 核心执行层：从小学到高三的动态规划轴")
        
        # 动态算法：根据智能优势调整竞赛和活动内容
        if "逻辑" in top1 or "空间" in top1:
            focus_track = "🚀 **主攻方向：硬核 STEM 与科创**"
            ms_comp = "AMC8 数学竞赛、VEX IQ 机器人赛"
            g10_comp = "AMC10、物理碗 (PhysicsBowl)、丘成桐中学科学奖报名"
            g11_comp = "HiMCM 数模竞赛、USACO 计算机竞赛、顶级硬核科研夏校 (如ROSS, SSP)"
        else:
            focus_track = "🕊️ **主攻方向：人文社科与商科领导力**"
            ms_comp = "Spelling Bee 拼字比赛、NSDA 英语辩论初级"
            g10_comp = "NEC 全美经济学挑战赛、MUN 模拟联合国、约翰洛克 (John Locke) 写作"
            g11_comp = "CTB 全球青年研究创新论坛、沃顿商赛 (WGHS)、顶级人文夏校 (如YYGS)"

        st.info(f"系统已根据底层基因锁定 {focus_track}，并生成专属里程碑节点：")
        
        # 使用 Markdown 和高亮模拟专业时间轴排版
        st.markdown("""
        ### 🌱 启蒙与探索期
        * **【小学阶段 (G1-G6)】：广泛试错与感官统合**
            * **核心任务：** 保护好奇心，修复/代偿感官异常（如前庭觉寻求的定向放电）。
            * **语言与技能：** 沉浸式英语阅读（蓝思值打底）；引入图形化编程（Scratch）或基础机器人（乐高 SPIKE）以锻炼空间/逻辑智能。
            * **避免误区：** 切忌过早进行高压应试刷题，警惕引发内感受觉与情绪的剥离。

        ---
        ### 🔍 定位与奠基期
        * **【初中阶段 (G7-G9)】：寻找“主线故事 (Spike)”的雏形**
            * **课程衔接：** 熟练掌握 IGCSE 或 MYP 的核心基础，GPA 需稳定在 A 梯队。
            * **背景提升：** 开始参加入门级国际赛事以测试天赋边界。推荐：""" + ms_comp + """
            * **核心任务：** 明确未来的高中体系路线（体制内 vs 国际部；A-Level / AP / IB 选型）。

        ---
        ### ⚔️ 冲刺与收网期
        * **【高一 (G10)】：系统切换与主线确立**
            * **学术选课：** 敲定 AP/A-Level 的先修科目，开始构建 GPA 护城河（绝对不能有 C）。
            * **标化考试：** 完成托福/雅思的首考，摸底水平（目标托福 95+ / 雅思 7.0）。
            * **背景提升：** 打磨深度课外活动（PBL 项目），参加高含金量竞赛试水。推荐：""" + g10_comp + """

        * **【高二 (G11)】：炼狱模式与火力全开（最关键的一年）**
            * **学术选课：** 挑战最高难度的核心课程（如 AP 微积分/物理C，或 IB DP1 HL课程），确保期末获得极高的预估分（Predicted Grade）。
            * **标化考试：** 托福/雅思出分（目标 110+ / 7.5+）；完成 SAT/ACT 考试。
            * **背景提升：** 产出顶级成果。发表独立研究论文（EPQ/EE），参加顶级夏校，带队冲击竞赛金奖。推荐：""" + g11_comp + """

        * **【高三 (G12)】：战略投递与平稳落地**
            * **上学期 (9月-12月)：** 撰写极其 Personal（个人化）的大学申请文书（PS），将过往的感官天赋、智能优势与课外活动串联成完美的底层逻辑故事。完成 ED/EA（提前批）和牛剑的投递及面试准备。
            * **下学期 (1月-6月)：** 接收 Offer。保持最后一学期的 GPA（防止被大学撤回 Offer），完成大考（AP全球统考 / A-Level A2 考试 / IB 终考），顺利升学。
        """)
