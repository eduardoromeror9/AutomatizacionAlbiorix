# WhatsApp Albiorix Lector

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
- `config/`: configuración editable.
