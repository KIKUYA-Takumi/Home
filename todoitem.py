from datetime import datetime, timedelta


class ToDoItem(object):
    #ToDo項目を保存するためのクラス

    def __init__(self,title,description,duedate,addeddate=None):
        #ToDo項目インスタンスを初期化する

    if not addeddate:
        addeddate = datetime.now()
        self.title = title
        self.description = description
        self.duedate = duedate
        self.addeddate = addeddate
        self.finished = False
        self.finisheddata = None