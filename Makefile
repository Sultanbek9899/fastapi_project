

.PHONY: run
run:
	@echo "Running server..."
	uvicorn main:app --host 0.0.0.0 --port 8005