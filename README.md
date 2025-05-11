Here is the final cleaned-up version of your README.md for Assignment 12 and 13 — ready to copy and paste into your GitHub repo:

⸻


# Assignment 12 & 13 – Service Layer, API, and CI/CD for Fitness Tracker

This repository contains the complete implementation of the Fitness Tracker system, including:

- Assignment 12: Service Layer & RESTful API using FastAPI
- Assignment 13: CI/CD pipeline using GitHub Actions with branch protection and automated testing

---

## ✅ Architecture Overview

- `services/` – Business logic services interacting with repositories
- `api/` – RESTful API layer using FastAPI
- `main.py` – FastAPI entry point
- `tests/` – Unit and integration tests using `pytest`
- `docs/` – Swagger UI note and OpenAPI placeholder
- `.github/workflows/` – CI/CD GitHub Actions workflow

---

## ✅ How to Run the API

```bash
pip install fastapi uvicorn
uvicorn main:app --reload

Visit Swagger UI:
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

✅ Running Tests Locally

pip install pytest
pytest tests/


⸻

✅ Swagger Documentation

Due to using GitHub’s browser-based environment (without a local Python runtime),
FastAPI’s Swagger UI (http://localhost:8000/docs) could not be launched.

However, the main.py file correctly includes all routers from:
	•	/api/user_api.py
	•	/api/fitness_profile_api.py
	•	/api/analytics_api.py

Swagger would auto-generate documentation for these endpoints if run in a local FastAPI environment.

⸻

✅ CI/CD Pipeline – Assignment 13

Continuous Integration (CI)
	•	Triggered on every push or pull request to main
	•	Runs pytest tests in /tests/
	•	Fails the PR if tests fail

Continuous Delivery (CD)
	•	On successful merge to main, GitHub automatically:
	•	Zips the project into fitness-tracker.zip
	•	Uploads it under “Artifacts” in the GitHub Actions tab

Branch Protection Rules
	•	Pull request reviews are required
	•	CI status checks must pass
	•	Direct pushes to main are blocked
	•	All rules are described in PROTECTION.md

⸻

✅ Author
	•	Name: Nsuku Sambo
	•	Student Number: 221358986
	•	Module: Software Engineering
