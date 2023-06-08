import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = "C:/Users/bdlk2/OneDrive/Área de Trabalho/python/PRO_1-1_C103_AtividadeDoAluno1-main"
class fileevent(FileSystemEventHandler):
    def oncreate(self,event):
        print(f"{event.src_path} foi criado")
    def ondelete(self,event):
        print(f"arquivo excluido{event.scr_path}")
    def onmodificate(self,event):
        print(f"arquivo modificado{event.scr_path}")
    def onmove(self,event):
        print(f"arquivo movido de {event.scr_path}para{event.dest_path}")    
eventh=fileevent()
observer=Observer()
observer.schedule(eventh,from_dir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("funcionando")
except KeyboardInterrupt:
    print("interrompido")
    observer.stop()

