"""
# app.py
from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib

# Flask 서버에서 차트를 파일로 저장하기 위해 Agg 사용
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

app = Flask(__name__)
# 한글 표시용 설정
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 현재 파일이 있는 폴더 기준 경로
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "sales.csv"
STATIC_DIR = BASE_DIR / "static"
"""