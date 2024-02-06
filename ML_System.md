# Diseño del Sistema de ML

# Índice
1. [Titulo](#diseño-del-sistema-de-ml)
2. [Extraccion de datos](#extraccion-de-datos)
3. [Matematicas financieras](#matematicas-financieras)
4. [Transformaciones](#transformaciones)

# Extraccion de datos
### Dataset crudo:
    - High
    - Low
    - Open
    - Close
    - Volume

- lista de cryptos: [
    "BTC",
    "ETH",
    "BNB",
    "DOGE",
    "TRX",
    "LTC",
    "XRP",
    "SOL",
    "MATIC",
    "ADA"
]    

## [Matematicas financieras](https://es.wikipedia.org/wiki/Matem%C3%A1tica_financiera)

## Transformaciones

- Trabajar con los retornos/ profit
    $ (P_t - P_t1) / P_t $

- Trabajar con lags:
    los lags son agregar como feature el precio o valor de un dia anterior $ t_i $

- crear features de analisis tecnico:
    ### Medias moviles:
    -  Medias móviles simples
    - Medias móviles ponderadas
    - Bandas de Bollinger 
    
    
    ### Osciladores:
    Los osciladores son modelos matemáticos aplicados al precio, basados en alguna observación específica sobre el comportamiento del mercado. Normalmente se grafican por debajo de la gráfica de cotizaciones, ya sea como líneas o histogramas, y miden la fortaleza de las tendencias o movimientos en el precio. Cuando se detecta debilidad en la tendencia, se sospecha que podría estar cerca de revertirse
    
    - Momentum (Momentum) [wikipedia](https://es.wikipedia.org/wiki/Momentum_(an%C3%A1lisis_t%C3%A9cnico))

    - Oscilador Estocástico (Oscilador estocástico): [wikipedia](https://es.wikipedia.org/wiki/Oscilador_estoc%C3%A1stico)

        $ S = 100(\frac{VC - Min}{Max - Min})$

    - RSI (Indice de fuerza relativa): [wikipedia](https://es.wikipedia.org/wiki/%C3%8Dndice_de_fuerza_relativa)
    
        $  RS = \frac{EMA[N] de U}{EMA[N] de D}$
    
        $ RSI = 100 - 100  \frac{1}{1+RS}$

    - MACD (Moving Average Convergence/Divergence - Convergencia/Divergencia del Promedio Móvil): [wikipedia]()

        $ MACD=PME(12)-PME(26)$ donde PME es Promedio Móvil Exponencial.

        $ Señal=PME(9,MACD)$

        $ Histograma= MACD-Señal$


### Que tipo de Features pueden agregar valor al vector X para producir una mejor prediccion


### Riesgo de mercado
El **riesgo de mercado** es el riesgo a las pérdidas del valor de un activo asociado a la fluctuación de su precio en el mercado

### Tipos
Algunos riesgos de mercado incluyen:

- **Riesgo de renta variable**, el riesgo de que el precio de acciones o índices bursátiles (p. ej. Euro Stoxx 50, etc.) y/o su volatilidad implícita cambiarán.
- **Riesgo de tipo de interés**, el riesgo de que el precio del tipo de interés (p. ej. Libor, Euribor, etc.) y/o su volatilidad implícita cambiarán.
- **Riesgo cambiario**, el riesgo de que los tipos de cambio (p. ej. EUR/USD, EUR/GBP, etc.) y/o su volatilidad implícita cambiarán.
- **Riesgo de mercancía**, el riesgo de que el precio de una mercancía (p. ej. maíz, cobre, petróleo, etc.) y/o su volatilidad implícita cambiarán.

## Sistema

```
