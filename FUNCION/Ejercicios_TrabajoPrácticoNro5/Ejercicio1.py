def validate_dni(number_dni):
    # Convierte el número de DNI a una cadena para contar los dígitos
    dni_str = str(number_dni)
    
    # Verifica si la longitud de la cadena está entre 7 y 8 dígitos
    if dni_str.isdigit() and 7 <= len(dni_str) <= 8:
        return True
    else:
        return False
