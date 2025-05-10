FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY model_getaround_real.pkl .

# Fixer les versions pour compatibilité binaire
RUN pip install --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir numpy==1.23.5 scikit-learn==1.2.2 joblib pandas streamlit

EXPOSE 7860

CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
