# use the official python image
FROM python:3.11-slim

WORKDIR /app

# copy the requirement file to the working directory
COPY requirements.txt .

# Install the python dependencies
RUN pip install -r requirements.txt

# copy the application code to the working directory
COPY . .

# Expose the port on which application will run
EXPOSE 8080

# Run the application using uvicorn server
CMD ["fastapi", "dev", "main.py"]