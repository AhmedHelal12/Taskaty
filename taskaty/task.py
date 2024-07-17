

class Task:
    def __init__(self,title,description,start_date,end_date,done):
        self.title=title
        self.description=description
        self.start_date=start_date
        self.end_date=end_date
        self.done=done

    def __str__(self):
        return f'{self.title}, {self.description}, {self.start_date}, {self.end_date}, {self.done}'
        
        