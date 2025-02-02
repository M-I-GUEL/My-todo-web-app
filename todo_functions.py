def get_todo(filepath='todos.txt'):
    '''Reads the file and returns a list
    of todos
    '''
    with open(filepath,'r') as file:
        todos= file.readlines()
        return todos
def write_todo(todos,filepath='todos.txt'):
    '''Writes the list of todos into
    a file
    '''
    with open(filepath,'w') as file:
        todos= file.writelines(todos)
if __name__== 'main':

  print('Just testing')