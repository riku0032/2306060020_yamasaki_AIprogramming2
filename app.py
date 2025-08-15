import streamlit as st
from logic import analyze_sentiment

st.title("文章感情分析アプリ")
st.write("文章を入力すると、ポジティブ / ネガティブ / ニュートラルを判定します。")

# ユーザー入力
user_input = st.text_area("文章を入力してください", "")

# ボタン押下で分析
if st.button("分析する"):
    result = analyze_sentiment(user_input)
    if result:
        label, score = result
        st.subheader("分析結果")
        st.write(f"感情: **{label}**")
        st.write(f"確信度: **{score}%**")
    else:
        st.warning("文章を入力してください。")
