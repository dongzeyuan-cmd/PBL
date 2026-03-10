import streamlit as st
import time

# 尝试导入大模型官方库 (如果没装，会提示错误，但由于是在云端，只要有 requirements.txt 就会自动装)
try:
    from openai import OpenAI
except ImportError:
    st.error("⚠️ 系统缺少 `openai` 依赖库。请在 GitHub 根目录的 `requirements.txt` 文件中添加一行 `openai`。")
    st.stop()

# ==========================================
# 0. 页面全局配置
# ==========================================
st.set_page_config(page_title="AI 生涯规划专家 | 真实大模型版", page_icon="🎓", layout="wide")

# ==========================================
# 1. 银行级安全验证与 API 配置
# ==========================================
st.markdown("### 🔒 欢迎进入 AI 升学与生涯推演系统 (大模型演算版)")

# 从云端保险箱读取密码和 API Key
try:
    CORRECT_PWD = st.secrets["GENERAL_PASSWORD"]
    API_KEY = st.secrets["API_KEY"]
    # 如果你用的是 DeepSeek，可以在 Secrets 里配 BASE_URL="https://api.deepseek.com/v1"
    # 如果没配，默认用 OpenAI 的地址
    BASE_URL = st.secrets.get("BASE_URL", "https://api.openai.com/v1") 
    MODEL_NAME = st.secrets.get("MODEL_NAME", "gpt-3.5-turbo") # 默认模型名，可改为 deepseek-chat
except Exception as e:
    st.warning("⚠️ 云端 Secrets 未配置完成。为保证演示，临时启用备用逻辑。")
    CORRECT_PWD = "VIP888"
    API_KEY = ""
    BASE_URL = ""
    MODEL_NAME = ""

access_code = st.text_input("请输入高级权限通行码", type="password")

if access_code != CORRECT_PWD:
    st.warning("⚠️ 权限校验未通过。请获取高级测试密钥。")
    st.stop()

st.success("✅ 密钥验证成功！全景演算沙盘已解锁。")
st.markdown("---")

# ==========================================
# 2. 核心大盘：四维参数输入
# ==========================================
st.title("🎓 国际教育路径与生涯全景推演引擎")
st.sidebar.header("🎛️ 临床精细级参数输入")

with st.sidebar.expander("🧠 1. 多元智能评估", expanded=True):
    mi_options = ["逻辑/数学智能", "视觉/空间智能", "身体/运动智能", "言语/语言智能", "音乐/节奏智能", "人际交往智能", "自我内省智能", "自然观察智能"]
    top1 = st.selectbox("🥇 第一优势", mi_options, index=0)
    top2 = st.selectbox("🥈 第二优势", mi_options, index=1)
    top3 = st.selectbox("🥉 第三优势", mi_options, index=6)

with st.sidebar.expander("👁️ 2. 核心职业感官雷达"):
    sensory_status = ["典型正常", "敏感/防卫 (容易过载)", "迟钝/忽略 (反应不足)", "感觉寻求 (极度渴望)"]
    vestibular = st.radio("⚖️ 前庭觉 (动静需求)", sensory_status, horizontal=True)
    proprioceptive = st.radio("💪 本体觉 (物理操作)", sensory_status, horizontal=True)
    auditory = st.radio("👂 听觉 (环境耐受)", sensory_status, horizontal=True)
    interoception = st.radio("🎭 情绪内感受 (抗压耐受)", sensory_status, horizontal=True)

with st.sidebar.expander("🎭 3. 心理与职业基因"):
    mbti = st.selectbox("MBTI 操作系统：", ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"])
    holland = st.multiselect("霍兰德职业兴趣：", ["R (实用型)", "I (研究型)", "A (艺术型)", "S (社会型)", "E (企业型)", "C (常规型)"])

# ==========================================
# 3. 核心生成逻辑 (混合架构：规则 UI + 真实 LLM)
# ==========================================
if st.button("🚀 启动大模型全景演算", type="primary"):
    
    # --- 阶段一：前端 UI 规则极速渲染 ---
    top_3_str = f"{top1}{top2}{top3}"
    
    if "逻辑" in top_3_str and ("视觉" in top_3_str or "身体" in top_3_str):
        track, a_level_score, ap_score, ib_score = "Hardcore STEM (硬核理工与具身智能)", 95, 85, 70
        subj_al, subj_ap = "进阶数学 + 物理 + 计算机科学", "AP微积分BC + AP物理C电磁学 + AP计算机A"
    elif "语言" in top_3_str and ("人际" in top_3_str or "内省" in top_3_str):
        track, a_level_score, ap_score, ib_score = "Humanities & Social Sci (人文社科与商业)", 75, 85, 95
        subj_al, subj_ap = "经济学 + 心理学 + 历史", "AP英语语言 + AP心理学 + AP微观经济"
    elif "空间" in top_3_str and ("身体" in top_3_str or "视觉" in top_3_str):
        track, a_level_score, ap_score, ib_score = "Design & Architecture (工业设计与建筑)", 80, 80, 85
        subj_al, subj_ap = "纯艺术 + 物理 + 进阶数学", "AP艺术设计 + AP物理1 + AP预微积分"
    else:
        track, a_level_score, ap_score, ib_score = "Business & Data Analysis (综合商科与量化)", 85, 85, 85
        subj_al, subj_ap = "数学 + 经济 + 商业研究", "AP微积分 + AP经济 + AP统计学"

    st.balloons()
    st.header(f"🎯 基础聚类赛道：{track}")
    
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("🇬🇧 A-Level 适配度", f"{a_level_score}%")
    col_b.metric("🇺🇸 AP 适配度", f"{ap_score}%")
    col_c.metric("🌐 IB 适配度", f"{ib_score}%")
    st.markdown("---")

    # --- 阶段二：调用真实大模型 API ---
    st.header("🧠 真·大模型深度定制报告")
    
    if not API_KEY:
        st.error("⚠️ 系统未检测到有效的 API_KEY，无法调用大模型。请在 Streamlit 控制台的 Secrets 中完成配置。")
        st.stop()

    # 构建发送给 AI 的 Prompt
    system_prompt = """你是一位顶级的国际教育升学指导专家和感统心理学博士。
    请根据用户提供的【智能优势、感官特质、MBTI、霍兰德兴趣】，输出一份专业的升学与生涯规划报告。
    报告必须包含以下模块，并使用 Markdown 格式：
    1. 底层基因诊断 (分析优势与感官风险)
    2. 国际学科与择校建议 (具体到科目和大学名字)
    3. 未来 10 年职业生态位推演 (AI时代下不可替代的岗位)
    4. K-12 逆向推演时间轴 (初中、高一、高二的具体竞赛/活动规划)
    语气要专业、客观、具有极客感，字数控制在 800 字左右。"""

    user_prompt = f"""
    请为该个体出具报告：
    - 前三智能优势：{top1}, {top2}, {top3}
    - 职业感官雷达：前庭觉[{vestibular}], 本体觉[{proprioceptive}], 听觉[{auditory}], 情绪内感受[{interoception}]
    - MBTI与霍兰德：{mbti}, {', '.join(holland) if holland else '未选择'}
    - 初步测算赛道为：{track}
    """

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    with st.spinner("🌍 正在链接大语言模型，进行高维数据交叉推理，请稍候..."):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                stream=True # 开启流式输出，极其炫酷
            )
            
            # 使用 st.write_stream 实现打字机效果
            st.write_stream(response)
            
        except Exception as e:
            st.error(f"🚨 大模型 API 调用失败，错误信息：\n{e}")
            st.info("请检查您的 API Key 是否欠费，或 BASE_URL 是否填写正确。")

    st.markdown("---")
    st.caption("🔍 *以上深度报告由 AI 大模型实时动态生成，每一次推演都独一无二。*")
