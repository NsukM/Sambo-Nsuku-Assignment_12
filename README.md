# Assignment 12 – Service Layer & API for Fitness Tracker

This repository contains the implementation of a full *Service Layer* and *RESTful API* for the Fitness Tracker project using *FastAPI*. This includes business logic services, API endpoints, Swagger documentation, and test coverage.

---

## ✅ Architecture Overview

- services/: Business logic services interacting with repositories
- api/: RESTful API layer using FastAPI
- main.py: FastAPI entry point
- tests/: Unit and integration tests
- docs/: Swagger screenshot and OpenAPI file

---

## ✅ How to Run the API

bash
pip install fastapi uvicorn
uvicorn main:app --reload

Visit Swagger UI at:
http://localhost:8000/docs

⸻

✅ Endpoints Summary

User Endpoints
	•	GET /api/users
	•	POST /api/users
	•	GET /api/users/{user_id}
	•	PUT /api/users/{user_id}
	•	DELETE /api/users/{user_id}

Fitness Profile Endpoints
	•	GET /api/profiles
	•	POST /api/profiles
	•	GET /api/profiles/{age}
	•	DELETE /api/profiles/{age}

Analytics
	•	GET /api/reports/summary

⸻

✅ Running Tests

pip install pytest
pytest tests/



⸻


✅ Swagger Documentation

Due to using GitHub's browser-based environment (without a local Python runtime),
FastAPI's Swagger UI (http://localhost:8000/docs) could not be launched.

However, the main.py file correctly includes all routers from:
- /api/user_api.py
- /api/fitness_profile_api.py
- /api/analytics_api.py

Swagger would auto-generate documentation for these endpoints if run in a local FastAPI environment.

Refer to main.py and README.md for a full breakdown of available routes.
⸻

## ✅ CI/CD Pipeline – Assignment 13

### Continuous Integration (CI)
- Triggered on every *push* or *pull request* to main
- Runs pytest tests in /tests/
- Fails the PR if tests fail

### Continuous Delivery (CD)
- On successful merge to main, GitHub automatically:
  - Zips the project into fitness-tracker.zip
  - Uploads it under "Artifacts" in the GitHub Actions tab

### Branch Protection Rules
- Pull request reviews are required
- CI status checks must pass
- Direct pushes to main are blocked
- All rules are described in PROTECTION.md

### Run tests locally
bash
pip install pytest
pytest tests/



✅ Author
	•	Name: Nsuku Sambo
	•	Student Number: 221358986
	•	Module: Software Engineering

---
