# Widgets antigos
from tkinter.ttk import Combobox, Progressbar, Separator, Treeview

# Botões
from tkinter import Button, Radiobutton, Checkbutton

# Widgets
from tkinter import Label, Entry, Frame, Spinbox, LabelFrame, PanedWindow, Canvas, Listbox, Text

# Menus
from tkinter import Menu, Menubutton, OptionMenu

# Variáveis
from tkinter import StringVar

# Caixas de menssagem
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter.messagebox import askquestion, askyesno, askokcancel, askretrycancel, askyesnocancel

from tkinter.filedialog import askopenfilename


INFO = 'Info'


class Construtor:
    """Estrutura geral:
    widgets = dict(
        nome_do_widget = dict(
            param = dict(kwargs),
            "position" = dict(kwargs),
        )
    )
    sendo que:
    'nome_do_widget' será o nome de children do widget
    'param' são os parâmetros do respectivo widget criado
    "position" pode ser trocado por uma das opções [pack, place, or grid]

    Serve para criar widgets de forma mais limpa
    No geral em todos é obrigatório colocar:
    master, name, background or bg, foreground or fg e font

    Isso depende da widget, ao longo do tempo
    vamos definindo todas as variáveis
    """

    @classmethod
    def labelframe(cls, kw=None):
        """master, background or bg, border or bd, text, anchor

        
        """
        for labelframe in kw:
            param = kw[labelframe]['param']
            nw_widget = LabelFrame(**param, name = labelframe)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = labelframe)

    @classmethod
    def frame(cls, kw=None):
        """O parâmetro name será automaticamente o nome do widget
        também deverá estar sempre em letras minusculas

        master, background or bg, border or bd, anchor, cursor

        
        """
        for frame in kw:
            param = kw[frame]['param']

            if not param.get('name', False):
                param['name'] = frame

            nw_widget = Frame(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = frame)

    @classmethod
    def label(cls, kw=None):
        """
        O parâmetro name será automaticamente o nome do widget
        Neste widget, por padrão sempre teremos uma variável criada
        para deficnição como textvariable
        master, background or bg, border or bd, text,
        anchor, cursor
        
        """
        for label in kw:
            param = kw[label]['param']
            nw_widget = Label(**param, name = label)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = label)

    # Input de texto ---------------------------------------------------------------------------------------------------
    @classmethod
    def entry(cls, kw=None):
        """ Estrutura:
        entrys = {
            nome_da_entry: {
                'param': {
                    master: Misc | None = ...,
                    background or bg: str = ...,
                    border or bd: str | float = ...,
                    borderwidth: str | float = ...,
                    cursor: str | tuple[str] | tuple[str, str] | tuple[str, str, str] | tuple[str, str, str, str] = ...,
                    disabledbackground: str = ...,
                    disabledforeground: str = ...,
                    exportselection: bool = ...,
                    font: Any = ...,
                    foreground or fg: str = ...,
                    highlightbackground: str = ...,
                    highlightcolor: str = ...,
                    highlightthickness: str | float = ...,
                    **initialvalue: str = ..., originalmente não existe
                    insertbackground: str = ...,
                    insertborderwidth: str | float = ...,
                    insertofftime: int = ...,
                    insertontime: int = ...,
                    insertwidth: str | float = ...,
                    invalidcommand or invcmd: () -> bool | str | list[str] | tuple[str, ...] = ...,
                    justify: Literal["left", "center", "right"] = ...,
                    name: str = ...,
                    readonlybackground: str = ...,
                    relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                    selectbackground: str = ...,
                    selectborderwidth: str | float = ...,
                    selectforeground: str = ...,
                    show: str = ...,
                    state: Literal["normal", "disabled", "readonly"] = ...,
                    takefocus: int | Literal[""] | (str) -> bool | None = ...,
                    textvariable: Variable = ...,
                    validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = ...,
                    validatecommand: () -> bool | str | list[str] | tuple[str, ...] = ...,
                    vcmd: () -> bool | str | list[str] | tuple[str, ...] = ...,
                    width: int = ...,
                    xscrollcommand: str | (float, float)
                },
                pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
            },
            ...
        }
             """
        for entry in kw:
            param = kw[entry]['param']

            if not param.get('name', False):
                param['name'] = entry

            nw_widget = Entry(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = entry)

    @classmethod
    def text(cls, kw=None):
        """ Estrutura:
                texts = {
                    nome_da_text: {
                        'param': {
                            master: Misc | None = ...,
                            autoseparators: bool = ...,
                            background or bg: str = ...,
                            blockcursor: bool = ...,
                            border or bd: str | float = ...,
                            borderwidth: str | float = ...,
                            cursor: str | tuple[str] | tuple[str, str] | tuple[str, str, str] = ...,
                            endline: int | Literal[""] = ...,
                            exportselection: bool = ...,
                            font: Any = ...,
                            foreground or fg: str = ...,
                            height: str | float = ...,
                            highlightbackground: str = ...,
                            highlightcolor: str = ...,
                            highlightthickness: str | float = ...,
                            inactiveselectbackground: str = ...,
                            insertbackground: str = ...,
                            insertborderwidth: str | float = ...,
                            insertofftime: int = ...,
                            insertontime: int = ...,
                            insertunfocussed: Literal["none", "hollow", "solid"] = ...,
                            insertwidth: str | float = ...,
                            maxundo: int = ...,
                            name: str = ...,
                            padx: str | float = ...,
                            pady: str | float = ...,
                            relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                            selectbackground: str = ...,
                            selectborderwidth: str | float = ...,
                            selectforeground: str = ...,
                            setgrid: bool = ...,
                            spacing1: str | float = ...,
                            spacing2: str | float = ...,
                            spacing3: str | float = ...,
                            startline: int | Literal[""] = ...,
                            state: Literal["normal", "disabled"] = ...,
                            tabs: str | float | tuple[str | float, ...] = ...,
                            tabstyle: Literal["tabular", "wordprocessor"] = ...,
                            takefocus: int | Literal[""] | (str) -> bool | None = ...,
                            undo: bool = ...,
                            width: int = ...,
                            wrap: Literal["none", "char", "word"] = ...,
                            xscrollcommand: str | (float, float) -> Any = ...,
                            yscrollcommand: str | (float, float) -> Any = ...
                        },
                        pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                    },
                    ...
                }
                     """
        for text in kw:
            param = kw[text]['param']

            if not param.get('name', False):
                param['name'] = text

            nw_widget = Text(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = text)

    # Listas de opções -------------------------------------------------------------------------------------------------
    @classmethod
    def combo_box(cls, kw=None):
        """ Estrutura:
                        texts = {
                            nome_da_text: {
                                'param': {
                                    master: Misc | None = ...,
                                    background: Any = ...,
                                     class_: str = ...,
                                     cursor: Any = ...,
                                     exportselection: bool = ...,
                                     font: Any = ...,
                                     foreground: Any = ...,
                                     height: int = ...,
                                     invalidcommand: Any = ...,
                                     justify: Literal["left", "center", "right"] = ...,
                                     name: str = ...,
                                     postcommand: () -> Any | str = ...,
                                     show: Any = ...,
                                     state: str = ...,
                                     style: str = ...,
                                     takefocus: Any = ...,
                                     textvariable: Variable = ...,
                                     validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = ...,
                                     validatecommand: Any = ...,
                                     values: list[str] | tuple[str, ...] = ...,
                                     width: int = ...,
                                     xscrollcommand: Any = ...
                                },
                                pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                            },
                            ...
                        }
        """
        for combo_box in kw:
            param = kw[combo_box]['param']

            if not param.get('name', False):
                param['name'] = combo_box

            nw_widget = Combobox(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = combo_box)

    @classmethod
    def list_box(cls, kw=None):
        for list_box in kw:
            param = kw[list_box]['param']
            nw_widget = Listbox(**param, name = list_box)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = list_box)

    @classmethod
    def spinbox(cls, kw=None):
        for spin_box in kw:
            param = kw[spin_box]['param']
            nw_widget = Spinbox(**param, name = spin_box)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = spin_box)

    # Botões -----------------------------------------------------------------------------------------------------------
    @classmethod
    def button(cls, kw=None):
        for button in kw:
            param = kw[button]['param']
            nw_widget = Button(**param, name = button)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = button)

    # Barra de carregamento --------------------------------------------------------------------------------------------
    @classmethod
    def progressbar(cls, kw=None):
        for progressbar in kw:
            param = kw[progressbar]['param']
            nw_widget = Progressbar(**param, name = progressbar)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = progressbar)

    # Organizadores ----------------------------------------------------------------------------------------------------
    @classmethod
    def separator(cls, kw=None):
        for separator in kw:
            param = kw[separator]['param']
            nw_widget = Separator(**param, name = separator)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = separator)

    # Criação de menus -------------------------------------------------------------------------------------------------
    @classmethod
    def menu(cls, kw=None):
        """O criador de menus depende das informações
        master: Misc | None = ...,
        activebackground: str = ...,
        activeborderwidth: str | float = ...,
        activeforeground: str = ...,
        background: str = ... or bg: str = ...,
        border: str | float = ... or bd: str | float = ...,
        borderwidth: str | float = ...,
        cursor: str | tuple[str] | tuple[str, str] | tuple[str, str, str] | tuple[str, str, str, str] = ...,
        disabledforeground: str = ...,
        font: Any = ...,
        foreground: str = ... or fg: str = ...,
        name: str = ...,
        postcommand: () -> Any | str = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        selectcolor: str = ...,
        takefocus: int | Literal[""] | (str) -> bool | None = ...,
        tearoff: int = ...,
        tearoffcommand: (str, str) -> Any | str = ...,
        title: str = ...,
        type: Literal["menubar", "tearoff", "normal"] = ..
        """
        for menu in kw:
            param = kw[menu]['param']
            nw_widget = Menu(**param, name = menu)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = menu)

    # Tabela de informações --------------------------------------------------------------------------------------------
    @classmethod
    def tree_view(cls, kw=None):
        """Estrutura:
        tree = {
            'params': dict(
                master: Misc | None = ...,
                columns: será construido a partir do que estiver em colunas,
                cursor: Any = ...,
                displaycolumns: str | list[str] | tuple[str, ...] | list[int] | tuple[int, ...] | Literal["#all"] = ...,
                height: int = ...,
                name: str = ...,
                padding: Any = ...,
                selectmode: Literal["extended", "browse", "none"] = ...,
                show: Literal["tree", "headings", "tree headings", ""] | list[str] | tuple[str, ...] = ...,
                style: str = ...,
                takefocus: Any = ...,
                xscrollcommand: Any = ...,
                yscrollcommand: Any = ...
            ),

            place or pack or grid: {verificar sobre regras para cada um nas infos do Tkinter},

            'colunas': dict(
                nome_da_coluna: {
                    heading: {
                        *text: se não criado, será o 'nome_da_coluna',
                        image: image_name,
                        anchor: [NW, N, NE, W, CENTER, E, SW, S, SE]
                        command: callback,
                    },
                    column:{
                        anchor: anchor,
                        minwidth: width,
                        stretch: True/False,
                        width: width,
                    }
                }
            )

        """
        param = kw['param']
        colunas = list(kw['colunas'].keys())

        nw_widget = Treeview(**param, columns = colunas)
        cls.__posiciona(nw_widget = nw_widget, kw = kw)
        for coluna in colunas:
            heading = kw['colunas'][coluna]['heading']
            column = kw['colunas'][coluna]['column']

            if not heading.get('text'):
                heading['text'] = coluna

            nw_widget.heading(coluna, **heading)
            nw_widget.column(coluna, **column)

    # Informacionais ---------------------------------------------------------------------------------------------------
    @classmethod
    def show_info(cls, titulo: str, mensagem: str):
        showinfo(title = titulo, message = mensagem)

    @classmethod
    def show_error(cls, titulo: str, mensagem: str):
        showerror(title = titulo, message = mensagem)

    @classmethod
    def show_warning(cls, titulo: str, mensagem: str):
        showwarning(title = titulo, message = mensagem)

    # Perguntas --------------------------------------------------------------------------------------------------------
    @classmethod
    def ask_question(cls, titulo: str, mensagem: str):
        askquestion(title = titulo, message = mensagem)

    @classmethod
    def ask_yesno(cls, titulo: str, mensagem: str):
        askyesno(title = titulo, message = mensagem)

    @classmethod
    def ask_okcancel(cls, titulo: str, mensagem: str):
        askokcancel(title = titulo, message = mensagem)

    @classmethod
    def ask_retrycancel(cls, titulo: str, mensagem: str):
        askretrycancel(title = titulo, message = mensagem)

    @classmethod
    def ask_yesnocancel(cls, titulo: str, mensagem: str):
        askyesnocancel(title = titulo, message = mensagem)

    @classmethod
    def abrir_arquivo(cls, titulo: str, extenssoes: list, options: dict):
        return askopenfilename(title = titulo, filetypes = extenssoes, options = options)

    @classmethod
    def __posiciona(cls, nw_widget, kw, widget=None):
        if not widget:
            if kw.get('place', False):
                nw_widget.place(**kw['place'])
            elif kw.get('grid', False):
                nw_widget.grid(**kw['grid'])
            elif kw.get('pack', False):
                nw_widget.pack(**kw['pack'])

        else:
            if kw[widget].get('place', False):
                nw_widget.place(**kw[widget]['place'])
            elif kw[widget].get('grid', False):
                nw_widget.grid(**kw[widget]['grid'])
            elif kw[widget].get('pack', False):
                if not kw[widget]['pack']:
                    nw_widget.pack()
                else:
                    nw_widget.pack(**kw[widget]['pack'])
