class menu:
  def __init__(self, lunes, martes, miercoles, jueves, viernes, sabado, domingo):
    self.lunes = lunes
    self.martes = martes
    self.miercoles = miercoles
    self.jueves = jueves
    self.viernes = viernes
    self.sabado = sabado
    self.domingo = domingo
    
  def guarnicion(self):
   print("guarnicion: papas fritas, ensalada verde o pure de papas")
   
menu1 = menu("arros", "estofado", "pati", "milanesa", "pizza", "asado", "pastas")
print(menu1.lunes)
menu1.guarnicion()