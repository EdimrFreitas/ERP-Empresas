# Widgets antigos
from tkinter.ttk import Combobox, Progressbar, Separator, Treeview, Notebook

# Botões
from tkinter import Button, Radiobutton, Checkbutton

# Widgets
from tkinter import Label, Entry, Frame, Spinbox, LabelFrame, PanedWindow, Canvas, Listbox, Text

# Menus
from tkinter import Menu, Menubutton, OptionMenu

# Caixas de menssagem
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter.messagebox import askquestion, askyesno, askokcancel, askretrycancel, askyesnocancel

from tkinter.filedialog import askopenfilename


class Construtor:
    """Serve para criar widgets de forma mais limpa
    No geral em todos é obrigatório colocar:
    master, name, background or bg, foreground or fg e font

    Isso depende da widget, ao longo do tempo
    vamos definindo todas as variáveis
    """

    # Countainers ------------------------------------------------------------------------------------------------------
    @classmethod
    def frame(cls, kw=None):
        """ Estrutura:
            frames = {
                nome_da_frame: {
                    'param': {
                        master: Misc | None = ...,
                        background: str = ...,
                        bd: str | float = ...,
                        bg: str = ...,
                        border: str | float = ...,
                        borderwidth: str | float = ...,
                        class_: str = ...,
                        colormap: Literal["new", ""] | Misc = ...,
                        container: bool = ...,
                        cursor: str | tuple[str] | ... | tuple[str, str, str, ,str] = ...,
                        height: str | float = ...,
                        highlightbackground: str = ...,
                        highlightcolor: str = ...,
                        highlightthickness: str | float = ...,
                        name: str = ...,
                        padx: str | float = ...,
                        pady: str | float = ...,
                        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        takefocus: int | Literal[""] | (str) -> bool | None = ...,
                        visual: str | tuple[str, int] = ...,
                        width: str | float = ...
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                },
                ...
            }
        """
        for frame in kw:
            param = kw[frame]['param']

            if not param.get('name', False):
                param['name'] = frame

            nw_widget = Frame(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = frame)

    @classmethod
    def label_frame(cls, kw=None):
        """ Estrutura:
            labelframes = {
                nome_da_labelframe: {
                    'param': {
                        master: Misc | None = ...,
                        background or bg: str = ...,
                        border or bd: str | float = ...,
                        borderwidth: str | float = ...,
                        class_: str = ...,
                        colormap: Literal["new", ""] | Misc = ...,
                        container: bool = ...,
                        cursor: str | tuple[str] | ... | tuple[str, str, str, str] = ...,
                        font: Any = ...,
                        foreground or fg: str = ...,
                        height: str | float = ...,
                        highlightbackground: str = ...,
                        highlightcolor: str = ...,
                        highlightthickness: str | float = ...,
                        labelanchor: Literal["nw", "n", "ne", "en", "e", "es", "se", "s", "sw", "ws", "w", "wn"] = ...,
                        labelwidget: Misc = ...,
                        name: str = ...,
                        padx: str | float = ...,
                        pady: str | float = ...,
                        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        takefocus: int | Literal[""] | (str) -> bool | None = ...,
                        text: float | str = ...,
                        visual: str | tuple[str, int] = ...,
                        width: str | float = ...
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                },
                ...
            }
        """
        for labelframe in kw:
            param = kw[labelframe]['param']

            if not param.get('name', False):
                param['name'] = labelframe

            nw_widget = LabelFrame(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = labelframe)

    @classmethod
    def paned_window(cls, kw=None):
        """ Estrutura:
            paned_windows = {
                nome_da_paned_window: {
                    'param': {
                        master: Misc | None = ...,
                        background ou bg: str = ...,
                        border ou bd: str | float = ...,
                        borderwidth: str | float = ...,
                        cursor: str | tuple[str] | ... | tuple[str, str, str, str] = ...,
                        handlepad: str | float = ...,
                        handlesize: str | float = ...,
                        height: str | float = ...,
                        name: str = ...,
                        opaqueresize: bool = ...,
                        orient: Literal["horizontal", "vertical"] = ...,
                        proxybackground: str = ...,
                        proxyborderwidth: str | float = ...,
                        proxyrelief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        sashcursor: str | tuple[str] | ... | tuple[str, str, str, str] = ...,
                        sashpad: str | float = ...,
                        sashrelief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        sashwidth: str | float = ...,
                        showhandle: bool = ...,
                        width: str | float = ...
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                },
                ...
            }
        """
        for paned_window in kw:
            param = kw[paned_window]['param']

            if not param.get('name', False):
                param['name'] = paned_window

            nw_widget = PanedWindow(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = paned_window)

    @classmethod
    def notebook(cls, kw=None):
        """ Estrutura:
            notebooks = {
                nome_do_notebook: {
                    'param': {
                        master: Misc | None = ...,
                        class_: str = ...,
                        cursor: Any = ...,
                        height: int = ...,
                        name: str = ...,
                        padding: Any = ...,
                        style: str = ...,
                        takefocus: Any = ...,
                        width: int = ...
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter},
                },
                ...,
            }
        """
        for notebook in kw:
            param = kw[notebook]['param']

            if not param.get('name', False):
                param['name'] = notebook
            print(param)
            nw_widget = Notebook(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = notebook)

    @classmethod
    def add_abas(cls, kw=None):
        """abas: {
            notebook: {Widget ao qual serão adicionados as abas},
            nome_aba_1: {
                child: Widget, geralmente a frame
                state: Literal["normal", "disabled", "hidden"] = ...,
                sticky: str = ...,
                padding: Any = ...,
                text: str = ...,
                image: Any = ...,
                compound: Any = ...,
                underline: int = ...
            },
            ...,
        },
        """
        abas = kw['abas']

        for aba in abas:
            info_aba = kw['abas'][aba]

            if not info_aba.get('text'):
                info_aba['text'] = aba

            kw['notebook'].add(**info_aba)

    @classmethod
    def cavas(cls, kw=None):
        """ Estrutura:
            cavas = {
                nome_da_cavas: {
                    'param': {
                        master: Misc | None = ...,
                        background ou bg: str = ...,
                        border ou bd: str | float = ...,
                        borderwidth: str | float = ...,
                        closeenough: float = ...,
                        confine: bool = ...,
                        cursor: str | tuple[str] | ... | tuple[str, str, str, str] = ...,
                        height: str | float = ...,
                        highlightbackground: str = ...,
                        highlightcolor: str = ...,
                        highlightthickness: str | float = ...,
                        insertbackground: str = ...,
                        insertborderwidth: str | float = ...,
                        insertofftime: int = ...,
                        insertontime: int = ...,
                        insertwidth: str | float = ...,
                        name: str = ...,
                        offset: Any = ...,
                        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        scrollregion: tuple[str | float, str | float, str | float, str | float] | tuple = ...,
                        selectbackground: str = ...,
                        selectborderwidth: str | float = ...,
                        selectforeground: str = ...,
                        state: Literal["normal", "disabled"] = ...,
                        takefocus: int | Literal[""] | (str) -> bool | None = ...,
                        width: str | float = ...,
                        xscrollcommand: str | (float, float) -> Any = ...,
                        xscrollincrement: str | float = ...,
                        yscrollcommand: str | (float, float) -> Any = ...,
                        yscrollincrement: str | float = ...
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                },
                ...
            }
        """
        for cavas in kw:
            param = kw[cavas]['param']

            if not param.get('name', False):
                param['name'] = cavas

            nw_widget = Canvas(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = cavas)

    # Labels -----------------------------------------------------------------------------------------------------------
    @classmethod
    def label(cls, kw=None):
        """ Estrutura:
            label = {
                nome_da_label: {
                    'param': {
                        master: Misc | None = ...,
                        activebackground: str = ...,
                        activeforeground: str = ...,
                        anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"] = ...,
                        background or bg: str = ...,
                        bitmap: str = ...,
                        border or bd: str | float = ...,
                        borderwidth: str | float = ...,
                        compound: Literal["top", "left", "center", "right", "bottom", "none"] = ...,
                        cursor: str | tuple[str] | ... | tuple[str, str, str, str] = ...,
                        disabledforeground: str = ...,
                        font: Any = ...,
                        foreground or fg: str = ...,
                        height: str | float = ...,
                        highlightbackground: str = ...,
                        highlightcolor: str = ...,
                        highlightthickness: str | float = ...,
                        image: _Image | str = ...,
                        justify: Literal["left", "center", "right"] = ...,
                        name: str = ...,
                        padx: str | float = ...,
                        pady: str | float = ...,
                        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        state: Literal["normal", "active", "disabled"] = ...,
                        takefocus: int | Literal[""] | (str) -> bool | None = ...,
                        text: float | str = ...,
                        textvariable: Variable = ...,
                        underline: int = ...,
                        width: str | float = ...,
                        wraplength: str | float = ...
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                },
                ...
            }
        """
        for label in kw:
            param = kw[label]['param']

            if not param.get('name', False):
                param['name'] = label

            nw_widget = Label(**param)
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
                    cursor: str | tuple[str] | ... | tuple[str, str, str, str] = ...,
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
                            cursor: str | tuple[str] | ... = ...,
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
            comboboxes = {
                nome_da_combobox: {
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
        """ Estrutura:
            list_boxes = {
                nome_da_list_box: {
                    'param': {
                        master: Misc | None = ...,
                        activestyle: Literal["dotbox", "none", "underline"] = ...,
                        background or bg: str = ...,
                        border or bd: str | float = ...,
                        borderwidth: str | float = ...,
                        cursor: str | tuple[str] | ... | tuple[str, str, str, str] = ...,
                        disabledforeground: str = ...,
                        exportselection: int = ...,
                        font: Any = ...,
                        foreground or fg: str = ...,
                        height: int = ...,
                        highlightbackground: str = ...,
                        highlightcolor: str = ...,
                        highlightthickness: str | float = ...,
                        justify: Literal["left", "center", "right"] = ...,
                        listvariable: Variable = ...,
                        name: str = ...,
                        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        selectbackground: str = ...,
                        selectborderwidth: str | float = ...,
                        selectforeground: str = ...,
                        selectmode: str = ...,
                        setgrid: bool = ...,
                        state: Literal["normal", "disabled"] = ...,
                        takefocus: int | Literal[""] | (str) -> bool | None = ...,
                        width: int = ...,
                        xscrollcommand: str | (float, float) -> Any = ...,
                        yscrollcommand: str | (float, float) -> Any = ...
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                },
                ...
            }
                """
        for list_box in kw:
            param = kw[list_box]['param']

            if not param.get('name', False):
                param['name'] = list_box

            nw_widget = Listbox(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = list_box)

    @classmethod
    def spinbox(cls, kw=None):
        """ Estrutura:
            spin_boxes = {
                nome_da_spin_box: {
                    'param': {
                        master: Misc | None = ...,
                        activebackground: str = ...,
                        background or bg: str = ...,
                        border or bd: str | float = ...,
                        borderwidth: str | float = ...,
                        buttonbackground: str = ...,
                        buttoncursor: str | tuple[str] | ... | tuple[str, str, str, str] = ...,
                        buttondownrelief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        buttonuprelief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        command: () -> Any | str | list[str] | tuple[str, ...] = ...,
                        cursor: str | tuple[str] | ... | tuple[str, str, str, str] = ...,
                        disabledbackground: str = ...,
                        disabledforeground: str = ...,
                        exportselection: bool = ...,
                        font: Any = ...,
                        foreground or fg: str = ...,
                        format: str = ...,
                        from_: float = ...,
                        highlightbackground: str = ...,
                        highlightcolor: str = ...,
                        highlightthickness: str | float = ...,
                        increment: float = ...,
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
                        repeatdelay: int = ...,
                        repeatinterval: int = ...,
                        selectbackground: str = ...,
                        selectborderwidth: str | float = ...,
                        selectforeground: str = ...,
                        state: Literal["normal", "disabled", "readonly"] = ...,
                        takefocus: int | Literal[""] | (str) -> bool | None = ...,
                        textvariable: Variable = ...,
                        to: float = ...,
                        validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = ...,
                        validatecommand or vcmd: () -> bool | str | list[str] | tuple[str, ...] = ...,
                        values: list[str] | tuple[str, ...] = ...,
                        width: int = ...,
                        wrap: bool = ...,
                        xscrollcommand: str | (float, float) -> Any = ...
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                },
                ...
            }
        """
        for spin_box in kw:
            param = kw[spin_box]['param']

            if not param.get('name', False):
                param['name'] = spin_box

            nw_widget = Spinbox(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = spin_box)

    # Botões -----------------------------------------------------------------------------------------------------------
    @classmethod
    def button(cls, kw=None):
        """ Estrutura:
            buttons = {
                nome_do_button: {
                    'param': {
                        master: Misc | None = ...,
                        activebackground: str = ...,
                        activeforeground: str = ...,
                        anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"] = ...,
                        background or bg: str = ...,
                        bitmap: str = ...,
                        border or bd: str | float = ...,
                        borderwidth: str | float = ...,
                        command: str | () -> Any = ...,
                        compound: Literal["top", "left", "center", "right", "bottom", "none"] = ...,
                        cursor: str | tuple[str] | ... | tuple[str, str, str, str] = ...,
                        default: Literal["normal", "active", "disabled"] = ...,
                        disabledforeground: str = ...,
                        font: Any = ...,
                        foreground or fg: str = ...,
                        height: str | float = ...,
                        highlightbackground: str = ...,
                        highlightcolor: str = ...,
                        highlightthickness: str | float = ...,
                        image: _Image | str = ...,
                        justify: Literal["left", "center", "right"] = ...,
                        name: str = ...,
                        overrelief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        padx: str | float = ...,
                        pady: str | float = ...,
                        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        repeatdelay: int = ...,
                        repeatinterval: int = ...,
                        state: Literal["normal", "active", "disabled"] = ...,
                        takefocus: int | Literal[""] | (str) -> bool | None = ...,
                        text: float | str = ...,
                        textvariable: Variable = ...,
                        underline: int = ...,
                        width: str | float = ...,
                        wraplength: str | float = ...
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                },
                ...
            }
        """
        for button in kw:
            param = kw[button]['param']

            if not param.get('name', False):
                param['name'] = button

            nw_widget = Button(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = button)

    @classmethod
    def check_button(cls, kw=None):
        """ Estrutura:
            check_buttons = {
                nome_do_check_button: {
                    'param': {
                        master: Misc | None = ...,
                        activebackground: str = ...,
                        activeforeground: str = ...,
                        anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"] = ...,
                        background oor bg: str = ...,
                        bitmap: str = ...,
                        border or bd: str | float = ...,
                        borderwidth: str | float = ...,
                        command: str | () -> Any = ...,
                        compound: Literal["top", "left", "center", "right", "bottom", "none"] = ...,
                        cursor: str | tuple[str] | ... | tuple[str, str, str, str] = ...,
                        disabledforeground: str = ...,
                        font: Any = ...,
                        foreground or fg: str = ...,
                        height: str | float = ...,
                        highlightbackground: str = ...,
                        highlightcolor: str = ...,
                        highlightthickness: str | float = ...,
                        image: _Image | str = ...,
                        indicatoron: bool = ...,
                        justify: Literal["left", "center", "right"] = ...,
                        name: str = ...,
                        offrelief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        offvalue: Any = ...,
                        onvalue: Any = ...,
                        overrelief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        padx: str | float = ...,
                        pady: str | float = ...,
                        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        selectcolor: str = ...,
                        selectimage: _Image | str = ...,
                        state: Literal["normal", "active", "disabled"] = ...,
                        takefocus: int | Literal[""] | (str) -> bool | None = ...,
                        text: float | str = ...,
                        textvariable: Variable = ...,
                        tristateimage: _Image | str = ...,
                        tristatevalue: Any = ...,
                        underline: int = ...,
                        variable: Variable | Literal[""] = ...,
                        width: str | float = ...,
                        wraplength: str | float = ...
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                },
                ...
            }
        """
        for check_button in kw:
            param = kw[check_button]['param']

            if not param.get('name', False):
                param['name'] = check_button

            nw_widget = Checkbutton(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = check_button)

    @classmethod
    def radio_button(cls, kw=None):
        """ Estrutura:
            radio_buttons = {
                nome_do_radio_button: {
                    'param': {
                        master: Misc | None = ...,
                        activebackground: str = ...,
                        activeforeground: str = ...,
                        anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"] = ...,
                        background or bg: str = ...,
                        bitmap: str = ...,
                        border or bd: str | float = ...,
                        borderwidth: str | float = ...,
                        command: str | () -> Any = ...,
                        compound: Literal["top", "left", "center", "right", "bottom", "none"] = ...,
                        cursor: str | tuple[str] | ... | tuple[str, str, str, str] = ...,
                        disabledforeground: str = ...,
                        font: Any = ...,
                        foreground or fg: str = ...,
                        height: str | float = ...,
                        highlightbackground: str = ...,
                        highlightcolor: str = ...,
                        highlightthickness: str | float = ...,
                        image: _Image | str = ...,
                        indicatoron: bool = ...,
                        justify: Literal["left", "center", "right"] = ...,
                        name: str = ...,
                        overrelief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        padx: str | float = ...,
                        pady: str | float = ...,
                        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
                        repeatdelay: int = ...,
                        repeatinterval: int = ...,
                        state: Literal["normal", "active", "disabled"] = ...,
                        takefocus: int | Literal[""] | (str) -> bool | None = ...,
                        text: float | str = ...,
                        textvariable: Variable = ...,
                        tristateimage: _Image | str = ...,
                        tristatevalue: Any = ...,
                        underline: int = ...,
                        width: str | float = ...,
                        wraplength: str | float = ...
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                },
                ...
            }
        """
        for radio_button in kw:
            param = kw[radio_button]['param']

            if not param.get('name', False):
                param['name'] = radio_button

            nw_widget = Radiobutton(**param)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = radio_button)

    # Barra de carregamento --------------------------------------------------------------------------------------------
    @classmethod
    def progressbar(cls, kw=None):
        """ Estrutura:
            radio_buttons = {
                nome_do_radio_button: {
                    'param': {
                        master: Misc | None = ...,
                        class_: str = ...,
                        cursor: Any = ...,
                        length: Any = ...,
                        maximum: float = ...,
                        mode: Literal["determinate", "indeterminate"] = ...,
                        name: str = ...,
                        orient: Literal["horizontal", "vertical"] = ...,
                        phase: int = ...,
                        style: str = ...,
                        takefocus: Any = ...,
                        value: float = ...,
                        variable: IntVar | DoubleVar = ..
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                },
                ...
            }
        """
        for progressbar in kw:
            param = kw[progressbar]['param']

            if not param.get('name', False):
                param['name'] = progressbar

            nw_widget = Progressbar(**param, name = progressbar)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = progressbar)

    # Organizadores ----------------------------------------------------------------------------------------------------
    @classmethod
    def separator(cls, kw=None):
        """ Estrutura:
            radio_buttons = {
                nome_do_radio_button: {
                    'param': {
                        master: Misc | None = ...,
                        class_: str = ...,
                        cursor: Any = ...,
                        name: str = ...,
                        orient: Literal["horizontal", "vertical"] = ...,
                        style: str = ...,
                        takefocus: Any = ...
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                },
                ...
            }
        """
        for separator in kw:
            param = kw[separator]['param']

            if not param.get('name'):
                param['name'] = separator

            nw_widget = Separator(**param, name = separator)
            cls.__posiciona(nw_widget = nw_widget, kw = kw, widget = separator)

    # Criação de menus -------------------------------------------------------------------------------------------------
    @classmethod
    def menu(cls, kw=None):
        """ Estrutura:
            radio_buttons = {
                nome_do_radio_button: {
                    'param': {
                        master: Misc | None = ...,
                        class_: str = ...,
                        cursor: Any = ...,
                        name: str = ...,
                        orient: Literal["horizontal", "vertical"] = ...,
                        style: str = ...,
                        takefocus: Any = ...
                    },
                    pack, place, grid: {verificar sobre regras para cada um nas infos do Tkinter}
                },
                ...
            }
        """
        for menu in kw:
            param = kw[menu]['param']

            if not param.get('name'):
                param['name'] = menu

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
