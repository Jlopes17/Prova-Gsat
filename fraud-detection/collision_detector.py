#!/usr/bin/python
import sys #provides information about constants, functions and methods of the python interpreter
networks = [] #networks refers to an empty list

class Node(object): #linked list, recursive data structure, Node class

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def find(self, data):
        node = self
        while node:
            if node.get_data()==data:
                return node
            node = node.get_next()
        return None

    def merge(self, list):
        node = self
        while node.get_next():
            node = node.get_next()
        node.set_next(list)

def check_nodes(a,b): #check if two nodes belong to the same collision network
    for network in networks:
        if (str(a) in network and str(b) in network):
            return True
    return False

def print_networks(): #print networks
    for network in networks:
        node = network
        while node:
            sys.stdout.write(str(node.get_data())+', ')
            node = node.get_next()
        print

def add_nodes(a, b): #add new nodes / add new collision between two nodes
    found1 = 0
    found2 = 0
    length = len(networks)
    i = 0
    while(i < length and not found1):
        node1  = networks[i].find(a)
        i+=1
        if node1:
            found1 = 1
            while(i < length and not found2):
                node2 = networks[i].find(b)
                if node2:
                    node1.merge(node2)
                    del networks[i]
                    found2 = 1
                    break
                i+=1
            if not found2:
                node1.merge(Node(b))
    if not found1:
        networks.append(Node(a, Node(b)))

with open("examples", "r+") as f: #open file "examples" with permissions
    pairs = [[int(n) for n in line.split()] for line in f.readlines()]
for pair in pairs:
    add_nodes(pair[0],pair[1])
