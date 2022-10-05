# Week 5 Submission

Submission for week 5 homework from mlzoomcamp. See instructions [here](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/cohorts/2022/05-deployment/homework.md)


Build the dockerfile

```
docker build -t card-prediction .
```

To run it, execute the command below:

```
docker run -it -p 9696:9696 card-prediction:latest
```

To test the prediction service, execute the command below:

```
python predict_test.py
```
