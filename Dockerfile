FROM python:3.8

RUN pytest tests/test_lens.py
RUN pytest tests/test_sensor.py

CMD ["python3","tests"]
