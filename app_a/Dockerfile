FROM python:3.7
ENV PORT 443
EXPOSE 443
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "app_a.py"]