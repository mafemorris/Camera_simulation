FROM python:3.8

RUN python3 -m pip install pytest
RUN python3 -m pip install numpy

COPY / /

RUN python3 -m pip install -e .

RUN pytest tests/test_sensor.py
RUN pytest tests/test_lens.py

CMD echo "Docker image for the tests."
