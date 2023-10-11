FROM python:alpine

# Install Poetry
RUN pip install poetry

# Copy the project files into the container
COPY . /app

# Set the working directory to the project directory
WORKDIR /app/CoinSense

# Install the project dependencies
RUN poetry install

# Expose the port for the application to run on
EXPOSE 8000

# Run the command to start the application
CMD ["poetry", "run", "python", "main.py"]