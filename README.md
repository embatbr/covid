# covid


## Installing

### Spark

- Go to [Spark page](https://spark.apache.org/) and follow the installation instructions;
- Create a link to Spark's directory named **spark** (mine is at "\~/apps/spark");


## Executing

### Spark

Spark can be executed alone (decouped from any API) by running the bash script *run.sh* in the spark directory. This script receives a parameter to choose the question (an integer between 1 and 5). For example, to execute question 4 (executed from the project's root directory):

```bash
$ ./spark/run.sh 4
```
