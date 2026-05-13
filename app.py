import streamlit as st

st.set_page_config(
    page_title="مشروع مصنع حقن بلاستيك",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 مشروع تصميم مصنع حقن بلاستيك")
st.write("موقع بسيط لعرض أقسام مشروع تصميم وتشغيل مصنع حقن بلاستيك")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📍 تحديد موقع المصنع")
    if st.button("فتح قسم الموقع"):
        st.write("""
        - القرب من الطرق الرئيسية
        - القرب من العملاء والأسواق
        - توفر الكهرباء والمياه
        - مساحة مناسبة للتوسعات
        - سهولة دخول وخروج الشاحنات
        """)

with col2:
    st.success("🏗️ Layout خط الإنتاج")
    if st.button("فتح قسم Layout"):
        st.write("""
        - منطقة استقبال الخامات
        - ماكينات حقن البلاستيك
        - منطقة التبريد
        - منطقة التشطيب والفحص
        - منطقة التعبئة والتخزين
        """)

with col3:
    st.warning("📊 PERT Chart")
    if st.button("فتح قسم PERT"):
        st.write("""
        مراحل إنشاء المصنع:
        1. دراسة الجدوى
        2. اختيار الموقع
        3. شراء الماكينات
        4. تجهيز الأرضية والكهرباء
        5. تركيب الماكينات
        6. التشغيل التجريبي
        """)

col4, col5, col6 = st.columns(3)

with col4:
    st.error("🚚 وسائل النقل")
    if st.button("فتح قسم النقل"):
        st.write("""
        - عربيات نقل صغيرة للتوزيع المحلي
        - شاحنات لنقل الخامات
        - ونش أو كلارك داخل المصنع
        - نظام تحميل وتفريغ آمن
        """)

with col5:
    st.info("⚙️ Machine Loading")
    if st.button("فتح قسم تحميل الماكينات"):
        st.write("""
        يتم حساب تحميل الماكينات حسب:
        - عدد الماكينات
        - زمن الدورة Cycle Time
        - عدد ساعات العمل
        - كمية الإنتاج المطلوبة
        - كفاءة التشغيل
        """)

with col6:
    st.success("📦 المنتجات والخامات")
    if st.button("فتح قسم المنتجات"):
        st.write("""
        منتجات ممكنة:
        - علب بلاستيك
        - أغطية
        - قطع صغيرة
        - مكونات صناعية

        خامات:
        - PP
        - PE
        - ABS
        - PVC
        """)

st.markdown("---")

st.subheader("🧮 حساب مبدئي للإنتاج")

machines = st.number_input("عدد ماكينات الحقن", min_value=1, value=3)
cycle_time = st.number_input("زمن الدورة بالثواني", min_value=1, value=30)
hours = st.number_input("عدد ساعات العمل يوميًا", min_value=1, value=8)

production = machines * hours * 3600 / cycle_time

st.success(f"الإنتاج التقريبي في اليوم = {int(production)} قطعة")