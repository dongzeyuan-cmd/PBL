import streamlit as st
import time

# ==========================================
# 0. 页面全局配置
# ==========================================
st.set_page_config(page_title="具身智能：人机对齐可视化", page_icon="🤖", layout="wide")

st.title("🤖 具身智能 (Embodied AI)：人机对齐与可视化教学系统")
st.markdown("---")

# ==========================================
# 1. 核心看板：人机对齐画布 (调用你上传的真实图片)
# ==========================================
col_canvas_h, col_canvas_r = st.columns([1, 1])

with col_canvas_h:
    st.subheader("👨‍⚕️ 人体：感官与神经系统架构")
    try:
        # 直接读取根目录下的图片
        st.image("human.jpg", use_container_width=True)
    except:
        st.error("⚠️ 未检测到 human.jpg，请确保文件已上传至 GitHub 根目录。")

with col_canvas_r:
    st.subheader("⚙️ 机器人：传感器与具身大脑架构")
    try:
        # 直接读取根目录下的图片
        st.image("robot.jpg", use_container_width=True)
    except:
        st.error("⚠️ 未检测到 robot.jpg，请确保文件已上传至 GitHub 根目录。")

st.markdown("---")

# ==========================================
# 2. 深度交互：传感器对齐实验室
# ==========================================
st.subheader("🔍 传感器与执行器深度对齐 (点击下方标签学习)")

# 初始化 session_state 避免刷新丢失
if 'sensor_active' not in st.session_state:
    st.session_state['sensor_active'] = None

c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("📷 深度摄像头 (Eyes)", use_container_width=True):
        st.session_state['sensor_active'] = 'camera'
with c2:
    if st.button("⚖️ IMU 惯性单元 (Vestibular)", use_container_width=True):
        st.session_state['sensor_active'] = 'imu'
with c3:
    if st.button("💪 关节编码器 (Proprioception)", use_container_width=True):
        st.session_state['sensor_active'] = 'encoder'
with c4:
    if st.button("🫀 触觉/压力阵列 (Tactile)", use_container_width=True):
        st.session_state['sensor_active'] = 'pressure'

# 动态显示详情信息
active = st.session_state['sensor_active']

if active == 'camera':
    with st.chat_message("assistant"):
        st.markdown("#### 👁️ 深度摄像头 (RGB-D Camera)")
        st.write("**对齐人类**：双眼与视神经。")
        st.write("**中学生原理**：不仅看到颜色，还能通过‘飞行时间(ToF)’算出物体的距离，为机器人建立三维深度地图。")
elif active == 'imu':
    with st.chat_message("assistant"):
        st.markdown("#### ⚖️ IMU 惯性测量单元")
        st.write("**对齐人类**：内耳前庭系统与小脑。")
        st.write("**中学生原理**：实时检测机器人的倾斜角度和加速度，防止像婴儿学步一样摔倒。")
elif active == 'encoder':
    with st.chat_message("assistant"):
        st.markdown("#### 💪 绝对值磁编码器")
        st.write("**对齐人类**：肌肉中的本体感受器。")
        st.write("**中学生原理**：时刻精确反馈每个电机关节转动的度数（甚至精确到0.01度），让机器人‘闭着眼’也知道自己的手在哪。")
elif active == 'pressure':
    with st.chat_message("assistant"):
        st.markdown("#### 🖐️ 触觉/力反馈阵列")
        st.write("**对齐人类**：皮肤触觉与指尖压力。")
        st.write("**中学生原理**：让机器人知道什么时候抓紧了杯子，什么时候该松手，防止把鸡蛋捏碎。")

# ==========================================
# 3. 终极逻辑：强化学习 (RL) 的暴力美学
# ==========================================
st.markdown("---")
st.subheader("🧩 具身智能的核心：强化学习 (Reinforcement Learning)")

col_rl_text, col_rl_demo = st.columns([1, 1])

with col_rl_text:
    st.write("""
    **为什么机器人不能直接编程？**
    人体有几百块肌肉，机器人有几十个电机。如果靠人手动写 `if/else` 代码来控制，代码量会爆炸且非常僵硬。
    
    **具身智能的做法：**
    1. **观察 (Observation)**：观察人类演示动作。
    2. **物理仿真 (Simulation)**：在虚拟世界里以1000倍速进行“千万次摔倒”。
    3. **奖励机制 (Reward)**：走稳了加分，摔倒了扣分。
    """)
    st.success("🤖 **最终产出**：大模型计算出每个电机在每一毫秒需要输出的**力矩大小**和**方向**。")

with col_rl_demo:
    # 模拟强化学习在虚拟世界里的试错日志
    st.code("""
    [Trial #001] Lift Left Leg -> Balance Lost -> FALL (Reward: -100)
    [Trial #450] Lean Forward -> Stability Maintained -> STEP (Reward: +50)
    [Trial #999] Dynamic Walking -> 10m Traveled -> SUCCESS (Reward: +1000)
    """, language="python")
