# Official Python runtime as parent image
FROM python:3.9-slim

# Set container working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

# Define entrypoint and default command
ENTRYPOINT ["python", "app.py"]
CMD ["data/input.mdf"]
