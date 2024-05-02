FROM python:3.10-slim

RUN pip install dagster dagster-pipes

COPY config/requirements.txt .
RUN pip install -r requirements.txt

COPY src/my_python_script.py .
ENTRYPOINT [ "python", "my_python_script.py" ]
