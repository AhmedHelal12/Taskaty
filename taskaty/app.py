
from argparse import ArgumentParser
from taskaty.taskController import TaskController

def main():
    controller=TaskController('task.txt')
    
    parser=ArgumentParser('Simple CLI Application')

    subparsers=parser.add_subparsers()


    add_task=subparsers.add_parser('add',help='Add a task')
    add_task.add_argument('title',metavar='',help='title of the task',default=None)
    add_task.add_argument('-d','--description',metavar='',help='description of the task',default=None)
    add_task.add_argument('-s','--start_date',metavar='',help='the start date of the task',default=None)
    add_task.add_argument('-e','--end_date',metavar='',help='the end date of the task')
    add_task.add_argument('--done',metavar='',help='check the task done or not',default=False)
    add_task.set_defaults(func=controller.add_task)

    check_task=subparsers.add_parser('check',help='Check the given task')
    check_task.add_argument('-t','--task',type=int)
    check_task.set_defaults(func=controller.check_task)

    list_tasks=subparsers.add_parser('list',help='list all the unfinished tasks')
    list_tasks.add_argument('-a','--all',help='list all the tasks',action='store_true')
    list_tasks.set_defaults(func=controller.display)

    remove_task=subparsers.add_parser('remove',help='remove a task')
    remove_task.add_argument('-t','--task',help='remove the given task(number)',type=int)
    remove_task.set_defaults(func=controller.remove_task)

    reset=subparsers.add_parser('reset',help='remove a task')
    reset.set_defaults(func=controller.reset)

    args=parser.parse_args()
    args.func(args)
if __name__=='__main__':
    main()
