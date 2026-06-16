# Albiorix WhatsApp Reader

Prototipo inicial para leer grupos de WhatsApp, detectar reportes de asistencia y generar una salida organizada para revisión operativa.

## Qué resuelve

Este prototipo reduce el tiempo dedicado a revisar múltiples grupos de WhatsApp, filtrar mensajes relevantes y preparar la información para su carga posterior en Albiorix. El objetivo es quitar trabajo repetitivo, bajar errores de lectura manual y dejar solo los registros útiles para validación.

## Estado del proyecto

El prototipo ya valida el flujo principal:

- abre WhatsApp Web con Selenium;
- entra a un grupo específico;
- lee mensajes visibles del día;
- detecta palabras clave operativas;
- genera Excel con resultados;
- genera un resumen TXT de ejecución.

Eso significa que el proyecto ya demuestra viabilidad real como base de automatización.

## Qué muestra el prototipo

El prototipo no es una versión final, pero sí es una demostración funcional de que el proceso puede automatizarse por etapas. Ya existe lectura, filtrado, consolidación y exportación de datos estructurados.

Eso lo convierte en una muy buena muestra de lo que puede lograrse a futuro cuando se agreguen más grupos, mejores reglas de filtrado y mayor precisión en la detección de local y comuna.

## Beneficios principales

### Ahorro de tiempo

El mayor beneficio es reducir el tiempo invertido en revisar chats manualmente. En lugar de leer grupo por grupo y mensaje por mensaje, el sistema entrega solo lo relevante.

### Menos errores

La automatización disminuye errores de copia, omisiones y confusión entre mensajes similares. También ayuda a estandarizar la salida para que la revisión final sea más ordenada.

### Menor carga operativa

Si el proceso de lectura y prefiltrado queda automatizado, se necesita menos personal para hacer la primera revisión. El equipo puede concentrarse en validar, corregir casos ambiguos y cargar la información final.

### Mejor control

El Excel estructurado permite revisar por grupo, local, comuna, nombre y RUT, lo que mejora la trazabilidad del trabajo diario.

## Impacto económico

La ganancia económica viene de dos lados:

- menos horas hombre dedicadas a tareas repetitivas;
- menos costo de errores y retrabajo.

En términos operativos, esto permite procesar más volumen con el mismo equipo o mantener el mismo volumen con menos personas dedicadas a revisión manual.

## Ventajas del enfoque

- Automatiza una tarea repetitiva y de alto desgaste.
- Reduce tiempos muertos en revisión manual.
- Ordena la información antes de cargarla en Albiorix.
- Facilita trabajar con varios grupos de WhatsApp.
- Permite escalar sin crecer de forma lineal en personal.

## Limitaciones actuales

- Los mensajes no siempre vienen con formato uniforme.
- WhatsApp Web puede cambiar selectores o tiempos de carga.
- Algunos mensajes seguirán requiriendo revisión humana.
- La extracción de local y comuna puede necesitar ajustes si cambia la forma del mensaje.

## Evolución esperada

La idea es que este prototipo evolucione hacia un lector más robusto capaz de manejar más grupos, más formatos de texto y mejores reglas de descarte de ruido. También puede incorporar priorización por institución, clasificación por comuna y una salida cada vez más limpia.

## Archivos del proyecto

- `main.py`: punto de entrada del prototipo.
- `src/models.py`: estructura de datos de salida.
- `src/parser/message_parser.py`: lógica de extracción de registros.
- `src/parser/location_extractor.py`: detección de local y comuna.
- `src/exporters/excel_exporter.py`: generación del Excel.
- `README_prototipo_albiorix.md`: presentación del proyecto.

## Mensaje final

Este prototipo ya sirve como muestra real de lo que puede construirse a futuro. No solo demuestra que la automatización es posible, sino que también confirma que puede aportar valor concreto en tiempo, orden, reducción de errores y optimización del trabajo humano.

## Corrección reciente

El lector ahora incluye scroll automático del historial visible para ampliar la captura de mensajes del día. También mejora la separación de local y comuna, y consolida mejor los registros cuando el chat trae varios bloques consecutivos de dotación.





################################################################################################


# Propuesta: automatización de lectura operativa desde WhatsApp para Albiorix

## Resumen

Actualmente, una parte importante del trabajo operativo depende de revisar manualmente mensajes en grupos de WhatsApp para identificar reportes útiles, interpretarlos y preparar la información para su revisión o carga posterior en Albiorix. Este proceso consume tiempo, exige atención humana constante, genera desgaste operativo y aumenta la probabilidad de errores por omisión, interpretación o transcripción, problemas que suelen repetirse en procesos manuales de alto volumen.

La propuesta busca automatizar una de las capas del trabajo: leer mensajes, detectar los casos relevantes y organizar la información para que el equipo humano se concentre en validar, corregir excepciones y mantener control operativo. El objetivo no es reemplazar al equipo, sino eliminar la parte más repetitiva, lenta y poco escalable del proceso.

## Problema actual

La operación actual enfrenta una dificultad estructural: información crítica llega a través de un canal no diseñado para procesamiento operativo, con mensajes variables, extensos y mezclados con contenido irrelevante. Esto obliga al equipo a invertir tiempo en leer, filtrar y ordenar manualmente grandes volúmenes de información antes de poder utilizarla.

A medida que aumenta el volumen de mensajes y grupos, también aumenta el tiempo de revisión, la dependencia de personas específicas y la exposición a errores manuales. En ese contexto, el modelo actual pierde eficiencia y se vuelve difícil de escalar sin aumentar tiempo administrativo o dotación operativa.

## Qué problema de negocio se busca resolver

El problema central no es WhatsApp como herramienta, sino el costo operativo de depender de lectura manual para transformar mensajes desordenados en información utilizable. Cada minuto dedicado a revisar conversaciones completas, detectar palabras clave y ordenar datos representa tiempo que no se utiliza en tareas de mayor valor, como validación, control de calidad y gestión operativa.

Además, este modelo aumenta la probabilidad de errores frecuentes en procesos repetitivos: omisiones, inconsistencias, duplicidad de esfuerzo y trabajo repetitivo por interpretaciones iniciales incorrectas. Desde el punto de vista de negocio, eso se traduce en menor productividad, mayor desgaste del equipo y menor capacidad para absorber crecimiento con eficiencia.

## Solución propuesta

Se propone implementar una solución de apoyo operativo que automatice la revisión inicial de mensajes de WhatsApp, identifique los casos relevantes y entregue una salida estructurada para revisión posterior. Esto permitiría pasar de un modelo donde se revisa todo manualmente a uno donde se revisa principalmente lo que el sistema ya identifica como útil o dudoso.

La propuesta está planteada como una mejora operacional gradual. El valor no está solo en automatizar una tarea, sino en rediseñar la forma de trabajo para reducir carga manual, aumentar consistencia y usar mejor el tiempo del equipo.

## Beneficios esperados

### Ahorro de tiempo

El mayor beneficio esperado es reducir el tiempo dedicado a leer conversaciones completas y filtrar manualmente mensajes relevantes. La automatización permite acelerar tareas repetitivas y disminuir el esfuerzo necesario para preparar información operativa.

### Menos errores

Automatizar la primera capa del proceso ayuda a reducir errores de omisión, copia, interpretación y clasificación inconsistente. En procesos con alto volumen y repetición, este tipo de falla representa uno de los principales costos ocultos de la operación.

### Menor carga operativa

Al disminuir la lectura manual exhaustiva, el equipo puede concentrarse en tareas de mayor valor: validar excepciones, revisar casos ambiguos y asegurar calidad de la información final. Esto mejora el uso del recurso humano y reduce horas invertidas en actividades de bajo valor agregado.

### Más escalabilidad

Sin automatización, más volumen implica más tiempo manual o más personas revisando. Con automatización, una parte relevante del crecimiento puede absorberse con el mismo equipo, lo que permite escalar la operación con mayor eficiencia.

### Mejor trazabilidad

Trabajar con una salida más estructurada mejora el control, seguimiento y consistencia de la revisión operativa. Esto facilita ordenar los registros útiles y separar los casos que requieren intervención humana.

## Impacto para la empresa

El impacto esperado de esta iniciativa debe evaluarse como una mejora directa de productividad, control y capacidad operativa. La automatización de procesos manuales suele generar valor al reducir tiempos administrativos, disminuir errores humanos y mejorar el uso del equipo existente.

En este caso, eso se traduce en una operación más rápida, más ordenada, menos expuesta a errores evitables y mejor preparada para manejar mayor volumen sin aumentar la carga al mismo ritmo.

## Errores que se pueden evitar

La implementación de esta solución puede ayudar a reducir una parte importante de los errores típicos del flujo manual actual:

- omisión de mensajes relevantes.
- errores de copia o transcripción.
- clasificaciones inconsistentes entre operadores.
- Repetir trabajo por mala lectura o interpretación inicial.
- tiempo perdido revisando mensajes que no aportan valor.

## Trabajo que se puede ahorrar

El ahorro más importante no es solamente “hacerlo más rápido”, sino dejar de usar horas del equipo en actividades repetitivas de bajo valor. La automatización permite cambiar la carga de trabajo desde la lectura completa de conversaciones hacia la validación de información ya preclasificada.

Eso significa ahorro en lectura manual, filtrado, ordenamiento previo y retrabajo derivado de errores iniciales. En términos de negocio, el sistema ayuda a transformar tiempo operativo improductivo en tiempo útil para control y toma de decisiones.

El tiempo que vamos a ganar, podríamos usarlo para mejorar las pautas, tema que suena con mas fuerza por la sobredotación de algunas instalaciones.

## Limitaciones y enfoque realista

La propuesta debe presentarse con expectativas correctas. No todos los mensajes llegarán en formatos uniformes y algunos casos seguirán necesitando revisión humana, especialmente cuando existan ambiguedades o falten datos clave. Además, al depender de WhatsApp Web como canal de origen, la solución requerirá mantenimiento si cambian sus condiciones o estructura visual.

Estas limitaciones no reducen el valor del proyecto; lo posicionan correctamente como una herramienta de eficiencia operativa que automatiza la parte más repetitiva del flujo y deja al equipo humano el control final de calidad.

## Propuesta de valor

La empresa tiene una oportunidad concreta de reducir tiempo perdido, disminuir errores evitables y mejorar la eficiencia de una tarea que hoy depende demasiado de lectura manual. Esta iniciativa no debe entenderse solo como un desarrollo tecnológico, sino como una mejora directa en productividad, orden y capacidad operativa.

El valor estratégico del proyecto está en liberar tiempo del equipo, reducir desgaste operativo y preparar a la organización para procesar mayor volumen con más control y menos dependencia de trabajo administrativo repetitivo.

## Próximo paso sugerido

El siguiente paso recomendado es validar la solución sobre operación real y medir indicadores simples de negocio: tiempo promedio de revisión manual, tiempo promedio con prefiltrado automatizado, volumen de mensajes descartados como ruido, cantidad de casos útiles detectados y porcentaje de registros que aún requieren revisión humana.

Con esa información, la empresa podrá evaluar la propuesta no solo como una buena idea, sino como una mejora operacional con impacto medible y potencial de escalamiento.

## Mensaje clave para tomar una decisión

Esta propuesta no busca incorporar tecnología por novedad. Busca resolver una pérdida operativa real, tiempo humano dedicado a revisar mensajes desordenados, repetitivos y no estructurados. Aprobar esta iniciativa permitiría transformar una tarea manual y poco escalable en un proceso más rápido, ordenado y controlable para la empresa.


