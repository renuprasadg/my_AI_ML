# Use the official lightweight Python image.
FROM python:3.9-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the requirements and others files file into the container.
COPY requirements.txt .
COPY main.py
COPY iris_model.pkl

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Render will use.
EXPOSE 8000

# Command to run the application.
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
