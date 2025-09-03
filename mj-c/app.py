import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 앱의 레이아웃을 'wide'로 설정하여 넓은 화면을 사용합니다.
st.set_page_config(layout="wide")

# HTML 파일의 경로를 'htmls' 폴더 내 'index.html'로 설정합니다.
# os.path.dirname(__file__)를 사용하여 현재 스크립트 파일의 디렉터리 경로를 가져옵니다.
script_dir = os.path.dirname(__file__)
html_file_path = os.path.join(script_dir, "htmls", "index.html")

# 지정된 경로에 HTML 파일이 존재하는지 확인합니다.
if not os.path.exists(html_file_path):
    st.error(f"오류: HTML 파일 '{html_file_path}'을(를) 찾을 수 없습니다. 'htmls' 폴더를 생성하고, 그 안에 'index.html' 파일을 저장했는지 확인해주세요.")
else:
    # 파일이 존재하면 내용을 읽어와서 변수에 저장합니다.
    try:
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Streamlit의 components.html 함수를 사용하여 HTML을 렌더링합니다.
        # height를 넉넉하게 설정하여 전체 페이지를 스크롤할 수 있도록 합니다.
        components.html(html_content, height=2000, scrolling=True)

    except Exception as e:
        # 파일을 읽는 도중 오류가 발생하면 사용자에게 알립니다.
        st.error(f"오류: HTML 파일을 읽는 중 문제가 발생했습니다: {e}")
