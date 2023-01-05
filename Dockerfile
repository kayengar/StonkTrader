FROM python:3.9

# Copy the code into the container
COPY . /app

# Set the working directory to the app directory
WORKDIR /app

# Install the required packages
RUN pip install -r requirements.txt

# Run the main function when the container starts
ENTRYPOINT ["python", "main.py"]
