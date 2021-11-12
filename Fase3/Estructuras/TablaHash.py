from Estructuras.HashNode import Node
import Estructuras.SolovayStrassen as ss

class tablaHash:
    def __init__(self):
        self.table_size=7
        self.hash_list=list()

        for i in range(self.table_size):
            new_node = Node("")
            self.hash_list.append(new_node)

    def get_table(self):
        for i in range(self.table_size):
            print(str(i)+ ") "+str(self.hash_list[i].carnet))

    
    def insert_value(self, carnet, apunte):
        if self.exist(carnet):
            posicion=self.index( carnet)
            self.hash_list[posicion].apuntes.append(apunte)
        else:    
            position=self.get_position_table(int(carnet))
            if self.get_percent_use()<= 0.50:
                if self.hash_list[position].carnet == "":
                    new_node=Node(carnet)
                    new_node.apuntes.append(apunte)
                    self.hash_list[position]=new_node
                elif self.hash_list[position].carnet==carnet:
                    self.hash_list[position].apuntes.append(apunte)
                else:
                    k=0
                    while True:
                        if self.hash_list[position].carnet=="":
                            new_node=Node(carnet)
                            new_node.apuntes.append(apunte)
                            self.hash_list[position]=new_node
                            break
                        if k<self.table_size:
                            k+=1
                            position=(position+int(pow(k,2)))%self.table_size

            else:
                for i in range((self.get_next_prime(self.table_size)-self.table_size)):
                    new_node=Node("")
                    self.hash_list.append(new_node)


                self.table_size = self.get_next_prime(self.table_size)

                if self.hash_list[position].carnet=="":
                    new_node=Node(carnet)
                    new_node.apuntes.append(apunte)
                    self.hash_list[position]=new_node
                elif self.hash_list[position].carnet==carnet:
                    self.hash_list[position].apuntes.append(apunte)
                else:
                    k=0
                    while True:
                        if self.hash_list[position].carnet=="":
                            new_node=Node(carnet)
                            new_node.apuntes.append(apunte)
                            self.hash_list[position]=new_node
                            break
                        if k<self.table_size:
                            k+=1
                            position=(position+int(pow(k,2)))%self.table_size

    def exist(self, carnet):
        for element in self.hash_list:
            if element.carnet == carnet:
                return True
        return False

    def index(self, carnet):
        counter=0
        for element in self.hash_list:
            if element.carnet == carnet:
                return counter
            counter+=1    

        

    def get_position_table(self,carnet):
        return carnet % self.table_size

    def get_next_prime(self, initial_size):
        return ss.next_prime(initial_size)
    
    def get_percent_use(self):
        counter = 0
        for i in range(self.table_size):
            if self.hash_list[i].carnet != "":
                counter +=1
        return counter/self.table_size

    def getApuntes(self, carnet):
        lista=list()
        for element in self.hash_list:
            if element.carnet == str(carnet):
                return element.apuntes
        return lista

    def getApunte(self, carnet, id):

        for element in self.hash_list:
            if element.carnet == str(carnet):
                for apunte in element.apuntes:
                    if apunte.id==id:
                        return apunte
        return None
