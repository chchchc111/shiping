# resume_app.py
import streamlit as st
from datetime import date

# ---------- 页面配置 ----------
st.set_page_config(page_title="个人简历生成器", layout="wide")
st.title("📄 个人简历生成器")

# ---------- 初始化会话状态 ----------
# 通用字段先全部给空字符串
fields = ["name", "phone", "email", "birth", "edu", "salary",
          "contact_time", "language", "skills", "intro", "photo"]
for f in fields:
    if f not in st.session_state:
        st.session_state[f] = "" if f != "skills" else []

# 单独给 gender 赋合法初值，避免 radio 报错
if "gender" not in st.session_state:
    st.session_state.gender = "男"

# ---------- 左右分栏 ----------
left, right = st.columns([1, 1])

# ================= 左侧：实时填写（无表单） =================
with left:
    st.header("① 填写信息")
    st.text_input("姓名", key="name")
    st.radio("性别", ["男", "女", "其他"], horizontal=True, key="gender")
    st.text_input("电话", key="phone")
    st.text_input("邮箱", key="email")
    st.date_input("出生日期", value=date(1990, 1, 1), key="birth")
    st.selectbox("学历", ["高中", "专科", "本科", "硕士", "博士"], key="edu")
    st.slider("工作经验（年）", 0, 30, 0, key="exp")
    st.text_input("期望薪资（如 10k-15k）", key="salary")
    st.time_input("每日最佳联系时间", value=None, key="contact_time")
    st.text_area("语言能力", key="language")
    st.multiselect(
        "技能（可多选）",
        ["Python", "Java", "C/C++", "数据分析", "机器学习", "前端", "SQL", "Office"],
        key="skills"
    )
    st.text_area("个人简介", key="intro")
    st.file_uploader("上传个人照片（jpg/png）", type=["jpg", "jpeg", "png"], key="photo")

# ================= 右侧：实时预览 =================
with right:
    st.header("② 简历预览")
    # 照片
    if st.session_state.photo:
        st.image(st.session_state.photo, width=150)
    else:
        st.info("📷 暂无照片")

    # 基本信息
    st.subheader(st.session_state.name or "姓名未填")
    st.write(f"性别：{st.session_state.gender}")
    st.write(f"出生日期：{st.session_state.birth}")
    st.write(f"电话：{st.session_state.phone or '未填'}")
    st.write(f"邮箱：{st.session_state.email or '未填'}")
    st.write(f"学历：{st.session_state.edu}")
    st.write(f"工作经验：{st.session_state.exp} 年")
    st.write(f"期望薪资：{st.session_state.salary or '未填'}")
    st.write(f"最佳联系时间：{st.session_state.contact_time or '未填'}")
    st.write(f"语言能力：{st.session_state.language or '暂无'}")
    st.write(f"技能：{', '.join(st.session_state.skills) or '暂无'}")

    # 个人简介
    st.write("---")
    st.write("**个人简介：**")
    st.write(st.session_state.intro or "这个人很神秘，没有留下任何介绍。")

    # 一键下载 Markdown 简历
    md_content = "\n\n".join([
        f"# {st.session_state.name or '姓名未填'}",
        f"> 性别：{st.session_state.gender}  |  出生日期：{st.session_state.birth}",
        f"> 电话：{st.session_state.phone}  |  邮箱：{st.session_state.email}",
        f"> 学历：{st.session_state.edu}  |  工作经验：{st.session_state.exp} 年",
        f"> 期望薪资：{st.session_state.salary}  |  最佳联系时间：{st.session_state.contact_time}",
        "## 语言能力",
        st.session_state.language or "暂无",
        "## 技能",
        ", ".join(st.session_state.skills) or "暂无",
        "## 个人简介",
        st.session_state.intro or "暂无"
    ])
    st.download_button(
        label="📥 下载 Markdown 简历",
        data=md_content,
        file_name=f"{st.session_state.name or 'resume'}.md",
        mime="text/markdown"
    )
