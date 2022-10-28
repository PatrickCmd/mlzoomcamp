setup:
	pipenv install
	pipenv install --dev

quality_checks:
	isort .
	black .

train_save_model:
	python train.py

bento_build:
	bentoml build

serve:
	bentoml serve smoke_detection:latest --production

containerize:
	bentoml containerize smoke_detection:latest

test:
	python detection_test.py