import streamlit as st
from openai import OpenAI

# ==========================================
# 1. 页面配置与 UI (和之前一样)
# ==========================================
st.set_page_config(page_title="AI 生涯规划专家", page_icon="🎓")
st.title("🎓 AI 赋能：学业与生涯规划系统")

# 收集参数
st.sidebar.header("🧠 请输入系统参数")
vestibular = st.sidebar.slider("前庭觉状态 (1=极度安静, 10=必须动手操作)", 1, 10, 5)
intelligence = st.sidebar.selectbox("突出的智能维度", ["逻辑数学", "语言表达", "空间想象"])
holland = st.sidebar.selectbox("职业倾向基因", ["R 实用型", "I 研究型", "E 企业型"])

# ==========================================
# 2. 核心大模型 API 调用模块 (以 DeepSeek 为例)
# ==========================================
# 这里的 API Key 需要你去各大平台免费申请一个，替换掉这串文字
API_KEY = "sk-e84c5f61c25f4241b80f0d818f552c08"
BASE_URL = "https://api.deepseek.com"  # 以国内 DeepSeek 为例

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

if st.button("🚀 召唤 AI 专家进行深度推演"):
    with st.spinner("AI 正在高速比对全球教育路径..."):

        # 组装 Prompt (提示词工程：把高中生的特征喂给大模型)
        system_prompt = "你是一位顶级的国际高中升学指导专家。请根据学生的生理特征和智能特征，推荐适合的体系(AP/IB/A-Level)和未来专业方向。语气要专业、有启发性。"
        user_prompt = f"该学生前庭觉活跃度为{vestibular}/10，最突出的多元智能是【{intelligence}】，霍兰德职业兴趣为【{holland}】。请直接给出规划建议。"

        try:
            # 向大模型服务器发送请求
            response = client.chat.completions.create(
                model="deepseek-chat",  # 或者你使用的其他模型名称
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )

            # 提取大模型的真实回答并展示在网页上
            ai_answer = response.choices[0].message.content
            st.success("推演完成！")
            st.markdown(ai_answer)  # 渲染输出结果
            st.balloons()

        except Exception as e:
            st.error(f"API 调用失败，请检查网络或密钥：{e}")