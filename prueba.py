# Análiis crecimiento y evolución del Producto Interno Bruto a precios del 2018(PIB real)

# Importar librerías.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

# Cargar archivo.

pib = pd.read_csv('data\pib-precios-2018.csv')

# Grafica 

# 1. Convertir los trimestres de Periodo en formato de fecha. (realmente este el paso 1: dar formato a las cosas)

pib['fecha'] = pd.PeriodIndex(pib['Periodos'].str.replace(r'(\d{4})/0?(\d)', r'\1Q\2', regex=True), freq='Q').to_timestamp()

print(pib.head(4))

# 2. Hacer grafica. 

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(pib['fecha'], pib['PIB'], color='red')

ax.set_title('México. Producto Interno Bruto trimestral, 1980-2026', fontsize=14, fontweight='bold')

# 3. configurar de mejor manera el formato del eje x

ax.xaxis.set_major_locator(mdates.YearLocator(4)) # El paso es cada dos año, modificar el numero para mas o menos años
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y')) # Indica que muestre el formato años
#plt.xticks(rotation=45, ha='right') # rotar el texto y aliniarlo de lado derecho, se puede usar para ha: center, right y left 

# 4. formato del eje y

ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:,.0f}'))
ax.set_ylabel('Millones de pesos')

# 5. Fuente y notas al pie de pagina.

fig.text(0.03, 0.01, 'Fuente: Elaboración propia con datos de INEGI, Banco de Información Económica.', fontsize=8, color='grey', ha='left')
fig.text(0.03, 0.03, 'Nota: Cifras en millones de pesos a precios de 2018.', fontsize=8, color='grey', ha='left')

plt.tight_layout(rect=[0, 0.03, 1, 1])

# 6. Mostrar grafica.

plt.show()