FROM python:3.12-alpine
WORKDIR /Fasting
COPY requirement.txt .
RUN pip install --no-cache -r requirement.txt
COPY . .
EXPOSE 3500
CMD [ "python3", "index.py" ]