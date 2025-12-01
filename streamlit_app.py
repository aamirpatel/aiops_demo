
import streamlit as st
import psutil
import time
import pandas as pd
import numpy as np


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


    
st.subheader("Log Explorer")
uploaded_file = st.file_uploader("Upload log file")
if uploaded_file:
    logs = uploaded_file.read().decode("utf-8").splitlines()
    keyword = st.text_input("Filter logs by keyword")
    filtered = [line for line in logs if keyword.lower() in line.lower()]
    st.dataframe(filtered)

    time.sleep(1)

df = pd.DataFrame(data)
st.line_chart(df)




cpu_data = np.array(data["CPU"])
threshold = cpu_data.mean() + 2 * cpu_data.std()
anomalies = [i for i, val in enumerate(cpu_data) if val > threshold]
st.write("Anomalies detected at indices:", anomalies)


