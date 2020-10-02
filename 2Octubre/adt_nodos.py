class Nodo:
    def __init__( self ,value, siguiente=None):
        self.data = value
        self.next = siguiente

class nodoDoble:
    def __init__ (self,value,siguiente=None,previo=None):
        self.data = value
        self.next = siguiente
        self.prev = previo

class ListaEnlazada:
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def get_tail(self):
        nodo_actual = self.__head
        #verificar que la lista no este vacia 
        while nodo_actual.next != None:
            nodo_actual = nodo_actual.next
        return nodo_actual
    
    def append(self, value):
        if self.is_empty():
            self.__head = Nodo(value)
        else:
            self.get_tail().next = Nodo(value)

    def prepend(self, value):
        if self.is_empty():
            self.__head = Nodo(value)
        else:
            self.__head = Nodo(value, self.__head)

    
    def add_after(self, reference_value, value):
        nodo_actual = self.__head
        while nodo_actual.data != reference_value:
            nodo_actual = nodo_actual.next
            if nodo_actual == None:
                return False
        #print(nodo_actual.data)
        nodo_actual.next = Nodo(value, nodo_actual.next)
        #nuevo = nodo_actual.next = Nodo(value, nodo_actual.next)
        
        
    def add_before(self, reference_value, value):
        nodo_actual = self.__head
        while nodo_actual.data != reference_value:
            nodo_prev= nodo_actual
            nodo_actual = nodo_actual.next
            if nodo_actual == None:
                return False
        nodo_prev.next = Nodo(value, nodo_actual)
        nodo_actual=None
        

    
    def transversal(self):
        nodo_actual = self.__head
        while nodo_actual.next:
            print(f"{nodo_actual.data} -->",end="")
            nodo_actual= nodo_actual.next
        print(nodo_actual.data)

    def remove(self, value):
        #values esta en head??
        nodo_actual = self.__head
        previo = nodo_actual
        while nodo_actual.data != value or nodo_actual.next == None:
            previo = nodo_actual
            #print(previo.data)
            nodo_actual = nodo_actual.next
        if nodo_actual.data == value:
            previo.next = nodo_actual.next
            nodo_actual=None
            return True
        elif nodo_actual.data == None:
            return False
            
    def pop(self):
        nodo_pop = self.__head
        previo = nodo_pop
        while nodo_pop.next != None:
            previo = nodo_pop
            nodo_pop = nodo_pop.next
        value = nodo_pop.data
        previo.next = nodo_pop.next
        nodo_pop=None
        return value

    def to_string(self, value):
        nodo_actual = self.__head
        for x in range(1, value+1, 1):
            nodoF = nodo_actual
            nodo_actual = nodo_actual.next
            if x == value:
                return nodoF
    
'''
Listas doblemente enlazadas
nov 7
'''
class ListaDobleEnlazada:
    def __init__(self):
        self.__head= None
        self.__tail= None
        
    def is_empty(self):
        return self.__head==None
    
    def append(self, value):
        #vacia?
        if self.is_empty():
            self.__head = nodoDoble(value)
            self.__tail = self.__head
        else:#no vacia?
            nuevo = nodoDoble(value)
            self.__tail.next=nuevo
            nuevo.prev = self.__tail
            self.__tail = nuevo
            '''
            self.__tail.next = NodoDoble(value,Nodo,self.__tail)
            self.__tail = self.tail.next
            '''
    def transversal(self):
        nodo_actual = self.__head
        while nodo_actual.next != None:
            print(f"{nodo_actual.data} -->",end="")
            nodo_actual= nodo_actual.next
        print(nodo_actual.data)
        
    def reverse_transversal( self ):
        nodo_actual = self.__tail
        while nodo_actual.prev != None:
            print(f"{nodo_actual.data} -->",end="")
            nodo_actual= nodo_actual.prev
        print(nodo_actual.data)
    
    def get_size(self):
        nodo_actual = self.__head
        contador = 1
        while nodo_actual.next != None:
            nodo_actual=nodo_actual.next
            contador += 1
        return contador
    
    def find_from_head( self, value):
        nodo_actual = self.__head
        
        while nodo_actual.data != value:
            if nodo_actual.next == None:
                return None
            nodo_actual = nodo_actual.next
            
        return nodo_actual
    def insert_from_head( self, reference_value, value):
        nodo = self.find_from_head(reference_value)
        print(nodo.data)
        if nodo != None:
            nuevo = nodoDoble(value, nodo.next, nodo)
            nodo.next = nuevo
            print(nodo.next.data)
            print(nuevo.data)
            print(nuevo.next.prev.data)
            nuevo.next.prev = nuevo
            print(nuevo.next.prev.data)
            
        
        
        
        
