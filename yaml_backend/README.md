# yaml_backend


<!-- *STEPS TO RUN the BE application
- Create virtual environment (python -m venvn "backend_venv" )
- Turn on venv =>  run "pip install -r requirement.txt"
- RUN BE server:
  + dev mode : uvicorn backend.main:app --reload
  + production mode: ... -->

*Using Scripts to deploy system
- command: ./deploy.sh

*Migration commands 
-Create: docker exec -it yaml_backend alembic revision --autogenerate -m "your_message"
-Apply migration to database: docker exec -it yaml_backend alembic upgrade head
-Revert migration 1 step: docker exec -it yaml_backend alembic downgrade -1