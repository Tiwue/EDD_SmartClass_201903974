from Estructuras.NodoMes import NodoMes


class ListaMeses:
    def __init__(self):
        self.Primero = None
        self.Ultimo = None

    def getSize(self):
        aux = self.Primero
        contador = 0
        while aux is not None:
            contador += 1
            aux = aux.next

        return contador

    def isEmpty(self):
        return self.Primero is None

    def getList(self):
        aux = self.Primero
        while aux is not None:
            print(aux.año)
            aux = aux.next

    def add(self, mes,hora, dia, tarea):
        if self.exist(mes):
            aux = self.Primero
            while aux is not None:
                if aux.mes == mes:
                    aux.tareas.add(hora, dia,tarea)
                aux = aux.next
        else:    
            nuevo = NodoMes(mes)
            nuevo.tareas.add(hora,dia,tarea)
            if self.isEmpty():
                self.Ultimo = nuevo
                self.Primero = self.Ultimo
            else:
                self.Ultimo.next = nuevo
                nuevo.Previous = self.Ultimo
                self.Ultimo = nuevo

    def exist(self,mes):
        aux = self.Primero
        while aux is not None:
            if aux.mes == mes:
                return True
            aux = aux.next
        return False

    def graficarMatriz(self, mes):
        if self.exist(mes):
            aux = self.Primero
            while aux is not None:
                if aux.mes == mes:
                    return aux.tareas.graficar(mes)
                aux = aux.next
        else:    
            return "No hay recordatorios para el mes solicitado"

    def graficarLista(self, mes,dia,hora):
        if self.exist(mes):
            aux = self.Primero
            while aux is not None:
                if aux.mes == mes:
                    return aux.tareas.graficarLista(mes, dia,hora)
                aux = aux.next
        else:    
            return "No hay recordatorios para el mes solicitado"        