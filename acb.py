# abc.py
import streamlit as st

st.set_page_config(page_title="视频中心")

# ---------- 视频库 ----------
video_arr = [
    {
        "title": "还珠格格第一部-第1集",
        # 如果下面这条外链失效，可换成任意 mp4 地址
        "url": "https://www.w3schools.com/html/movie.mp4"
    },
    {
        "title": "还珠格格第一部-第2集",
        "url": "https://media.w3.org/2010/05/sintel/trailer.mp4"
    },
    {
        "title": "还珠格格第一部-第3集",
        "url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4"
    }
]

# ---------- 会话状态 ----------
if "ind" not in st.session_state:
    st.session_state.ind = 0

# ---------- 标题 ----------
st.title(video_arr[st.session_state.ind]["title"])

# ---------- 视频播放器 ----------
st.video(video_arr[st.session_state.ind]["url"])

# ---------- 选集按钮 ----------
st.write("**选集**")
cols = st.columns(3)          # 一行放 3 个按钮，可自行调整
for i, v in enumerate(video_arr):
    with cols[i % 3]:         # 自动换行排列
        if st.button(f"第 {i+1} 集", key=f"btn_{i}"):
            st.session_state.ind = i
            st.rerun()
