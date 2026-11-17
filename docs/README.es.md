# Fixen UI Studio

[English — documentación principal](../README.md) · [Bahasa Indonesia](README.id.md) · Español · [Português (Brasil)](README.pt-BR.md) · [简体中文](README.zh-CN.md)

**Diseño basado en el producto, interfaces funcionales y revisión visual con pruebas.**

Fixen UI Studio es una habilidad de código abierto para agentes de IA que diseñan, implementan, revisan y mejoran interfaces web. Conecta el análisis del producto, la dirección artística, UX, el desarrollo frontend, la revisión visual y la búsqueda opcional de imágenes reales.

**v1.2.1 · Experimental.** Antes se llamaba Fixenzo UI Studio. Se invoca con `$fixen-ui-studio`. Es un paquete de instrucciones Markdown/YAML; el agente anfitrión proporciona el modelo, las herramientas y los permisos.

## Instalación

Descarga `fixen-ui-studio-v1.2.1.zip` desde [GitHub Releases](https://github.com/riantosee/Fixen-ui-Studio/releases). Extrae la carpeta `fixen-ui-studio/` en el directorio de habilidades de Codex, de modo que el archivo de entrada quede en:

```text
~/.codex/skills/fixen-ui-studio/SKILL.md
```

En Windows, `~` suele ser la carpeta de tu perfil. Si configuraste `CODEX_HOME`, utiliza su directorio de habilidades. Guarda una copia de las personalizaciones antes de reemplazarlas. También puedes clonar el repositorio y copiar únicamente `skills/fixen-ui-studio/`. No se han probado todos los demás entornos.

## Ejemplos

```text
Usa $fixen-ui-studio para crear un panel de gestión de envíos.
Prioriza entregas retrasadas, filtros y acciones claras de resolución.
Utiliza la tecnología del proyecto y datos sintéticos.
```

```text
Usa $fixen-ui-studio para revisar la jerarquía y accesibilidad de esta página.
Presenta pruebas y recomendaciones concretas. No modifiques archivos.
```

```text
Usa $fixen-ui-studio para una interfaz de reservas con inglés como idioma
principal y versiones en español y árabe. Reutiliza el sistema i18n;
revisa precios, fechas, diseño móvil y navegación RTL.
```

## Idiomas e imágenes

El inglés es el idioma principal de la documentación. El agente debe comunicarse en el idioma solicitado por el usuario. El idioma de la interfaz sigue las decisiones del producto y las convenciones del repositorio. Para un producto nuevo sin indicaciones, se usa inglés y se declara esta suposición. La [guía de localización](../skills/fixen-ui-studio/systems/localization.md) cubre formatos regionales, expansión de texto, fuentes y RTL. La habilidad no instala un motor de traducción ni garantiza calidad en todos los idiomas.

La [búsqueda de imágenes](../skills/fixen-ui-studio/design/asset-sourcing.md) es opcional y depende de las herramientas disponibles. Seleccionar, descargar, integrar y verificar el resultado son etapas distintas. Una petición de selección termina en recomendaciones. Registra fuentes, autores, condiciones y verificaciones en el [registro de recursos](../skills/fixen-ui-studio/templates/asset-register.md). Las imágenes de terceros conservan sus propias licencias.

## Contribuciones y validación

Consulta [CONTRIBUTING.md](../CONTRIBUTING.md), disponible en inglés. Las traducciones son bienvenidas; conserva identificadores, comandos, rutas, el significado de la licencia y los límites de las pruebas. Si hay diferencias, consulta el [README en inglés](../README.md) y el [historial de cambios](../CHANGELOG.md) e informa de la discrepancia.

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s scripts -p "test_*.py" -v
```

Estos controles para colaboradores requieren Python 3.10+; usar las instrucciones no lo requiere. La validación estructural no demuestra calidad visual, calidad de traducción, conformidad de accesibilidad ni superioridad en evaluaciones. Consulta el [alcance de la validación](validation.md). Las traducciones del README no equivalen a pruebas de navegador en cada idioma.

## Seguridad y licencia

Se prohíben la explotación no autorizada, el robo de credenciales, la inyección maliciosa de instrucciones, el malware y las acciones destructivas en las contribuciones y espacios de la comunidad. Se permiten evaluaciones defensivas autorizadas con entornos aislados y datos sintéticos. Informa de vulnerabilidades de forma privada según la [política de seguridad](../SECURITY.md) y respeta el [código de conducta](../CODE_OF_CONDUCT.md). La habilidad no es un entorno aislado ni garantiza resistencia a la inyección de instrucciones.

La [licencia MIT](../LICENSE) permite uso comercial, modificación, redistribución y venta conservando los avisos de derechos de autor y licencia. Las políticas de seguridad y comunidad no modifican estos permisos ni autorizan ataques a otros sistemas. Los forks deben indicar su origen y sus cambios, sin presentarse como versiones oficiales.
