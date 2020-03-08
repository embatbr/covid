# covid


## Installing

### Spark

- Go to [Spark page](https://spark.apache.org/) and follow the installation instructions;
- Create a link to Spark's directory named **spark** (mine is at "\~/apps/spark");

### API

- Create a python virtual environment (suggestion: use virtualenvwrapper);
- Install [Falcon API](https://falcon.readthedocs.io/en/stable/).


## Executing

### Spark

Spark can be executed alone (decouped from any API) by running the bash script *run.sh* in the spark directory. This script receives a parameter to identify the job and another to choose the question (an integer between 1 and 5). For example, to execute question 4 (executed from the project's root directory):

```bash
$ ./spark/run.sh <JOB_ID> 4
```

### API

Run the basch script in directory *api*:

```bash
$ ./api/run.sh
```
