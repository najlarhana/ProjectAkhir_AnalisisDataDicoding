import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data
def load_data():
    # Load the merged data from the CSV file
    data = pd.read_csv("selected_data_geolocation.csv") 
    data2 = pd.read_csv("selected_data_cicilan.csv")
    return data, data2

# Function to perform EDA and visualization
def perform_eda(data, data2, selected_option):
    st.title("Dashboard E-Commerce dataset")
    st.markdown(
        """
        <style>
            body {
                background-color: #f0f6fc;
            }
            .stTitle {
                color: #0077cc;
            }
            .stMarkdown {
                color: #0077cc;
            }
            .stButton {
                background-color: #0077cc;
                color: #ffffff;
            }
            .css-1v3fvcr {
                background-color: #ebf5ff;
            }
            .stPlot {
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar for option selection
    st.sidebar.title("Pilih Visualisasi Data")
    selected_option = st.sidebar.selectbox("", ["Geolocation City Customer", "Installment Payment"])

    # Load data
    data, data2 = load_data()

    # Perform EDA and visualization based on the selected option
    if selected_option == "Geolocation City Customer":
        st.sidebar.subheader("Top 5 Geolocation City - Bar Plot")
        st.sidebar.write("Visualisasi Bar Plot untuk Top 5 Geolocation City dengan Jumlah Pelanggan Terbanyak.")
        top5_cities_bar = data.groupby('geolocation_city')['customer_id'].nunique().sort_values(ascending=False).head(5)
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=top5_cities_bar.index, y=top5_cities_bar.values, color='#99c2ff', ax=ax)
        plt.title('Top 5 Geolocation City dengan Jumlah Pelanggan Terbanyak')
        plt.xlabel('Geolocation City')
        plt.ylabel('Jumlah Pelanggan')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

        st.sidebar.subheader("Top 5 Geolocation City - Pie Chart")
        st.sidebar.write("Visualisasi Pie Chart untuk Top 5 Geolocation City dengan Jumlah Pelanggan Terbanyak.")
        top5_cities_pie = data.groupby('geolocation_city')['customer_id'].nunique().sort_values(ascending=False).head(5)
        fig, ax = plt.subplots(figsize=(8, 8))
        plt.pie(top5_cities_pie.values, labels=top5_cities_pie.index, autopct='%1.1f%%', colors=sns.color_palette('viridis'), startangle=90)
        plt.title('Top 5 Geolocation City dengan Jumlah Pelanggan Terbanyak (Pie Chart)')
        st.pyplot(fig)

    elif selected_option == "Installment Payment":
        st.sidebar.subheader("Installment Payments - Count Plot")
        st.sidebar.write("Visualisasi Count Plot untuk jumlah pelanggan yang melakukan pembayaran cicilan berdasarkan Jenis Pembayaran.")
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.countplot(x='payment_type', data=data2, color='#99c2ff', ax=ax)
        plt.title('Jumlah Pelanggan yang Melakukan Pembayaran Cicilan berdasarkan Jenis Pembayaran')
        plt.xlabel('Jenis Pembayaran')
        plt.ylabel('Jumlah Pelanggan')
        st.pyplot(fig)

        st.sidebar.subheader("Installment Payments - Percentage Pie Chart")
        st.sidebar.write("Visualisasi Count Plot untuk jumlah pelanggan yang melakukan pembayaran cicilan berdasarkan Jenis Pembayaran.")
        payment_type_percentage = data2['payment_type'].value_counts(normalize=True) * 100
        fig, ax = plt.subplots(figsize=(8, 8))
        plt.pie(payment_type_percentage, labels=payment_type_percentage.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('viridis'))
        plt.title('Persentase Pelanggan yang Melakukan Pembayaran Cicilan berdasarkan Jenis Pembayaran')
        plt.legend(title='Jenis Pembayaran', loc='upper right', bbox_to_anchor=(1.2, 1))
        st.pyplot(fig)

# Initialize Streamlit app
if __name__ == '__main__':
    perform_eda(None, None, None)  # Load data and perform initial visualization