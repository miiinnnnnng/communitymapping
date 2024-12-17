import streamlit as st
import pandas as pd
import os

# CSV 파일 경로
CSV_FILE = "yeokchon.csv"

# CSV 파일 초기화: 파일이 없으면 생성
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["작성자", "문제점", "해결방법"])
    df.to_csv(CSV_FILE, index=False)

# 페이지 제목 및 설명
st.title("역촌동 마스터 해결방법")
st.subheader("우리 마을의 문제점과 해결방법을 자유롭게 적어봅시다.")

# CSV 파일 불러오기
df = pd.read_csv(CSV_FILE)

# CSV 파일 내용 표시
st.dataframe(df)  # 표 형태로 CSV 내용 출력

# 사이드바 입력 폼
st.sidebar.header("문제점과 해결방법을 입력하세요.")
작성자 = st.sidebar.text_input("작성자 이름")
문제점 = st.sidebar.text_input("문제점")
해결방법 = st.sidebar.text_area("해결방법")

# 저장 버튼
if st.sidebar.button("저장"):
    if 작성자 and 문제점 and 해결방법:  # 입력값 검증
        # 새 데이터 추가
        new_data = pd.DataFrame([{"작성자": 작성자, "문제점": 문제점, "해결방법": 해결방법}])
        df = pd.concat([df, new_data], ignore_index=True)  # 기존 데이터와 병합
        
        # CSV 파일에 저장
        df.to_csv(CSV_FILE, index=False)
        
        # 성공 메시지
        st.sidebar.success("저장되었습니다!")
        st.rerun()  # 페이지 새로고침으로 업데이트 반영
    else:
        st.sidebar.error("모든 입력 칸을 채워주세요.")