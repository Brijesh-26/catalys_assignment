# Python image from the Docker Hub
FROM python:3.9-slim

# Setting the working directory in the container
WORKDIR /app

# Copying the requirements file into the container at /app
COPY requirements.txt ./

# Installing any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying the rest of the application code into the container
COPY . .

# Specifying the command to run on container start
CMD ["python", "app.py"]

# Expose port 5000 to the outside world
EXPOSE 5000
