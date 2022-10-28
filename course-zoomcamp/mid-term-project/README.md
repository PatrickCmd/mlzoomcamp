# MID TERM PROJECT (Smoke Detection Dataset)

This is mid term project for the [MLZoomCamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) course here sponsored by [DataTalks.Club](https://datatalks.club/)


## Dataset
The chosen dataset for this project is the Smoke Detection Dataset from [Kaggle](https://www.kaggle.com/datasets/deepcontractor/smoke-detection-dataset)


## Project Setup
clone the project from the repository
```
git clone https://github.com/PatrickCmd/mlzoomcamp.git
```

Change to project directory
```
cd mlzoomcamp/course-zoomcamp/mid-term-project
```

Setup and install project dependencies (uses pipenv for virtual environment)
```
make setup
```

Train and save the model. Uses [BentoML](https://docs.bentoml.org/en/latest/tutorial.html)
```
make train_save_model
```

Build a Bento
```
make bento_build
```

Create a detection web service locally
```
make serve
```

Or if you have [docker](https://www.docker.com/products/docker-desktop/) installed and setup on your machine, you can run the containerized service
```
make containerize
```

And then run the docker image from the above command
```
docker run -it --rm -p 3000:3000 smoke_detection:model-tag serve --production
```

Make sure to replace the `model-tag` with the tag from the containerize command

![screenshot 1](images/Screenshot-03.png)

## Test the model service

Test the detection service locally in new terminal tab or window by running the test script below
```
make test
```

Or browse to http://localhost:3000/ in your web browser and test our the service with the `detect` endpoint

![screenshot 1](images/Screenshot-01.png)

![screenshot 1](images/Screenshot-02.png)


