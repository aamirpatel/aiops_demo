
import streamlit as st
import psutil

import time
import pandas as pd


st.title("AIOps Dashboard")

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

st.metric("CPU Usage", f"{cpu}%")
st.metric("RAM Usage", f"{ram}%")
st.metric("Disk Usage", f"{disk}%")

st.subheader("System Metrics Over Time")
data = {"CPU": [], "RAM": [], "Disk": []}

for _ in range(10):  # Collect 10 samples
    data["CPU"].append(psutil.cpu_percent())
    data["RAM"].append(psutil.virtual_memory().percent)
    data["Disk"].append(psutil.disk_usage('/').percent)
    time.sleep(1)

df = pd.DataFrame(data)
st.line_chart(df)

