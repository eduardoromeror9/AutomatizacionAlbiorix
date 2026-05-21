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
