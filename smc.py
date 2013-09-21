import ast
from astmonkey import transformers
import sys
import json

class treeGen(ast.NodeVisitor):
    fxns = {}
    def generic_visit(self, node):
#print type(node).__name__
        ast.NodeVisitor.generic_visit(self, node)
    def visit_FunctionDef(self, node):
	if not self.fxns.has_key(node.name):
	    self.fxns[node.name] = {}
#print "Functions are awesome"
#print node.name
#self.getFxnCalls(node)
	ast.NodeVisitor.generic_visit(self, node)
#    def visit_Module(self, node):
#print "Modules"
#	for i in ast.iter_child_nodes(node):
#print type(i)
#	ast.NodeVisitor.generic_visit(self, node)
    def visit_arguments(self, node):
	theseArgs = node.args
	while(node and type(node) != ast.FunctionDef):
	    node = node.parent
	if(type(node) == ast.FunctionDef):
	    if(not self.fxns[node.name].has_key('args')):
		self.fxns[node.name]['args'] = []
	    for i in theseArgs:
	        self.fxns[node.name]['args'].append(i.id)

    def visit_Call(self, node):
	if('id' in node.func._fields):
	    callId = node.func.id
#	    print "Called ", callId
#    print self.fxns.has_key(callId)
	    if not self.fxns.has_key(callId):
		self.fxns[callId] = {}
	    while(node and type(node) != ast.FunctionDef):
#		print type(node)
		node = node.parent
#	    print "Finished loop"
#	    print type(node)
	    if(type(node) == ast.FunctionDef):
		if not self.fxns[node.name].has_key('calls'):
		    self.fxns[node.name]['calls'] = []
		self.fxns[node.name]['calls'].append(callId)

    #get all functions calls within a functionDef
#    def getFxnCalls(self, node):
#	print "Fxn Calls for ", node.name
#	for i in ast.iter_child_nodes(node):
#	    print type(i)

def visitNode(node):
    for i in ast.iter_child_nodes(node):
        if(type(i) == ast.FunctionDef):
            print "Function: ", i.name
        elif(type(i) == ast.ClassDef):
            print "Class"
        elif(type(i) == ast.Module):
            print "Module"
        elif(type(i) == ast.Expr):
            print "Expression"
        elif(type(i) == ast.Name):
            print "Name", i.id
        visitNode(i)
    for i in ast.iter_fields(node):
        print "Field"
        print i

def getD3Data(fxnArr):
    data = []
    links = []
    curId = 0
    for fxn in fxnArr:
        if(fxnArr[fxn].has_key('args')):
	    thisArgs = fxnArr[fxn]['args']
	else:
	    thisArgs = []
	if(fxnArr[fxn].has_key('calls')):
	    thisCalls = fxnArr[fxn]['calls']
	else:
	    thisCalls = []
        newObj = {
	    'name': fxn,
	    'args': thisArgs,
	    'calls': thisCalls,
	    'id': curId, 
	}
        fxnArr[fxn]['id'] = curId
        curId += 1
        data.append(newObj)

# now have id for each fxn, and can create links
    for i in data:
        for c in i['calls']:
	    newLink = {
		'source': i['id'],
		'target': fxnArr[c]['id'],
		'value': 5,
	    }
            links.append(newLink)
    d3Data = {
	'nodes': data,
	'links': links,
    }
    return d3Data


def getStructure():
    if(len(sys.argv) != 2):
        print "Need a filename\n"
        exit()

    fileName = sys.argv[1]
    f = open(fileName, 'r')
    codeBase = f.read()
    codeAst = transformers.ParentNodeTransformer().visit(ast.parse(codeBase))

    #print(ast.dump(codeAst))
    tg = treeGen()
    tg.visit(codeAst)
    return getD3Data(tg.fxns)
    #visitNode(codeAst)
