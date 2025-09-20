# CalculoDescuentoPython.py

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento dado un monto total y un porcentaje de descuento.
    
    :param monto_total: float, el monto total de la compra
    :param porcentaje_descuento: float, el porcentaje de descuento (por defecto 10%)
    :return: float, el monto del descuento
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
if __name__ == "__main__":
    # Primera llamada: solo con monto total (usa descuento por defecto del 10%)
    monto1 = 150.00
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1
    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento aplicado (10%): ${descuento1:.2f}")
    print(f"Monto final a pagar: ${total1:.2f}\n")

    # Segunda llamada: con monto total y porcentaje de descuento personalizado
    monto2 = 200.00
    porcentaje2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje2)
    total2 = monto2 - descuento2
    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento aplicado ({porcentaje2}%): ${descuento2:.2f}")
    print(f"Monto final a pagar: ${total2:.2f}")
