.PHONY: run install dev test lint format clean

# Run application in development mode
run:
	uvicorn payments_api.main:app --app-dir src --reload

# Install project dependencies
install:
	pip install -e .

# Install development dependencies
dev:
	pip install -e ".[dev]"

# Run tests
test:
	pytest -v

# Lint code with ruff
lint:
	ruff check src

# Format code
format:
	ruff format src

# Clean cache and build artifacts
clean:
	rm -rf .pytest_cache .ruff_cache dist build *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
