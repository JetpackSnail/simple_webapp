##  Containers for Deployment and Scaling Pre-Course Assignment

### How to run locally

1) Install prequisites in virtual environment

```
virtualenv .env/workshop01
source .env/workshop01/bin/activate
pip3 install -r requirements.txt
```

2) Launch flask app

```
flask --app application.py run
```

### Deploying to AWS EBS

Useful links
- [Elastic Beanstalk CLI setup](https://github.com/aws/aws-elastic-beanstalk-cli-setup)
- [Deploying Flask app to AWS EBS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)