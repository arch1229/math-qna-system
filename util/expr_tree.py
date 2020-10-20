'''
NOT USING THIS MODULE ANYMORE, WILL BE DELETED SOON
'''

from pythonds.basic import Stack
from pythonds.trees import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal((i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

def traverse_postorder(tree):
    if tree != None:
        traverse_postorder(tree.getLeftChild())
        traverse_postorder(tree.getRightChild())
        print(tree.getRootVal())

input_expr = "( ( x + 5 ) * 3 )"
pt = buildParseTree(input_expr)
traverse_postorder(pt)