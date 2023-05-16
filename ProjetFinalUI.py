#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    May 16, 2023 03:45:19 PM EDT  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

#import unknown_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    style.map('TNotebook.Tab', background =
            [('selected', _bgcolor), ('active', _tabbg1),
            ('!active', _ana2color)], foreground =
            [('selected', _fgcolor), ('active', _tabfg1), ('!active',  _tabfg2)])
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+660+210")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top
        self.combobox = tk.StringVar()

        _style_code()
        self.TNotebook1 = ttk.Notebook(self.top)
        self.TNotebook1.place(relx=0.0, rely=0.0, relheight=1.013
                , relwidth=1.007)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text='''Garage''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t1.configure(background="#9742ff")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text='''Voiture''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t2.configure(background="#ffff80")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(2, text='''Réparation''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t3.configure(background="#ff77ff")
        self.TNotebook1_t3.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t3.configure(highlightcolor="black")
        self.TNotebook1_t4 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t4, padding=3)
        self.TNotebook1.tab(3, text='''Consultations''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t4.configure(background="#80ffff")
        self.TNotebook1_t4.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t4.configure(highlightcolor="black")
        self.Labelframe1 = tk.LabelFrame(self.TNotebook1_t1)
        self.Labelframe1.place(relx=0.033, rely=0.07, relheight=0.43
                , relwidth=0.933)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="#000000")
        self.Labelframe1.configure(text='''infos garage''')
        self.Labelframe1.configure(background="#fd4456")
        self.Label1 = tk.Label(self.Labelframe1)
        self.Label1.place(relx=0.018, rely=0.162, height=31, width=64
                , bordermode='ignore')
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''nom:''')
        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.018, rely=0.378, height=31, width=64
                , bordermode='ignore')
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Adresse:''')
        self.Label3 = tk.Label(self.Labelframe1)
        self.Label3.place(relx=0.018, rely=0.595, height=41, width=64
                , bordermode='ignore')
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''téléphone:''')
        self.Button1 = tk.Button(self.Labelframe1)
        self.Button1.place(relx=0.321, rely=0.865, height=24, width=157
                , bordermode='ignore')
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''créer garage''')
        self.Entry1 = tk.Entry(self.Labelframe1)
        self.Entry1.place(relx=0.161, rely=0.162, height=30, relwidth=0.471
                , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry2 = tk.Entry(self.Labelframe1)
        self.Entry2.place(relx=0.161, rely=0.378, height=30, relwidth=0.614
                , bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry3 = tk.Entry(self.Labelframe1)
        self.Entry3.place(relx=0.161, rely=0.595, height=30, relwidth=0.382
                , bordermode='ignore')
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Label4 = tk.Label(self.TNotebook1_t1)
        self.Label4.place(relx=0.05, rely=0.581, height=41, width=104)
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Fichier:''')
        self.Button2 = tk.Button(self.TNotebook1_t1)
        self.Button2.place(relx=0.05, rely=0.837, height=44, width=101)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Déserialiser''')
        self.Button3 = tk.Button(self.TNotebook1_t1)
        self.Button3.place(relx=0.65, rely=0.837, height=44, width=117)
        self.Button3.configure(activebackground="beige")
        self.Button3.configure(activeforeground="black")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(compound='left')
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Sérialiser''')
        self.Entry4 = tk.Entry(self.TNotebook1_t1)
        self.Entry4.place(relx=0.25, rely=0.581, height=40, relwidth=0.457)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Labelframe2 = tk.LabelFrame(self.TNotebook1_t2)
        self.Labelframe2.place(relx=0.0, rely=0.023, relheight=0.36
                , relwidth=0.983)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="#000000")
        self.Labelframe2.configure(text='''infos voiture''')
        self.Labelframe2.configure(background="#ff8040")
        self.Label5 = tk.Label(self.Labelframe2)
        self.Label5.place(relx=0.017, rely=0.116, height=37, width=94
                , bordermode='ignore')
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Num. Plaque:''')
        self.Label6 = tk.Label(self.Labelframe2)
        self.Label6.place(relx=0.017, rely=0.387, height=37, width=94
                , bordermode='ignore')
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Marque:''')
        self.Label7 = tk.Label(self.Labelframe2)
        self.Label7.place(relx=0.017, rely=0.71, height=37, width=94
                , bordermode='ignore')
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''couleur:''')
        self.Entry5 = tk.Entry(self.Labelframe2)
        self.Entry5.place(relx=0.203, rely=0.129, height=30, relwidth=0.261
                , bordermode='ignore')
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry6 = tk.Entry(self.Labelframe2)
        self.Entry6.place(relx=0.203, rely=0.387, height=30, relwidth=0.312
                , bordermode='ignore')
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")
        self.Entry7 = tk.Entry(self.Labelframe2)
        self.Entry7.place(relx=0.203, rely=0.71, height=30, relwidth=0.244
                , bordermode='ignore')
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")
        self.Label8 = tk.Label(self.Labelframe2)
        self.Label8.place(relx=0.559, rely=0.387, height=41, width=74
                , bordermode='ignore')
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Modele:''')
        self.Label9 = tk.Label(self.Labelframe2)
        self.Label9.place(relx=0.559, rely=0.71, height=31, width=74
                , bordermode='ignore')
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(compound='left')
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Anné:''')
        self.Entry8 = tk.Entry(self.Labelframe2)
        self.Entry8.place(relx=0.729, rely=0.387, height=40, relwidth=0.244
                , bordermode='ignore')
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(insertbackground="black")
        self.Entry9 = tk.Entry(self.Labelframe2)
        self.Entry9.place(relx=0.729, rely=0.71, height=30, relwidth=0.193
                , bordermode='ignore')
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(insertbackground="black")
        self.Labelframe3 = tk.LabelFrame(self.TNotebook1_t2)
        self.Labelframe3.place(relx=0.0, rely=0.395, relheight=0.5
                , relwidth=0.983)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="#000000")
        self.Labelframe3.configure(text='''infos propriétaire''')
        self.Labelframe3.configure(background="#ff8040")
        self.Label10 = tk.Label(self.Labelframe3)
        self.Label10.place(relx=0.017, rely=0.14, height=31, width=74
                , bordermode='ignore')
        self.Label10.configure(anchor='w')
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(compound='left')
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Nom:''')
        self.Label11 = tk.Label(self.Labelframe3)
        self.Label11.place(relx=0.017, rely=0.326, height=31, width=74
                , bordermode='ignore')
        self.Label11.configure(anchor='w')
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(compound='left')
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''Prénom:''')
        self.Label12 = tk.Label(self.Labelframe3)
        self.Label12.place(relx=0.017, rely=0.512, height=31, width=74
                , bordermode='ignore')
        self.Label12.configure(anchor='w')
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(compound='left')
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''courriel:''')
        self.Label13 = tk.Label(self.Labelframe3)
        self.Label13.place(relx=0.017, rely=0.744, height=31, width=74
                , bordermode='ignore')
        self.Label13.configure(anchor='w')
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(compound='left')
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text='''Téléphone:''')
        self.Entry10 = tk.Entry(self.Labelframe3)
        self.Entry10.place(relx=0.153, rely=0.14, height=30, relwidth=0.295
                , bordermode='ignore')
        self.Entry10.configure(background="white")
        self.Entry10.configure(disabledforeground="#a3a3a3")
        self.Entry10.configure(font="TkFixedFont")
        self.Entry10.configure(foreground="#000000")
        self.Entry10.configure(insertbackground="black")
        self.Entry11 = tk.Entry(self.Labelframe3)
        self.Entry11.place(relx=0.153, rely=0.326, height=30, relwidth=0.414
                , bordermode='ignore')
        self.Entry11.configure(background="white")
        self.Entry11.configure(disabledforeground="#a3a3a3")
        self.Entry11.configure(font="TkFixedFont")
        self.Entry11.configure(foreground="#000000")
        self.Entry11.configure(insertbackground="black")
        self.Entry12 = tk.Entry(self.Labelframe3)
        self.Entry12.place(relx=0.153, rely=0.512, height=30, relwidth=0.498
                , bordermode='ignore')
        self.Entry12.configure(background="white")
        self.Entry12.configure(disabledforeground="#a3a3a3")
        self.Entry12.configure(font="TkFixedFont")
        self.Entry12.configure(foreground="#000000")
        self.Entry12.configure(insertbackground="black")
        self.Entry13 = tk.Entry(self.Labelframe3)
        self.Entry13.place(relx=0.153, rely=0.744, height=30, relwidth=0.397
                , bordermode='ignore')
        self.Entry13.configure(background="white")
        self.Entry13.configure(disabledforeground="#a3a3a3")
        self.Entry13.configure(font="TkFixedFont")
        self.Entry13.configure(foreground="#000000")
        self.Entry13.configure(insertbackground="black")
        self.Button4 = tk.Button(self.TNotebook1_t2)
        self.Button4.place(relx=0.1, rely=0.907, height=34, width=97)
        self.Button4.configure(activebackground="beige")
        self.Button4.configure(activeforeground="black")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(compound='left')
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''ajouter''')
        self.Button5 = tk.Button(self.TNotebook1_t2)
        self.Button5.place(relx=0.517, rely=0.907, height=34, width=137)
        self.Button5.configure(activebackground="beige")
        self.Button5.configure(activeforeground="black")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(compound='left')
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Rechercher''')
        self.Label14 = tk.Label(self.TNotebook1_t3)
        self.Label14.place(relx=0.033, rely=0.047, height=41, width=114)
        self.Label14.configure(anchor='w')
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(compound='left')
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(text='''Numéro plaque:''')
        self.Label15 = tk.Label(self.TNotebook1_t3)
        self.Label15.place(relx=0.033, rely=0.186, height=41, width=114)
        self.Label15.configure(anchor='w')
        self.Label15.configure(background="#d9d9d9")
        self.Label15.configure(compound='left')
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(text='''Numéro technicien:''')
        self.Entry14 = tk.Entry(self.TNotebook1_t3)
        self.Entry14.place(relx=0.25, rely=0.047, height=40, relwidth=0.34)
        self.Entry14.configure(background="white")
        self.Entry14.configure(disabledforeground="#a3a3a3")
        self.Entry14.configure(font="TkFixedFont")
        self.Entry14.configure(foreground="#000000")
        self.Entry14.configure(insertbackground="black")
        self.Entry15 = tk.Entry(self.TNotebook1_t3)
        self.Entry15.place(relx=0.25, rely=0.186, height=40, relwidth=0.307)
        self.Entry15.configure(background="white")
        self.Entry15.configure(disabledforeground="#a3a3a3")
        self.Entry15.configure(font="TkFixedFont")
        self.Entry15.configure(foreground="#000000")
        self.Entry15.configure(insertbackground="black")
        self.Labelframe4 = tk.LabelFrame(self.TNotebook1_t3)
        self.Labelframe4.place(relx=0.017, rely=0.326, relheight=0.453
                , relwidth=0.95)
        self.Labelframe4.configure(relief='groove')
        self.Labelframe4.configure(foreground="#000000")
        self.Labelframe4.configure(text='''infos réparation''')
        self.Labelframe4.configure(background="#ff8040")
        self.Label16 = tk.Label(self.Labelframe4)
        self.Label16.place(relx=0.018, rely=0.113, height=46, width=101
                , bordermode='ignore')
        self.Label16.configure(anchor='w')
        self.Label16.configure(background="#d9d9d9")
        self.Label16.configure(compound='left')
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(text='''Code:''')
        self.Label17 = tk.Label(self.Labelframe4)
        self.Label17.place(relx=0.018, rely=0.4, height=46, width=104
                , bordermode='ignore')
        self.Label17.configure(anchor='w')
        self.Label17.configure(background="#d9d9d9")
        self.Label17.configure(compound='left')
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(text='''Description:''')
        self.Label18 = tk.Label(self.Labelframe4)
        self.Label18.place(relx=0.018, rely=0.769, height=35, width=104
                , bordermode='ignore')
        self.Label18.configure(anchor='w')
        self.Label18.configure(background="#d9d9d9")
        self.Label18.configure(compound='left')
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(foreground="#000000")
        self.Label18.configure(text='''Date:''')
        self.Entry16 = tk.Entry(self.Labelframe4)
        self.Entry16.place(relx=0.211, rely=0.113, height=40, relwidth=0.253
                , bordermode='ignore')
        self.Entry16.configure(background="white")
        self.Entry16.configure(disabledforeground="#a3a3a3")
        self.Entry16.configure(font="TkFixedFont")
        self.Entry16.configure(foreground="#000000")
        self.Entry16.configure(insertbackground="black")
        self.Entry17 = tk.Entry(self.Labelframe4)
        self.Entry17.place(relx=0.211, rely=0.359, height=60, relwidth=0.709
                , bordermode='ignore')
        self.Entry17.configure(background="white")
        self.Entry17.configure(disabledforeground="#a3a3a3")
        self.Entry17.configure(font="TkFixedFont")
        self.Entry17.configure(foreground="#000000")
        self.Entry17.configure(insertbackground="black")
        self.Entry18 = tk.Entry(self.Labelframe4)
        self.Entry18.place(relx=0.228, rely=0.769, height=40, relwidth=0.253
                , bordermode='ignore')
        self.Entry18.configure(background="white")
        self.Entry18.configure(disabledforeground="#a3a3a3")
        self.Entry18.configure(font="TkFixedFont")
        self.Entry18.configure(foreground="#000000")
        self.Entry18.configure(insertbackground="black")
        self.Label19 = tk.Label(self.Labelframe4)
        self.Label19.place(relx=0.526, rely=0.769, height=31, width=64
                , bordermode='ignore')
        self.Label19.configure(anchor='w')
        self.Label19.configure(background="#d9d9d9")
        self.Label19.configure(compound='left')
        self.Label19.configure(disabledforeground="#a3a3a3")
        self.Label19.configure(foreground="#000000")
        self.Label19.configure(text='''Montant:''')
        self.Entry19 = tk.Entry(self.Labelframe4)
        self.Entry19.place(relx=0.649, rely=0.769, height=30, relwidth=0.218
                , bordermode='ignore')
        self.Entry19.configure(background="white")
        self.Entry19.configure(disabledforeground="#a3a3a3")
        self.Entry19.configure(font="TkFixedFont")
        self.Entry19.configure(foreground="#000000")
        self.Entry19.configure(insertbackground="black")
        self.Button6 = tk.Button(self.TNotebook1_t3)
        self.Button6.place(relx=0.067, rely=0.814, height=44, width=97)
        self.Button6.configure(activebackground="beige")
        self.Button6.configure(activeforeground="black")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(compound='left')
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Ajouter''')
        self.Button7 = tk.Button(self.TNotebook1_t3)
        self.Button7.place(relx=0.367, rely=0.814, height=44, width=107)
        self.Button7.configure(activebackground="beige")
        self.Button7.configure(activeforeground="black")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(compound='left')
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''Supprimer''')
        self.Label20 = tk.Label(self.TNotebook1_t4)
        self.Label20.place(relx=0.033, rely=0.047, height=51, width=114)
        self.Label20.configure(anchor='w')
        self.Label20.configure(background="#d9d9d9")
        self.Label20.configure(compound='left')
        self.Label20.configure(disabledforeground="#a3a3a3")
        self.Label20.configure(foreground="#000000")
        self.Label20.configure(text='''Numéro plaque:''')
        self.Label21 = tk.Label(self.TNotebook1_t4)
        self.Label21.place(relx=0.033, rely=0.209, height=41, width=114)
        self.Label21.configure(anchor='w')
        self.Label21.configure(background="#d9d9d9")
        self.Label21.configure(compound='left')
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#000000")
        self.Label21.configure(text='''Marque voiture:''')
        self.TCombobox1 = ttk.Combobox(self.TNotebook1_t4)
        self.TCombobox1.place(relx=0.283, rely=0.047, relheight=0.119
                , relwidth=0.288)
        self.TCombobox1.configure(textvariable=self.combobox)
        self.TCombobox1.configure(takefocus="")
        self.Button8 = tk.Button(self.TNotebook1_t4)
        self.Button8.place(relx=0.65, rely=0.047, height=44, width=137)
        self.Button8.configure(activebackground="beige")
        self.Button8.configure(activeforeground="black")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(compound='left')
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''Afficher réparations''')
        self.Entry20 = tk.Entry(self.TNotebook1_t4)
        self.Entry20.place(relx=0.267, rely=0.209, height=40, relwidth=0.24)
        self.Entry20.configure(background="white")
        self.Entry20.configure(disabledforeground="#a3a3a3")
        self.Entry20.configure(font="TkFixedFont")
        self.Entry20.configure(foreground="#000000")
        self.Entry20.configure(insertbackground="black")

def start_up():
    unknown_support.main()

# if __name__ == '__main__':
#     unknown_support.main()



if __name__ == '__main__':
    root=tk.Tk()
    projetfinalui:ProjetFinalUI=ProjetFinalUI(root)
    root.mainloop()
