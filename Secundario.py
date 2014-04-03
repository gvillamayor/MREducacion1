#!/usr/bin/env python

# Read specific rows at csv file
# 
# Usage:
#    a csv file
#    a column to filter as (usually a name)
#    a column to assign as values of that name to check
#
import csv
import mincemeat
import string




def mapfn(key,val):
   
    for w in val:
        provincia = w.split(",")[0]
        cantidad = w.split(",")[1]
        yield provincia, int(cantidad)

def reducefn(provincia, cantidad):
    result = 0
    for v in provincia:
        result = sum(cantidad)
        print provincia, sum(cantidad)     
        return provincia, result
     
if __name__ == '__main__':

    import sys
    if len(sys.argv) != 4:
        print "Usage:\n", sys.argv[0], \
                    " [CSV file] [filter column] [number column]"
        exit(-1)

    fname = sys.argv[1]
    col_n = int(sys.argv[2])
    col_v = int(sys.argv[3])
    
    f = open(fname, 'r')     # Open input CSV file
    allrows = csv.reader(f, dialect=csv.excel)
    primeraEtapa = {}
    errores =0
    index=0
    
    for index, row in enumerate(allrows):
        try:
            
            b = string.join (row, ',')
            primeraEtapa[index]=[row[col_n]+","+row[col_v]]
            #print(row[col_v])
        except:
            errores = errores + 1
    #print (source_data)
    print ("Errores: ",errores)
    s = mincemeat.Server()
    s.datasource = primeraEtapa
    s.mapfn = mapfn
    s.reducefn = reducefn
    resultado = s.run_server(password="changeme")
    print "resultados",resultado
    

