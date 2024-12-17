import streamlit as st

st.title("우리동네 마.스.터 프로젝트")

st.image('master.jpg', use_container_width=True)

st.markdown(
    """
    <div style="text-align: center; font-size: 24px; font-weight: bold;">
        내가 보고싶은 지역을 왼쪽 메뉴에서 클릭해보세요.
    </div>
    """,
    unsafe_allow_html=True
)