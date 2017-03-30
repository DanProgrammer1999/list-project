from tkinter import *
from com.ListModel import *

window = Tk()
list = ListModel('todolist')
remove_pic = PhotoImage(file='/home/dan/Programming/Python/Project_Y/com/Remove.png', width=50, height=50)

class EntryFrame(object):
    __root = None
    __entry = None
    __list = None

    def saveEntry(self):
        return True

    def changeState(self):
        return True

    def removeEntry(self, event):
        print('removing of element "' + self.__entry.getText() + '" with id ' + str(self.__entry.getId()))
        list.removeEntry(self.__entry.getId())

    def getEntry(self):
        return self.__entry

    def __init__(self, root, entry):
        self.__root = root
        self.__entry = entry
        state = IntVar()
        state.set(entry.getState())

        entry_frame = Frame(self.__root, bg='#a59c9a')

        eCheck = Checkbutton(entry_frame, variable=state, onvalue=1, offvalue=0)
        eText = Text(entry_frame, height=1, width=20, font='Ubuntu 14', wrap=WORD)
        eText.insert(1.10, self.__entry.getText())
        eRemoveBtn = Button(entry_frame, image=remove_pic)

        eRemoveBtn.bind('<Button-1>', self.removeEntry)

        eText.pack()
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
        #self.__text_field = Entry(frame, height=1, width=20, font='Ubuntu 14', wrap=WORD)
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

        self.__text_field.place(bordermode='inside', relwidth=0.963, height=30, relx=0, rely=0, x=2.47)
        self.__save_but.place(bordermode='inside', relx=0, rely=0.7,relwidth=0.47)
        self.__cancel_but.place(bordermode='inside', relx=0.5, rely=0.7, relwidth=0.47)

        frame.place(bordermode='inside', relwidth=1, relheight=1, relx=0.025, rely=0.05, width=-10, height=-10)

        self.__root.mainloop()

    def __save(self, event):
        text = self.__get_text()
        list.createEntry(text)
        print('Saved text ' + text)
        self.__window.destroy()

    def __cancel(self, event):
        print('Cancelled')
        self.__window.destroy()

    def __get_text(self):
        return self.__text_field.get()


class ListModelFrame(object):
    __dataModel = None
    __entrysRoot = None
    __add_butt = None

    def addEntry(self, event):
        AddFrame(self.__entrysRoot)

    def update(self):
        return True

    def render(self):
        for e in self.__dataModel.getList():
            EntryFrame(self.__entrysRoot, e)
        self.__entrysRoot.pack(fill='both')

    def __init__(self, root, dataModel):
        self.__dataModel = dataModel
        main_frame = Frame(root, bg='white')

        self.__entrysRoot = Frame(main_frame, bg='white')
        self.render()

        buttonsFrame = Frame(main_frame, bg='white')
        addButton = Button(buttonsFrame, text=u'Add')
        scrollbar = Scrollbar(main_frame, orient='vert')

        addButton.bind('<Button-1>', self.addEntry)

        main_frame.pack(fill='both')
        addButton.pack()
        buttonsFrame.pack(expand=True)

a = ListModelFrame(window, list)
window.title('TO DO List')
window.mainloop()
