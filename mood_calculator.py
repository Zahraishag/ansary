
import streamlit as st

st.title("🧠 الآلة الحاسبة الذكية للمشاعر")

st.write("🎯 أدخلي مشاعرك اليوم بالأرقام (من 0 إلى 10):")

happiness = st.slider("😊 السعادة", 0, 10, 5)
stress = st.slider("😰 التوتر", 0, 10, 5)
excitement = st.slider("🤩 الحماس", 0, 10, 5)
boredom = st.slider("😴 الملل", 0, 10, 5)

# حساب نتائج بسيطة
mood_score = happiness + excitement - stress - boredom

st.write("📊 **مجموعك المزاجي اليوم:**", mood_score)

# اقتراح بناءً على النتيجة
if mood_score >= 10:
    st.success("يبدو أنك في مزاج ممتاز! استثمريه في تعلم شيء جديد 💡")
elif 5 <= mood_score < 10:
    st.info("مزاجك جيد، لكن يمكن تحسينه… جربي تمشية أو كوب شاي ☕")
elif 0 <= mood_score < 5:
    st.warning("يبدو أنك تحتاجين راحة… ابعدي عن الهاتف وخذي نفسًا عميقًا 🌿")
else:
    st.error("مزاج منخفض جدًا. شاركي مشاعرك مع من تثقين به 🤍")
