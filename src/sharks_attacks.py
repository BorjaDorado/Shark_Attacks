import pandas as pd
import numpy as np
import re

def clean_date(date):
    pattern = r'(\d{2})[/-](\w{3})[/-](\d{4})'  # Patrón regex para identificar la fecha
    match = re.match(pattern, date)  # Buscar el patrón en la fecha

    if match:
        day = match.group(1)  # Extraer el día
        month = match.group(2)  # Extraer el mes
        year = match.group(3)  # Extraer el año

        # Convertir el mes a formato deseado (en este caso, triple abreviatura)
        month_dict = {
            'Jan': 'Jan', 'Feb': 'Feb', 'Mar': 'Mar', 'Apr': 'Apr', 'May': 'May', 'Jun': 'Jun',
            'Jul': 'Jul', 'Aug': 'Aug', 'Sep': 'Sep', 'Oct': 'Oct', 'Nov': 'Nov', 'Dec': 'Dec'
        }

        if month in month_dict:
            month = month_dict[month]

        # Devolver la fecha en el formato deseado
        return f'{day}-{month}-{year}'

    else:
        return None  # Devolver None si no se encuentra el patrón en la fecha

def clean_date_case_number(case_number):
    case_number = str(case_number)
    pattern = r'(\d{4})\.(\d{2})\.(\d{2})'
    match = re.search(pattern, case_number)

    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))

        if month == 0 or day == 0:
            return np.nan

        try:
            return pd.to_datetime(f'{year}-{month:02d}-{day:02d}')
        except ValueError:
            return np.nan
    else:
        return np.nan

def clean_strings(x):
    x = str(x)
    pattern= re.findall(r'[a-zA-Z\(\)\-\?]+', x)
    if x == 'Unknown':
        return None
    elif pattern:
        return x.lower()

def clean_location(df, columna):
    df[columna] = df[columna].astype(str)
    df[columna] = df[columna].apply(lambda x: re.sub(r'(\d+|º)', '', x))  # eliminar datos numéricos y símbolo º
    df[columna] = df[columna].apply(lambda x: re.sub(r'\b(west|north|south|east)\b', '', x, flags=re.IGNORECASE))  # eliminar palabras "west", "north", "south" y "east"
    df[columna] = df[columna].apply(lambda x: x.strip())  # eliminar espacios en blanco al inicio o final
    df[columna] = np.where(df[columna].str.isnumeric(), np.nan, df[columna])  # valores numéricos como NaN
    return df

def limpiar_genero(df, columna):
    df[columna] = df[columna].astype(str)
    df[columna] = df[columna].apply(lambda x: re.sub(r'[^\w\s]', '', x))  # eliminar todos los símbolos
    df[columna] = df[columna].apply(lambda x: re.sub(r'\s+', '', x))  # eliminar espacios en blanco
    df[columna] = np.where(df[columna].str.contains('^F|^f|^Fe|^fe', regex=True), 'F',
                           np.where(df[columna].str.contains('^M|^m|^Ma|^ma', regex=True), 'M', np.nan))
    return df

def age_filt(x):
    x = str(x)
    age_pattern = r"\b(\d{2})\b"  # Extracts two-digit numbers
    match = re.search(age_pattern, x)

    if match:
        age = int(match.group(1))
        return int(age)
    else:
        return np.nan

def clean_fatal(x):
    x = str(x)
    pattern1 = r"[nN]"
    pattern2 = r"[yY]"

    if x == 'UNKNOWN':

        return np.nan

    elif re.findall(pattern1, x):

        return False

    elif re.findall(pattern2, x):

        return True

def limpiar_hora(hora):
    if isinstance(hora, str):
        hora = hora.strip().lower()
        if 'between' in hora:
            hora = hora.split('between')[-1].strip()
        if 'sometime' in hora:
            hora = hora.split('sometime')[-1].strip()

        # Limpieza del formato hhoo
        if 'oo' in hora:
            hora = hora.replace('oo', '00')

        # Limpieza del formato hhmm
        if hora.endswith('h') or hora.endswith('hh'):
            hora = hora[:-1].strip()
            if len(hora) < 4:
                hora = hora.zfill(4)

        if hora.startswith('just before') or hora.startswith('just after'):
            hora = hora.split('before')[-1].strip()
            hora = hora.split('after')[-1].strip()

        # Limpieza de otros formatos
        formatos_fecha = ['%Hh%M', '%Hh%M:%S', '%H:%M']
        for formato in formatos_fecha:
            try:
                hora_dt = pd.to_datetime(hora, format=formato)
                return hora_dt.time()
            except ValueError:
                continue

    return np.nan

