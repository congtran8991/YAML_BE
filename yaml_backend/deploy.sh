#!/bin/bash
echo "Starting Docker Compose deployment..."

images_list=("coffee_web_backend:latest")

# Stop and delete old containers and images
echo "Stop and delete old containers and images"
docker-compose down
docker rmi ${images_list}

# Build and up all containers
echo "Build and up all containers"
docker-compose up yaml_sql_db -d 
sleep 3
docker-compose up yaml_backend -d 

#Migrate the database
echo "Apply migrations to database"
docker exec -it yaml_backend alembic upgrade head

echo "Deployment successfully"
