[![codecov](https://codecov.io/gh/nielsrolf/scheduler/branch/master/graph/badge.svg)](https://codecov.io/gh/nielsrolf/scheduler)
![Test](https://github.com/nielsrolf/scheduler/workflows/Test/badge.svg)

# Scheduler

Write a training loop from logically separated steps!

```
batch = Schedule().first().do(batch_info)
batch.forNext(5).every(1).do(update_g)
batch.then().do(update_d)
training = Schedule()
training.every(1).do(lambda step, scope: batch.withScope(learning_rate=scope.get('learning_rate', 5/(step+5))))
training.every(10).do(save)
training.every(10).do(plot_training)
training.forNext(20)
training.then().do(training.withScope(learning_rate=0.1).forNext(20))
training.execute()
```

## Install
```
pip install git+https://github.com/nielsrolf/scheduler.git
python setup.py install
python setup.py develop
```
