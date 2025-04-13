class TextEditor:
    def __init__(self):
        self.text_stack = []
        self.history_stack = []

    def type(self, char):
        self.text_stack.append(char)
        self.history_stack.append(('type', char))

    def delete(self):
        if self.text_stack:
            char = self.text_stack.pop()
            self.history_stack.append(('delete', char))

    def undo(self):
        if not self.history_tack:
            return
            
        action, char = self.history_stack.pop()

        if action == 'type':
            self.text_stack.pop()
        elif action == 'delete':
            self.text_stack.append(char)

    def getText(self):
        return ''.join(self.text_stack)
            
editor = TextEditor()
editor.type('H')
editor.type('e')
editor.type('y')
editor.delete()
editor.undo()

print(editor.getText())