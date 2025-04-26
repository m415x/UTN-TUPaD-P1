def leer_entero_validado(
    mensaje="Ingrese un número entero", min=float("-Inf"), max=float("Inf")
) -> int:
    """Solicita un número entero al usuario y lo valida dentro de un rango específico."""

    num = int(input(f"{mensaje}: "))
    while num < min or num > max:
        num = int(input(f"ERROR! {mensaje}: "))

    return num
