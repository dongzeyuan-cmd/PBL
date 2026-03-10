import streamlit as st
import pandas as pd

# ==========================================
# 0. 页面全局配置 (必须在 pages 目录下)
# ==========================================
st.set_page_config(page_title="具身智能：人机对齐可视化", page_icon="🤖", layout="wide")

st.title("🤖 具身智能 (Embodied AI)：人机对齐与可视化教学系统")
st.markdown("---")
st.markdown("""
### 👋 欢迎来到具身智能的造物主实验室！
具身智能不仅是 AI，更是拥有物理身体的智能。它是如何像人一样感知世界、控制身体、甚至通过观察人类来学习动作的？
**👇 请在下方点击对应的系统模块，开启对齐学习。**
""")

# ==========================================
# 1. 核心教学选项卡 (三个维度对齐)
# ==========================================
tab_nerve, tab_skeleton, tab_muscle = st.tabs([
    "🧠 1. 神经与控制系统 (感知与决策)", 
    "🦴 2. 骨骼与机械结构 (支撑与自由度)", 
    "💪 3. 肌肉与执行系统 (动力与力量)"
])

# ------------------ Tab 1: 神经与控制对齐 ------------------
with tab_nerve:
    col_human_n, col_robot_n = st.columns([1, 1])
    
    with col_human_n:
        st.subheader("👨‍⚖️ 人体：感官与中枢神经系统")
        # 这里未来替换成你生成的 Midjourney 人体图
        st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=Human1&backgroundColor=b6e3f4", caption="人体感觉器官分布图 (演示图)", use_container_width=True)
        
        with st.expander("👁️ 视觉系统 (Visual)", expanded=True):
            st.write("**人类原理**：双眼捕获光线，在视网膜成像，通过视神经传导至大脑皮层进行物体识别和深度感知。")
        
        with st.expander("⚖️ 前庭与平衡 (Vestibular)", expanded=False):
            st.write("**人类原理**：内耳中的半规管和耳石器，感知头部旋转和直线加速度，小脑据此维持身体平衡。")
            
        with st.expander("💪 本体感觉 (Proprioception)", expanded=False):
            st.write("**人类原理**：存在于肌肉、肌腱和关节中的感受器，时刻向大脑汇报身体各部位的相对位置和力量状态。")

    with col_robot_n:
        st.subheader("🤖 机器人：传感器与具身智能大脑")
        # 这里未来替换成你生成的 Midjourney 机器人图
        st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=Robot1&backgroundColor=f1f5f9", caption="机器人传感器分布图 (演示图)", use_container_width=True)
        
        st.markdown("**👉 请点击传感器标签，学习其工作原理：**")
        
        # 模拟点击展开传感器详情
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("📷 深度摄像头", key="cam_btn"):
                st.session_state['active_sensor'] = 'camera'
        with c2:
            if st.button("⚖️ IMU 惯性传感器", key="imu_btn"):
                st.session_state['active_sensor'] = 'imu'
        with c3:
            if st.button("💪 关节编码器", key="enc_btn"):
                st.session_state['active_sensor'] = 'encoder'

        # 根据点击显示不同详情 (这是降维打击的秘诀)
        active_sensor = st.session_state.get('active_sensor', None)
        if active_sensor == 'camera':
            with st.chat_message("ai"):
                st.markdown("**📷 深度摄像头 (对齐：眼睛)**")
                st.write("**具体类型**：Structured Light (结构光) 或 Time-of-Flight (ToF) 摄像头。")
                st.write("**中学生原理**：像蝙蝠一样！它发出一束红外光，测量光线碰到物体反弹回来的时间差，从而不仅看到颜色，还能算出物体离自己有多远，生成“深度图”。")
        elif active_sensor == 'imu':
            with st.chat_message("ai"):
                st.markdown("**⚖️ IMU 惯性传感器 (对齐：前庭/内耳)**")
                st.write("**具体类型**：6轴/9轴惯性测量单元 (集成陀螺仪+加速度计+磁力计)。")
                st.write("**中学生原理**：就像手机里玩“神庙逃亡”时的重力感应器！它能时刻算出机器人的头部是不是歪了、身体是不是正在向前冲，帮助具身大脑维持站立平衡。")
        elif active_sensor == 'encoder':
            with st.chat_message("ai"):
                st.markdown("**💪 关节编码器 (对齐：本体感觉)**")
                st.write("**具体类型**：绝对值磁编码器 (Absolute Magnetic Encoder)。")
                st.write("**中学生原理**：就像每个关节上的精密刻度尺！哪怕机器人关机再开机，编码器也能瞬间告诉具身大脑：“我的左胳膊目前抬高了 35.5 度”，让大脑时刻掌握身体的精确姿态。")

# ------------------ Tab 2: 骨骼与机械对齐 ------------------
with tab_skeleton:
    col_h_s, col_r_s = st.columns([1, 1])
    with col_h_s:
        st.subheader("🦴 人体骨骼系统")
        st.write("- **核心功能**：提供刚性支撑，保护内脏，通过关节实现运动。")
        st.write("- **自由度**：人体大约有 200 多个自由度，光是手部就有二十多个。")
    with col_r_s:
        st.subheader("🦾 机器人机械结构")
        st.write("- **核心功能**：轻量化高强度铝合金/碳纤维支架，实现物理拓扑支撑。")
        st.write("- **自由度**：特斯拉 Optimus 大约有 40 个全身体自由度。")

# ------------------ Tab 3: 肌肉与执行对齐 ------------------
with tab_muscle:
    col_h_m, col_r_m = st.columns([1, 1])
    with col_h_m:
        st.subheader("💪 人体肌肉与肌腱")
        st.write("- **人类原理**：肌肉收缩产生拉力，肌腱传递力量，拉动骨骼运动。")
        st.write("- **特点**：爆发力强，柔韧性高，自带阻尼。")
    with col_r_m:
        st.subheader("💥 机器人驱动器 (电机)")
        st.write("- **人类原理**：谐波减速器 + 无刷电机 (无框力矩电机)。")
        st.write("- **特点**：极其精准的力矩控制、位置控制和速度控制。")

# ==========================================
# 3. 终极奥义：强化学习如何“看人学动作”？
# ==========================================
st.markdown("---")
st.subheader("🧠 具身智能的终极奥义：它是如何“看人学动作”的？(强化学习可视化)")

r1, r2, r3 = st.columns([1, 1, 2])

with r1:
    st.markdown("**1. 观察 (Observe)**")
    st.write("🤖 机器人通过摄像头捕捉人类的动作姿态。")
    # 这里放一张人类跑步的gif演示
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjR0bXh3djlsbnR4em91eTZ5M2F5Njhnb3l2YW83NnVwOW16b3ozZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9w8I53N9EaG0FvC8hU/giphy.gif", use_container_width=True)

with r2:
    st.markdown("**2. 对齐与映射 (Map)**")
    st.write("🧠 具身智能大脑将人类的姿态坐标，映射到自己的机器人身体模型（URDF）上。")
    # 这里放一张机器人姿态估计的演示图
    st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=Align&backgroundColor=b6e3f4", use_container_width=True)

with r3:
    st.markdown("**3. 强化学习推演 (RL Reinforcement Learning)**")
    st.write("💥 **核心难点**：看到人做动作容易，但不知道人用了多大的力气。")
    
    # 模拟强化学习在虚拟世界里的试错
    with st.chat_message("user"):
        st.markdown("**🤖 具身大脑在“物理仿真器（Issac Sim）”里疯狂试错：**")
        st.write("➡️ *尝试 1：左腿电机力矩 +10Nm ➔ 摔倒。报错！惩罚 -100。*")
        st.write("➡️ *尝试 100：双腿电机协调输出力矩，IMU 反馈身体平衡 ➔ 成功向前迈出 1 厘米。奖励 +50。*")
        st.write("➡️ *一万次试错后...*")
        st.write("✅ **学习成功！** 大脑终于算出，要做出和人一样的动作，每个电机需要输出多大的**力量（电流安培数）**和**方向（正反转）**。")

    st.success("🎉 这就是具身智能的魅力：它不需要我们手动写代码去控制每一个电机，它通过在仿真世界里的‘疯狂试错’，自己悟出了力量的真谛！")
