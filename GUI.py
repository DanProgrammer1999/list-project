from tkinter import *
from ListModel import *

window = Tk()
list = ListModel('todolist')
remove_pic = PhotoImage(file='Remove.png', width=50, height=50)

class EntryFrame(object):
    __root = None
    __entry = None
    __db_entry = None
    __list = None

    def destroy(self):
        self.__entry.destroy()

    def saveEntry(self, event):
        self.__db_entry.setText(event.widget.get())
        print(self.__entry.focus_get())
        self.__entry.focus()
        return True

    def changeState(self, event):
        self.__db_entry.changeState()

    def removeEntry(self, event):
        print('removing of element "' + self.__db_entry.getText() + '" with id ' + str(self.__db_entry.getId()))
        list.removeEntry(self.__db_entry.getId())
        self.__entry.destroy()

    def getEntry(self):
        return self.__entry

    def __init__(self, root, db_entry):
        self.__root = root
        self.__db_entry = db_entry
        self.__state = IntVar()
        self.__state.set(db_entry.getState())

        self.__entry = entry_frame = Frame(self.__root, bg='#a59c9a')

        eCheck = Checkbutton(entry_frame, variable=self.__state, onvalue=1, offvalue=0)
        eCheck.bind('<Button-1>', self.changeState)

        eText = Entry(entry_frame, font='Ubuntu 14')
        eText.insert(0, self.__db_entry.getText())
        eText.bind('<FocusOut>', self.saveEntry)
        eText.bind('<Return>', self.saveEntry)
        eRemoveBtn = Button(entry_frame, image=remove_pic)

        eRemoveBtn.bind('<Button-1>', self.removeEntry)

        eText.pack(fill='x')
        eRemoveBtn.pack(side=RIGHT)
        eCheck.pack(side=RIGHT)
        entry_frame.pack(fill='x')

class AddFrame(object):
    __window=None
    __text_field = None
    __save_but = None
    __cancel_but = None
    __root = None

    def __init__(self, root):

        self.__root = root

        self.__window = Toplevel()
        frame = Frame(self.__window)
        #self.__text_field = Text(frame, height=1, width=20, font='Ubuntu 14')
        self.__text_field = Entry(frame, font='Ubuntu 14')
        self.__cancel_but = Button(frame, text='Cancel')
        self.__save_but = Button(frame, text='Add')

        self.__window.resizable(False, False)
        self.__window.geometry('500x100+200+200')
        self.__window.title('Add Entry')

        self.__save_but.bind('<Button-1>', self.__save)
        self.__text_field.bind('<Key-Return>', lambda x: self.__save_but.focus())
        self.__save_but.bind('<Key-Return>', self.__save)
        self.__cancel_but.bind('<Button-1>', self.__cancel)
        self.__text_field.focus()

        self.__text_field.place(bordermode='inside', relwidth=0.963, height=30, relx=0, rely=0, x=2.47,)
        self.__save_but.place(bordermode='inside', relx=0, rely=0.7,relwidth=0.47)
        self.__cancel_but.place(bordermode='inside', relx=0.5, rely=0.7, relwidth=0.47)

        frame.place(bordermode='inside', relwidth=1, relheight=1, relx=0.025, rely=0.05, width=-10, height=-10)

        self.__window.mainloop()

    def __save(self, event):

        text = self.__get_text()
        print('Saved text ' + text)
        self.__window.destroy()
        self.__root.update(text)

    def __cancel(self, event):
        print('Cancelled')
        self.__window.destroy()

    def __get_text(self):
        return self.__text_field.get()


class ListModelFrame(object):

    __root = None
    __dataModel = None
    __entrysRoot = None
    __add_butt = None
    __entry_list = []

    def addEntry(self, event):

        AddFrame(self)

    def update(self, text):

        '''for elem in self.__entry_list:
            elem.destroy()
        self.render()'''
        frame = EntryFrame(self.__entrysRoot, list.createEntry(text))
        self.__entry_list.append(frame)

    def render(self):

        for e in self.__dataModel.getList():
            frame = EntryFrame(self.__entrysRoot, e)
            self.__entry_list.append(frame)
        self.__entrysRoot.pack(fill='both', side='top')
        
    def __init__(self, root, dataModel):

        self.__dataModel = dataModel

        buttonsFrame = Frame(root, bg='white')
        self.__entrysRoot = Canvas( bg='white', width=300, height=300, scrollregion=(0,0,5000000,500000000))

        scrollbar = Scrollbar(self.__entrysRoot, orient='vert', command=self.__entrysRoot.yview)
        scrollbar.pack(side='right', fill='y')
        self.__entrysRoot.configure(yscrollcommand=scrollbar.set)

        self.render()

        addButton = Button(buttonsFrame, text=u'Add')

        #scrollbar = Scrollbar(main_frame, orient='vert')

        addButton.bind('<Button-1>', self.addEntry)

        addButton.pack(side='bottom')
        buttonsFrame.pack(expand=False)

a = ListModelFrame(window, list)
window.title('TO DO List')
window.mainloop()
