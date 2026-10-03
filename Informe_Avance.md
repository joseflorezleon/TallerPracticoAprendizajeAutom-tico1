# Informe de Avance — Taller Práctico Ingenio Providencia

> Documento de trabajo (borrador vivo). Se irá completando tarea por tarea según el enunciado en `contexto.txt`. Al final, este contenido se traspasará al formato oficial IEEE en `ArchivosImportantes/Formato presentacion documentos.doc` para la entrega (máx. 5 páginas, sin código anexo).

---

## Tarea 1 — Introducción y Contexto del Negocio

> **Cambio (28/9/2026):** la introducción del notebook se reescribió para que siga el documento del equipo `Recursos/Taller Cana de Azucar - Introducción.docx` (dos párrafos y las mismas 9 referencias, con el texto en un tono más natural). Lo que aparece debajo es la **versión extendida anterior**: ya no está en el notebook, pero se conserva aquí como material de apoyo (las cifras sirven para la sustentación oral).
>
> No se tocó nada de lo que el equipo editó a mano: los nombres del encabezado (celda 0) y las celdas de la sección 3.2 (interpretación de la correlación y propuesta de `TCH × %Sacarosa/100`).
>
> Pendiente de revisar en las referencias: la [7] dice "Ingenio Providencia produce el 15% del azúcar en Colombia (2024)", pero el enlace del documento apunta a una nota titulada "100 años Ingenio Providencia" (2026). Conviene confirmar que título y enlace sean la misma fuente.

### (Material de apoyo) 1.1 Importancia Económica y Social del sector azucarero (Valle del Cauca y Colombia)

La agroindustria de la caña de azúcar es uno de los pilares económicos del Valle del Cauca:

- **Participación en el PIB:** el sector representa el **0,6% del PIB nacional** y el **2,4% del PIB agrícola del país**. A nivel regional, su peso es mucho mayor: **21,1% del PIB agrícola** y **10,2% del PIB industrial** del Valle del Cauca [1].
- **Generación de empleo:** la agroindustria genera aproximadamente **286.000 empleos** distribuidos en **50 municipios** de la región (cifra 2025; reportes previos hablaban de ~180.000 empleos, lo que evidencia el crecimiento reciente del sector) [1].
- **Número de ingenios:** operan **13 ingenios azucareros** en la región, de los cuales **6 cuentan con plantas de bioetanol**, diversificando la cadena de valor más allá del azúcar de mesa [1].
- **Producción y productividad:** en 2025 se molieron cerca de **23 millones de toneladas de caña**, un 5% más que en 2024, produciendo cerca de **2 millones de toneladas de azúcar** [1][2]. El rendimiento promedio colombiano (~120 t/ha) **duplica el promedio mundial** (~60 t/ha) [2], aunque ha mostrado caídas recientes (de 127 a ~102-118 t/ha) atribuibles a fenómenos climáticos (La Niña, exceso de lluvias) e inseguridad regional que ha comprometido más de 5.000 hectáreas desde 2014 [2].

**Relevancia para el taller:** estas cifras justifican por qué predecir con precisión el TCH y el %Sac.Caña no es un ejercicio académico aislado — errores de pocos puntos porcentuales en productividad, multiplicados por millones de toneladas, representan pérdidas económicas significativas para una industria que sostiene cientos de miles de empleos en la región.

---

### 1.2 Factores Clave del Rendimiento

#### a) TCH (Toneladas de Caña por Hectárea)

Los principales factores agronómicos que determinan el TCH son:

- **Edad del cultivo y número de cortes:** en estudios de machine learning aplicados a caña de azúcar, el **número de cortes** aparece consistentemente como una de las variables con **mayor importancia predictiva** para el rendimiento [4]. Esto es directamente relevante para el dataset del taller, que incluye `Edad Ult Cos`, `cortes` y `F.Ult.Corte`.
- **Clima:** exceso o déficit de lluvias afecta directamente la productividad — el reciente descenso del rendimiento colombiano se explica en gran parte por un incremento del 25% en las precipitaciones respecto al promedio de 20 años durante el fenómeno de La Niña [2]. Esto valida la inclusión de las numerosas variables climáticas del dataset (`Lluvias Ciclo`, `Temp. Media Ciclo`, `Radiacion Solar Ciclo`, `Evaporacion Ciclo`, etc.).
- **Riego y tecnología:** Cenicaña (centro de investigación del sector) ha impulsado sistemas de riego que reducen el consumo de agua en ~50%, junto con tecnología de sensores y programas de sostenibilidad como *Integra* [2].
- **Suelo, variedad y distancia:** el tipo de suelo, la variedad sembrada y la distancia al ingenio (logística de transporte y tiempo entre corte y molienda) son factores agronómicos y operativos clásicos que también están representados en el dataset (`Suelo`, `Variedad`, `Dist Km`).
- **Estado del arte en modelado:** estudios recientes en Colombia (Universidad Nacional, predicción espacial del rendimiento de caña en el Valle del río Cauca) muestran que modelos de machine learning como **Random Forest, XGBoost y CatBoost superan consistentemente a la regresión lineal y a los modelos penalizados (Ridge/Lasso)** en la predicción de TCH, integrando datos climáticos, de suelo y de manejo agrícola [5]. Esto es un antecedente importante: se espera que nuestros modelos lineales (benchmark del taller) tengan margen de mejora frente a modelos no lineales, lo cual debe discutirse en la sección de conclusiones del informe final.

#### b) Porcentaje de Sacarosa (%Sac.Caña)

La calidad de la caña (contenido de azúcar extraíble) depende de:

- **Variedad:** existen diferencias marcadas entre variedades "precoces" (alcanzan alto contenido de sacarosa a edad temprana) y "tardías" — la variedad determina directamente el potencial de sacarosa, el proceso de maduración y la morfología del tallo [3].
- **Maduración:** es un proceso fisiológico crítico. La sacarosa se acumula cuando la planta detiene su crecimiento vegetativo; **si el agua y el nitrógeno son abundantes, la planta no madura** — de ahí la importancia agronómica de aplicar "madurantes" químicos (dosis controladas) para inducir ese estrés fisiológico, exactamente lo que registran las variables `Dosis Madurante` y `Semanas mad.` del dataset [3].
- **Radiación solar y temperatura:** la tasa fotosintética (que produce la sacarosa) es óptima alrededor de **34°C**; temperaturas más altas durante la maduración disocian la sacarosa en fructosa y glucosa, reduciendo su acumulación. La radiación solar insuficiente también reduce la sacarosa al limitar la fotosíntesis [3][6].
- **Humedad:** la maduración requiere un ambiente relativamente seco (humedad relativa inferior al 65%) [3].

**Relevancia para el taller:** esto confirma que variables como `lluvias`, `Temp. Media Ciclo`, `Dosis Madurante`, `Semanas mad.` y `variedad` no son solo columnas disponibles por casualidad — tienen un fundamento agronómico sólido para ser predictoras relevantes tanto de TCH como de %Sac.Caña, y deben priorizarse en la selección de variables (Tarea 2).

---

### 1.3 El Ingenio Providencia

- **Ubicación y tamaño:** fundado en 1926 por Modesto Cabal Galindo, ubicado en el valle del río Cauca, con su planta principal en **El Cerrito, Valle del Cauca**. Procesa **3,4 millones de toneladas de caña al año**, produciendo cerca de **270.000 toneladas de azúcar** y **67 millones de litros de alcohol** [7].
- **Participación de mercado:** produce el **15% del azúcar de Colombia** [7][8] — es uno de los ingenios más grandes del país (de los 13 que operan en la región).
- **Mercado interno vs. exportación:** aproximadamente el **65% de su producción se queda en el mercado local**, mientras el resto se exporta a **35 países** [7].
- **Sostenibilidad:** es el **primer productor de azúcar orgánica de Colombia** [7], y alcanzó **autosostenibilidad energética**, generando **250.951 MWh** a partir de la biomasa de la caña (bagazo) [7].
- **Implicación para el análisis de datos:** el hecho de que Providencia combine producción convencional y orgánica, y que exporte a mercados exigentes (que probablemente demandan mayor calidad/trazabilidad), sugiere que podrían existir **sub-poblaciones distintas** dentro del dataset (ej. por `grupo_tenencia`, `variedad`, o prácticas de manejo) que valdría la pena explorar en el EDA, ya que un lote destinado a exportación orgánica podría tener un perfil agronómico distinto a uno de mercado interno convencional.

---

### 1.4 Estado del Arte: Machine Learning en Agricultura de Precisión y Predicción de Rendimiento

- **Algoritmos más efectivos:** la evidencia consistente en la literatura reciente (incluyendo estudios colombianos aplicados específicamente al Valle del río Cauca) indica que **Random Forest, XGBoost y CatBoost superan a la regresión lineal y a los métodos penalizados (Ridge/Lasso)** en precisión predictiva para TCH [4][5]. Esto no invalida el uso de modelos lineales en este taller (que sirven como *benchmark* interpretable, tal como pide el enunciado), pero sí anticipa que su desempeño será un piso, no un techo, y justifica proponerlos como "trabajo futuro" en las conclusiones.
- **Variables más predictivas:** el **número de cortes** aparece repetidamente como una de las variables de mayor importancia en modelos de ML para TCH [4]. Otros estudios usan **índices de percepción remota** (NDVI - vegetación, MSI - estrés hídrico, evapotranspiración del cultivo) como entradas de modelos lineales para estimar rendimiento, combinando sensores satelitales con variables de campo [4].
- **Aplicación industrial (no solo agronómica, sino de proceso):** en la industria azucarera colombiana ya se aplican modelos de ML en la planta de procesamiento, no solo en campo. Por ejemplo, el propio **Ingenio Providencia** reportó una **mejora del rendimiento del 10%** y una **reducción del consumo energético del 12%** tras implementar modelos analíticos (regresión lineal y árboles de decisión) sobre variables de proceso (Brix, pureza del jugo, humedad de la caña, peso molido) siguiendo la metodología **CRISP-DM** [9]. Esto confirma que la casa matriz del dataset ya tiene cultura analítica instalada, lo que le da mayor relevancia práctica a este taller.
- **Principal desafío reportado en la literatura:** la **falta de conjuntos de datos de alta calidad** (valores faltantes, inconsistencias, variables no documentadas) es señalada como el principal obstáculo para aplicar ML en agricultura [4] — un desafío que anticipamos enfrentar directamente en la Tarea 2, dado que el dataset `HISTORICO_SUERTES.xlsx` tiene ~60 columnas climáticas/de insumos sin documentar en el diccionario oficial provisto.

---

### Fuentes citadas (Tarea 1)

[1] El País Cali, *"Caña de azúcar, el gran motor de la economía en el Valle del Cauca"* / Asocaña, 2025. https://www.asocana.org/modules/documentos/14167.aspx

[2] La República, *"Rendimiento de la caña de azúcar en Colombia duplica el promedio mundial"*, 2024. https://www.larepublica.co/economia/rendimiento-de-la-cana-de-azucar-en-colombia-duplica-el-promedio-mundial-3876015

[3] Cenicaña, *"Control y Características de Maduración"* y *"Calidad de la Caña de Azúcar"*, Libro El Cultivo de la Caña. https://www.cenicana.org/pdf_privado/documentos_no_seriados/libro_el_cultivo_cana/libro_p297-313.pdf

[4] ResearchGate, *"Predicción del rendimiento de cultivos agrícolas usando aprendizaje automático"*, 2021. https://www.researchgate.net/publication/349207652

[5] Universidad Nacional de Colombia, *"Predicción espacial del rendimiento del cultivo de caña de azúcar (Saccharum officinarum) mediante aprendizaje de máquina"* (Valle del río Cauca, La Candelaria). https://repositorio.unal.edu.co/items/34c4a06a-c916-4060-ad57-28e848712f2b

[6] Agencia de Noticias UNAL / AgroNET, *"Poca luz solar disminuye la sacarosa en el cultivo de caña de azúcar"*. https://agenciadenoticias.unal.edu.co/detalle/poca-luz-solar-disminuye-la-sacarosa-en-el-cultivo-de-cana-de-azucar

[7] Yahoo Finanzas / Tecnicaña, *"Ingenio Providencia produce el 15% del azúcar en Colombia"*, 2024. https://tecnicana.org/2024/05/03/ingenios/ingenio-providencia/ingenio-providencia-produce-el-15-del-azucar-en-colombia/

[8] El País Cali, *"Providencia, primer productor de azúcar orgánica en Colombia"*. https://www.elpais.com.co/contenido/providencia-primer-productor-de-azucar-organica-en-colombia.html

[9] LinkedIn, José Rodríguez, *"De los datos al azúcar: cómo la analítica revoluciona..."* (recurso compartido por el profesor, referencia a mejoras del 10% en rendimiento y 12% en consumo energético en Ingenio Providencia mediante CRISP-DM). https://www.linkedin.com/pulse/de-los-datos-al-az%C3%BAcar-c%C3%B3mo-la-anal%C3%ADtica-revoluciona-jose-rodriguez-p2dqe/

---

## Tarea 2 — Análisis Exploratorio de Datos (EDA) y Preprocesamiento

Desarrollada directamente en el notebook (`Notebooks/Taller_Ingenio_Providencia.ipynb`, secciones 3.1 a 3.12), no en este documento. Resumen de lo que quedó decidido ahí:

- Se filtraron 294 registros de semilla del dataset de regresión.
- TCH y %Sac.Caña tienen correlación baja (r = -0.168) → se modelan por separado.
- Se identificaron y excluyeron 17 variables de *data leakage* (TCHM, TAH, Rdto, Brix, Pureza, etc.), con evidencia numérica de correlación.
- Imputación de nulos según el significado real del vacío (`Producto`/`Dosis Madurante` = "no se aplicó madurante", no una media genérica).
- Vacío estructural de variables climáticas de estación (78% nulas, 2017-2021) documentado como limitación, no imputado con la media global.
- Outliers de TCH evaluados con criterio de negocio (umbrales del Ingenio), no con IQR ciego.
- Chequeo de información mutua para las lluvias (Pearson bajo, pero sí aportan señal no lineal).
- VIF máximo ≈ 4.1 entre las variables numéricas (sin multicolinealidad severa).
- **Definición de niveles alto/medio/bajo para clasificación — cambiado el 1/10/2026:** el profesor indicó que los umbrales de negocio del Ingenio no se pueden usar aquí (son el tema de otro documento del curso). Se reemplazaron por un método estadístico: recortar 5% de cada extremo de la distribución y dividir el resto en tercios. Umbrales resultantes: **TCH ≤127/≤155** (antes 125/150) y **Sacarosa ≤12,33/≤13,27** (antes 12,2/12,9). Esto obligó a recalcular toda la Tarea 3 de clasificación y la Tarea 4 — ver más abajo.
- **Visualización exploratoria (sección 3.9.1, agregada a partir de la propuesta del equipo en `categorizacion variables.docx`):** mapa de calor de correlación, scatterplots de cada numérica vs. cada objetivo, boxplots de outliers de las variables predictoras, y barras/pastel para las categóricas — confirma visualmente que `Cultivo orgánico` tiene menos sacarosa y que `Tipo Quema accidental` tiene menos TCH.

### ✅ Resuelto — propuesta del equipo sobre variables (`categorizacion variables.docx`)

El equipo propuso agregar `Pureza`, `Fosfato Jugo` y `Urea 46%` como predictoras. Se verificó que **`Pureza` y `Fosfato Jugo` nunca llegaron a incluirse en el código** (el notebook ya las excluye desde la sección 3.4, por ser variables de leakage — `Pureza` está nombrada explícitamente como ejemplo de leakage en el FAQ del profesor).

Sobre los fertilizantes, en vez de usar `Urea 46%` sola (solo 3.4% de cobertura), se siguió la propuesta final del equipo: **`usa_fertilizante`**, una bandera binaria que combina los 7 fertilizantes comerciales (`NITO_XTEND`, `Sul.Amonio`, `Boro Granul.`, `MicroZinc`, `MEZ`, `NITRAX-S`, `Urea 46%`), excluyendo explícitamente `Vinaza` (no es fertilizante, es subproducto de la caña para alcohol carburante). Quedó con distribución 76%/24% (ni rara ni dominante), así que se incluyó como variable candidata en ambos modelos de regresión — ya está en el notebook, sección 3.5 y 3.9.

### 📝 Nota abierta / boceto — variable combinada TCH × %Sacarosa/100 (pendiente de decidir)

Durante el EDA se calculó `TAH_aprox = TCH * %Sac.Caña / 100` únicamente como comprobación: confirma que la columna real `TAH` (ya excluida por leakage) es prácticamente reconstruible a partir de los dos objetivos (r = 0.99 contra `TAH`).

Mis compañeros de equipo, trabajando sobre el mismo notebook, propusieron ir más allá y **usar esa misma fórmula como una tercera variable objetivo** (no solo como comprobación), con la idea de que captura mejor el propósito real del negocio: cantidad y calidad de caña juntas, no por separado. También ajustaron el texto de interpretación de la correlación TCH vs. %Sac.Caña (celda 19 del notebook).

Puntos a resolver antes de la entrega final (quedan aquí documentados para retomarlos, ya que por ahora el notebook es solo un boceto):

1. **Decidir si se implementa el tercer modelo** (`TAH_aprox` como objetivo, predicho con las variables agronómicas ya seleccionadas — nunca con TCH o %Sac.Caña como predictores, porque ahí sí sería leakage).
2. Si se implementa, dejar clarísimo en el informe que es un **modelo adicional/bono**, no un reemplazo de los dos que pide explícitamente el enunciado del taller (TCH y %Sac.Caña por separado).
3. Revisar la redacción de la celda 19: quedó como "no se puede observar una relación clara, ni lineal ni no lineal" — es un poco impreciso, porque sí existe una correlación (débil, r=-0.168); conviene ajustarla para que sea numéricamente exacta antes de la entrega.

*(Decisión pospuesta a propósito — se retoma cuando el equipo avance más el boceto.)*

## Tarea 3 — Metodología de Modelamiento

Desarrollada en el notebook (sección 4). Protocolo: hold-out 80/20 primero, hiperparámetros con validación cruzada de 5 vueltas solo sobre el train, y todo el preprocesamiento (imputar, escalar, codificar) dentro de un `Pipeline`.

**Regresión** (`HISTORICO_SUERTES`, 20.733 lotes sin semilla; regresión lineal, Ridge y Lasso):

| Objetivo | R² CV | R² test | RMSE test | MAE test |
|---|---|---|---|---|
| TCH | 0,251 | 0,238 | 28,3 t/ha | 21,3 t/ha |
| %Sac.Caña | 0,283 | 0,289 | 0,97 | 0,75 |

- Ridge y Lasso quedan igual que la lineal (sin sobreajuste; CV y test coinciden).
- Supuestos: Breusch-Pagan y Shapiro-Wilk rechazan (p ≈ 0); Durbin-Watson ≈ 2. Los p-valores son poco confiables, así que se interpretan tamaño y signo.
- TCH: pesan la edad (+9,5 t/ha por desviación estándar), el corte (-4,5), la distancia (-3,5) y, sobre todo, suelo y zona.
- Sacarosa: orgánico (-1,18 pts), sin madurante (-0,70 pts) y lluvia de los 2 meses previos (-0,26 por desviación estándar). La dosis casi no agrega una vez se sabe si se aplicó madurante.

**Clasificación** (`BD_IPSA_1940`, 2.187 lotes, 438 en test; logística L1/L2, logística balanceada y KNN, contra una referencia que siempre responde la clase más común) — con los umbrales de recorte 5%+tercios y, **desde el 2/10/2026, con `grupo_tenencia` y `mes` codificadas como categóricas (one-hot)**:

> **Cambio (2/10/2026):** `mes` entraba como número 1-12 (escala lineal) y ahora entra como categórica; esa variable tiene un patrón estacional fuerte en sacarosa (promedio de 12,15 en junio a 13,43 en octubre) que una escala numérica no podía capturar. Además, el k de KNN en sacarosa se fijó en 13 (la búsqueda automática elegía 21 por una diferencia de 0,0006, dentro del ruido). Se recalcularon todas las cifras de clasificación de aquí en adelante.

| Objetivo | Mejor F1 macro (partición al azar) | Recall "Bajo": logística normal → balanceada | Kappa |
|---|---|---|---|
| TCH | KNN, 0,462 (k = 11) | 0,13 → 0,42 | 0,13 a 0,19 |
| Sacarosa | KNN, 0,527 (k = 13 fijo); logística balanceada 0,526 | 0,46 → 0,66 | 0,23 a 0,30 |

- L1 y L2 dan prácticamente lo mismo (F1 en TCH: 0,405 las dos; en sacarosa: 0,512 y 0,515).
- **Efecto de codificar `mes` como categórica:** en sacarosa el Kappa de la logística balanceada pasó de 0,168 a 0,302 (de "leve" a "razonable"); en TCH, el del mejor modelo pasó de 0,161 a 0,191.
- **Sacarosa:** logística balanceada y KNN quedan empatadas en F1 (0,526 y 0,527). La logística gana en Kappa (0,302 contra 0,268) y detecta mejor los extremos (recall Bajo 0,66, Alto 0,70); KNN reparte el acierto de forma más pareja entre las tres clases (recall 0,54 / 0,50 / 0,53).
- **k de KNN en sacarosa:** la curva de validación cruzada es una meseta (k = 13, 19, 21 y 27 dan F1 entre 0,525 y 0,526). Probados en datos no vistos, k = 13 supera a k = 21 (F1 0,527 contra 0,501 en el test; 0,480 contra 0,471 con partición por finca-periodo). No es que los k grandes generalicen peor: bajo finca-periodo los peores fueron k = 1 y k = 3.
- **Robustez (partición por finca-periodo, F1 macro, azar → finca-periodo):** TCH: L2 0,405→0,369, L2 balanceada 0,419→0,351, KNN 0,462→0,429. Sacarosa: L2 0,512→0,479, L2 balanceada 0,526→0,446, KNN 0,527→0,480. KNN es el más estable en los dos objetivos; la logística balanceada es la que más cae. Parte de la ganancia de `mes` bajo partición al azar está inflada, porque todos los lotes de una misma finca-periodo comparten mes.
- Un signo por revisar con el Ingenio: `pct_diatrea` sale con efecto contrario al esperado en TCH Bajo (coeficiente −0,30) — **persiste con los tres esquemas probados** (umbrales del Ingenio, recorte 5%+tercios con `mes` numérico y con `mes` categórica), así que no es un artefacto de la definición de los niveles ni de la codificación.

**Pendiente (Tarea 4):** ninguno; el informe IEEE se regeneró el 3/10/2026 con estas cifras.

## Tarea 4 — Reporte de Resultados

Desarrollada en el notebook (sección 5) y convertida en el informe final `Informe_Final_IEEE.docx`/`.pdf` (formato IEEE, 2 columnas, sin código), **regenerado el 3/10/2026 con las cifras de clasificación vigentes** (recorte 5%+tercios, `mes` y `grupo_tenencia` categóricas, k = 13 en sacarosa).

**Importancia de variables (permutación):**

| | Regresión | Clasificación (logística balanceada, caída de F1) |
|---|---|---|
| TCH | Edad al cosechar domina (caída R² 0,182) | `cortes` y `edad` empatadas (0,023); `mes` 0,009 |
| Sacarosa | Si se aplicó madurante domina (caída R² 0,201), luego lluvia 2 meses (0,106) | **`mes` domina (0,162)**, luego `lluvias` (0,031), `edad` y `semsmad` (0,022) |

**Valor de negocio de las alertas "Bajo":**

| Objetivo | Modelo | Reales | Alertas | Precisión | Recall | Vs. azar |
|---|---|---|---|---|---|---|
| TCH | Log. balanceada | 116 | 138 | 35,5% | 42,2% | 1,3× |
| TCH | KNN (k = 11) | 116 | 77 | 42,9% | 28,4% | 1,6× |
| Sacarosa | Log. balanceada | 134 | 152 | 57,9% | 65,7% | 1,9× |
| Sacarosa | KNN (k = 13) | 134 | 119 | 60,5% | 53,7% | 2,0× |

En los dos objetivos persiste el compromiso entre precisión y recall: la logística balanceada para detectar más lotes "Bajo", KNN para emitir menos alertas pero más certeras. Con `mes` como categórica, las alertas de sacarosa mejoraron mucho frente al esquema anterior (precisión de 45-55% a 58-61%).
