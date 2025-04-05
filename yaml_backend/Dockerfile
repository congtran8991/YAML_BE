# Stage 1: Build stage
FROM python:3.10-alpine as builder

# Set the working directory
WORKDIR /yaml_backend/backend

# Copy only the requirements.txt file to install dependencies
COPY ./backend/requirements.txt .

# Install dependencies and save into /install
RUN pip install --prefix=/install -r requirements.txt

# Stage 2: Final stage
FROM python:3.10-alpine

# Set the working directory
WORKDIR /yaml_backend/backend

# Copy the application to the final image
COPY ./backend .

RUN chmod +x load_backend.sh

# Copy dependencies from build stage
COPY --from=builder /install /usr/local

# Expose the port your app will run on (default for Uvicorn is 8000)
EXPOSE 8000

# Run the app through load_backend.sh
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
CMD ["/bin/sh", "load_backend.sh"]

