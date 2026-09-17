# Informe de Avance — Taller Práctico Ingenio Providencia

> Documento de trabajo (borrador vivo). Se irá completando tarea por tarea según el enunciado en `contexto.txt`. Al final, este contenido se traspasará al formato oficial IEEE en `ArchivosImportantes/Formato presentacion documentos.doc` para la entrega (máx. 5 páginas, sin código anexo).

---

## Tarea 1 — Introducción y Contexto del Negocio

### 1.1 Importancia Económica y Social del sector azucarero (Valle del Cauca y Colombia)

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
*(Pendiente — siguiente paso)*

## Tarea 3 — Metodología de Modelamiento
*(Pendiente)*

## Tarea 4 — Reporte de Resultados
*(Pendiente)*
