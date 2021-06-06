FROM python:3.8
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt -f  https://download.pytorch.org/whl/torch_stable.html
CMD python main.py
