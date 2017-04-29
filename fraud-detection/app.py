#!fraud/bin/python
from flask import Flask, jsonify
from collision_detector import add_nodes, print_networks
from flask import request
import ast
app = Flask(__name__)



@app.route('/fraud/api/v1.0/add_collision', methods=['POST'])
def add_collision():

    data = jsonify(request.data)
    data = ast.literal_eval(request.data)
    
    lst_nodes = []
   

    for i in data:
        lst_nodes.append(i.get('nodes'))
    #print lst_nodes
    
    for i in lst_nodes:
        add_nodes(i[0],i[1])
    
    print_networks()
    return "nodes added successfully."



if __name__ == '__main__':
    app.run(debug=True)