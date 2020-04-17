from scheduler import Schedule


def batch_info(step, scope):
    print(f"Learning rate: {scope['learning_rate']}")


def save(step, scope):
    print("Export...")


def update_g(step, scope):
    print("Update G")


def update_d(step, scope):
    print("Update D")


def plot_training(step, scope):
    print("Plot")


batch = Schedule().first().do(batch_info)
batch.forNext(5).every(1).do(update_g)
batch.then().do(update_d)
training = Schedule()
training.every(1).do(
    lambda step, scope: batch.withScope(
        learning_rate=scope.get("learning_rate", 5 / (step + 5))
    )
)
training.every(10).do(save)
training.every(10).do(plot_training)
training.forNext(20)
training.then().do(training.withScope(learning_rate=0.1).forNext(20))
training.execute()
