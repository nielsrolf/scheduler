class Schedule:
    """Schedule for ordered and reocurring jobs, like training loops

    Arguments:
        scope {Dict} -- Some constants that are available to all functions during
            execution.
    """

    class Scheduler:
        def __init__(self, parent):
            """Helper class to trigger a certain job in the parent schedule.
            Return type of Schedule().first/every/then()
            
            Arguments:
                parent {Schedule} -- The Schedule object on which the job
                will be scheduled
            """
            self.parent = parent

    class FirstScheduler(Scheduler):
        def do(self, job):
            self.parent.schedule_first(job)
            return self.parent

    class RecurrentScheduler(Scheduler):
        def __init__(self, parent, period, first_step):
            self.parent = parent
            self.period = period
            self.first_step = first_step % period

        def do(self, job):
            self.parent.schedule_recurrent(job, self.period, self.first_step)
            return self.parent

    class FinalScheduler(Scheduler):
        def do(self, job):
            self.parent.schedule_final(job)
            return self.parent

    def __init__(self, **scope):
        self.scope = scope
        self._first = []
        self._recurrent = []
        self._final = []
        self._until = []
        self._while = []

    # Methods used by scheduler objects
    def schedule_first(self, job):
        self._first.append(job)

    def schedule_recurrent(self, job, period, first_step):
        self._recurrent.append((first_step, period, job))

    def schedule_final(self, job):
        self._final.append(job)

    # External API
    def first(self):
        return Schedule.FirstScheduler(self)

    def every(self, period, first_step=-1):
        """Schedule a recurrent jop
        
        Arguments:
            period {int}
        
        Keyword Arguments:
            first_step {int} -- When the first step should happen,
                egative values are counted from the end of the first period
                (default: {-1})
        
        Returns:
            Schedule.Scheduler
        """
        return Schedule.RecurrentScheduler(self, period, first_step)

    def then(self):
        return Schedule.FinalScheduler(self)

    def until(self, condition):
        self._until.append(condition)
        return self

    def whileTrue(self, condition):
        self._while.append(condition)
        return self

    def forNext(self, steps):
        self._while.append(lambda step, scope: step < steps)
        return self

    def withScope(self, **scope):
        merged = dict(**self.scope)
        merged.update(scope)
        schedule = Schedule(**merged)
        schedule._first = list(self._first)
        schedule._recurrent = list(self._recurrent)
        schedule._final = list(self._final)
        schedule._while = list(self._while)
        schedule._until = list(self._until)
        return schedule

    # Run time methods
    def should_continue(self, step):
        for condition in self._while:
            if not condition(step, self.scope):
                return False

        for condition in self._until:
            if condition(step, self.scope):
                return False

        return len(self._recurrent) > 0

    def execute_job(self, job, step, scope):
        maybe_subschedule = job(step, self.scope)
        if isinstance(maybe_subschedule, Schedule):
            maybe_subschedule.execute()

    def execute(self):
        step = 0
        for job in self._first:
            self.execute_job(job, step, self.scope)

        while self.should_continue(step):
            for first_step, period, job in self._recurrent:
                if (step - first_step) % period == 0:
                    self.execute_job(job, step, self.scope)
            step += 1

        for job in self._final:
            self.execute_job(job, step, self.scope)

    def __call__(self, step, scope):
        self.execute()
