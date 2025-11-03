import streamlit as st
import numpy as np
import statistics as stats

st.title("자료의 대표값 계산기 📊")

st.write("왼쪽 사이드바에서 예시 데이터를 선택하거나, 직접 자료를 입력해보세요.")

# 🎯 미리 준비된 예시 데이터
examples = {
    "예시 1️⃣ {5, 3, 28, 3, 8, 7}": [5, 3, 28, 3, 8, 7],
    "예시 2️⃣ {72, 54, 54, 72, 54, 63, 81, 81, 63}": [72, 54, 54, 72, 54, 63, 81, 81, 63],
    "예시 3️⃣ {95, 100, 90, 95, 100, 90, 100, 95, 100, 90, 90, 5, 105, 95, 100, 110, 100, 105, 100, 105}":
        [95, 100, 90, 95, 100, 90, 100, 95, 100, 90, 90, 5, 105, 95, 100, 110, 100, 105, 100, 105]
}

# 🧭 왼쪽 사이드바
st.sidebar.header("📂 예시 데이터 선택")
selected_example = None
for label, data in examples.items():
    if st.sidebar.button(label):
        selected_example = data

# 🧾 직접 입력
st.subheader("✏️ 직접 자료 입력")
data_input = st.text_area("자료를 쉼표로 구분하여 입력하세요 (예: 150,160,155,165,170)")

# ✅ 데이터 결정 (버튼 클릭 > 직접 입력 순서)
if selected_example:
    data = selected_example
elif data_input:
    try:
        data = [float(x.strip()) for x in data_input.split(",") if x.strip() != ""]
    except ValueError:
        st.error("❌ 숫자만 입력하세요. (예: 150,160,155,165,170)")
        data = None
else:
    data = None

# 📊 대표값 계산 및 출력
if data:
    mean = np.mean(data)
    median = np.median(data)
    modes = stats.multimode(data)

    st.markdown("### 📈 결과")
    st.markdown(f"**평균 :** {mean:.2f}")
    st.markdown(f"**중앙값 :** {median:.2f}")

    if len(modes) == len(set(data)):
        st.markdown("**최빈값 :** 없음")
    else:
        mode_str = ", ".join([str(round(m, 2)) for m in modes])
        st.markdown(f"**최빈값 :** {mode_str}")

    st.success("✅ 계산이 완료되었습니다!")
else:
    st.info("⬅️ 왼쪽에서 예시 데이터를 선택하거나, 아래에 직접 입력해보세요.")
