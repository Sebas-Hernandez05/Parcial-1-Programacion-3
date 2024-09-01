from sodapy import Socrata
import pandas as pd

def extraccion(limite_registros, nombre_departamento):
    client = Socrata("www.datos.gov.co", None)

    dataset_identifier = "gt2j-8ykr"

    results = client.get(dataset_identifier, where=f"departamento_nom='{nombre_departamento}'", limit=limite_registros)

    if results:

        results_df = pd.DataFrame.from_records(results)

        subset = results_df[['departamento_nom', 'ciudad_municipio_nom', 'edad','fuente_tipo_contagio', 'estado']]
        return subset
       
    else:
        print("No se encontraron datos para el departamento especificado.")