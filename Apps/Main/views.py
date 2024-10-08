from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db import connections
from django.http import JsonResponse
from django.http import HttpResponse, Http404
import requests
import json
from base64 import b64encode
import requests
from requests.exceptions import Timeout, ConnectionError

# Create your views here.


def LogIn (request):
    return render (request, 'Main/Login/login.html')

@login_required
def GM(request):
    return render (request, 'Main/Main/index.html')

@login_required
def verPlus(request):
    return render (request, 'Main/Plus/verPlus.html')

@csrf_exempt
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            data = "Se inicio sesion."
            return JsonResponse({'Message': 'success', 'data': data})
        else:
            data = "No se pudo iniciar sesión, verifique los datos."
            return JsonResponse({'Message': 'Error', 'data': data})
    else:
        data = "No se pudo resolver la Petición"
        return JsonResponse({'Message': 'Error', 'Nota': data})
    



######################## PLUS ###########################


#Petición datos iniciales:

def dataInicialPlus(request):
    if request.method == 'GET':
        try:
            with connections['GM'].cursor() as cursor:

                listado_mercado = []
                listado_etiqueta = [{'IdEtiqueta': '0', 'Descripcion': 'TODO'}]
                listado_especie = [{'IdEspecie': '0', 'Descripcion': 'TODO'}]
                listado_calibres = [{'IdCalibre': '0', 'Calibre': 'TODO'}]

                ## MERCADO
                sql = """SELECT Nombre, Descripcion FROM Mercado WHERE Nombre NOT IN ('CON','MIN', 'IND')"""
                cursor.execute(sql)
                consulta = cursor.fetchall()
                if consulta:
                    for row in consulta:
                        nombre = str(row[0])
                        descripcion = str(row[1])
                        datos = {'IdMercado': nombre, 'Descripcion': descripcion}
                        listado_mercado.append(datos)

                ## ETIQUETA
                sql2 = """SELECT IdEtiqueta, Descripcion FROM Etiqueta"""
                cursor.execute(sql2)
                consulta2 = cursor.fetchall()
                if consulta2:
                    for row2 in consulta2:
                        idEtiqueta = str(row2[0])
                        descripcion1 = str(row2[1])
                        datos2 = {'IdEtiqueta': idEtiqueta, 'Descripcion': descripcion1}
                        listado_etiqueta.append(datos2)

                ## ESPECIE
                sql3 = """SELECT IdEspecie, Nombre FROM Especie ORDER BY Nombre"""
                cursor.execute(sql3)
                consulta3 = cursor.fetchall()
                if consulta3:
                    for row3 in consulta3:
                        idEspecie = str(row3[0])
                        nombre = str(row3[1])
                        datos3 = {'IdEspecie': idEspecie, 'Descripcion': nombre}
                        listado_especie.append(datos3)

                sql4 = """SELECT TRIM(LEADING '0' FROM USR_DES) AS ID, TRIM(LEADING '0' FROM USR_DES) AS CALIBRE 
                        FROM `USR_CALIBRE` 
                        WHERE USR_DES NOT IN ('000','1/2','GENERICO','SAF') 
                        ORDER BY USR_DES;"""
                cursor.execute(sql4)
                consulta4 = cursor.fetchall()
                if consulta4:
                    for row4 in consulta4:
                        idCalibre = str(row4[0])
                        calibre = str(row4[1])
                        datos4 = {'IdCalibre': idCalibre, 'Calibre': calibre}
                        listado_calibres.append(datos4)


                if listado_mercado and listado_etiqueta and listado_especie:
                    return JsonResponse({'Message': 'Success', 'DataMercado': listado_mercado, 'DataEtiqueta': listado_etiqueta, 'DataEspecie': listado_especie, 'DataCalibres': listado_calibres})
                else:
                    return JsonResponse({'Message': 'Not Found', 'Nota': 'No se pudieron obtener los datos.'})
        except Exception as e:
            error = str(e)
            return JsonResponse({'Message': 'Error', 'Nota': error})
        finally:
            cursor.close()
            connections['GM'].close()
    else:
        return JsonResponse({'Message': 'No se pudo resolver la petición.'})
    
@csrf_exempt
def dataSubItems(request):
    if request.method == 'POST':
        tipo = request.POST['Tipo']
        IdElemento = request.POST['IdElemento']
        values = [IdElemento,IdElemento]
        try:
            with connections['GM'].cursor() as cursor:

                listado = [{'Id': '0', 'Descripcion': 'TODO'}]
                listado2 = [{'Id': '0', 'Descripcion': 'TODO'}]
                
                if tipo == 'VAR':
                    sql = """SELECT IdVariedad, Nombre FROM Variedad WHERE (%s = '0' OR IdEspecie = %s) ORDER BY Nombre"""
                    cursor.execute(sql, values)
                    consulta = cursor.fetchall()
                    if consulta:
                        for row in consulta:
                            Id = str(row[0])
                            descripcion = str(row[1])
                            datos = {'Id': Id, 'Descripcion': descripcion}
                            listado.append(datos)
                    sql2 = """SELECT E.IdEnvase, RTRIM(E.Nombre) FROM Envase AS E LEFT JOIN TamañoEnvase AS TE ON (E.IdEnvase = TE.IdEnvase) WHERE (%s = '0' OR TE.IdEspecie = %s) ORDER BY E.Nombre;"""
                    cursor.execute(sql2, values)
                    consulta2 = cursor.fetchall()
                    if consulta2:
                        for row in consulta2:
                            Id = str(row[0])
                            descripcion = str(row[1])
                            datos2 = {'Id': Id, 'Descripcion': descripcion}
                            listado2.append(datos2)


                if tipo == 'CLI':
                    sql = """SELECT VTMCLH_NROCTA, VTMCLH_NOMBRE FROM VTMCLH WHERE (%s = '0' OR VTMCLH_CODZON = %s) ORDER BY VTMCLH_NOMBRE;"""
                    cursor.execute(sql, values)
                    consulta = cursor.fetchall()
                    if consulta:
                        for row in consulta:
                            Id = str(row[0])
                            descripcion = str(row[1]).upper()
                            datos = {'Id': Id, 'Descripcion': descripcion}
                            listado.append(datos)

                if listado:
                    return JsonResponse({'Message': 'Success', 'Tipo': tipo, 'DataListado':listado, 'DataListado2': listado2})
                else:
                    return JsonResponse({'Message': 'Not Found', 'Nota': 'No se pudo obtener los datos.'})
        except Exception as e:
            error = str(e)
            return JsonResponse({'Message': 'Error', 'Nota': error})
    else:
        return JsonResponse({'Message': 'No se pudo resolver la petición.'})
    

@csrf_exempt
def busquedaData(request):
    if request.method == 'POST':
        desde = request.POST['Inicio']
        hasta = request.POST['Final']
        mercado = request.POST['Mercado']
        cliente = request.POST['Cliente']
        especie = request.POST['Especie']
        variedad = request.POST['Variedad']
        envase = request.POST['Envase']
        marca = request.POST['Marca']
        calibres = request.POST['Calibres']
        url2 = "http://tresasesvpn.ddnsfree.com:8000/api/demo-general/data-general/with-crc/"

        datos = {
        "Inicio":desde,
        "Final":hasta,
        "Mercado":mercado,
        "Cliente":cliente,
        "Especie":especie,
        "Variedad":variedad,
        "Envase":envase,
        "Marca":marca,
        "Calibres":calibres
        }
        cabeceras = {

        }
        #return JsonResponse({'Message': 'Error', 'Nota': 'Tiempo de espera agotado.'})
        try:
            respuesta = requests.post(url2, json=datos, headers=cabeceras, stream=True, timeout=45)
            respuesta.raise_for_status()  # Lanza una excepción si el código de estado no es 200

            return HttpResponse(respuesta.iter_content(chunk_size=10024), content_type='application/json')

        except requests.exceptions.Timeout:
            return JsonResponse({'Message': 'Error', 'Nota': 'Tiempo de espera agotado.'})

        except requests.exceptions.ConnectionError:
            return JsonResponse({'Message': 'Error', 'Nota': 'Error de conexión.'})

        except requests.exceptions.HTTPError as errh:
            return JsonResponse({'Message': 'Error', 'Nota': f'Error HTTP: {errh}'})

        except requests.exceptions.RequestException as err:
            return JsonResponse({'Message': 'Error', 'Nota': f'Error inesperado: {err}'})

        except Exception as e:
            return JsonResponse({'Message': 'Error', 'Nota': f'Error desconocido: {e}'})
    else:
        return JsonResponse({'Message': 'No se pudo resolver la petición.'})
    


                # datos = respuesta.json()
        
                # # Acceder a los datos
                # mensaje = datos['Message']
                # liquidaciones = datos['Liquidaciones']
                
                # # Imprimir los datos
                # print("Mensaje:", mensaje)
                # print("Liquidaciones:")
                # for liquidacion in liquidaciones:
                #     print("IdLiquidacion:", liquidacion['IdLiquidacion'])
                #     print("Liquidacion:", liquidacion['Liquidacion'])