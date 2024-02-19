# Definiciones Generales

- 2FN / 3FN. Tienen en cuenta todas las claves candidatas

- 1FN. Modificaci´on no afecta a 1FN ya que es independiente de claves

- Atributo Primo. Atributo que es parte de alguna CK


# 1FN


# 2FN

**2FN**. Un esquema R esta en 2FN si todo atributo no primo A de R no depende parcialmente (de manera funcional) de ninguna clave de R

**2FN. Definicion Alternativa**. Un esquema R esta en 2FN si todo atributo no primo A de R depende completamente (de manera funcional) de todas las claves de R

# 3FN

**3FN**. Un esquema R esta en 3FN si, para toda dependencia funcional no trivial X → A de R, se cumple alguna de las siguientes condiciones: 
- X es SK de R 
- A es atributo primo de R

**DF trivial**. La DF A → B es trivial si B es un subconjunto de atributos de A.
Ej. A → A es una DF trivial