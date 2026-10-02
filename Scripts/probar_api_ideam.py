"""Prueba de conexión a la API de precipitación del IDEAM (datos.gov.co, dataset s54a-sgyg).

Solo librería estándar. Dos modos:
  explorar : muestra cómo vienen los campos y qué estaciones hay en un municipio.
  dia      : suma la lluvia por estación y por día y la guarda en data/ideam/*.csv

Ejemplos:
  python probar_api_ideam.py explorar --municipio CERRITO
  python probar_api_ideam.py dia --municipio CERRITO --desde 2023-01-01 --hasta 2023-02-01
"""
import argparse
import csv
import json
import os
import time
import urllib.parse
import urllib.request

BASE = "https://www.datos.gov.co/resource/s54a-sgyg.json"


def consulta(params, token=None, timeout=180):
    url = BASE + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    headers = {"Accept": "application/json"}
    if token:
        headers["X-App-Token"] = token
    inicio = time.time()
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=timeout) as r:
        datos = json.load(r)
    print(f"  -> {len(datos)} filas en {time.time() - inicio:.1f}s")
    return datos


def filtro(municipio, desde, hasta, departamento="VALLE DEL CAUCA"):
    # OJO: sin filtrar por departamento, "CERRITO" matchea un municipio homónimo en Santander.
    # En El Cerrito (Valle) el IDEAM NO tiene estaciones de precipitación; la más cercana
    # con datos reales es Palmira (2 estaciones, ~960k lecturas historicas).
    return (f"departamento='{departamento}' AND upper(municipio) like '%{municipio.upper()}%' "
            f"AND fechaobservacion >= '{desde}T00:00:00' AND fechaobservacion < '{hasta}T00:00:00'")


def explorar(args):
    print("1) Tres filas cualquiera, para ver el formato de los campos:")
    for fila in consulta({"$limit": 3}, args.token):
        print("   ", fila)

    print(f"\n2) Estaciones y sensores en '{args.municipio}' entre {args.desde} y {args.hasta}:")
    filas = consulta({
        "$select": "codigoestacion,nombreestacion,municipio,departamento,descripcionsensor,unidadmedida,latitud,longitud,count(*) as n",
        "$where": filtro(args.municipio, args.desde, args.hasta),
        "$group": "codigoestacion,nombreestacion,municipio,departamento,descripcionsensor,unidadmedida,latitud,longitud",
        "$limit": 200,
    }, args.token)
    for f in filas:
        print("   ", f)
    if not filas:
        print("   (vacío: prueba otro texto de municipio o otro rango de fechas)")


def dia(args):
    print(f"Lluvia diaria por estación en '{args.municipio}' entre {args.desde} y {args.hasta}")
    filas = consulta({
        "$select": "codigoestacion,nombreestacion,municipio,date_trunc_ymd(fechaobservacion) as dia,sum(valorobservado) as lluvia_mm,count(*) as lecturas",
        "$where": filtro(args.municipio, args.desde, args.hasta) + " AND upper(descripcionsensor) like '%PRECIPITACI%'",
        "$group": "codigoestacion,nombreestacion,municipio,dia",
        "$order": "dia",
        "$limit": 50000,
    }, args.token)
    if not filas:
        print("Sin datos.")
        return
    os.makedirs(os.path.join("data", "ideam"), exist_ok=True)
    ruta = os.path.join("data", "ideam", f"lluvia_diaria_{args.municipio.lower()}_{args.desde}_{args.hasta}.csv")
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    print(f"Guardado en {ruta}")
    for f in filas[:5]:
        print("   ", f)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("modo", choices=["explorar", "dia"])
    p.add_argument("--municipio", default="PALMIRA", help="texto contenido en el nombre del municipio (dentro de Valle del Cauca)")
    p.add_argument("--desde", default="2023-01-01")
    p.add_argument("--hasta", default="2023-02-01")
    p.add_argument("--token", default=os.environ.get("SOCRATA_APP_TOKEN"))
    a = p.parse_args()
    explorar(a) if a.modo == "explorar" else dia(a)
