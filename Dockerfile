FROM python:3.11-bookworm AS build

WORKDIR /boopy/

COPY boopy/ /boopy/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM build
CMD [ "python", "main.py" ]

