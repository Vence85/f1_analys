import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.title("F1 Analytics - Docker/Azure test")

try:
    r = requests.get(f"{API_URL}/health", timeout=3)
    st.success(f"Backend OK: {r.json()}")
except Exception as e:
    st.error(f"Backend not reachable: {e}")
