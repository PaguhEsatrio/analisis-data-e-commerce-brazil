import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from io import BytesIO
sns.set(style='dark')
all_df = pd.read_csv('dashboard/Semua Data.csv')

# =================== Header
st.header('Visualisasi E-Commerce Public Dataset')
# =================== Header

#============================================================================================== Produk Laris
# Produk Laris Function
def produkLaris(df):
    produkLaris = df.groupby("product_category_name_english")["product_id"].count().reset_index()
    produkLaris = produkLaris.rename(columns={"product_id": "jumlah"})
    return produkLaris
# Produk Laris Function 

# Subheader
st.subheader("Penjualan Paling Banyak dan Sedikit")
col1, col2 = st.beta_columns(2)

with col1:
    produkLaris_df = produkLaris(all_df)
    highest_product_sold = produkLaris_df['jumlah'].max()
    st.markdown(f"Penjualan Paling Banyak : **{highest_product_sold}**")

with col2:
    lowest_product_sold = produkLaris_df['jumlah'].min()
    st.markdown(f"Penjualan Paling Sedikit: **{lowest_product_sold}**")

colors = ["#068DA9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))


sns.barplot(
    y="product_category_name_english",
    x="jumlah",
    data=produkLaris_df.sort_values(by="jumlah", ascending=False).head(5),
    palette=colors,
    ax=ax[0]
)
ax[0].set_title("Penjualan Paling Banyak", loc="center", fontsize=15)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].tick_params(axis='x', labelsize=12)

sns.barplot(
    y="product_category_name_english",
    x="jumlah",
    data=produkLaris_df.sort_values(by="jumlah", ascending=True).head(5),
    palette=colors,
    ax=ax[1]
)
ax[1].set_title("Penjualan Paling Sedikit", loc="center", fontsize=15)
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].tick_params(axis='x', labelsize=12)
# Display Plot in Streamlit
st.pyplot(fig)
#============================================================================================== Produk Laris


#============================================================================================== Customer terbanyak
# Customer terbanyak State Function
def banyakState(df):
    banyakState = df.groupby(["customer_state"])["customer_id"].nunique().reset_index()
    banyakState = banyakState.rename(columns={"customer_id": "jumlah"})
    return banyakState
# Customer terbanyak State Function 

# Customer terbanyak State Function
def banyakStateKota(df):
    banyakStateKota  = df.groupby(["customer_city"])["customer_id"].nunique().reset_index()
    banyakStateKota  = banyakStateKota.rename(columns={"customer_id": "jumlah"})
    return banyakStateKota 
# Customer terbanyak State Function 

# Subheader
st.subheader("Customer Terbanyak")
col1, col2 = st.beta_columns(2)

with col1:
    banyakState_df = banyakState(all_df)
    stateBanyak = banyakState_df['jumlah'].max()
    spillState =  banyakState_df.loc[banyakState_df['jumlah'].idxmax()]['customer_state']
    st.markdown(f"Customer Paling Banyak State : **{stateBanyak}** (**{spillState}**) ")

with col2:
    banyakStateKota_df = banyakStateKota(all_df)
    stateBanyakKota = banyakStateKota_df['jumlah'].max()
    spillKota =  banyakStateKota_df.loc[banyakState_df['jumlah'].idxmax()]['customer_city']
    st.markdown(f"Customer Paling Banyak State : **{stateBanyakKota}** (**{spillKota}**) ")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

sns.barplot(x='customer_state',
            y='jumlah',
            data= banyakState_df.sort_values(by="jumlah", ascending=False).head(5),
            ax=ax[0]
)
ax[0].set_title("Grafik Customer Setiap Sate", fontsize=15)
ax[0].set_ylabel("Jumlah Customers")
ax[0].set_xlabel("State")
ax[0].tick_params(axis='x', labelsize=10)

sns.barplot(
            x='customer_city',
            y='jumlah',
            data=banyakStateKota_df.sort_values(by="jumlah", ascending=False).head(5),
            ax=ax[1]
)
ax[1].set_title("Grafik Customer Setiap Kota", fontsize=15)
ax[1].set_ylabel("Jumlah Customers")
ax[1].set_xlabel("State")
ax[1].tick_params(axis='x', labelsize=10)
# Display Plot in Streamlit
st.pyplot(fig)
#=============================================================================================== Customer terbanyak


#============================================================================================== Pembayaran Favorit 
# Pembayaran Favorit
def bayar(df):
    bayar = df.groupby(["payment_type"])["order_id"].nunique().reset_index()
    bayar = bayar.rename(columns={"order_id": "jumlah"})
    return bayar
# Pembayaran Favorit 

# Subheader
st.subheader("Pembayaran Favorit")
col1, col2 = st.beta_columns(2)

with col1:
    bayar_df = bayar(all_df)
    pembayaranFavorit = bayar_df['jumlah'].max()
    spillpem =  bayar_df.loc[bayar_df['jumlah'].idxmax()]['payment_type']
    st.markdown(f"Jenis Pembayaran Favorit : **{pembayaranFavorit}** (**{spillpem}**)")

with col2:
    pembayaranNonFav = bayar_df['jumlah'].min()
    spillnon =  bayar_df.loc[bayar_df['jumlah'].idxmin()]['payment_type']
    st.markdown(f"Jenis Pembayaran Kurang Favorit : **{pembayaranNonFav}** (**{spillnon}**)")

plt.figure(figsize=(16, 8))

sns.barplot(
   x='payment_type',
   y='jumlah',
   data=bayar_df.sort_values(by="jumlah", ascending=False),
)
plt.xlabel("Tipe Pembayaran")
plt.ylabel("Jumlah Customers")
plt.xticks(fontsize=10, rotation=25)
plt.yticks(fontsize=10)
plt.legend()
st.pyplot(plt)

# Pembayaran Favorit St
def bayarSt(df):
  bayarSt = all_df.groupby(["payment_type","customer_state"])["order_id"].nunique().reset_index()
  bayarSt = bayarSt.rename(columns={"order_id": "jumlah"})
  return bayarSt
# Pembayaran Favorit St

bayarSt_df = bayarSt(all_df)
plt.figure(figsize=(16, 8))
bayarSt_df = bayarSt_df.sort_values(by='jumlah', ascending=False)

sns.barplot(x='jumlah',
            y='customer_state',
            hue='payment_type',
            data=bayarSt_df)

plt.title("Grafik Pembayaran di Setiap state", fontsize=15)
plt.ylabel("State")
plt.xlabel("Jumlah")
plt.xticks(fontsize=10)
plt.legend(title="Payment Type")
plt.yticks(fontsize=10)
st.pyplot(plt)
#============================================================================================== Pembayaran Favorit 


#============================================================================================== pendapatan selama beberapa bulan terakhir?
all_df['order_approved_at'] = pd.to_datetime(all_df['order_approved_at'])

# Fungsi untuk mendapatkan data pengeluaran per bulan
def bulan(df):
    bulan = df.resample(rule='M', on='order_approved_at').agg({
                "price": "sum"
    }).reset_index()
    bulan.rename(columns={
                "price": "Pengeluaran"
            }, inplace=True)
    bulan = bulan[(bulan['order_approved_at'] >= '2018-01-01') & (bulan['order_approved_at'] <= '2018-12-31')]
    # Konversi ke nama bulan Tahun
    bulan['order_approved_at'] = bulan['order_approved_at'].dt.strftime('%B %Y')
    custom_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    bulan['month_cat'] = pd.Categorical(bulan['order_approved_at'], categories=custom_order, ordered=True)
    bulan = bulan.sort_values(by='month_cat')
    bulan = bulan.drop(columns=['month_cat'])
    return bulan

# Subheader
st.subheader("Pendapatan selama beberapa bulan terakhir (2018)?")
col1, col2 = st.beta_columns(2)

with col1:
    bulan_df = bulan(all_df)
    pendapatan = bulan_df['Pengeluaran'].sum()
    st.markdown(f"Pendapatan selama beberapa bulan terakhir (2018) : **{pendapatan}**")

with col2:
    ratarata = bulan_df['Pengeluaran'].mean()
    st.markdown(f"Rata-rata Pengeluaran per bulan: **{ratarata}**")

# Plot grafik pendapatan per bulan
plt.figure(figsize=(16, 8))

plt.plot(
    bulan_df["order_approved_at"],
    bulan_df["Pengeluaran"],
    marker='o',
    linewidth=2,
    color="#72BCD4"
)
ax.plt.title("Pengeluaran Customer 2018 ", loc="center", fontsize=20)
ax.plt.xticks(fontsize=10, rotation=25)
ax.plt.yticks(fontsize=10)

# Simpan gambar ke dalam BytesIO
image_stream = BytesIO()
plt.savefig(image_stream, format='png')
image_stream.seek(0)

# Tampilkan gambar menggunakan st.image
st.image(image_stream, caption='Grafik Pendapatan per Bulan', use_column_width=True)
#============================================================================================== pendapatan selama beberapa bulan terakhir?

#============================================================================================== review 
def review(df):
    review_counts = df['review_score'].value_counts().sort_index()
    return review_counts

# Subheader
st.subheader("Review Rating")
review_counts = review(all_df)


# Plot bar chart untuk menunjukkan jumlah review untuk setiap skor
plt.figure(figsize=(16, 8))
sns.barplot(
    x=review_counts.index, 
    y=review_counts.values, 
    order=review_counts.index,
)

plt.title("Rating customers for service", fontsize=15)
plt.xlabel("Rating")
plt.ylabel("Customer")
plt.xticks(fontsize=12)
st.pyplot(plt)
#============================================================================================== review 

with st.sidebar:
    
    # Menambahkan logo perusahaan
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png")
    st.write('Copyright (C) © 2023 by Paguh')

