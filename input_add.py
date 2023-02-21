def input_add(txt):
        
        self.insert_text(txt, end='')
        self.saveTF = True
        self.mode = 'input'
        addex = ''
        

        while self.mode == 'input':
            self.update()
            time.sleep(0.1)
            
            if self.input_str:
                addex = self.input_str
                self.input_str = ''
                break

        self.insert_text(addex, end='')
        self.saveTF = False
        self.input_str = addex
        return addex