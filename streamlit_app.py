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
        modes = stats.multimode(data)  # 여러 최빈값 모두 반환

        # 결과 출력
        st.markdown(f"**평균 :** {mean:.2f}")
        st.markdown(f"**중앙값 :** {median:.2f}")

        # 최빈값 여러 개면 쉼표로 구분해서 출력
        if len(modes) == len(set(data)):
            st.markdown("**최빈값 :** 없음")
        else:
            mode_str = ", ".join([str(round(m, 2)) for m in modes])
            st.markdown(f"**최빈값 :** {mode_str}")

    except ValueError:
        st.error("❌ 숫자만 입력하세요. (예: 150,155,160,165,170)")
else:
    st.info("⬆️ 위에 데이터를 입력하면 결과가 표시됩니다.")
