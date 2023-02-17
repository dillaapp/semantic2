FROM pypy:latest AS builder

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
Run python -m spacy download en_core_web_md

COPY . /app

FROM pypy:latest

WORKDIR /app

COPY --from=builder /app /app

CMD python garden.py
