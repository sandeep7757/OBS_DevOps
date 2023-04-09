# Use an official Python runtime as a parent image
FROM python:3.9
ENV DJANGO_SUPERUSER_PASSWORD=sandeep

# Set the working directory to /app
WORKDIR /app

# install the SQL DB
RUN apt-get update && \
    apt-get install -y sqlite3 libsqlite3-dev

# Copy the application files into the container
COPY . .

# Set the default command to run the Python application
CMD ["python", "app.py"]

# Create a virtual environment and activate it
RUN python3 -m venv venv
RUN . venv/bin/activate

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r OBS_DevOps/requirements.txt

#create the Django superuser
RUN python3 manage.py createsuperuser --noinput \
    --email=admin@admin.com

# Run the Django development server
CMD python3 manage.py runserver 0:8000
