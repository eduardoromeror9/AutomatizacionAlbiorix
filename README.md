<!-- # WhatsApp Albiorix Lector

Prototipo en Python para leer grupos de WhatsApp Web con Selenium, detectar mensajes del día actual con palabras clave relevantes para Albiorix y exportar resultados a Excel.

## Qué hace esta versión

- Abre WhatsApp Web en Chrome.
- Reutiliza una sesión de navegador persistente.
- Recorre chats visibles del panel lateral y hace scroll para cargar más.
- Intenta detectar grupos y omitir chats individuales.
- Lee mensajes visibles del día actual.
- Busca palabras clave y variantes configurables.
- Extrae RUT chileno si está presente.
- Marca casos ambiguos cuando falta nombre o RUT.
- Exporta un Excel único y un log TXT por ejecución.

## Limitaciones del prototipo

- WhatsApp Web cambia selectores con el tiempo, por lo que puede requerir ajustes.
- La detección de grupos es heurística.
- La lectura del día actual depende de la información visible del mensaje en WhatsApp Web.
- El parser está pensado para una primera demo y luego debe perfeccionarse con mensajes reales.

## Instalación

```bash
pip install -r requirements.txt
```

## Configuración

Edita `config/settings.json` y `config/keywords.json`.

Campos importantes en `settings.json`:

- `output_dir`: carpeta donde se guardará el Excel.
- `log_dir`: carpeta donde se guardará el TXT y el log de ejecución.
- `chrome_profile_dir`: carpeta del perfil separado de automatización.
- `max_sidebar_scrolls`: cuántas veces baja por la barra lateral.
- `max_chats_to_process`: límite de grupos a revisar por ejecución.

## Primer uso

1. Ejecuta el script.
2. Se abrirá Chrome con el perfil de automatización.
3. Inicia sesión en WhatsApp Web si lo pide.
4. Espera a que carguen tus chats.
5. El script comenzará a leer grupos y generará los archivos de salida.

## Ejecución

```bash
python main.py
```

## Salida esperada

- Excel `.xlsx` con resultados ordenados.
- TXT con resumen de ejecución.
- Log `.log` para depurar errores.

## Estructura principal

- `main.py`: entrada principal.
- `src/app.py`: orquesta todo el flujo.
- `src/whatsapp/`: interacción con WhatsApp Web.
- `src/parser/`: normalización, detección de palabras y parser.
- `src/exporters/`: Excel y TXT.
- `config/`: configuración editable. -->

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