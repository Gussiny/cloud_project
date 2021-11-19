import sys
from mpi4py import MPI
from math import pi, sqrt

comm = MPI.COMM_WORLD
r = comm.Get_rank()

args = sys.argv
altura = 0
radio = 0

figura = int(args[1])

altura = float(args[2])
if (len(args) > 3):
    radio = float(args[3])

if (len(args) > 4):
    ancho = float(args[3])
    largo = float(args[4])


## CILINDRO
if ( figura == 1 ):

    if r == 0:
        print ( "CILINDRO")

        print ( "NODO %d (AREA)" % r )
        area = (2 * radio * pi) * (altura + radio)
        comm.send(area, dest=1)
        
    elif r == 1:
        print ( "NODO %d (VOLUMEN)" % r )
        volumen = ((radio ** 2) * pi * altura)
        print ( "RESULTADO %f" % volumen )
        area = comm.recv(source = 0)
        print ( "RESULTADO %f" % area )

## CUBO
elif ( figura == 2): 

    if r == 0:
        print ( "CUBO")

        print ( "NODO %d (AREA)" % r )
        area = ( 6 * (altura ** 2) )
        print ( "RESULTADO %f" % area )

    elif r == 1:
        print ( "NODO %d (VOLUMEN)" % r )
        volumen = (altura ** 3)
        print ( "RESULTADO %f" % volumen )

## ESFERA
elif ( figura == 3 ): 

    if r == 0:
        print ( "ESFERA")

        print ( "NODO %d (AREA)" % r )
        area = ( 4 * pi * (altura ** 2) )
        print ( "RESULTADO %f" % area )

    elif r == 1:
        print ( "NODO %d (VOLUMEN)" % r )
        volumen = ( 4 * pi  * (altura ** 3) ) / 3
        print ( "RESULTADO %f" % volumen )

## CONO
elif ( figura == 4 ): 

    if r == 0:
        print ( "CONO")

        print ( "NODO %d (AREA)" % r )
        g = sqrt((altura ** 2) + (radio ** 2))
        area = ( (pi * (radio ** 2)) + ( g * pi * radio) )
        print ( "RESULTADO %f" % area )

    elif r == 1:
        print ( "NODO %d (VOLUMEN)" % r )
        volumen = ( (radio ** 2) * pi  * altura ) / 3
        print ( "RESULTADO %f" % volumen )

## PRISMA
elif ( figura == 5 ): 

    if r == 0:
        print ( "PRISMA")

        print ( "NODO %d (AREA)" % r )
        area = ( 2 * altura  * (ancho + largo) + (2 * ancho * largo) )
        print ( "RESULTADO %f" % area )

    elif r == 1:
        print ( "NODO %d (VOLUMEN)" % r )
        volumen = ancho * largo * altura
        print ( "RESULTADO %f" % volumen )