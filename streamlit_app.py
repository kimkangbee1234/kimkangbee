import streamlit as st
import numpy as np
import statistics as stats

st.title("자료의 대표값 계산기 📊")

data_input = st.text_area("자료를 쉼표로 구분하여 입력하세요 (예: 150,160,155,165,170)")

if data_input:
    try:
        # 입력값 전처리
        data = [float(x.strip()) for x in data_input.split(",") if x.strip() != ""]

        # 대표값 계산
        mean = np.mean(data)
        median = np.median(data)
        try:
            mode = stats.mode(data)
        except:
            mode = "없음 (중복 최빈값)"

        # 결과 출력 (요구한 형식)
        st.markdown(f"**평균 :** {mean:.2f}")
        st.markdown(f"**중앙값 :** {median:.2f}")
        st.markdown(f"**최빈값 :** {mode if isinstance(mode, str) else round(mode, 2)}")

    except ValueError:
        st.error("❌ 숫자만 입력하세요. (예: 150,160,155,165,170)")
else:
    st.info("⬆️ 위에 데이터를 입력하면 결과가 표시됩니다.")
