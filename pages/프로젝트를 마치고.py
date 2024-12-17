import streamlit as st

st.title("서로의 느낀점을 나누어봅시다.")

# Padlet 공유 링크
padlet_url = "https://padlet.com/yeokchon21602/padlet-oxn2ugnmxi5teweb"

# HTML iframe 태그를 사용해 임베드
st.markdown(f"""
<iframe src="{padlet_url}" width="800" height="600" style="border:none;"></iframe>
""", unsafe_allow_html=True)