[![codecov](https://codecov.io/gh/nielsrolf/scheduler/branch/master/graph/badge.svg)](https://codecov.io/gh/nielsrolf/scheduler)
![Test](https://github.com/nielsrolf/scheduler/workflows/Test/badge.svg)
![Lint](https://github.com/nielsrolf/scheduler/workflows/Lint/badge.svg)

# Scheduler

Write a training loop from logically separated steps!

```Python
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

Or finally be able to solve the fizzbuzz challenge:
```Python
Schedule().every(3).do(
    lambda i, d: print('Fizz', end='')
).every(5).do(
    lambda i, d: print("Buzz", end='')
).every(1).do(
    lambda i, d: print(i+1, end='') if ((i+1)%3)*((i+1)%5) != 0 else None
).every(1).do(
    lambda i, d: print()
).forNext(100).execute()
```

## Install
```
pip install git+https://github.com/nielsrolf/scheduler.git
python setup.py install
python setup.py develop
```
