# In tree.py

class Tree:
    def __init__(self, root):
        self.root = root

    # Depth-first traversal approach
    def get_element_by_id_depth_first(self, id_value):
        return self._depth_first_search(self.root, id_value)

    def _depth_first_search(self, node, id_value):
        if node is None:
            return None
        if node['id'] == id_value:
            return node
        for child in node['children']:
            result = self._depth_first_search(child, id_value)
            if result:
                return result
        return None

    # Breadth-first traversal approach
    def get_element_by_id_breadth_first(self, id_value):
        return self._breadth_first_search(id_value)

    def _breadth_first_search(self, id_value):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node['id'] == id_value:
                return node
            for child in node['children']:
                queue.append(child)
        return None
