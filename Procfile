web: gunicorn main:app -w 1 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
worker: streamlit run streamlit.py --server.port 8000
