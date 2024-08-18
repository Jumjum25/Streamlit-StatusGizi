import pickle # untuk meload dot  sav
import streamlit as st # untuk membut kodingan streamlit

# membaca model
DataGizi_model = pickle.load(open('StatusGiziAnak_model.sav', 'rb'))

# judul web
st.title('Memprediksi Status Gizi Anak Menggunakan Algoritma Decision Tree Di Puskesmas Perawatan Hitu Kabupaten Maluku Tengah')
st.title('')
# membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Jenis_Kelamin = st.text_input ('Jenis Kelamin')

with col1 :
    Umur_Bulan = st.text_input ('Umur(Bulan)')

with col2 :
    Berat_Badan = st.text_input ('Berat Badan(Kg) ')

with col2 :
    Tinggi_Badan  = st.text_input ('Tinggi Badan(Cm)')

# code untuk prediksi
status_gizi = ''

# membuat tombol untuk prediksi
if st.button('Status Gizi Anak') :
    datagizi_prediction = DataGizi_model.predict([[Jenis_Kelamin,Umur_Bulan,Berat_Badan,Tinggi_Badan]])


    if(datagizi_prediction[0] ==1):
        status_gizi = 'Gizi Normal'
    else :
        status_gizi = 'Gizi kurang'

    st.success(status_gizi)