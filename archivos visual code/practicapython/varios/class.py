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

print("El menu del lunes es:", menu1.lunes)
print("El menu del martes es:", menu1.martes)
print("El menu del miércoles es:", menu1.miercoles)
print("El menu del jueves es:", menu1.jueves)
print("El menu del viernes es:", menu1.viernes)
print("El menu del sábado es:", menu1.sabado)
print("El menu del domingo es:", menu1.domingo)