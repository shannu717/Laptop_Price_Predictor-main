import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻",
                   layout="wide")

#import model
st.title("Laptop Price Predictor 💻")
pipe=pickle.load(open("pipe.pkl","rb"))
df=pickle.load(open("df.pkl","rb"))

# making 2 cols left_column, right_column
left_column, right_column = st.columns(2)
with left_column:
    # brand input
    company = st.selectbox("Brand", df["Brand"].unique())

with right_column:
    # Ram size
    ram = st.selectbox("Ram (in GB)", df["Ram_Size"].unique())

# making 2 cols left_column, right_column
left_column, right_column = st.columns(2)
with left_column:
    # screen size
    Screen_size = st.number_input("Screen Size (in Inches)")

with right_column:
    # cpu input
    cpu = st.selectbox("CPU Brand", df["CPU_brand"].unique())

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # hdd input
    hdd = st.selectbox("HDD(in GB)", [0, 128, 256, 512, 1024, 2048])

with middle_column:
    # ssd input
    ssd = st.selectbox("SSD(in GB)", [0, 8, 128, 256, 512, 1024])


with right_column:
    # ssd input
    EMMC = st.selectbox("EMMC(in GB)", [0, 8, 128, 256, 512, 1024])

#os input
os=st.selectbox("OS Type",df["OS"].unique())

#RAM_type input
Ram_type=st.selectbox("RAM Type",df["Ram_Type"].unique())

if st.button("Predict Price"):
    query=np.array([company, type, ram, cpu, hdd, ssd, EMMC, os, Ram_type])

    query=query.reshape(1, -1)
    st.title("The Predicted Price of Laptop = Rs "+str(int(np.exp(pipe.predict(query)[0]))))
