FROM python:3.9-slim
WORKDIR /home
RUN mkdir data_files
COPY proj /home
RUN pip install -r requirements.txt
CMD ["python", "main.py"]