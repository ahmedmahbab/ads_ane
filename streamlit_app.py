import streamlit as st

# يجب أن يكون استدعاء set_page_config أول سطر في البرنامج
st.set_page_config(page_title="حاسبة الفائدة ورأس المال", page_icon="💰", layout="centered")

# تنسيق الهيدر مع تكبير حجم الخط
st.markdown("<h1 style='text-align: center; color: #4CAF50; font-size: 50px;'>حاسبة الفائدة ورأس المال 💰</h1>", unsafe_allow_html=True)

# إدخال القيم المتغيرة من خلال واجهة Streamlit
st.markdown("<h3 style='text-align: center; font-size: 24px;'>أدخل المعطيات</h3>", unsafe_allow_html=True)
selling_price = st.number_input("🟢 أدخل مبلغ البيع", min_value=0.0, value=330.0)
buying_price = st.number_input("🔵 أدخل مبلغ الشراء", min_value=0.0, value=235.0)
invoice_amount = st.number_input("🟡 أدخل مبلغ الفاتورة", min_value=0.0, value=1000.0)

# حساب نسبة الفائدة
profit_percentage = (selling_price - buying_price) / selling_price * 100

# حساب نسبة رأس المال
capital_percentage = 100 - profit_percentage

# حساب قيمة الفائدة
profit_value = invoice_amount * (profit_percentage / 100)

# حساب قيمة رأس المال
capital_value = invoice_amount * (capital_percentage / 100)

# عرض النتائج باستخدام Streamlit
st.markdown("<h3 style='text-align: center; font-size: 28px;'>📊 النتائج</h3>", unsafe_allow_html=True)

# عرض نسبة الفائدة باللون الأحمر مع تكبير الخط
st.markdown(f"<p style='color:red; text-align: center; font-size: 18px;'>🔻 نسبة الفائدة: {profit_percentage:.2f}%</p>", unsafe_allow_html=True)

# عرض قيمة الفائدة مع تكبير الخط
st.markdown(f"<p style='text-align: center; font-size: 22px;'>💰 <strong>قيمة الفائدة:</strong> {profit_value:.2f} DZD</p>", unsafe_allow_html=True)

# عرض نسبة رأس المال باللون الأخضر مع تكبير الخط
st.markdown(f"<p style='color:green; text-align: center; font-size: 18px;'>🔺 نسبة رأس المال: {capital_percentage:.2f}%</p>", unsafe_allow_html=True)

# عرض قيمة رأس المال مع تكبير الخط
st.markdown(f"<p style='text-align: center; font-size: 22px;'>💵 <strong>قيمة رأس المال:</strong> {capital_value:.2f} DZD</p>", unsafe_allow_html=True)

# تخصيص نهاية الصفحة مع تكبير النص
st.markdown("<hr style='border:2px solid #4CAF50'>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; font-size: 18px;'>تم تطويره بواسطة 🌟 Al Nour Elite 🌟</h4>", unsafe_allow_html=True)


