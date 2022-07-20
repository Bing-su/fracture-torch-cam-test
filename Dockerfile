FROM python:3.9

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install micropipenv[toml] && \
    micropipenv install --deploy && \
    pip cache purge

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
