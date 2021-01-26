FROM python:3.7
COPY . /vgsapp
WORKDIR /vgsapp
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["appstart.py"]