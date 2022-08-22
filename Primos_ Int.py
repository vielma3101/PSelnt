# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	print " introduzca un numero"
	x = float(raw_input())
	cont = 0
	for a in range(1,x+1):
		if x%1==0:
			cont = cont+1
	if cont==2:
		print x," es un numero primo"
	else:
		print x," no es un numero primo"

