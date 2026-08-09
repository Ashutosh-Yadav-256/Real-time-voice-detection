.PHONY: install train eval export upload clean

install:
	pip install -r requirements.txt

train:
	python -m src.training.trainer

eval:
	python -m src.evaluation.evaluator

export:
	python scripts/export_model.py --model_path weights.pt --output_path model.onnx

upload:
	python scripts/upload_model.py --file_path model.onnx --bucket models-bucket --model_name vad --version v1

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
