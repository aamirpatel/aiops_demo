
import streamlit as st
import psutil

st.title("AIOps Dashboard")

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

st.metric("CPU Usage", f"{cpu}%")
st.metric("RAM Usage", f"{ram}%")
st.metric("Disk Usage", f"{disk}%")
