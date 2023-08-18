from api.AI import AIAPI
import streamlit as st
from PIL import Image


@st.cache_resource
def get_api():
    return AIAPI(font="resources/malgun.ttf")


def main():
    api = get_api()

    st.title("2023 HAI 여름방학 Web APP 개발 과제")

    # Text2Text API 활용
    st.subheader("1. OCR API 활용")
    st.markdown("이미지를 입력받아 텍스트를 출력하는 API를 사용해 보겠습니다.\n- 입력된 이미지의 텍스트를 인식해줍니다.")

    query = st.file_uploader('Upload image', accept_multiple_files=False, type=[
                             'png', 'jpg', 'jpeg'], key='ocr')
    if query is not None:
        response = api.query_image2text(query)
        st.markdown("**API Output**")
        st.code(f"{response}", language="csv")

    # Text2Image API 활용
    st.subheader("2. gpt 기반 요약 API 활용")
    st.markdown("- 텍스트를 입력받아 요약된 텍스트를 출력하는 API를 사용해 보겠습니다.\n- 입력된 텍스트를 요약해줍니다.")

    query = st.text_area('Enter text', key="summarization")

    if query is not None:
        title, summary = api.query_text2text(query)
        st.title("**Summary**")
        st.text("제목: " + title)
        st.text("요약:\n" + summary)


if __name__ == '__main__':
    main()
