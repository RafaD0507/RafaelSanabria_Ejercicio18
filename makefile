primera: grafica_primera.pdf

grafica_primera.pdf : primera_derivada_grafica.py datos_primera.txt
	python primera_derivada_grafica.py

datos_primera.txt : d_p.x
	./d_p.x > datos_primera.txt
	rm d_p.x

d_p.x : primera_derivada.cpp
	c++ primera_derivada.cpp -o d_p.x

segunda: grafica_segunda.pdf

grafica_segunda.pdf : segunda_derivada_grafica.py datos_segunda.txt
	python segunda_derivada_grafica.py

datos_segunda.txt : d_s.x
	./d_s.x > datos_segunda.txt
	rm d_s.x

d_s.x : segunda_derivada.cpp
	c++ segunda_derivada.cpp -o d_s.x
