
class task:
    def __init__(self, taskName, taskDesc, isComplete):
        self.taskName = taskName
        self.taskDesc = taskDesc
        self.isComplete = isComplete
    
    def displayTask(self):
            print(f'''{self.taskName}:
Description: {self.taskDesc}
Complete: {self.isComplete}''')

    def markComplete(self):
        if self.isComplete == False:
            self.isComplete = True 
        else:
            print('Task already completed!')    


class dueDateTask(task):
    def __init__(self, taskName, taskDesc, isComplete, dueDate):
        super().__init__(taskName, taskDesc, isComplete)
        self.dueDate = dueDate

    def displayTask(self):
        if self.dueDate != None:
            print(f'''{self.taskName}:
Description: {self.taskDesc}
Due Date: {self.dueDate}
Complete: {self.isComplete}''')

    def markComplete(self):
        if self.isComplete == False:
            self.isComplete = True 
        else:
            print('Task already completed!')    

    

t1 = task('Homework', 'do my homework', '10.02.2022', False)
t1.displayTask()