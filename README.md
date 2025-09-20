# 🧮 Cálculo de Descuento en Compras - Python

Este proyecto en Python tiene como objetivo practicar el uso de **funciones con parámetros**, **valores predeterminados** y **retorno de valores**, mediante el cálculo de descuentos en compras.

---

## 📌 Descripción

El programa contiene una función llamada `calcular_descuento` que toma como entrada el monto total de una compra y un porcentaje de descuento (por defecto 10%), y devuelve el monto del descuento calculado. Luego, muestra el resultado y el monto final a pagar.

---

## ⚙️ Funcionalidades

- Calcula el descuento basado en un porcentaje.
- Usa un valor predeterminado de 10% si no se indica uno diferente.
- Imprime el detalle del monto original, descuento aplicado y monto final.

---

## 🧪 Ejecución del Programa

Ejemplo de uso en el programa principal (`main`):

```python
# Llamada con descuento por defecto del 10%
calcular_descuento(150.00)

# Llamada con descuento personalizado del 15%
calcular_descuento(200.00, 15)
