web: gunicorn app.main:app -w 1 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT
worker: streamlit run streamlit.py --server.port $PORT
