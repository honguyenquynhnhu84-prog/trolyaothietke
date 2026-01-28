#!/usr/bin/env bash
set -e

if [ -f .venv/bin/activate ]; then
  source .venv/bin/activate
else
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
fi

if [ -z "$GEMINI_API_KEY" ]; then
  echo "Chưa đặt GEMINI_API_KEY. Bạn có thể xuất biến môi trường trước khi chạy:"
  echo "  export GEMINI_API_KEY=your_key_here"
fi

streamlit run streamlit_app.py
