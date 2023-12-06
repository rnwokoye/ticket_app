FROM python:3.10
WORKDIR /streamlit_app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "ticket_app.py"]
