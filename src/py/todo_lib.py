import json

class Todo():
    """
    Este Modulo possue divertas ferramentas nescessarias para manipulacao de uma Lista de Tarefas.
    """
    def __init__(self, name:str):
        self.name = name
        self._todo_list = []
        self._todo_list_trash = []
        #cada tarefa deve ter a estrutura do dicionario a seguir: {'id':0,'task':'tarefa','visible':True}
        self.load_file()

    def add(self, task:str)-> None : #ok
        """
        Adiciona uma tarefa a lista
        task:str - 'Uma tarefa adicionada!'
        """
        self._todo_list.append({'id':len(self._todo_list) ,
                                'task':task,
                                'visible': True})

    def remove_by_id(self,*args):#ok
        """
        Remove por ID a tarefa indicada.
        """
        for id in args:
            if  id <= len(self._todo_list) and  isinstance(id, int):##isinstance(id, int) é necessario para que o codigo n rode com float ou strs
                if not id in self._todo_list_trash:
                    self._todo_list_trash.append(id)
                for item in self._todo_list:
                    if item['id'] == id:
                        item['visible'] = False
    
    def remove_last(self): #nao funciona, poe ele tem de remover o ultimo visivel e nao somente o ultimo adicionado
        last_id = len(self._todo_list) - 1
        if last_id >= 0:
            self._todo_list_trash.append(last_id)
            self._todo_list[last_id]['visible']=False

            
    def recovery_by_id(self,*args):#ok
        """
        Recupera por ID a tarefa oculta (apagada).
        """
        for id in args:
            if  id <= len(self._todo_list) and isinstance(id, int) and id in self._todo_list_trash:##isinstance(id, int) é necessario para que o codigo n rode com float ou strs
                self._todo_list_trash.remove(id)
                for item in self._todo_list:
                    if item['id'] == id:
                        item['visible'] = True
    
    def recovery_last(self): #ok
        """
        Recupera a ultima tarefa oculta (apagada).
        """
        last_id = self._todo_list_trash[-1:][0]
        if last_id >= 0:
            self._todo_list_trash.remove(last_id)
            self._todo_list[last_id]['visible']=True
    
    def recovery_all(self):#ok
        """
        Recupera todos os item apagados, exceto os que foram apagados em definitivo.
        """
        self._todo_list_trash = []
        for item in self._todo_list:
            item['visible']=True 

    def remove_all(self) -> None:
        self._todo_list_trash = []
        for item in self._todo_list:
            item['visible']=False 


    def clear_trash(self):
        """
        Essa acao é permanente.
        Exclui definitivamente todos os arquivos apagados
        """
        itens_to_erase = self._todo_list_trash
        itens_to_erase.sort()
        itens_to_erase.reverse()
        for index in itens_to_erase:
            value_to_erase = self._todo_list[index]
            self._todo_list.remove(value_to_erase)
        self._todo_list_trash = []



    def list_all(self,all:bool=False) -> list:#ok
        """
        Lista todas as tarefas visiveis por padrao. 
        Se all==True,lista todas
        """
        lista_tarefas = []
        if not all :
            for tarefa in self._todo_list:
                if tarefa['visible']:
                    lista_tarefas.append({'id':tarefa['id'] ,
                                        'task':tarefa['task'],
                                        })
            return lista_tarefas

        return self._todo_list


    def save_file(self):
        with open(self.name + '.json','w') as f:
            todo_lists = {'todo_list' : self._todo_list, 'todo_list_trash_index' : self._todo_list_trash}
            json.dump(todo_lists,f)
            


    def load_file(self):
        try:
            with open(self.name + '.json','r') as f:
                data = json.load(f)
                self._todo_list = data['todo_list']
                self._todo_list_trash = data['todo_list_trash_index']
        except:
            pass
            

if __name__ == '__main__':
   ...