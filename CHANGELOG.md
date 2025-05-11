# CHANGELOG – Assignment 12 & 13

## [v3.0.0] – Assignment 13: CI/CD and Branch Protection

### Added
- .github/workflows/ci.yml for CI/CD pipeline
- Automatic test runs using pytest on push and pull requests
- Artifact generation (fitness-tracker.zip) on successful merge to main
- Branch protection policy documented in PROTECTION.md
- README.md updated with CI/CD and protection rules

---

## [v2.0.0] – Assignment 12: Full Service Layer & REST API

### Added
- services/ layer: user, profile, analytics
- api/ endpoints for all services (FastAPI)
- main.py application entry
- tests/services/ unit tests
- tests/api/ integration tests
- Swagger auto-generated at /docs
- README.md with usage instructions

### Future Enhancements
- Token-based authentication
- Deployment on AWS (Lambda, API Gateway)
