from scheduler import Schedule


line = (
    Schedule(length=10)
    .every(1)
    .do(lambda step, scope: print(".", end=""))
    .whileTrue(lambda step, scope: step < scope["length"])
)
line.then().do(lambda step, scope: print())
line.withScope(length=10).execute()
triangle = Schedule().every(1).do(lambda step, scope: line.withScope(length=step))
triangle.first().do(line)
triangle.forNext(20).execute()
triangle.then().do(line)
Schedule(h=10).every(1).do(line).until(lambda step, scope: step == scope["h"]).execute()
