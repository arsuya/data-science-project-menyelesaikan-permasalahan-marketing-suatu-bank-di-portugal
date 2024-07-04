import streamlit as st
import pandas as pd
import pickle

# Fungsi untuk memuat model yang sudah dilatih
@st.cache_data()
def load_model(model_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

# Fungsi untuk melakukan prediksi
def predict(model, input_data):
    X_new = pd.DataFrame(input_data, index=[0])
    y_pred = model.predict(X_new)
    y_pred_label = ['yes' if pred == 1 else 'no' for pred in y_pred]
    return y_pred_label[0]

# Fungsi utama dashboard
def main():
    # Judul dashboard
    st.title('Prediksi Berlangganan Deposito Berjangka')

    # Deskripsi dan informasi input data
    st.header('Masukkan Data untuk Prediksi')
    st.markdown('Isi kolom-kolom berikut dengan data klien yang ingin Anda prediksi.')

    # Kolom input untuk masukkan data
    age = st.number_input('Umur', min_value=18, max_value=100, value=56)
    job = st.selectbox('Pekerjaan', ['housemaid', 'services', 'admin.', 'blue-collar', 'technician', 'retired', 'management', 'unemployed', 'self-employed', 'unknown', 'entrepreneur', 'student'], index=0)
    marital = st.selectbox('Status Pernikahan', ['married', 'single', 'divorced', 'unknown'], index=0)
    education = st.selectbox('Pendidikan', ['basic.4y', 'high.school', 'basic.6y', 'basic.9y', 'professional.course', 'unknown', 'university.degree', 'illiterate'], index=0)
    housing = st.selectbox('Kredit Perumahan', ['no', 'yes', 'unknown'], index=0)
    loan = st.selectbox('Pinjaman Pribadi', ['no', 'yes', 'unknown'], index=0)
    contact = st.selectbox('Jenis Kontak', ['telephone', 'cellular'], index=0)
    month = st.selectbox('Bulan Kontak Terakhir', ['may', 'jun', 'jul', 'aug', 'oct', 'dec', 'mar', 'apr', 'sep', 'nov'], index=0)
    day_of_week = st.selectbox('Hari Kontak Terakhir', ['mon', 'tue', 'wed', 'thu', 'fri'], index=0)
    campaign = st.number_input('Jumlah Kontak Selama Kampanye Ini', min_value=1, value=1)
    previous = st.number_input('Jumlah Kontak Sebelumnya', min_value=0, value=0)
    poutcome = st.selectbox('Hasil Kampanye Sebelumnya', ['nonexistent', 'failure', 'success'], index=0)
    emp_var_rate = st.number_input('Variabel Rate Ketenagakerjaan', value=1.1)
    cons_price_idx = st.number_input('Indeks Harga Konsumen', value=93.994)
    cons_conf_idx = st.number_input('Indeks Kepercayaan Konsumen', value=-36.4)
    euribor3m = st.number_input('Euribor 3 Bulan', value=4.857)
    nr_employed = st.number_input('Jumlah Karyawan', value=5191.0)
    is_service_job = st.selectbox('Pekerjaan di Sektor Jasa?', ['no', 'yes'], index=0)
    contact_rate = st.number_input('Tingkat Kontak', value=0.0)

    # Tombol untuk memulai prediksi
    if st.button('Prediksi'):
        # Load model
        model = load_model('model.pkl')

        # Masukkan data ke dalam dictionary
        is_service_job = 1 if is_service_job == 'yes' else 0
        input_data = {
            'age': age, 
            'job': job, 
            'marital': marital, 
            'education': education, 
            'housing': housing, 
            'loan': loan, 
            'contact': contact, 
            'month': month, 
            'day_of_week': day_of_week, 
            'campaign': campaign, 
            'previous': previous, 
            'poutcome': poutcome, 
            'emp.var.rate': emp_var_rate, 
            'cons.price.idx': cons_price_idx, 
            'cons.conf.idx': cons_conf_idx, 
            'euribor3m': euribor3m, 
            'nr.employed': nr_employed,
            'is_service_job': is_service_job,
            'contact_rate': contact_rate
        }

        # Lakukan prediksi
        prediction = predict(model, input_data)

        # Tampilkan hasil prediksi
        if prediction == 'yes':
            st.success('Hasil Prediksi: Berlangganan')
        else:
            st.warning('Hasil Prediksi: Tidak Berlangganan')

# Memanggil fungsi utama untuk menjalankan dashboard
if __name__ == '__main__':
    main()
