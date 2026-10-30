<a href="https://remakelist.com/es/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=intro-es"><img src="assets/brand-banner.svg" alt="RemakeList — software recreations and classic game ports" width="920"></a>

# Awesome RemakeList

Reimplementaciones de software, motores de juegos y adaptaciones a otras plataformas, con los requisitos para empezar a usarlos.

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · **Español**

[Explorar RemakeList](https://remakelist.com/es/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=intro-es) · [Sugerir un proyecto](https://github.com/CharlexH/awesome-remakelist/issues/new?template=project.yml)

[![Catalog checks](https://github.com/CharlexH/awesome-remakelist/actions/workflows/check.yml/badge.svg?branch=main)](https://github.com/CharlexH/awesome-remakelist/actions/workflows/check.yml) [![Website sync](https://github.com/CharlexH/awesome-remakelist/actions/workflows/sync.yml/badge.svg?branch=main)](https://github.com/CharlexH/awesome-remakelist/actions/workflows/sync.yml)

Los nombres de los proyectos llevan a las fuentes de sus autores. Despliega cada entrada para consultar los requisitos de dispositivos, archivos del juego y compilación; en RemakeList también encontrarás capturas y explicaciones de instalación.

## Por dónde empezar

| Proyecto | Ver detalles | Cómo empezar |
| --- | --- | --- |
| [Graphite](https://remakelist.com/es/remakes/graphite/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=graphite-featured-es) | Adobe Illustrator | [Probar en el navegador](https://editor.graphite.art/) |
| [Webamp](https://remakelist.com/es/remakes/webamp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=webamp-featured-es) | Winamp 2 | [Probar en el navegador](https://webamp.org/) |
| [OpenTTD](https://remakelist.com/es/remakes/openttd/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openttd-featured-es) | Transport Tycoon Deluxe | [Descargar](https://www.openttd.org/) |
| [OpenRCT2](https://remakelist.com/es/remakes/openrct2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openrct2-featured-es) | RollerCoaster Tycoon 2 | [Descargar y aportar tus archivos del juego](https://openrct2.io/download) |
| [D2R Mobile](https://remakelist.com/es/remakes/d2r-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=d2r-mobile-featured-es) | Diablo II: Resurrected | [Compilar y aportar tus archivos del juego](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) |
| [nxnative](https://remakelist.com/es/remakes/nxnative/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nxnative-featured-es) | Juegos de Nintendo Switch | [Compilar y aportar tus archivos del juego](https://github.com/seedds/nxnative#pack-an-ipa) |

## Explorar categoría

- [Herramientas de diseño y creación](#creative) · 13
- [Herramientas de uso diario y recreaciones de interfaces](#everyday) · 9
- [Motores y recreaciones de juegos](#classic_games) · 30
- [Adaptaciones y proyectos de compatibilidad](#ports) · 91

<img src="assets/overview-es.svg" alt="Índice" width="920">

<a id="creative"></a>

## Herramientas de diseño y creación

### [Compositor](https://github.com/robbietilton/Compositor)

Un editor de composición por capas y posprocesamiento para Mac con Apple silicon, diseñado en torno a flujos de trabajo similares a Photoshop.

Original o referencia: **Adobe Photoshop** · Alternativa funcional independiente  
[Descargar](https://github.com/robbietilton/Compositor/releases/tag/v1.5.12) · [Explorar RemakeList](https://remakelist.com/es/remakes/compositor/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=compositor-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Mac con Apple silicon · macOS 26+

**Estado:** v1.5.12 · Apple silicon · macOS 26+

**Qué necesitas:** No hace falta instalar Photoshop. Requiere un Mac con Apple silicon y macOS 26+; compilar desde el código fuente requiere Xcode 26+. Eres responsable de los derechos sobre los medios que editas.

**Qué está disponible:** v1.5.12 ofrece un DMG para Mac con Apple silicon y macOS 26+. Compilar desde el código requiere Xcode 26+. La interfaz solo está en inglés. La importación PSD/PSB admite RGB de 8 bits, no CMYK; algunos vectores y textos verticales se rasterizan. RemakeList no lo ha instalado ni probado.

**Licencia del código:** [MIT](https://github.com/robbietilton/Compositor/blob/main/LICENSE)  
**Autor:** robbietilton  
[Documentación oficial](https://github.com/robbietilton/Compositor/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [PhotoCraft](https://github.com/storytold/photocraft)

Una reimplementación en Rust de flujos de edición de imágenes al estilo de Photoshop, creada por el equipo ArtCraft y actualmente en fase alfa.

Original o referencia: **Adobe Photoshop** · Reimplementación del flujo de trabajo  
[Descargar](https://github.com/storytold/photocraft/releases/tag/v0.17.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/photocraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=photocraft-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux / FreeBSD / Web

**Estado:** v0.17.0 · alfa inicial

**Qué necesitas:** No hace falta instalar Photoshop. Las imágenes que edites deben contar con los derechos adecuados; las fuentes e iconos incluidos tienen licencias independientes. Las marcas ArtCraft quedan excluidas de la licencia del código.

**Qué está disponible:** v0.17.0 ofrece paquetes para Windows, macOS, Linux, FreeBSD y web. Sigue en una fase alfa inicial; la versión actualiza la gestión de documentos y mesas de trabajo y el renderizado, mientras que la compatibilidad con Photoshop y los flujos profesionales continúan incompletos.

**Licencia del código:** [MIT OR Apache-2.0](https://github.com/storytold/photocraft/blob/main/LICENSE-MIT)  
**Autor:** storytold  
[Documentación oficial](https://github.com/storytold/photocraft/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [Graphite](https://github.com/GraphiteEditor/Graphite)

Una herramienta de diseño vectorial de código abierto que combina capas y nodos para crear de forma no destructiva en el navegador.

Original o referencia: **Adobe Illustrator** · Alternativa funcional independiente  
[Probar en el navegador](https://editor.graphite.art/) · [Explorar RemakeList](https://remakelist.com/es/remakes/graphite/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=graphite-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Web

**Estado:** Alfa · editor web disponible

**Qué necesitas:** No hace falta instalar Illustrator ni disponer de sus archivos originales. Aporta tus propias imágenes, fuentes y recursos creativos.

**Qué está disponible:** El editor web ya está disponible para probar diseño vectorial sin Illustrator. Sigue en fase alfa; las capacidades más amplias de edición fotográfica, animación, publicación y VFX siguen evolucionando, por lo que no debe considerarse un sustituto de todo un flujo de trabajo Adobe.

**Licencia del código:** [MIT OR Apache-2.0](https://graphite.art/license/)  
**Autor:** Graphite community  
[Documentación oficial](https://github.com/GraphiteEditor/Graphite/blob/master/README.md) · Fuentes revisadas: 2026-10-12

</details>

### [Friction](https://github.com/friction2d/friction)

Una herramienta de gráficos animados 2D de código abierto con animación vectorial y de mapa de bits, líneas de tiempo y expresiones.

Original o referencia: **Adobe After Effects** · Alternativa funcional independiente  
[Descargar](https://friction.graphics/#download) · [Explorar RemakeList](https://remakelist.com/es/remakes/friction/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=friction-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux

**Estado:** Descargas de escritorio · gráficos animados 2D

**Qué necesitas:** No hace falta instalar After Effects. Aporta tus propias imágenes, fuentes, audio y vídeo.

**Qué está disponible:** Se ofrecen descargas para Windows, Linux y macOS. Permite crear animación 2D y gráficos en movimiento; los efectos con shaders personalizados siguen siendo experimentales y no se promete compatibilidad con proyectos, complementos o cadenas completas de efectos de After Effects.

**Licencia del código:** [GPL-3.0-only](https://github.com/friction2d/friction/blob/main/LICENSE.md)  
**Autor:** Ole-André Rodlie &amp; contributors  
[Documentación oficial](https://friction.graphics/) · Fuentes revisadas: 2026-10-12

</details>

### [OpenCut](https://github.com/OpenCut-app/OpenCut)

Un editor de vídeo de código abierto orientado a la edición al estilo de CapCut, con una versión clásica en beta temprana en línea mientras se reescribe la próxima versión.

Original o referencia: **CapCut** · Alternativa funcional independiente  
[Probar en el navegador](https://opencut.app/) · [Explorar RemakeList](https://remakelist.com/es/remakes/opencut/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=opencut-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Web

**Estado:** Beta temprana · reescritura en curso

**Qué necesitas:** No hace falta instalar CapCut. Importa vídeos, imágenes y audio que tengas derecho a usar.

**Qué está disponible:** El sitio oficial ofrece actualmente la beta temprana clásica. Su código está archivado y la nueva versión se está reescribiendo; es una opción para explorar, sin dar por hecho que pueda sustituir por completo el uso diario de CapCut.

**Licencia del código:** [MIT](https://github.com/OpenCut-app/OpenCut/blob/main/LICENSE)  
**Autor:** OpenCut contributors  
[Documentación oficial](https://github.com/OpenCut-app/OpenCut/blob/main/README.md) · Fuentes revisadas: 2026-10-12

</details>

### [Penpot](https://github.com/penpot/penpot)

Una plataforma de diseño colaborativo y prototipado de código abierto, alojada o en un servidor propio.

Original o referencia: **Figma** · Alternativa funcional independiente  
[Registrarse o alojarlo por tu cuenta](https://design.penpot.app) · [Explorar RemakeList](https://remakelist.com/es/remakes/penpot/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=penpot-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Navegador / alojamiento propio

**Estado:** Consulta la documentación oficial

**Qué necesitas:** No necesitas software ni recursos de Figma. Para migrar tus diseños, debes exportarlos e importarlos.

**Qué está disponible:** Regístrate en el servicio alojado o ejecuta tu propia instalación. Trasladar diseños existentes requiere exportarlos e importarlos; consulta la página de precios para conocer los planes del servicio alojado.

**Licencia del código:** [MPL-2.0](https://github.com/penpot/penpot/blob/develop/LICENSE)  
**Autor:** penpot  
[Documentación oficial](https://penpot.app/penpot-vs-figma) · Fuentes revisadas: 2026-10-11

</details>

### [VectorCraft](https://github.com/storytold/vectorcraft)

Una reimplementación en Rust de ArtCraft de flujos al estilo de Adobe Illustrator: dibujo con pluma, operaciones booleanas de trazados, efectos de apariencia e ilustración vectorial.

Original o referencia: **Adobe Illustrator** · Reimplementación del flujo de trabajo  
[Descargar](https://github.com/storytold/vectorcraft/releases/tag/v0.18.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/vectorcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vectorcraft-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Estado:** v0.18.0 · Alfa

**Qué necesitas:** No se necesita la aplicación comercial original. Aporta documentos y medios que tengas derecho a usar; las fuentes, imágenes y marcas incluidas tienen licencias independientes.

**Qué está disponible:** v0.18.0 ofrece instaladores y archivos de escritorio, además de una compilación web. Corrige texto enlazado duplicado, la recuperación del flujo de texto, transformaciones de trazados compuestos y cambios del perfil de trabajo RGB. Alfa: útil para probar el dibujo vectorial cotidiano; aún hay que comprobar el intercambio de archivos complejos y la fidelidad de los efectos. No lo hemos instalado ni probado a fondo.

**Licencia del código:** [MIT OR Apache-2.0](https://github.com/storytold/vectorcraft/blob/main/LICENSE-MIT)  
**Autor:** ArtCraft  
[Documentación oficial](https://github.com/storytold/vectorcraft/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [FilmCraft](https://github.com/storytold/filmcraft)

Una reimplementación en Rust de ArtCraft de flujos al estilo de Adobe Premiere Pro: monitores de origen y de programa, líneas de tiempo multipista y edición por recorte.

Original o referencia: **Adobe Premiere Pro** · Reimplementación del flujo de trabajo  
[Descargar](https://github.com/storytold/filmcraft/releases/tag/v0.14.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/filmcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=filmcraft-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Estado:** v0.14.0 · Alfa

**Qué necesitas:** No se necesita la aplicación comercial original. Aporta documentos y medios que tengas derecho a usar; las fuentes, imágenes y marcas incluidas tienen licencias independientes.

**Qué está disponible:** v0.14.0 ofrece instaladores y archivos de escritorio, además de una compilación web. Mejora el recorte de audio y vídeo vinculados, la selección de puntos de máscara y el comportamiento del portapapeles en Lift/Extract. Alfa: dispone de flujos de edición y exportación; el rendimiento con medios grandes, el renderizado de efectos y el intercambio de proyectos profesionales siguen incompletos. No lo hemos instalado ni probado a fondo.

**Licencia del código:** [MIT OR Apache-2.0](https://github.com/storytold/filmcraft/blob/main/LICENSE-MIT)  
**Autor:** ArtCraft  
[Documentación oficial](https://github.com/storytold/filmcraft/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [LightCraft](https://github.com/storytold/lightcraft)

Una reimplementación en Rust de ArtCraft de flujos al estilo de Adobe Lightroom: gestión de bibliotecas fotográficas, revelado RAW y ajuste de color no destructivo.

Original o referencia: **Adobe Lightroom** · Reimplementación del flujo de trabajo  
[Descargar](https://github.com/storytold/lightcraft/releases/tag/v0.15.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/lightcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=lightcraft-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Estado:** v0.15.0 · Alfa

**Qué necesitas:** No se necesita la aplicación comercial original. Aporta documentos y medios que tengas derecho a usar; las fuentes, imágenes y marcas incluidas tienen licencias independientes.

**Qué está disponible:** v0.15.0 ofrece instaladores y archivos de escritorio, además de una compilación web. Añade un perfil de cámara Sony α7R V y mejora la exportación a tamaño completo y la gestión de recursos de los decodificadores RAW/HEIF. Alfa: permite probar JPEG, DNG y muchos formatos RAW de cámaras; la calibración de color de las cámaras y algunas variantes RAW comprimidas siguen incompletas. No lo hemos instalado ni probado a fondo.

**Licencia del código:** [MIT OR Apache-2.0](https://github.com/storytold/lightcraft/blob/main/LICENSE-MIT)  
**Autor:** ArtCraft  
[Documentación oficial](https://github.com/storytold/lightcraft/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [EffectCraft](https://github.com/storytold/effectcraft)

Una reimplementación en Rust de ArtCraft de flujos al estilo de Adobe After Effects: composición por capas, animación con fotogramas clave, gráficos en movimiento y efectos.

Original o referencia: **Adobe After Effects** · Reimplementación del flujo de trabajo  
[Descargar](https://github.com/storytold/effectcraft/releases/tag/v0.18.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/effectcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=effectcraft-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Estado:** v0.18.0 · Alfa

**Qué necesitas:** No se necesita la aplicación comercial original. Aporta documentos y medios que tengas derecho a usar; las fuentes, imágenes y marcas incluidas tienen licencias independientes.

**Qué está disponible:** v0.18.0 ofrece instaladores y archivos de escritorio, además de una compilación web. Actualiza los paneles acoplados y las pestañas de composición y corrige la edición de texto con foco y el comportamiento de los menús. Alfa: adecuado para experimentar con animación y composición, no para entregas a clientes. No admite formatos de proyecto propietarios ni complementos del SDK de After Effects. Las comprobaciones de renderizado se centran en composiciones pequeñas; macOS es la plataforma más probada. RemakeList no lo ha instalado ni probado a fondo.

**Licencia del código:** [MIT OR Apache-2.0](https://github.com/storytold/effectcraft/blob/main/LICENSE-MIT)  
**Autor:** ArtCraft  
[Documentación oficial](https://github.com/storytold/effectcraft/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [DesignCraft](https://github.com/storytold/designcraft)

Una reimplementación en Rust de ArtCraft de flujos al estilo de Adobe InDesign: maquetación de páginas enfrentadas, marcos de texto enlazados, páginas maestras y documentos de publicación.

Original o referencia: **Adobe InDesign** · Reimplementación del flujo de trabajo  
[Descargar](https://github.com/storytold/designcraft/releases/tag/v0.14.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/designcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=designcraft-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Estado:** v0.14.0 · Prealfa

**Qué necesitas:** No se necesita la aplicación comercial original. Aporta documentos y medios que tengas derecho a usar; las fuentes, imágenes y marcas incluidas tienen licencias independientes.

**Qué está disponible:** v0.14.0 ofrece instaladores y archivos de escritorio, además de una compilación web. Mejora la importación de tablas DOCX, la edición de notas al pie, los metadatos de documentos PDF y la salida de celdas de tabla con degradados. Prealfa: hay compilaciones con funciones de maquetación y exportación; los archivos de publicación complejos, la tipografía y los flujos de preimpresión requieren comprobaciones individuales. RemakeList no lo ha instalado ni probado a fondo.

**Licencia del código:** [MIT OR Apache-2.0](https://github.com/storytold/designcraft/blob/main/LICENSE-MIT)  
**Autor:** ArtCraft  
[Documentación oficial](https://github.com/storytold/designcraft/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [SoundCraft](https://github.com/storytold/soundcraft)

Una reimplementación en Rust de ArtCraft de flujos al estilo de Avid Pro Tools: grabación de pistas, una ventana de edición, un mezclador y arreglos MIDI.

Original o referencia: **Avid Pro Tools** · Reimplementación del flujo de trabajo  
[Descargar](https://github.com/storytold/soundcraft/releases/tag/v0.14.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/soundcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=soundcraft-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Estado:** v0.14.0 · Prealfa

**Qué necesitas:** No se necesita la aplicación comercial original. Aporta documentos y medios que tengas derecho a usar; las fuentes, imágenes y marcas incluidas tienen licencias independientes.

**Qué está disponible:** v0.14.0 ofrece instaladores y archivos de escritorio, además de una compilación web. Corrige la gestión estéreo de Auto Pan, el pegado y Strip Silence, y mejora el procesamiento de la exportación de mezclas. Prealfa: existen flujos de grabación, edición, mezcla y exportación; aún faltan la selección de dispositivo de audio/búfer, la grabación con controladores MIDI y el intercambio AAF/OMF. No lo hemos instalado ni probado a fondo.

**Licencia del código:** [MIT OR Apache-2.0](https://github.com/storytold/soundcraft/blob/main/LICENSE-MIT)  
**Autor:** ArtCraft  
[Documentación oficial](https://github.com/storytold/soundcraft/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [CADCraft](https://github.com/storytold/cadcraft)

Una reimplementación en Rust de ArtCraft de flujos al estilo de Autodesk AutoCAD: dibujo técnico mediante línea de comandos, referencias a objetos, capas, cotas y presentaciones de planos.

Original o referencia: **Autodesk AutoCAD** · Reimplementación del flujo de trabajo  
[Descargar](https://github.com/storytold/cadcraft/releases/tag/v0.14.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/cadcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=cadcraft-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Estado:** v0.14.0 · Desarrollo inicial

**Qué necesitas:** No se necesita la aplicación comercial original. Aporta documentos y medios que tengas derecho a usar; las fuentes, imágenes y marcas incluidas tienen licencias independientes.

**Qué está disponible:** v0.14.0 ofrece instaladores y archivos de escritorio, además de una compilación web. Mejora la recuperación de dibujos y los avisos para guardar, el escape de texto DXF y la gestión de geometría y restricciones. Desarrollo inicial: adecuado para probar dibujos 2D y trazado a PDF; no sustituye todos los flujos 3D, DWG y de complementos sectoriales de AutoCAD. No lo hemos instalado ni probado a fondo.

**Licencia del código:** [MIT OR Apache-2.0](https://github.com/storytold/cadcraft/blob/main/LICENSE-MIT)  
**Autor:** ArtCraft  
[Documentación oficial](https://github.com/storytold/cadcraft/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>


<a id="everyday"></a>

## Herramientas de uso diario y recreaciones de interfaces

### [ONLYOFFICE Desktop Editors](https://github.com/ONLYOFFICE/DesktopEditors)

Una alternativa de código abierto a Microsoft Office que reúne edición sin conexión de documentos, hojas de cálculo, presentaciones y PDF en una aplicación de escritorio.

Original o referencia: **Microsoft Office** · Alternativa funcional independiente  
[Descargar](https://www.onlyoffice.com/download-desktop) · [Explorar RemakeList](https://remakelist.com/es/remakes/onlyoffice/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=onlyoffice-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux

**Estado:** Versiones estables disponibles

**Qué necesitas:** No hace falta instalar Microsoft Office ni tener una cuenta para editar localmente. La colaboración en la nube requiere un servicio compatible, que puede ser de pago.

**Qué está disponible:** Hay instaladores para Windows, macOS y Linux, con almacenamiento local y edición sin conexión. El uso de escritorio es gratuito; los servicios en la nube y las ediciones empresariales tienen planes independientes. Comprueba los documentos con diseños complejos antes de cambiar.

**Licencia del código:** [AGPL-3.0](https://github.com/ONLYOFFICE/DesktopEditors/blob/master/LICENSE)  
**Autor:** ONLYOFFICE  
[Documentación oficial](https://github.com/ONLYOFFICE/DesktopEditors) · Fuentes revisadas: 2026-10-12

</details>

### [Grist](https://github.com/gristlabs/grist-core)

Una alternativa de código abierto para flujos de Excel y Airtable que combina datos relacionales con edición al estilo de una hoja de cálculo.

Original o referencia: **Microsoft Excel / Airtable** · Alternativa funcional independiente  
[Descargar](https://github.com/gristlabs/grist-desktop/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/grist/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=grist-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux

**Estado:** Núcleo comunitario v1.7.22 · versión de escritorio publicada por separado

**Qué necesitas:** La aplicación de escritorio edita archivos locales. El alojamiento propio requiere un entorno de servidor; los planes alojados requieren una cuenta y tienen límites de uso y funciones.

**Qué está disponible:** El núcleo comunitario v1.7.22 incorpora un creador de widgets dentro del documento, más controles de ordenación y mensajes más claros sobre importación y reglas de acceso. La versión de GitHub no tiene archivos adjuntos; el README incluye instrucciones para Docker y ejecución desde el código fuente. Los paquetes de escritorio se publican por separado, y los planes alojados gratuitos/de pago y las funciones empresariales siguen siendo opciones independientes. El autoalojamiento necesita un servidor; los planes alojados requieren una cuenta y tienen límites de uso. Su modelo de datos difiere del de Excel.

**Licencia del código:** [Apache-2.0](https://github.com/gristlabs/grist-core/blob/main/LICENSE.txt)  
**Autor:** Grist Labs  
[Documentación oficial](https://github.com/gristlabs/grist-core) · Fuentes revisadas: 2026-10-30

</details>

### [LibreOffice](https://github.com/LibreOffice/core)

Una alternativa gratuita y de código abierto a Microsoft Office con Writer, Calc e Impress para documentos, hojas de cálculo y presentaciones.

Original o referencia: **Microsoft Office** · Alternativa funcional independiente  
[Descargar](https://www.libreoffice.org/download/download-libreoffice/) · [Explorar RemakeList](https://remakelist.com/es/remakes/libreoffice/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=libreoffice-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux

**Estado:** Versiones estables disponibles

**Qué necesitas:** No necesitas instalar Microsoft Office ni tener una suscripción o cuenta. Instala la versión de escritorio para tu sistema y utiliza archivos que tengas permiso para editar.

**Qué está disponible:** Hay descargas para Windows, macOS y Linux, con un conjunto completo de herramientas de oficina cotidianas. Prueba tus propios archivos primero si dependes de macros VBA, plantillas complejas de Office o una reproducción exacta del diseño.

**Licencia del código:** [MPL-2.0 (primarily)](https://www.libreoffice.org/licenses/)  
**Autor:** The Document Foundation  
[Documentación oficial](https://www.libreoffice.org/) · Fuentes revisadas: 2026-10-12

</details>

### [Webamp](https://github.com/captbaritone/webamp)

Una reimplementación de Winamp 2 para navegador, con la interfaz clásica del reproductor y compatibilidad con skins.

Original o referencia: **Winamp 2** · Reimplementación web  
[Probar en el navegador](https://webamp.org/) · [Explorar RemakeList](https://remakelist.com/es/remakes/webamp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=webamp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Navegador

**Estado:** Consulta la documentación oficial

**Qué necesitas:** No hace falta instalar Winamp. El audio y las skins de terceros conservan sus propios derechos.

**Qué está disponible:** Puedes abrir directamente el reproductor en línea en tu navegador. No hace falta el programa original; aporta el audio que quieras reproducir.

**Licencia del código:** [MIT](https://github.com/captbaritone/webamp/blob/master/LICENSE.txt)  
**Autor:** captbaritone  
[Documentación oficial](https://github.com/captbaritone/webamp/blob/master/README.md) · Fuentes revisadas: 2026-10-11

</details>

### [WinXP in React](https://github.com/ShizukuIchi/winXP)

Una recreación para navegador del escritorio de Windows XP, su menú Inicio y pequeñas aplicaciones clásicas.

Original o referencia: **Escritorio de Windows XP** · Recreación de la interfaz  
[Probar en el navegador](https://winxp.vercel.app/) · [Explorar RemakeList](https://remakelist.com/es/remakes/winxp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=winxp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Navegador

**Estado:** Consulta la documentación oficial

**Qué necesitas:** No requiere archivos de instalación de Windows XP.

**Qué está disponible:** Hay una demostración en línea que no necesita archivos de instalación de Windows XP. Abarca el escritorio y las aplicaciones recreadas; no puede ejecutar cualquier programa de XP.

**Licencia del código:** [MIT (project code)](https://github.com/ShizukuIchi/winXP/blob/master/LICENSE)  
**Autor:** ShizukuIchi  
[Documentación oficial](https://github.com/ShizukuIchi/winXP/blob/master/README.md) · Fuentes revisadas: 2026-10-11

</details>

### [PdfCraft](https://github.com/storytold/pdfcraft)

Una reimplementación en Rust de ArtCraft de flujos al estilo de Adobe Acrobat: lectura de PDF, anotaciones, organización de páginas, combinación y división.

Original o referencia: **Adobe Acrobat** · Reimplementación del flujo de trabajo  
[Descargar](https://github.com/storytold/pdfcraft/releases/tag/v0.15.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/pdfcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pdfcraft-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Estado:** v0.15.0 · Alfa inicial

**Qué necesitas:** No se necesita la aplicación comercial original. Aporta documentos y medios que tengas derecho a usar; las fuentes, imágenes y marcas incluidas tienen licencias independientes.

**Qué está disponible:** v0.15.0 ofrece instaladores y archivos de escritorio, además de una compilación web. Mejora los formularios XFA, los comentarios importados, el recorte de imágenes y los destinos al abrir documentos. Alfa inicial: están disponibles los flujos de lectura y gestión de páginas; no sustituye por completo los flujos de edición, firma y preimpresión de Acrobat. No lo hemos instalado ni probado a fondo.

**Licencia del código:** [MIT OR Apache-2.0](https://github.com/storytold/pdfcraft/blob/main/LICENSE-MIT)  
**Autor:** ArtCraft  
[Documentación oficial](https://github.com/storytold/pdfcraft/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [WordCraft](https://github.com/storytold/wordcraft)

Una reimplementación en Rust de ArtCraft de flujos al estilo de Microsoft Word: procesamiento de textos, estilos, tablas, control de cambios y diseño de documentos.

Original o referencia: **Microsoft Word** · Reimplementación del flujo de trabajo  
[Descargar](https://github.com/storytold/wordcraft/releases/tag/v0.12.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/wordcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wordcraft-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Estado:** v0.12.0 · Alfa

**Qué necesitas:** No se necesita la aplicación comercial original. Aporta documentos y medios que tengas derecho a usar; las fuentes, imágenes y marcas incluidas tienen licencias independientes.

**Qué está disponible:** v0.12.0 ofrece instaladores y archivos de escritorio, además de una compilación web. Mejora detalles de importación DOCX/RTF, la numeración de listas en árabe, la disposición de párrafos y la importación de binomios LaTeX. Alfa: se pueden probar los flujos de escritura y DOCX; la paginación, la fidelidad de gráficos/SmartArt al importar y volver a exportar y la impresión nativa aún requieren trabajo. No lo hemos instalado ni probado a fondo.

**Licencia del código:** [MIT OR Apache-2.0](https://github.com/storytold/wordcraft/blob/main/LICENSE-MIT)  
**Autor:** ArtCraft  
[Documentación oficial](https://github.com/storytold/wordcraft/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [DeckCraft](https://github.com/storytold/deckcraft)

Una reimplementación en Rust de ArtCraft de flujos al estilo de Microsoft PowerPoint: patrones de diapositivas, temas, formas, animación y reproducción de presentaciones.

Original o referencia: **Microsoft PowerPoint** · Reimplementación del flujo de trabajo  
[Descargar](https://github.com/storytold/deckcraft/releases/tag/v0.12.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/deckcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=deckcraft-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Estado:** v0.12.0 · Alfa

**Qué necesitas:** No se necesita la aplicación comercial original. Aporta documentos y medios que tengas derecho a usar; las fuentes, imágenes y marcas incluidas tienen licencias independientes.

**Qué está disponible:** v0.12.0 ofrece instaladores y archivos de escritorio, además de una compilación web. Añade selección de intervalos de diapositivas y reutilización selectiva, y mejora la importación de esquemas y los controles de presentación. Alfa: permite crear y mostrar presentaciones; no debe suponerse que los archivos PPTX complejos y las animaciones se comportan igual que en PowerPoint. No lo hemos instalado ni probado a fondo.

**Licencia del código:** [MIT OR Apache-2.0](https://github.com/storytold/deckcraft/blob/main/LICENSE-MIT)  
**Autor:** ArtCraft  
[Documentación oficial](https://github.com/storytold/deckcraft/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [GridCraft](https://github.com/storytold/gridcraft)

Una reimplementación en Rust de ArtCraft de flujos al estilo de Microsoft Excel: hojas de cálculo, fórmulas, tablas, gráficos y flujos de tablas dinámicas.

Original o referencia: **Microsoft Excel** · Reimplementación del flujo de trabajo  
[Descargar](https://github.com/storytold/gridcraft/releases/tag/v0.13.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/gridcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gridcraft-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Estado:** v0.13.0 · Alfa

**Qué necesitas:** No se necesita la aplicación comercial original. Aporta documentos y medios que tengas derecho a usar; las fuentes, imágenes y marcas incluidas tienen licencias independientes.

**Qué está disponible:** v0.13.0 ofrece instaladores y archivos de escritorio, además de una compilación web. Mejora casos límite de fórmulas, conserva los identificadores de las hojas al reescribir XLSX y puede abrir libros guardados sin recalcular. Alfa: se pueden probar los flujos básicos de hojas de cálculo; la fidelidad de XLSX reales, el rendimiento con libros grandes, las funciones de gráficos y la importación de formatos antiguos aún requieren trabajo. No lo hemos instalado ni probado a fondo.

**Licencia del código:** [MIT OR Apache-2.0](https://github.com/storytold/gridcraft/blob/main/LICENSE-MIT)  
**Autor:** ArtCraft  
[Documentación oficial](https://github.com/storytold/gridcraft/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>


<a id="classic_games"></a>

## Motores y recreaciones de juegos

### [Vanguard Engine](https://github.com/harshilmathur/openra2)

Un motor RTS independiente para navegador que utiliza datos de Red Alert 2, actualmente centrado en una versión parcial de desarrollo con escaramuzas soviéticas para un jugador.

Original o referencia: **Datos de Red Alert 2 / Yuri’s Revenge** · Reimplementación del motor  
[Compilar desde el código fuente](https://github.com/harshilmathur/openra2/blob/master/README.md#quickstart) · [Explorar RemakeList](https://remakelist.com/es/remakes/vanguard/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vanguard-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Navegador · servidor de desarrollo local

**Estado:** Versión parcial de desarrollo · sin lanzamiento formal

**Qué necesitas:** El modo Classic necesita archivos RA2/YR de una copia adquirida legalmente. El modo Original utiliza recursos creados para el repositorio y no necesita el juego original; ambos modos permanecen separados. Requiere Node.js 20.19+ y un servidor de desarrollo local.

**Qué está disponible:** Es una versión parcial de desarrollo sin lanzamiento formal, que requiere Node.js 20.19+ y un servidor de desarrollo local. El modo Classic necesita archivos RA2/YR obtenidos legalmente; el modo Original no necesita el juego original. Las fuerzas aliadas, el juego en red y la jugabilidad de Yuri no están completos, por lo que no es una recreación completa de Red Alert 2.

**Licencia del código:** [GPL-3.0-or-later](https://github.com/harshilmathur/openra2/blob/master/LICENSE)  
**Autor:** harshilmathur  
[Documentación oficial](https://github.com/harshilmathur/openra2/blob/master/README.md) · Fuentes revisadas: 2026-10-12

</details>

### [OpenTTD](https://github.com/OpenTTD/OpenTTD)

La jugabilidad de Transport Tycoon reconstruida para plataformas modernas, con multijugador ampliado.

Original o referencia: **Transport Tycoon Deluxe** · Reimplementación del juego  
[Descargar](https://www.openttd.org/) · [Explorar RemakeList](https://remakelist.com/es/remakes/openttd/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openttd-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux

**Estado:** Consulta la documentación oficial

**Qué necesitas:** Los gráficos básicos son obligatorios; puedes usar OpenGFX2 u OpenGFX gratuitos. Los sonidos OpenSFX y la música OpenMSX son opcionales. Este método gratuito no requiere archivos del juego original.

**Qué está disponible:** Hay versiones de escritorio disponibles. Empieza con los gráficos gratuitos obligatorios OpenGFX2 u OpenGFX; los sonidos OpenSFX y la música OpenMSX son opcionales. Este método no requiere archivos del juego original.

**Licencia del código:** [GPL-2.0; third-party components have separate licenses](https://github.com/OpenTTD/OpenTTD/blob/master/COPYING.md)  
**Autor:** OpenTTD  
[Documentación oficial](https://github.com/OpenTTD/OpenTTD/blob/master/README.md) · Fuentes revisadas: 2026-10-11

</details>

### [OpenRCT2](https://github.com/OpenRCT2/OpenRCT2)

RollerCoaster Tycoon 2 en plataformas modernas, con mejoras como multijugador cooperativo.

Original o referencia: **RollerCoaster Tycoon 2** · Reimplementación del juego  
[Descargar y aportar tus archivos del juego](https://openrct2.io/download) · [Explorar RemakeList](https://remakelist.com/es/remakes/openrct2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openrct2-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux

**Estado:** Consulta la documentación oficial

**Qué necesitas:** Debes aportar los archivos de datos originales de RCT2. Los datos de RCT1 pueden añadir escenarios.

**Qué está disponible:** Hay versiones disponibles, pero debes aportar los archivos de datos originales de RCT2. Los datos de RCT1 pueden añadir sus escenarios; el motor gratuito no incluye los recursos comerciales originales.

**Licencia del código:** [GPL-3.0-or-later](https://github.com/OpenRCT2/OpenRCT2/blob/develop/licence.txt)  
**Autor:** OpenRCT2  
[Documentación oficial](https://github.com/OpenRCT2/OpenRCT2/blob/develop/readme.md) · Fuentes revisadas: 2026-10-11

</details>

### [OpenMW](https://github.com/OpenMW/openmw)

Un motor moderno de código abierto para Morrowind, con mejoras de compatibilidad y opciones gráficas.

Original o referencia: **The Elder Scrolls III: Morrowind** · Reimplementación del motor  
[Descargar y aportar tus archivos del juego](https://www.openmw.org) · [Explorar RemakeList](https://remakelist.com/es/remakes/openmw/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openmw-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux

**Estado:** Consulta la documentación oficial

**Qué necesitas:** Jugar a Morrowind requiere poseer el juego original y configurar sus archivos de datos.

**Qué está disponible:** El motor se puede descargar, pero jugar a Morrowind requiere poseer el juego original y configurar sus archivos de datos. Algunos mods originales son incompatibles; comprueba si tu configuración actual de mods es compatible.

**Licencia del código:** [GPLv3; some fonts separately licensed](https://github.com/OpenMW/openmw/blob/master/LICENSE)  
**Autor:** OpenMW  
[Documentación oficial](https://github.com/OpenMW/openmw/blob/master/README.md) · Fuentes revisadas: 2026-10-11

</details>

### [OpenRA](https://github.com/OpenRA/OpenRA)

Juegos clásicos de estrategia en tiempo real reinventados con controles modernos y tres mods oficiales.

Original o referencia: **Red Alert 1 / Command &amp; Conquer / Dune 2000** · Reinterpretación del juego  
[Descargar](https://www.openra.net/) · [Explorar RemakeList](https://remakelist.com/es/remakes/openra/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openra-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux

**Estado:** Consulta la documentación oficial

**Qué necesitas:** Se siguen utilizando recursos de los juegos originales. El instalador oficial puede descargar los necesarios en la primera ejecución o importarlos de discos originales.

**Qué está disponible:** Hay descargas para Windows, macOS y Linux. Se necesitan recursos de los juegos originales; según el proyecto, la configuración inicial puede descargar los recursos necesarios o importarlos de discos originales.

**Licencia del código:** [GPL-3.0-or-later (engine)](https://github.com/OpenRA/OpenRA/blob/bleed/COPYING)  
**Autor:** OpenRA  
[Documentación oficial](https://www.openra.net/about/) · Fuentes revisadas: 2026-10-11

</details>

### [fheroes2](https://github.com/ihhub/fheroes2)

Una recreación del motor de Heroes of Might and Magic II para escritorio y Android, con mejoras modernas.

Original o referencia: **Heroes of Might and Magic II** · Reimplementación del motor  
[Descargar y aportar tus archivos del juego](https://github.com/ihhub/fheroes2/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/fheroes2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fheroes2-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux / Android

**Estado:** Versiones disponibles · datos originales o de demo

**Qué necesitas:** Requiere datos del juego original completo o de la demo oficial en inglés; INSTALL.md documenta el procedimiento incluido para descargar la demo. Los recursos de la demo solo proporcionan el contenido limitado autorizado por su licencia.

**Qué está disponible:** Las versiones requieren los datos del juego original completo o de la demo oficial en inglés; las instrucciones de instalación explican cómo obtener la demo. Esta incluye contenido limitado, jugar al contenido completo sigue requiriendo recursos originales adquiridos legalmente, y la configuración varía según la plataforma.

**Licencia del código:** [GPL-2.0-or-later](https://github.com/ihhub/fheroes2/blob/master/LICENSE)  
**Autor:** ihhub  
[Documentación oficial](https://github.com/ihhub/fheroes2/blob/master/README.md) · Fuentes revisadas: 2026-10-12

</details>

### [OpenXcom](https://github.com/OpenXcom/OpenXcom)

Una reimplementación de escritorio de los dos juegos clásicos X-COM, con compatibilidad con mods adicionales.

Original o referencia: **UFO: Enemy Unknown / Terror from the Deep** · Reimplementación del juego  
[Descargar y aportar tus archivos del juego](https://github.com/OpenXcom/OpenXcom/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/openxcom/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openxcom-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux

**Estado:** Motor de escritorio · requiere datos originales

**Qué necesitas:** Requiere datos originales sin modificar de UFO: Enemy Unknown o Terror from the Deep. El instalador de Windows puede extraer recursos de tu copia de Steam.

**Qué está disponible:** Las versiones de escritorio requieren datos originales sin modificar de cualquiera de los dos juegos. El instalador de Windows puede extraer recursos de tu copia de Steam; los mods adicionales pueden tener sus propios requisitos de recursos.

**Licencia del código:** [GPL-3.0-or-later](https://github.com/OpenXcom/OpenXcom/blob/master/LICENSE.txt)  
**Autor:** OpenXcom  
[Documentación oficial](https://github.com/OpenXcom/OpenXcom/blob/master/README.md) · Fuentes revisadas: 2026-10-12

</details>

### [VCMI](https://github.com/vcmi/vcmi)

Un motor de código abierto para Heroes III, con versiones de escritorio y móvil, mods y multijugador.

Original o referencia: **Heroes of Might and Magic III** · Reimplementación del motor  
[Descargar y aportar tus archivos del juego](https://vcmi.eu/download/) · [Explorar RemakeList](https://remakelist.com/es/remakes/vcmi/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vcmi-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux / Android / iOS

**Estado:** Versión pública · requiere datos originales

**Qué necesitas:** Para el juego completo necesitas datos de tu copia de Heroes III Complete o Shadow of Death. El lanzador puede importar un instalador sin conexión de GOG o una instalación existente. HD Edition por sí sola no basta: es una extensión opcional y sigue requiriendo Complete/SoD. El directorio oficial de mods también documenta compatibilidad limitada con la demo.

**Qué está disponible:** La versión 1.7.5 es pública. Hay paquetes para Windows, macOS, Linux y Android; iOS utiliza TestFlight o instalación externa. No se garantiza compatibilidad total. RemakeList no lo ha ejecutado.

**Licencia del código:** [GPL-2.0-or-later code; VCMI-created assets CC-BY-SA 4.0; original game assets separate](https://github.com/vcmi/vcmi/blob/66fa496c6328a276c4eb14c0011b3a9d751dfac3/license.txt)  
**Autor:** VCMI Team  
[Documentación oficial](https://github.com/vcmi/vcmi/blob/66fa496c6328a276c4eb14c0011b3a9d751dfac3/docs/Readme.md) · Fuentes revisadas: 2026-10-18

</details>

### [Julius](https://github.com/bvschaik/julius)

Una reimplementación fiel de Caesar III para ordenadores modernos, Android y otras plataformas.

Original o referencia: **Caesar III** · Reimplementación del juego  
[Descargar y aportar tus archivos del juego](https://github.com/bvschaik/julius/releases/tag/v1.8.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/julius/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=julius-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows · Linux · macOS · Android · Web (Emscripten) · PS Vita · Nintendo Switch

**Estado:** Publicado · requiere datos del juego original

**Qué necesitas:** Necesitas una instalación completa de tu copia de Caesar III en CD-ROM, GOG o Steam, actualizada a 1.0.1.0. Julius utiliza esa carpeta y necesita permiso para guardar partidas en ella. La licencia del código no proporciona ni licencia los recursos del juego original.

**Qué está disponible:** La versión 1.8.0 ofrece descargas para Windows, Linux, macOS y Android, además de paquetes para Vita, Switch y Emscripten. El paquete de navegador necesita configuración y tus archivos del juego. RemakeList no lo ha ejecutado.

**Licencia del código:** [AGPL-3.0 · engine code; original Caesar III assets are separate](https://github.com/bvschaik/julius/blob/34d1ecd54befb845c0139b371fa8a0438210dac1/LICENSE.txt)  
**Autor:** Bianca van Schaik and contributors  
[Documentación oficial](https://github.com/bvschaik/julius/blob/34d1ecd54befb845c0139b371fa8a0438210dac1/README.md) · Fuentes revisadas: 2026-10-18

</details>

### [CorsixTH](https://github.com/CorsixTH/CorsixTH)

Una recreación del motor de Theme Hospital para sistemas de escritorio modernos, con alta resolución y campañas de hospitales personalizables.

Original o referencia: **Theme Hospital** · Reimplementación del juego  
[Descargar y aportar tus archivos del juego](https://github.com/CorsixTH/CorsixTH/releases/tag/v0.70.1) · [Explorar RemakeList](https://remakelist.com/es/remakes/corsixth/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=corsixth-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows · macOS · Linux · BSD

**Estado:** Publicado · requiere datos originales o de la demo

**Qué necesitas:** Necesitas datos de una copia legal de Theme Hospital en CD o instalación digital; selecciona su carpeta de datos al iniciar por primera vez. La demo oficial es una alternativa con un solo nivel y sin la mayoría de las pantallas de gestión. La licencia del motor no concede derechos sobre los recursos originales.

**Qué está disponible:** La versión 0.70.1 está disponible para Windows y macOS, con AppImage y paquetes de distribuciones Linux. También admite BSD. La versión para Mac desactiva el MIDI por hardware de RtMidi. RemakeList no lo ha ejecutado.

**Licencia del código:** [MIT · engine code; Theme Hospital assets are separate](https://github.com/CorsixTH/CorsixTH/blob/master/LICENSE.txt)  
**Autor:** CorsixTH team and contributors  
[Documentación oficial](https://github.com/CorsixTH/CorsixTH/blob/master/README.md) · Fuentes revisadas: 2026-10-19

</details>

### [Warzone 2100](https://github.com/Warzone2100/warzone2100)

La continuación comunitaria del juego de estrategia 3D de 1999, con campaña completa, unidades personalizables y multijugador en escritorio.

Original o referencia: **Warzone 2100 (1999)** · Continuación de código abierto  
[Descargar](https://wz2100.net/) · [Explorar RemakeList](https://remakelist.com/es/remakes/warzone2100/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=warzone2100-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows · macOS · Linux · Web

**Estado:** Publicado · ediciones de escritorio y navegador

**Qué necesitas:** No requiere comprar por separado el juego original ni aportar una imagen de disco. Usa los paquetes oficiales; en algunas plataformas los vídeos de la campaña pueden requerir una descarga oficial adicional. El código, los datos y cada componente conservan sus licencias indicadas.

**Qué está disponible:** La versión 4.7.0 ofrece descargas para Windows, macOS y Linux; el paquete de Mac admite Intel y chips de Apple. La edición oficial para navegador incluye campaña y escaramuzas, con gráficos reducidos y sin multijugador online. RemakeList no lo ha ejecutado.

**Licencia del código:** [GPL-2.0-or-later and component licenses](https://github.com/Warzone2100/warzone2100/blob/master/COPYING)  
**Autor:** Warzone 2100 Project  
[Documentación oficial](https://github.com/Warzone2100/warzone2100/blob/master/README.md) · Fuentes revisadas: 2026-10-19

</details>

### [ScummVM](https://github.com/scummvm/scummvm)

Ejecuta aventuras clásicas como Monkey Island, Myst y Blade Runner en dispositivos modernos con motores de juego reimplementados.

Original o referencia: **Aventuras clásicas y juegos de rol** · Reimplementación del motor  
[Descargar y aportar tus archivos del juego](https://www.scummvm.org/downloads/) · [Explorar RemakeList](https://remakelist.com/es/remakes/scummvm/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=scummvm-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux / Android / iOS

**Estado:** Publicado · compatibilidad según el juego y la plataforma

**Qué necesitas:** ScummVM no incluye juegos. La mayoría de los títulos comerciales requieren tus propios datos de una versión compatible. La página oficial Freeware Games ofrece por separado versiones completas gratuitas, como Beneath a Steel Sky; no son las demos limitadas de la página Demos. Extrae el juego elegido en una carpeta y añádela al lanzador. Cada juego mantiene sus condiciones de distribución.

**Qué está disponible:** La versión estable 2026.4.0 ofrece descargas para Windows, macOS y Linux. El 19 de octubre de 2026, la página oficial aún enumera Android e iOS como 2026.3.0 en versiones anteriores. RemakeList no ha ejecutado ningún juego.

**Licencia del código:** [GPL-3.0-or-later engine code; individual game data retains its own terms](https://github.com/scummvm/scummvm/blob/7d2709da5136866589f7602f5f5a7b17de03420e/COPYING)  
**Autor:** ScummVM Team  
[Documentación oficial](https://github.com/scummvm/scummvm/blob/7d2709da5136866589f7602f5f5a7b17de03420e/README.md) · Fuentes revisadas: 2026-10-19

</details>

### [RigelEngine](https://github.com/lethal-guitar/RigelEngine)

Un motor nativo de Duke Nukem II con pantalla panorámica, movimiento más fluido, guardado rápido y mejor soporte para mandos.

Original o referencia: **Duke Nukem II** · Reimplementación del motor  
[Descargar y aportar tus archivos del juego](https://github.com/lethal-guitar/RigelEngine/releases/tag/v0.9.1) · [Explorar RemakeList](https://remakelist.com/es/remakes/rigelengine/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rigelengine-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux

**Estado:** Publicado · en mantenimiento

**Qué necesitas:** Aporta NUKEM2.CMP de una instalación de Duke Nukem II. Los cuatro episodios completos requieren datos de la versión registrada; el shareware tiene contenido limitado. NUKEM2.F1 a NUKEM2.F5 añaden vídeos introductorios opcionales. Al iniciar por primera vez, selecciona la carpeta de datos. El README oficial enlaza un archivo shareware y un vendedor autorizado del juego completo; RemakeList no incluye datos originales.

**Qué está disponible:** Los paquetes oficiales de 0.9.1 incluyen ZIP de Windows x64, DMG de macOS x64 y DEB de Linux x64. La publicación remite a los usuarios de chips Apple a una versión universal de Mac de terceros. El README indica que la versión web no está disponible actualmente. RemakeList no lo ha ejecutado.

**Licencia del código:** [GPL-2.0-or-later engine code; original Duke Nukem II data is separate](https://github.com/lethal-guitar/RigelEngine/blob/30afeff8f0b105eac77ee0a2fbd54b06e1a49b60/LICENSE.md)  
**Autor:** Nikolai Wuttke and contributors  
[Documentación oficial](https://github.com/lethal-guitar/RigelEngine/blob/30afeff8f0b105eac77ee0a2fbd54b06e1a49b60/README.md) · Fuentes revisadas: 2026-10-19

</details>

### [OpenLoco](https://github.com/OpenLoco/OpenLoco)

Una reimplementación moderna en C++ de Chris Sawyer’s Locomotion que lleva su simulación de empresas de transporte a los ordenadores actuales.

Original o referencia: **Chris Sawyer’s Locomotion** · Reimplementación del juego  
[Descargar y aportar tus archivos del juego](https://openloco.io/download/) · [Explorar RemakeList](https://remakelist.com/es/remakes/openloco/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openloco-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x86/x64 · Linux x64 · macOS con chip de Apple

**Estado:** Publicado · requiere datos del juego original

**Qué necesitas:** Aporta datos de tu copia legal de Locomotion, como una instalación de Steam o GOG. Mantén los archivos originales separados de la aplicación. Los añadidos de OpenGraphics no eliminan el requisito documentado de datos originales; MIT no concede derechos sobre los recursos comerciales del juego.

**Qué está disponible:** v26.09 ofrece ZIP para Windows de 32/64 bits, AppImage de Linux x86-64 y una aplicación nativa macOS arm64. La descarga de Mac requiere un chip de Apple y no está firmada ni notarizada. RemakeList no ha ejecutado estas versiones.

**Licencia del código:** [MIT · engine code; original game assets are separate](https://github.com/OpenLoco/OpenLoco/blob/v26.09/LICENSE)  
**Autor:** OpenLoco developers  
[Documentación oficial](https://github.com/OpenLoco/OpenLoco/blob/v26.09/README.md) · Fuentes revisadas: 2026-10-19

</details>

### [The Force Engine](https://github.com/TheForceEngine/TheForceEngine)

Juega a Dark Forces en pantalla panorámica, con controles de ratón modernos, guardado rápido y compatibilidad con los mods de su comunidad original.

Original o referencia: **Star Wars: Dark Forces** · Reimplementación del motor  
[Descargar y aportar tus archivos del juego](https://github.com/TheForceEngine/TheForceEngine/releases/tag/v1.22.420) · [Explorar RemakeList](https://remakelist.com/es/remakes/the-force-engine/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=the-force-engine-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / Linux · macOS mediante compilación del código fuente

**Estado:** Publicado · compatible con Dark Forces

**Qué necesitas:** Necesitas tu instalación adquirida de Dark Forces. El motor intenta detectar las instalaciones de Steam y GOG; si no la encuentra, selecciona la carpeta de datos en Settings &gt; Game. La licencia del motor no incluye los archivos del juego comercial.

**Qué está disponible:** Está disponible el ZIP oficial 1.22.420 para Windows. El README actual recomienda Flathub para Linux y documenta la compilación desde el código fuente para macOS. No se ha confirmado un paquete oficial de Mac listo para instalar.

**Licencia del código:** [GPL-2.0 engine code; original Dark Forces assets are separate](https://github.com/TheForceEngine/TheForceEngine/blob/master/LICENSE)  
**Autor:** Lucius and The Force Engine contributors  
[Documentación oficial](https://github.com/TheForceEngine/TheForceEngine#readme) · Fuentes revisadas: 2026-10-19

</details>

### [OpenJazz](https://github.com/AlisterT/openjazz)

Vuelve al juego de plataformas original Jazz Jackrabbit en ordenadores modernos con tus propios archivos del juego o los datos del shareware original.

Original o referencia: **Jazz Jackrabbit** · Reimplementación del motor  
[Descargar y aportar tus archivos del juego](https://github.com/AlisterT/openjazz/releases/tag/20260301) · [Explorar RemakeList](https://remakelist.com/es/remakes/openjazz/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openjazz-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux

**Estado:** Publicado · requiere datos del juego original o del shareware

**Qué necesitas:** Aporta los archivos de una instalación del primer Jazz Jackrabbit que poseas o de su versión shareware original. Los datos del juego completo son independientes del motor gratuito; el shareware incluye episodios limitados. Mantén juntos los archivos extraídos e indica su carpeta a OpenJazz.

**Qué está disponible:** La versión 20260301 ofrece binarios para Windows x86-64 y Linux x86-64; la versión de Linux requiere glibc 2.35. Mac Source Ports distribuye por separado una aplicación firmada Universal 2 para Mac con Apple silicon e Intel.

**Licencia del código:** [GPL-2.0-or-later engine code; Jazz Jackrabbit data is separate](https://github.com/AlisterT/openjazz/blob/master/doc/licenses.txt)  
**Autor:** AJ Thomson, Carsten Teibes and contributors  
[Documentación oficial](https://github.com/AlisterT/openjazz#readme) · Fuentes revisadas: 2026-10-19

</details>

### [cnc-port](https://github.com/dk8827/cnc-port)

Adapta el código de Tiberian Dawn publicado por EA a sistemas modernos.

Original o referencia: **Command &amp; Conquer: Tiberian Dawn** · Continuación de código abierto  
[Compilar y aportar tus archivos del juego](https://github.com/dk8827/cnc-port#readme) · [Explorar RemakeList](https://remakelist.com/es/remakes/cnc-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=cnc-port-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** macOS · Android depuración · iOS Simulador

**Estado:** Código fuente · móvil en desarrollo

**Qué necesitas:** Prepara datos GDI y Nod de C&amp;C Gold Windows 95. El autor enlaza copias comunitarias del freeware histórico; no incluye datos. La licencia del código no concede derechos sobre el juego original, sus imágenes ni sus datos comerciales.

**Qué está disponible:** Hay que compilar: menús y juego táctico probados en Mac; APK Android de depuración y Simulador iOS documentados. Compilar o iniciar en el Simulador no demuestra juego en dispositivos reales. Las copias no están alojadas por EA.

**Licencia del código:** [GPLv3 with additional EA terms. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/dk8827/cnc-port#license-and-notice)  
**Autor:** dk8827  
[Documentación oficial](https://github.com/dk8827/cnc-port#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Generals Zero Hour for Mac, iPhone &amp; iPad](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad)

Generals: Zero Hour para Apple, basado en el código EA y GeneralsX.

Original o referencia: **Command &amp; Conquer: Generals — Zero Hour** · Continuación de código abierto  
[Compilar y aportar tus archivos del juego](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad#readme) · [Explorar RemakeList](https://remakelist.com/es/remakes/generals-apple/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=generals-apple-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Mac Apple Silicon / iPhone / iPad

**Estado:** Adaptación jugable · requiere compilar

**Qué necesitas:** Tus archivos comerciales o Steam de Zero Hour, un Mac Apple Silicon compatible y las herramientas documentadas. La licencia del código no concede derechos sobre el juego original, sus imágenes ni sus datos comerciales.

**Qué está disponible:** Compila en Mac; iPhone/iPad requieren además Xcode y firma Apple. El autor informa de campañas y escaramuzas jugables. Proceso desde código fuente, no edición móvil oficial de EA; datos y firma son requisitos separados.

**Licencia del código:** [GPLv3 with upstream terms. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad#readme)  
**Autor:** ammaarreshi  
[Documentación oficial](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad#readme) · Fuentes revisadas: 2026-10-19

</details>

### [geow2](https://github.com/techknight/geow2)

geow2 — Seis modos y multijugador local. Una adaptación independiente de Geometry Wars: Retro Evolved 2 para los dispositivos indicados.

Original o referencia: **Geometry Wars: Retro Evolved 2** · Reimplementación del juego  
[Descargar y aportar tus archivos del juego](https://github.com/techknight/geow2/releases/tag/v1.2.6) · [Explorar RemakeList](https://remakelist.com/es/remakes/geow2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=geow2-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS 11+ / Linux x64

**Estado:** v1.2.6 · escritorio y Flatpak

**Qué necesitas:** Aporta tus propios archivos obtenidos legalmente: Xbox Live Arcade · 584108FF · v0x102 · FFmpeg. El proyecto es gratuito; el juego original va aparte. Aquí no se ofrecen archivos del juego, claves ni paquetes listos para jugar.

**Qué está disponible:** v1.2.6 ofrece archivos para Windows, macOS y Linux, además de un Flatpak para Linux/Steam Deck, y corrige el comportamiento al mantener pulsado Escape/Enter. Aporta tu propio título XBLA 584108FF versión 0x102. La extracción inicial de audio necesita FFmpeg; el Flatpak lo incluye, y una carpeta de datos ya preparada no lo necesita. Windows/Linux requieren Vulkan; macOS 11+ admite Apple Silicon e Intel. El multijugador es local para hasta cuatro jugadores; la sincronización opcional de puntuaciones en línea usa un servidor independiente de amigos. RemakeList no lo ha instalado ni jugado.

**Licencia del código:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/techknight/geow2/blob/main/LICENSE)  
**Autor:** techknight  
[Documentación oficial](https://github.com/techknight/geow2#readme) · Fuentes revisadas: 2026-10-30

</details>

### [NOVA Swift](https://github.com/SirStig/NovaSwift)

NOVA Swift — Combate espacial, historias y complementos comunitarios. Una adaptación independiente de Escape Velocity Nova para los dispositivos indicados.

Original o referencia: **Escape Velocity Nova** · Reimplementación del motor  
[Descargar y aportar tus archivos del juego](https://sirstig.github.io/NovaSwift/download.html) · [Explorar RemakeList](https://remakelist.com/es/remakes/nova-swift/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nova-swift-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** macOS / iOS / iPadOS / tvOS / Linux / Windows / Steam Deck

**Estado:** Beta; quedan errores y pruebas incompletas.

**Qué necesitas:** Aporta tus propios archivos obtenidos legalmente: EV Nova · datos originales del juego. El proyecto es gratuito; el juego original va aparte. Aquí no se ofrecen archivos del juego, claves ni paquetes listos para jugar.

**Qué está disponible:** Vía oficial: macOS / iOS / iPadOS / tvOS / Linux / Windows / Steam Deck. Beta; quedan errores y pruebas incompletas. Elige el paquete oficial adecuado para tu sistema.

**Licencia del código:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/SirStig/NovaSwift/blob/main/LICENSE)  
**Autor:** SirStig  
[Documentación oficial](https://github.com/SirStig/NovaSwift#readme) · Fuentes revisadas: 2026-10-19

</details>

### [PeonPad](https://github.com/chrissotraidis/peonpad)

PeonPad — Gestos táctiles para estrategia clásica en tiempo real. Una adaptación independiente de Warcraft II para los dispositivos indicados.

Original o referencia: **Warcraft II** · Reimplementación del motor  
[Descargar y aportar tus archivos del juego](https://github.com/chrissotraidis/peonpad/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/peonpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=peonpad-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** iPadOS 16+

**Estado:** Versión para desarrolladores · IPA sin firmar · firma propia necesaria

**Qué necesitas:** Necesitas tus propios archivos de Warcraft II y un Mac o PC con las herramientas Wargus para generar la carpeta data.Wargus completa. Cópiala tras instalar la aplicación firmada. El IPA gratuito no contiene datos del juego ni concede derechos sobre el contenido de Blizzard.

**Qué está disponible:** Versión preliminar para iPadOS 16+. La versión previa de GitHub ofrece un IPA sin firmar y sin datos de Warcraft II. Fírmalo e instálalo tú; compilar la aplicación es opcional. En un Mac o PC, extrae los datos de tu juego con Wargus y copia la carpeta data.Wargus completa a On My iPad/PeonPad/data.Wargus. No hay importador interno, App Store ni TestFlight.

**Licencia del código:** [GPL-2.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/chrissotraidis/peonpad/blob/main/LICENSE)  
**Autor:** chrissotraidis  
[Documentación oficial](https://github.com/chrissotraidis/peonpad#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Pocket Wormhole](https://github.com/adamkulik/pocket-wormhole)

Pocket Wormhole — Controles táctiles e importación local de ftl.dat. Una adaptación independiente de FTL: Faster Than Light para los dispositivos indicados.

Original o referencia: **FTL: Faster Than Light** · Reimplementación del motor  
[Descargar y aportar tus archivos del juego](https://github.com/adamkulik/pocket-wormhole/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/pocket-wormhole/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pocket-wormhole-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Android 8+ · GLES 3.0

**Estado:** Versión preliminar jugable o experimental.

**Qué necesitas:** Aporta tus propios archivos obtenidos legalmente: Steam / GOG · ftl.dat · ~280 MB. El proyecto es gratuito; el juego original va aparte. Aquí no se ofrecen archivos del juego, claves ni paquetes listos para jugar.

**Qué está disponible:** Vía oficial: Android 8+ · GLES 3.0. Versión preliminar jugable o experimental. La transferencia de partidas entre motores tiene límites; lee la guía. Elige el paquete oficial adecuado para tu sistema.

**Licencia del código:** [GPL-2.0-or-later applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/adamkulik/pocket-wormhole/blob/main/LICENSE)  
**Autor:** adamkulik  
[Documentación oficial](https://github.com/adamkulik/pocket-wormhole#readme) · Fuentes revisadas: 2026-10-19

</details>

### [ra-port](https://github.com/dk8827/ra-port)

Port del primer Red Alert para sistemas modernos. Requiere tus datos originales y compilar el código; aún no tiene multijugador en red.

Original o referencia: **Command &amp; Conquer: Red Alert** · Continuación de código abierto  
[Compilar y aportar tus archivos del juego](https://github.com/dk8827/ra-port#readme) · [Explorar RemakeList](https://remakelist.com/es/remakes/ra-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ra-port-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** macOS / Linux / Android / iOS / iPadOS

**Estado:** Compilación propia · requiere juego original

**Qué necesitas:** Aporta tus archivos obtenidos legalmente que correspondan a: Red Alert 1 · Allied + Soviet discs. El contenido comercial es independiente y RemakeList no lo proporciona.

**Qué está disponible:** Solo compilación del código: macOS y Linux, más versiones debug locales para Android e iOS. No hay aplicación Mac empaquetada ni lanzamiento móvil; no tiene red multijugador.

**Licencia del código:** [GPL-3.0 with EA additional terms](https://github.com/dk8827/ra-port#readme)  
**Autor:** dk8827  
[Documentación oficial](https://github.com/dk8827/ra-port#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Rugrats: Search for Reptar — Rust Port](https://github.com/toyz/rugrats)

Reimplementación en Rust de Rugrats: Search for Reptar para PC. Necesita tu disco de PS1 y compilar el proyecto.

Original o referencia: **Rugrats: Search for Reptar** · Reimplementación del juego  
[Compilar y aportar tus archivos del juego](https://github.com/toyz/rugrats#readme) · [Explorar RemakeList](https://remakelist.com/es/remakes/rugrats-rust-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rugrats-rust-port-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows

**Estado:** Compilación propia · requiere juego original

**Qué necesitas:** Aporta tus archivos obtenidos legalmente que correspondan a: PlayStation USA · SLUS-00650 · owned disc. El contenido comercial es independiente y RemakeList no lo proporciona.

**Qué está disponible:** El autor documenta niveles jugables hasta los créditos. La instalación exige Rust y compilar el código; no se ha confirmado un instalador listo para usar.

**Licencia del código:** [MIT OR Apache-2.0 authored code; original game data excluded](https://github.com/toyz/rugrats#readme)  
**Autor:** toyz  
[Documentación oficial](https://github.com/toyz/rugrats#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Rich4 Renew](https://github.com/iam567/rich4-renew-app)

Una recreación no oficial de Richman 4 para ordenadores y móviles, con gráficos redibujados en alta resolución, compraventa de propiedades, bolsa, cartas y partidas de grupo en línea.

Original o referencia: **Richman 4** · Reimplementación del juego  
[Descargar](https://github.com/iam567/rich4-renew-app/releases/tag/v0.8.1) · [Explorar RemakeList](https://remakelist.com/es/remakes/rich4-renew/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rich4-renew-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Android / iOS

**Estado:** v0.8.1 · controles de reglas de partida · recursos sujetos a restricciones

**Qué necesitas:** Ejecutar el código fuente requiere rich4-assets.tar, que el autor proporciona por separado. Contiene material derivado del juego original, gráficos redibujados en alta resolución, mapas y sonidos. Estos recursos quedan excluidos de la GPL y el autor los restringe al uso privado. Los scripts de empaquetado incluyen los recursos en las aplicaciones, pero no se ha inspeccionado de forma independiente el contenido de los paquetes publicados. Una descarga gratuita no implica permiso para redistribuir las ilustraciones ni el material del juego original.

**Qué está disponible:** v0.8.1 ofrece descargas de ZIP para Windows, DMG universal para Mac, APK para Android e IPA sin firmar para iOS. Los anfitriones pueden fijar fondos iniciales compartidos, movimiento, permisos sobre terrenos, límites de tiempo y reglas de victoria; la sala móvil en horizontal permite desplazarse para que el botón de inicio siga accesible. iOS requiere firma propia; Windows no está firmado y Mac no está notarizado. Los recursos derivados del original y los redibujados quedan fuera de GPL, y la declaración de uso privado del autor no acredita autorización del titular de derechos. No se inspeccionaron de forma independiente los contenidos ni las firmas de la versión. RemakeList no ha compilado, instalado ni jugado esta versión.

**Licencia del código:** [GPL-3.0-or-later · code only](https://github.com/iam567/rich4-renew-app/blob/main/LICENSE)  
**Autor:** iam567 (Liang)  
[Documentación oficial](https://github.com/iam567/rich4-renew-app/blob/main/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [Model 3-Vulkan](https://github.com/Igloo-Garage/Model-3-Vulkan)

Bifurcación con mejoras Vulkan de Supermodel, emulador de las recreativas Sega Model 3. Gratis y de código abierto; requiere ROM de juegos obtenidas legalmente por el usuario.

Original o referencia: **Arcade Sega Model 3 / Supermodel** · emulator-enhancement-fork  
[Descargar y aportar tus archivos del juego](https://github.com/Igloo-Garage/Model-3-Vulkan/releases/tag/v0.9.8.3b) · [Explorar RemakeList](https://remakelist.com/es/remakes/supermodel-vk/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=supermodel-vk-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64, Linux x86-64 y macOS 11+ (Intel / Apple Silicon)

**Estado:** v0.9.8.3b · Model 3-Vulkan · requiere tus propias ROM

**Qué necesitas:** No incluye ROM de juegos. El usuario debe aportar archivos ZIP de ROM Model 3 obtenidos legalmente. La licencia GPL del código no cubre los datos de los juegos, sus recursos gráficos ni las marcas comerciales.

**Qué está disponible:** Model 3-Vulkan es el nuevo nombre del proyecto Supermodel-VK. v0.9.8.3b ofrece archivos para Windows, Linux y macOS, restaura los efectos de sonido perdidos en v0.9.8.3a y añade soporte nativo para paquetes de texturas DDS. Sigue siendo un emulador que requiere tus propios conjuntos de ROM. La compatibilidad y el rendimiento varían según el juego. La portada existente es un fotograma histórico de una vista previa, no una captura recién verificada de v0.9.8.3b. RemakeList no ha instalado ni ejecutado esta versión. El paquete de macOS no está notarizado y Gatekeeper puede bloquearlo; sigue las instrucciones de instalación del autor.

**Licencia del código:** [GPL-3.0-or-later · emulator code](https://github.com/Igloo-Garage/Model-3-Vulkan/blob/master/Docs/LICENSE.txt)  
**Autor:** Igloo-Garage · upstream: The Supermodel Team  
[Documentación oficial](https://github.com/Igloo-Garage/Model-3-Vulkan/blob/master/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [pokerecomp](https://github.com/Decryptu/pokerecomp)

Reimplementación Godot de las dos primeras generaciones Pokémon con gráficos y controles modernos. Lee contenido de tus ROM GB/GBC compatibles.

Original o referencia: **Pokémon Red/Blue/Yellow and Gold/Silver/Crystal** · Reimplementación del juego  
[Descargar y aportar tus archivos del juego](https://github.com/Decryptu/pokerecomp/releases/tag/v0.1.86) · [Explorar RemakeList](https://remakelist.com/es/remakes/pokerecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pokerecomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64/ARM64; Linux x64/ARM64; macOS; Android; iOS; Switch homebrew

**Estado:** v0.1.86 · generaciones 1–2 · requiere ROM propia

**Qué necesitas:** Tu revisión compatible de Red, Blue, Yellow, Gold, Silver o Crystal con hash coincidente. El motor no incluye los juegos originales.

**Qué está disponible:** v0.1.86 ofrece versiones de escritorio, APK Android, IPA iOS sin firma y paquete Switch homebrew. iOS requiere firma personal/instalación externa; Switch, un entorno homebrew existente. La generación 3 es experimental y no jugable. Rechaza revisiones ROM no admitidas. Apple no es una publicación normal de App Store: macOS tiene firma ad hoc y la firma iOS con cuenta gratuita suele renovarse periódicamente.

**Licencia del código:** [The rewritten engine code is MIT. Original Pokémon code, ROM content, artwork and music remain outside that license.](https://github.com/Decryptu/pokerecomp/blob/main/LICENSE)  
**Autor:** Decryptu  
[Documentación oficial](https://github.com/Decryptu/pokerecomp/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [Streetball Revival](https://github.com/luckvj/streetball-revival)

Recreación Rust de NBA Street Vol. 2 con controles de escritorio y juego en línea experimental. Carga tu disco PS2 USA compatible.

Original o referencia: **NBA Street Vol. 2 (PS2)** · Reimplementación del juego  
[Descargar y aportar tus archivos del juego](https://github.com/luckvj/streetball-revival/releases/tag/v0.1.4-beta) · [Explorar RemakeList](https://remakelist.com/es/remakes/streetball-revival/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=streetball-revival-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows; Linux

**Estado:** v0.1.4-beta · Windows/Linux · juego en línea experimental

**Qué necesitas:** Tu ISO PS2 USA NBA Street Vol. 2, SLUS-20651, con el hash requerido. El motor no incluye datos originales.

**Qué está disponible:** v0.1.4-beta ofrece instalador/archivo Windows y archivo Linux. El juego en línea sigue en desarrollo y necesita más pruebas de jugadores. La equivalencia es incompleta: equipos controlados por ordenador, gráficos y cámara Gamebreaker pueden diferir. La tabla del autor mide conductas seleccionadas, no un porcentaje de fidelidad de todo el juego.

**Licencia del código:** [The rewritten engine is MIT. The license does not include EA’s original game data, artwork or music.](https://github.com/luckvj/streetball-revival/blob/main/LICENSE)  
**Autor:** luckvj  
[Documentación oficial](https://github.com/luckvj/streetball-revival/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [Torchlight Rekindled](https://github.com/GreenSwampDweller/torchlight-rekindled)

Motor Torchlight para portátiles y escritorio que sigue la lógica orientada a mando de Xbox 360. Usa datos de tu copia PC o Xbox 360.

Original o referencia: **Torchlight** · Reimplementación del motor  
[Descargar y aportar tus archivos del juego](https://github.com/GreenSwampDweller/torchlight-rekindled/releases/tag/1.1.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/torchlight-rekindled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=torchlight-rekindled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Switch homebrew / Android 12+ arm64 / iOS / Windows / Linux

**Estado:** 1.1.0 · soporte de mods; sin nuevo IPA adjunto

**Qué necesitas:** pak.zip/Pak.zip y carpeta de música de tu edición completa comprada PC o Xbox 360. Los datos PC usan la interfaz alternativa de consola del proyecto. No distribuye datos del juego.

**Qué está disponible:** 1.1.0 ofrece NRO para Switch, APK para Android y archivos para Windows/Linux, y añade soporte para carpetas de mods de PC y correcciones de juego. Esta versión no tiene IPA adjunto; las compilaciones de iOS siguen necesitando firma personal. Aporta tu propio pak.zip completo y la música de PC/Xbox 360; los datos de PC recurren a la interfaz de consola. Android requiere versión 12+, ARM64 y acceso a todos los archivos de la carpeta del juego elegida. Las pruebas de escritorio se limitan al portátil del autor con un mando; Steam Deck no está verificado.

**Licencia del código:** [GPL-3.0 for the engine; game data and third-party components retain separate rights](https://github.com/GreenSwampDweller/torchlight-rekindled/blob/main/LICENSE)  
**Autor:** GreenSwampDweller  
[Documentación oficial](https://github.com/GreenSwampDweller/torchlight-rekindled/blob/main/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [ZQuest Classic](https://github.com/ZQuestClassic/ZQuestClassic)

Motor, reproductor de aventuras y editor gratuitos al estilo del Zelda original de NES. Juega creaciones comunitarias o crea las tuyas.

Original o referencia: **The Legend of Zelda / Zelda-style adventures** · Reimplementación del motor  
[Descargar](https://zquestclassic.com/releases/) · [Explorar RemakeList](https://remakelist.com/es/remakes/zquest-classic/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=zquest-classic-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux / Web (experimental)

**Estado:** Versión de escritorio estable · reproductor web experimental

**Qué necesitas:** El motor usa archivos de aventuras: obténlos de sus autores o crea los tuyos. GPL no concede derechos sobre nombres/arte Nintendo ni recursos de terceros; comprueba las condiciones de cada aventura.

**Qué está disponible:** La estable 2.55.17 ofrece Windows x64/x86, macOS y Linux; la web oficial tiene reproductor experimental. Se elige 2.55.17 estable; las versiones preliminares 3.0 son una línea separada. La web es experimental, también en móvil. Compatibilidad y condiciones de recursos varían por autor y versión del motor. RemakeList solo verificó documentación y metadatos, sin instalar ni jugar aventuras.

**Licencia del código:** [GPL-3.0 for the engine; individual quests and their media have separate rights](https://github.com/ZQuestClassic/ZQuestClassic/blob/main/LICENSE)  
**Autor:** ZQuestClassic  
[Documentación oficial](https://github.com/ZQuestClassic/ZQuestClassic/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>


<a id="ports"></a>

## Adaptaciones y proyectos de compatibilidad

### [D2R Mobile](https://github.com/jhaizhou-ops/d2r-mobile)

Una capa de compatibilidad para usar tus propios archivos de Diablo II: Resurrected y Reign of the Warlock de Switch en dispositivos Apple, Android y HarmonyOS, con preparación específica para cada plataforma.

Original o referencia: **Diablo II: Resurrected** · Capa de compatibilidad entre plataformas  
[Compilar y aportar tus archivos del juego](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) · [Explorar RemakeList](https://remakelist.com/es/remakes/d2r-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=d2r-mobile-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** iPhone / iPad / Mac con Apple silicon / Android ARM64 / HarmonyOS NEXT

**Estado:** v2.1.0 · archivos propios de Switch · cámara experimental opcional

**Qué necesitas:** Aporta los archivos ExeFS y RomFS de tu compra legal del juego base de Switch y Reign of the Warlock, actualizados a la versión de consola 1.0.34.0, denominada 3.3.94012 por las herramientas. Los archivos de PC y de otras consolas no sirven como sustituto. Los recursos ocupan unos 5,6 GB; los chips Apple antiguos necesitan un paquete de texturas adicional de aproximadamente 1 GB generado a partir de tus archivos. Apple requiere como mínimo A14/M1; elige la versión normal o la de API antiguas para iOS 26+ frente a 18–25 y macOS 26+ frente a 15–25. Android necesita ARM64, Android 12+ y Vulkan 1.1. HarmonyOS NEXT requiere una cuenta de desarrollador, herramientas de firma y un paquete de ejecución preparado por ti.

**Qué está disponible:** v2.1.0 actualiza la APK de Android y los dos ZIP de entrada para compilar iOS. Android conserva el paquete de importación y las partidas existentes; iOS requiere crear y firmar una nueva app con los nuevos archivos y el código v2.1.0. La HAP de HarmonyOS sin firmar sigue siendo la de v2.0.0 y necesita tu firma de desarrollador y un paquete de ejecución. Mac solo permite compilar desde el código. Solo funciona sin conexión. En Android quedan detalles táctiles incompletos y fallos gráficos en ciertos dispositivos. Los dispositivos Apple con 4 GB de RAM tienen poca memoria disponible; la firma mediante herramientas de instalación externa y el empaquetado en Linux siguen sin verificar. Un Apple ID gratuito requiere renovar la firma cada 7 días y no permite sincronizar por iCloud. Apple TV solo llega a una vista previa de selección de personaje. No redistribuyas paquetes que incluyan contenido del juego. RemakeList no lo ha compilado, instalado ni jugado.

**Licencia del código:** [MIT covers project code; original game files and third-party components retain separate rights and licenses.](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/LICENSE)  
**Autor:** joe jiang (@happyjoejiang)  
[Documentación oficial](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [MW2 Recompiled](https://github.com/PaulCombal/mw2-recompiled)

Recompilación nativa de Modern Warfare 2 (2009) de Xbox 360 para Windows y Linux.

Original o referencia: **Modern Warfare 2 (2009)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/PaulCombal/mw2-recompiled/releases/tag/v0.8.1) · [Explorar RemakeList](https://remakelist.com/es/remakes/mw2-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mw2-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / Linux x64 · SSE4.2 · Vulkan 1.2

**Estado:** Estable v0.8.1 · versión preliminar v0.8.2 disponible

**Qué necesitas:** Aporta tu propia ISO de un disco de Xbox 360 de Estados Unidos o Europa, versión 1.0.557, obtenida legalmente; el lanzador la comprueba y descarga y aplica Title Update 6. Requiere un procesador x64 con SSE4.2, Vulkan 1.2, unos 8 GB de disco y un mando; el teclado solo controla los menús. La importación experimental de mapas personalizados de PC también necesita recursos de tu propia copia para PC.

**Qué está disponible:** La descarga principal sigue siendo la versión estable v0.8.1 para Windows y Linux. v0.8.2 es una versión preliminar independiente. Ejecuta mw2-launcher con tu ISO compatible y usa el paquete normal de tu plataforma; los archivos -steam/-lan de la misma versión son descargas de compatibilidad duplicadas. No admite emparejamiento público ni partidas clasificatorias; los mapas personalizados siguen en beta. Otros usuarios de Steam pueden encontrar las partidas SYSTEM LINK, y los usuarios de un relay o LAN compartidos también pueden acceder. Usa la misma versión y juega con personas de confianza. El autor informa de correcciones de red; RemakeList no ha auditado su seguridad ni lo ha instalado o jugado.

**Licencia del código:** [GPL-3.0-only](https://github.com/PaulCombal/mw2-recompiled/blob/master/LICENSE)  
**Autor:** PaulCombal  
[Documentación oficial](https://github.com/PaulCombal/mw2-recompiled/blob/master/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [Zelda 64: Recompiled](https://github.com/Zelda64Recomp/Zelda64Recomp)

Recompilación estática de Majora’s Mask para escritorio, con controles y opciones gráficas modernos.

Original o referencia: **Majora’s Mask** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/Zelda64Recomp/Zelda64Recomp/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/zelda64-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=zelda64-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / Linux / macOS

**Estado:** Publicado · recursos originales

**Qué necesitas:** Necesita tu ROM norteamericana de Majora’s Mask para N64. Ni el repositorio ni las versiones incluyen recursos del juego.

**Qué está disponible:** Hay binarios v1.2.2 para Windows, Linux y macOS. Requiere una API gráfica compatible. No ejecutado aquí.

**Licencia del código:** [GPL-3.0](https://github.com/Zelda64Recomp/Zelda64Recomp/blob/dev/COPYING)  
**Autor:** Zelda64Recomp team  
[Documentación oficial](https://github.com/Zelda64Recomp/Zelda64Recomp/blob/dev/README.md) · Fuentes revisadas: 2026-10-14

</details>

### [MacNativeGames · Tears of the Kingdom](https://github.com/ly05010419/MacNativeGames)

Crea una app nativa de Tears of the Kingdom para Mac Apple silicon o iPhone/iPad con tus archivos de Switch. Experimental; exige compilación local y firma del dispositivo.

Original o referencia: **The Legend of Zelda: Tears of the Kingdom** · Capa de compatibilidad entre plataformas  
[Compilar y aportar tus archivos del juego](https://github.com/ly05010419/MacNativeGames#build-the-app) · [Explorar RemakeList](https://remakelist.com/es/remakes/zelda-totk-mac-research/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=zelda-totk-mac-research-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Mac Apple silicon · macOS 26+; iPhone 14+ / iPad · iOS/iPadOS 26+

**Estado:** Experimental · compilación y firma local · sin versión formal

**Qué necesitas:** Requiere tu juego Switch base v1.0.0 en XCI/NSP y claves/archivos del sistema extraídos de tu consola. Mac admite actualizaciones separadas v1.1.2/v1.2.1/v1.4.3 en NSP/NSZ; solo v1.4.3 está probada en iOS. Mac Apple silicon con macOS 26+, Metal 4 y 16 GB RAM recomendados. Además del juego: unos 25 GB para la base Mac, 17 GB extra sin clonado APFS y 40 GB para una compilación nueva actualizada. iOS necesita Xcode 26 completo, iOS/iPadOS 26+, como mínimo iPhone 14 para teléfonos, y firma con permiso de memoria ampliada; reserva 45 GB para base nueva o 60 GB con actualización. La app contiene el juego y es solo para uso propio. No ofrecemos juegos, claves, firmware, apps firmadas ni sombreadores derivados.

**Qué está disponible:** Compilación desde código sin Releases formales. El autor informa de pruebas en Mac M4 y de jugar v1.4.3 en iPhone 14 y un iPad A16; RemakeList no lo probó. Los antiguos 90 FPS aproximados con caché preparada en Mac no garantizan rendimiento estable ni completar el juego. iPhone 14 usa casi 4 GB y iOS lo cerró dos veces tras unos ocho minutos en zonas exigentes. En iOS pueden faltar objetos por sombreadores ausentes; nuevas escenas Mac pueden dar tirones. Sin online ni amiibo.

**Licencia del código:** [Project code MIT · game rights and third-party licenses separate](https://github.com/ly05010419/MacNativeGames/blob/main/LICENSE)  
**Autor:** Yong Li / liyong (@liyong2077)  
[Documentación oficial](https://github.com/ly05010419/MacNativeGames/blob/b75be8cfa704df3701e86130c8ced268e79d6b11/README.md) · Fuentes revisadas: 2026-10-20

</details>

### [Dusklight](https://github.com/TwilitRealm/dusklight)

Una adaptación nativa de Twilight Princess con resoluciones superiores, opciones de fotogramas por segundo y un explorador de mods integrado.

Original o referencia: **The Legend of Zelda: Twilight Princess** · Proyecto basado en descompilación  
[Descargar y aportar tus archivos del juego](https://twilitrealm.dev/install/) · [Explorar RemakeList](https://remakelist.com/es/remakes/dusklight/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=dusklight-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / Linux / macOS / iOS / Android

**Estado:** Publicado · requiere recursos originales

**Qué necesitas:** Extrae tu propia copia comercial de Twilight Princess para GameCube o Wii. La edición coreana de Wii no es compatible. El proyecto no proporciona recursos del juego protegidos por derechos de autor.

**Qué está disponible:** Hay versiones oficiales para ordenador y móvil; iOS requiere instalación externa. Se recomienda D3D12, Vulkan 1.1+ o Metal. Los sistemas gráficos antiguos ofrecen precisión y rendimiento limitados. RemakeList no lo ha ejecutado.

**Licencia del código:** [CC0-1.0 · project code; original game assets excluded](https://github.com/TwilitRealm/dusklight/blob/main/LICENSE.md)  
**Autor:** Twilit Realm  
[Documentación oficial](https://github.com/TwilitRealm/dusklight/blob/main/README.md) · Fuentes revisadas: 2026-10-18

</details>

### [Mega Man X4 Recompiled](https://github.com/mstan/MegaManX4Recomp)

Una recompilación nativa de Mega Man X4 con cooperación para dos jugadores, X y Zero, en local o por red. La versión actual es una beta pública.

Original o referencia: **Mega Man X4** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/mstan/MegaManX4Recomp/releases/tag/v1.0.17) · [Explorar RemakeList](https://remakelist.com/es/remakes/mega-man-x4-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mega-man-x4-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / Linux x86-64 (glibc 2.38+)

**Estado:** v1.0.17 · beta pública

**Qué necesitas:** Aporta tu propia imagen de disco original y sin modificar de Mega Man X4 USA (SLUS-00561), con sus archivos .cue y .bin, incluso si desactivas todos los mods. No se admiten discos parcheados, versiones undub ni imágenes retraducidas. Se incluye OpenBIOS; aportar una copia de la BIOS es opcional. El contenido original del juego queda fuera de la licencia MIT.

**Qué está disponible:** v1.0.17 es una beta pública con paquetes para Windows x64 y Linux x64. Corrige los menús de pausa emparejados y varios casos de cámara y escenarios con dos jugadores. Conserva las partidas nativas de tarjetas de memoria y todos los jugadores en red deben actualizar; la grabación de diagnóstico sigue siendo opcional y está desactivada por defecto. Las cámaras independientes aún pueden causar ralentizaciones y continúan investigándose informes de fallos de inicio de sesión o arranque en línea. Linux necesita glibc 2.38+. Los experimentos con cuatro jugadores son independientes; no se ha acreditado una campaña completa, la secuencia de créditos ni una partida completa por LAN. Aporta el disco USA compatible sin modificar. RemakeList no lo ha compilado, instalado ni jugado.

**Licencia del código:** [MIT · original project code; dependencies retain their licenses](https://github.com/mstan/MegaManX4Recomp/blob/master/LICENSE)  
**Autor:** Matthew Stanley  
[Documentación oficial](https://github.com/mstan/MegaManX4Recomp/blob/master/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [Tekken 3 Recompiled](https://github.com/FishB0nes98/Tekken3Recompiled)

Una versión preliminar para Windows de una recompilación híbrida de Tekken 3, con pantalla panorámica, atuendos personalizados e importación opcional de Jun Kazama.

Original o referencia: **Tekken 3** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/FishB0nes98/Tekken3Recompiled/releases/tag/v0.1.4) · [Explorar RemakeList](https://remakelist.com/es/remakes/tekken-3-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=tekken-3-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64

**Estado:** Recompilación híbrida preliminar · disco propio necesario

**Qué necesitas:** Aporta tu propio disco de Tekken 3 USA (SLUS-00402), poseído legalmente, en formato CUE/BIN. Jun requiere además los ZIP arcade no fusionados tektagt (World C1) y tekken3 (World E1); desactiva Include Jun Kazama si no dispones de ellos. El proyecto indica que excluye datos comerciales del juego, BIOS de Sony y recursos donantes extraídos; utiliza OpenBIOS. La licencia del código no concede derechos sobre el juego original.

**Qué está disponible:** Versión preliminar pública Easy Setup v0.1.4 para Windows x64. La primera instalación descarga herramientas con versiones fijadas y compila localmente; requiere Internet y al menos 4 GB de espacio de trabajo. Linux y Steam Deck no están verificados. RemakeList no lo ha ejecutado.

**Código visible; sujeto a restricciones de licencia:** [Source available under PolyForm Noncommercial 1.0.0; dependencies retain their licenses](https://github.com/FishB0nes98/Tekken3Recompiled/blob/main/LICENSE)  
**Autor:** FishB0nes98  
[Documentación oficial](https://github.com/FishB0nes98/Tekken3Recompiled/blob/main/README.md) · Fuentes revisadas: 2026-10-18

</details>

### [DevilutionX](https://github.com/diasurgical/DevilutionX)

Diablo y Hellfire en ordenadores y móviles actuales, con pantalla panorámica, mandos y mejoras de comodidad opcionales.

Original o referencia: **Diablo / Hellfire** · Proyecto basado en descompilación  
[Descargar y aportar tus archivos del juego](https://github.com/diasurgical/DevilutionX/releases/tag/1.5.5) · [Explorar RemakeList](https://remakelist.com/es/remakes/devilutionx/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=devilutionx-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux / Android / iOS

**Estado:** Publicado · el juego completo requiere datos propios

**Qué necesitas:** Diablo completo requiere DIABDAT.MPQ de tu CD original o instalación comprada. Hellfire necesita además hellfire.mpq, hfmonk.mpq, hfmusic.mpq y hfvoice.mpq. La guía oficial ofrece spawn.mpq para la parte shareware limitada; no desbloquea el juego completo. Los textos chinos, japoneses y coreanos también necesitan fonts.mpq del proyecto.

**Qué está disponible:** La versión oficial 1.5.5 ofrece ZIP para Windows, DMG universal para macOS, versiones para Linux, APK para Android e IPA para iOS. iOS requiere instalación externa. Se revisaron las listas de paquetes y la documentación; RemakeList no ha ejecutado el juego.

**Código visible; sujeto a restricciones de licencia:** [Source available under Sustainable Use License 1.0; redistribution must be free of charge and non-commercial; original game assets excluded](https://github.com/diasurgical/DevilutionX/blob/0011dc9670c2093d5ab0084c1cdbeb086556563a/LICENSE.md)  
**Autor:** diasurgical / DevilutionX contributors  
[Documentación oficial](https://github.com/diasurgical/DevilutionX/blob/0011dc9670c2093d5ab0084c1cdbeb086556563a/README.md) · Fuentes revisadas: 2026-10-18

</details>

### [ACFA-Port](https://github.com/sulphurs16/acfa-port)

Adaptación no oficial de ARMORED CORE for Answer a Windows desde tus archivos de PS3.

Original o referencia: **ARMORED CORE for Answer** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/SulphurS16/ACFA-Port/releases/tag/v0.7.4) · [Explorar RemakeList](https://remakelist.com/es/remakes/acfa-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=acfa-port-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64

**Estado:** v0.7.4 · compilación local en Windows

**Qué necesitas:** Se requieren tus archivos PS3 USA BLUS30187, RPCS3 y software de sistema PS3 4.93; actualización 01.35 opcional. La licencia del código no concede derechos sobre el juego original, sus imágenes ni sus datos comerciales.

**Qué está disponible:** v0.7.4 ofrece un ZIP con un lanzador para Windows que compila el juego localmente, con correcciones del control de VOB con ratón y de las entradas de menú. Requiere tus propios archivos del disco USA de PS3 BLUS30187, RPCS3 y el firmware 4.93 de Sony; la actualización 01.35 es opcional. Se necesitan Windows 10 1903+/11 x64, AVX2 y Direct3D 11. El proyecto no incluye el juego original ni el firmware; RemakeList no lo ha compilado ni jugado.

**Licencia del código:** [MIT. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/SulphurS16/ACFA-Port/blob/main/LICENSE)  
**Autor:** SulphurS16  
[Documentación oficial](https://github.com/sulphurs16/acfa-port#readme) · Fuentes revisadas: 2026-10-30

</details>

### [AgePad](https://github.com/chrissotraidis/agepad)

Vista previa para iPad de Age of Empires II: Definitive Edition usando tu copia Steam para Mac.

Original o referencia: **Age of Empires II: Definitive Edition** · Capa de compatibilidad entre plataformas  
[Compilar y aportar tus archivos del juego](https://github.com/chrissotraidis/agepad#readme) · [Explorar RemakeList](https://remakelist.com/es/remakes/agepad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=agepad-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** iPad · 8 GB+ RAM

**Estado:** Vista previa · riesgo de cuenta sin resolver

**Qué necesitas:** Juego Steam para Mac, versiones compatibles de juego y Steam, Mac, iPad con al menos 8 GB de RAM y 25 GB libres y firma para instalación externa. La licencia del código no concede derechos sobre el juego original, sus imágenes ni sus datos comerciales.

**Qué está disponible:** La vista previa 0.1.0 combina en Mac el pequeño paquete del autor con tus archivos del juego y Steam; después se firma e instala. Compatibilidad con Steam y seguridad de la cuenta sin confirmar. Partidas completas en línea y otros equipos además del iPad M2 del autor no verificados.

**Licencia del código:** [MIT (AgePad code). The code license grants no rights to the original game, artwork or commercial data.](https://github.com/chrissotraidis/agepad#credits-and-license)  
**Autor:** chrissotraidis  
[Documentación oficial](https://github.com/chrissotraidis/agepad#readme) · Fuentes revisadas: 2026-10-19

</details>

### [BearBirdPad](https://github.com/chrissotraidis/bearbirdpad)

Integración móvil Apple de BanjoRecomp para Banjo-Kazooie.

Original o referencia: **Banjo-Kazooie** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/chrissotraidis/bearbirdpad#readme) · [Explorar RemakeList](https://remakelist.com/es/remakes/bearbirdpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=bearbirdpad-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** iPhone / iPad · iOS 16+

**Estado:** Vista previa para compilar

**Qué necesitas:** Se requieren tu ROM NTSC-U 1.0, Mac Apple Silicon con Xcode e identidad de firma Apple. La licencia del código no concede derechos sobre el juego original, sus imágenes ni sus datos comerciales.

**Qué está disponible:** Compila y firma en un Mac Apple Silicon con Xcode o PadMint; las publicaciones contienen recetas, no aplicaciones. Probado por el autor en iPhone 14 y iPad Pro; mandos y ciclo de vida con verificación incompleta. Sin App Store/TestFlight.

**Licencia del código:** [GPL-3.0-or-later. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/chrissotraidis/bearbirdpad#legal-and-acknowledgements)  
**Autor:** chrissotraidis  
[Documentación oficial](https://github.com/chrissotraidis/bearbirdpad#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Birdman64](https://github.com/noahvl/birdman64)

Pilotwings 64 nativo para ordenador a partir de tu ROM USA.

Original o referencia: **Pilotwings 64** · Proyecto basado en descompilación  
[Descargar y aportar tus archivos del juego](https://github.com/noahvl/birdman64/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/birdman64/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=birdman64-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / Linux · Android experimental · iOS requiere compilar

**Estado:** Escritorio disponible · móvil experimental

**Qué necesitas:** Tu ROM USA e internet para la primera compilación; no se descarga ninguna ROM. La licencia del código no concede derechos sobre el juego original, sus imágenes ni sus datos comerciales.

**Qué está disponible:** Publicaciones de escritorio con preparación local inicial. Android experimental; iPhone/iPad requieren compilar. La verificación móvil es limitada; no hay aplicación iOS lista para descargar.

**Licencia del código:** [MIT (project code). The code license grants no rights to the original game, artwork or commercial data.](https://github.com/NoahVl/Birdman64#license)  
**Autor:** NoahVl  
[Documentación oficial](https://github.com/noahvl/birdman64#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Chupathingy](https://github.com/ChupathingyCE/chupathingyce)

Adaptación nativa multiplataforma basada en la descompilación de Halo CE y OpenCE.

Original o referencia: **Halo: Combat Evolved** · Proyecto basado en descompilación  
[Descargar y aportar tus archivos del juego](https://github.com/ChupathingyCE/chupathingyce/releases/tag/v0.8.1d) · [Explorar RemakeList](https://remakelist.com/es/remakes/chupathingy/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=chupathingy-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux / Android

**Estado:** v0.8.1d · Publicado · requiere datos originales de Xbox

**Qué necesitas:** Se requiere imagen de disco o mapas de tu copia Xbox. Mapas opcionales de PC y Custom Edition en carpetas separadas. La licencia del código no concede derechos sobre el juego original, sus imágenes ni sus datos comerciales.

**Qué está disponible:** v0.8.1d ofrece paquetes para Windows, macOS, Linux y Android y adopta la versión de red 41, la más reciente de OpenCE. Ahora hay un AppImage de Linux x64 adjunto a la versión; los paquetes de 32 bits y Android ARM64 se eligen por separado. El juego principal sigue requiriendo los mapas originales de Xbox. La compilación de Android ARM64 es una opción experimental independiente; siguen vigentes las limitaciones de memoria de mapas y compatibilidad de red. RemakeList no ha compilado, instalado ni jugado esta versión.

**Licencia del código:** [GPL-3.0-or-later from 0.8.0; earlier releases through 0.7.5d CC0. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/ChupathingyCE/chupathingyce#license)  
**Autor:** Milenko (MrMilenko) and ChupathingyCE contributors; credits retain OpenCE and Halo decomp authors  
[Documentación oficial](https://github.com/ChupathingyCE/chupathingyce#readme) · Fuentes revisadas: 2026-10-30

</details>

### [CTRPad](https://github.com/chrissotraidis/ctrpad)

Integración de CTR Native y CTR-ModSDK para plataformas Apple y el Crash Team Racing original, con controles táctiles e importación local de disco. Crea una app personal con PadMint en Mac o su GitHub Cloud Build para iPhone/iPad.

Original o referencia: **Crash Team Racing (1999)** · Proyecto basado en descompilación  
[Compilar y aportar tus archivos del juego](https://github.com/chrissotraidis/ctrpad#readme) · [Explorar RemakeList](https://remakelist.com/es/remakes/ctrpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ctrpad-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Mac Apple Silicon (macOS 11+) / iPhone / iPad (iOS/iPadOS 15+)

**Estado:** v0.2.4 · compilación personal · publicación solo de receta

**Qué necesitas:** Importa tu propio BIN compatible NTSC-U SCUS944.26, de una sola pista, raw MODE2/2352 y desde el byte cero. Selecciona el BIN, no el CUE; no admite ISO convertidas, CHD ni archivos comprimidos. La compilación Apple local requiere las herramientas documentadas de compilación y firma; iPhone/iPad en la nube usa su ruta de firma documentada. La licencia del código no cubre datos ni arte del juego original.

**Qué está disponible:** v0.2.4 corrige el arranque horizontal y la disposición táctil del iPad. La publicación solo incluye una receta PadMint y su suma de verificación, no una app. Compila en un Mac Apple Silicon o usa GitHub Cloud Build de PadMint para iPhone/iPad sin Mac; importa tu BIN compatible después de instalar. Mantén privadas las compilaciones personales; no hay versión App Store/TestFlight. El autor informa de partidas en Mac/iPhone/iPad y una comprobación de la corrección en un iPad físico; las pruebas generales, de mandos y de multijugador local siguen incompletas. RemakeList no lo ha instalado ni jugado.

**Licencia del código:** [GPL-3.0. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/chrissotraidis/ctrpad/blob/main/LICENSE)  
**Autor:** chrissotraidis  
[Documentación oficial](https://github.com/chrissotraidis/ctrpad#readme) · Fuentes revisadas: 2026-10-28

</details>

### [Def Jam: Fight for NY Recompiled](https://github.com/vyanhursky/DefJamFFNY-recomp)

Compila una versión nativa de Def Jam: Fight for NY para Windows, Mac o Linux a partir de tu propia copia extraída compatible de la edición estadounidense para la Xbox original, con mayor resolución y hasta cuatro jugadores locales. La pantalla panorámica sigue en beta.

Original o referencia: **Def Jam: Fight for NY** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/vyanhursky/DefJamFFNY-recomp/releases/tag/v0.12.3) · [Explorar RemakeList](https://remakelist.com/es/remakes/defjam-ffny-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=defjam-ffny-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 (Direct3D 11) / macOS con Apple silicon / Linux x86-64 / Steam Deck

**Estado:** v0.12.3 · compilación local

**Qué necesitas:** Aporta tu propia imagen de disco estadounidense de la Xbox original o una copia extraída que coincida con el manifiesto admitido por el autor. Las versiones de PS2 y GameCube no sirven como sustituto. La herramienta verifica, recompila y construye localmente; generar texturas HD requiere más tiempo y espacio de disco. La licencia del código no concede derechos sobre el juego ni sus ilustraciones originales.

**Qué está disponible:** v0.12.3 ofrece un instalador para Windows, un DMG para Mac con Apple silicon y un archivo para Linux x64. Uniformiza la cadencia de fotogramas de la simulación y corrige las compilaciones con GCC más reciente/CachyOS. El instalador analiza y compila localmente tu propio disco del juego; el proceso de actualización conserva partidas y mods. La compatibilidad con pantalla panorámica y mods sigue siendo limitada; esta versión corrige la cadencia de fotogramas, pero no acredita todas las escenas ni configuraciones. El multijugador es local. La versión de macOS no está firmada; RemakeList no lo ha instalado ni jugado.

**Licencia del código:** [MIT project code; separate toolkit licenses. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/vyanhursky/DefJamFFNY-recomp#credits-and-licensing)  
**Autor:** vyanhursky  
[Documentación oficial](https://github.com/vyanhursky/DefJamFFNY-recomp#readme) · Fuentes revisadas: 2026-10-29

</details>

### [DOAXVB Native PC Port](https://github.com/norain211/doaxvb-re)

Adaptación nativa no oficial de Dead or Alive Xtreme Beach Volleyball, compilada localmente desde tu disco Xbox estadounidense. La beta recomendada v0.6.0 tiene nuevo lanzador y paquetes de escritorio, pero conserva fallos gráficos.

Original o referencia: **Dead or Alive Xtreme Beach Volleyball** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/NoRain211/doaxvb-re/releases/tag/v0.6.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/doaxvb-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=doaxvb-native-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 / macOS Apple silicon·Intel / Linux x86-64·Steam Deck

**Estado:** Beta recomendada v0.6.0 · compilación local · pruebas incompletas

**Qué necesitas:** Aporta tu propia imagen compatible de disco Xbox estadounidense; la instalación valida y genera el código del juego localmente. Mac/Linux también requieren las herramientas de compilación documentadas; Steam Deck usa un contenedor con compilador. El contenido generado del juego y el arte original quedan fuera de la licencia GPL-3.0-or-later del proyecto.

**Qué está disponible:** v0.6.0 sustituye a v0.5.3 como beta recomendada por el autor y ofrece ZIP para Windows, Mac y Linux. Cada uno compila desde tu disco: extrae en una carpeta nueva y vuelve a compilar porque cambió la receta, y después copia tus partidas privadas anteriores. Windows ahora descarga llvm-mingw y no requiere Visual Studio. El autor no ha realizado una sesión completa de juego con v0.6.0. Se documentan comprobaciones de compilación de los ZIP Windows/Linux, pero el ZIP Mac no se compiló en un Mac; los controles del lanzador se comprobaron con un mando virtual. Persisten parpadeos en la orilla y fallos de transición en la piscina. En Mac/Linux faltan algunas nieblas, luces y sombras; la opción GI con trazado de rayos no tiene efecto en las versiones publicadas. RemakeList no lo ha compilado ni jugado.

**Licencia del código:** [GPL-3.0-or-later. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/norain211/doaxvb-re#license)  
**Autor:** NoRain211  
[Documentación oficial](https://github.com/norain211/doaxvb-re#readme) · Fuentes revisadas: 2026-10-28

</details>

### [Forza Horizon 1: ReImagined](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined)

Compila localmente una adaptación nativa para Windows y Linux a partir de tus propios archivos de Forza Horizon de Xbox 360, con servicios en línea comunitarios, ajustes de coches y opciones de imagen.

Original o referencia: **Forza Horizon** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined/releases/tag/v0.2.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/forza-horizon-reimagined/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=forza-horizon-reimagined-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 / Linux x86-64; macOS solo como compilación experimental desde código

**Estado:** v0.2.0 publicada · Compilación local · VR experimental

**Qué necesitas:** Aporta tu propia imagen de disco de Forza Horizon de Xbox 360, paquete Games on Demand o carpeta extraída, obtenidos legalmente. Debes aportar por separado Title Update 4 y los DLC; Horizon Rally y 1000 Club requieren TU4. Reserva unos 4 GB de RAM libre y 15 GB de disco. La opción Vulkan requiere Vulkan 1.3; Windows también ofrece Direct3D 12. La configuración inicial necesita descargar o instalar herramientas de compilación.

**Qué está disponible:** v0.2.0 ofrece un instalador para Windows, un archivo para Linux x86-64 y un Flatpak. El lanzador genera y compila el juego localmente a partir de tus archivos; después de actualizar hay que recompilarlo una vez. macOS sigue siendo una opción experimental de compilación desde código, sin descarga para Mac. El rendimiento en Steam Deck y equipos modestos continúa siendo limitado, con problemas gráficos o cierres en algunas GPU. El autor probó VR en Quest 3 con WiVRn para Linux; VR en Windows no se ha probado. En macOS siguen pendientes las carreras completas, la recarga de partidas y los mandos físicos. Quienes usan TU4 y quienes usan el juego base tienen salas en línea separadas, y las partidas de TU4 no pueden volver directamente al juego base. RemakeList no lo ha compilado ni jugado.

**Licencia del código:** [The current project code uses GPL-3.0-or-later, with an additional permission described in NOTICE.md for graphics, VR and platform components. Earlier releases and commits published under MIT remain available under MIT. Original game content and third-party components retain separate rights; the linked Forza Live server and website have their own AGPL-3.0-or-later terms.](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined/blob/main/LICENSE)  
**Autor:** Dyotson  
[Documentación oficial](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined#readme) · Fuentes revisadas: 2026-10-30

</details>

### [Gears of War 2 PC Port](https://github.com/santiquiroz/gears-of-war-2-pc-port)

Una adaptación nativa no oficial que utiliza tus propios archivos de Gears of War 2 de Xbox 360, con renderizado de alta resolución, pantalla dividida y cooperación mediante System Link. Android sigue siendo experimental y no se ha verificado la campaña completa.

Original o referencia: **Gears of War 2** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/santiquiroz/gears-of-war-2-pc-port/releases/tag/v0.3.11) · [Explorar RemakeList](https://remakelist.com/es/remakes/gears-of-war-2-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gears-of-war-2-native-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 (DirectX 12) / Android 10+ ARM64 (Vulkan, experimental)

**Estado:** v0.3.11 · Versión pública · campaña probada parcialmente · Android experimental

**Qué necesitas:** Aporta tu propia ISO de la versión comercial de Gears of War 2 para Xbox 360 (ID 4D53082D), obtenida legalmente, o una carpeta completa con default.xex y GearGame. La extracción inicial de la ISO en Windows necesita unos 8 GB. La importación en Android copia los datos al almacenamiento de la app y requiere espacio para otra copia completa. RemakeList no proporciona datos del juego.

**Qué está disponible:** v0.3.11 ofrece paquetes para Windows x64 y Android ARM64 experimental. El comprobador de actualizaciones de PC conserva su estado y la elección de omitir una versión; en Android solo cambia la versión del paquete. Los cambios anteriores de Android en 0.3.10 y el contador de fotogramas siguen sin probarse en teléfonos. Solo el Acto 1 tiene una partida completa reportada por el autor; las revisiones de capítulos no verifican los Actos 2–5. El calor afecta al rendimiento en Android. El cooperativo de tres/cuatro jugadores y el juego por internet mantienen escenarios sin probar y requieren la misma versión. El emborronamiento en AMD tiene la alternativa Emulated EDRAM; persisten los fallos del texto de menús en Vega y de D3D12 en Proton. Los archivos de Windows no están firmados; las afirmaciones del autor sobre análisis de seguridad no son una certificación. RemakeList no lo ha compilado, instalado ni jugado.

**Licencia del código:** [BSD-3-Clause applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/santiquiroz/gears-of-war-2-pc-port/blob/master/LICENSE)  
**Autor:** santiquiroz  
[Documentación oficial](https://github.com/santiquiroz/gears-of-war-2-pc-port#readme) · Fuentes revisadas: 2026-10-30

</details>

### [GoldenEye 007 PC Port](https://github.com/jkdansereau/goldeneye-pc-port)

GoldenEye 007 PC Port — Pantalla panorámica, ratón y pantalla dividida. Una adaptación independiente de GoldenEye 007 para los dispositivos indicados.

Original o referencia: **GoldenEye 007** · Proyecto basado en descompilación  
[Descargar y aportar tus archivos del juego](https://github.com/jkdansereau/goldeneye-pc-port/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/goldeneye-007-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=goldeneye-007-pc-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / Linux / Steam Deck

**Estado:** Versión preliminar jugable o experimental.

**Qué necesitas:** Aporta tus propios archivos obtenidos legalmente: Nintendo 64 · GoldenEye 007 ROM · USA. El proyecto es gratuito; el juego original va aparte. Aquí no se ofrecen archivos del juego, claves ni paquetes listos para jugar.

**Qué está disponible:** Vía oficial: Windows / Linux / Steam Deck. Versión preliminar jugable o experimental. Compatibilidad con ROM PAL y japonesas incompleta. Elige el paquete oficial adecuado para tu sistema.

**Licencia del código:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/jkdansereau/goldeneye-pc-port/blob/main/LICENSE)  
**Autor:** jkdansereau  
[Documentación oficial](https://github.com/jkdansereau/goldeneye-pc-port#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Gravity Rush 2 Native Port](https://github.com/HayatoG/gr2_pc)

Gravity Rush 2 Native Port — Servicios de PS4 adaptados a gráficos Vulkan de escritorio. Una adaptación independiente de Gravity Rush 2 para los dispositivos indicados.

Original o referencia: **Gravity Rush 2** · Capa de compatibilidad entre plataformas  
[Descargar y aportar tus archivos del juego](https://github.com/HayatoG/gr2_pc/releases/tag/v2026.10.24-a2e69a1) · [Explorar RemakeList](https://remakelist.com/es/remakes/gravity-rush-2-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gravity-rush-2-native-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Linux x86-64 (glibc 2.39+) · Windows 10/11 x64 (juego sin verificar) · Vulkan

**Estado:** v2026.10.24-a2e69a1 · experimental; Windows sin validar

**Qué necesitas:** Aporta tus propios archivos base de PS4 Gravity Rush 2 USA CUSA03694 combinados con la actualización exacta 01.11, incluido el eboot.bin de esa actualización (unos 28 GB en total). El audio necesita además libSceNgs2.sprx de tu propio firmware de PS4, colocado en system_lib/. No se incluyen archivos del juego ni del firmware.

**Qué está disponible:** v2026.10.24-a2e69a1 ofrece archivos para Linux x86-64 (glibc 2.39+) y Windows 10/11 x64. Aborda bloqueos de shaders/GPU en cinemáticas e importaciones del cargador de DLC. Se informa de juego funcional en Linux; el paquete de Windows se declara explícitamente aún sin probar dentro del juego. El juego en Windows, las partidas guardadas y la cobertura del mundo abierto siguen en validación. El rendimiento en Linux reportado por el autor no garantiza el de todos los equipos. RemakeList no ha compilado, instalado ni jugado esta versión. Archivos originales / configuración: Aporta tus propios archivos base de PS4 Gravity Rush 2 USA CUSA03694 combinados con la actualización exacta 01.11, incluido el eboot.bin de esa actualización (unos 28 GB en total). El audio necesita además libSceNgs2.sprx de tu propio firmware de PS4, colocado en system_lib/. No se incluyen archivos del juego ni del firmware.

**Licencia del código:** [GPL-2.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/HayatoG/gr2_pc/blob/main/port/LICENSE)  
**Autor:** HayatoG  
[Documentación oficial](https://github.com/HayatoG/gr2_pc#readme) · Fuentes revisadas: 2026-10-29

</details>

### [inFAMOUS Second Son Native Port](https://github.com/HayatoG/iss_pc)

Adaptación no oficial de compatibilidad para PC de inFAMOUS Second Son, con tus propios archivos de PS4 y paquetes para Linux y Windows. Hay documentación de los primeros capítulos; persisten problemas gráficos y de rendimiento.

Original o referencia: **inFAMOUS Second Son** · Capa de compatibilidad entre plataformas  
[Descargar y aportar tus archivos del juego](https://github.com/HayatoG/iss_pc/releases/tag/v1.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/infamous-second-son-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=infamous-second-son-native-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Linux x86-64 / Windows 10 (1903+)–11 x64 · Vulkan 1.3

**Estado:** Estable v1.0 · beta-rc1 opcional · archivos originales de PS4

**Qué necesitas:** Aporta tus propios archivos descifrados del juego base PS4 CUSA00223 de EE. UU., versión 1.00, combinados con la actualización 1.07: unos 33 GB. Requiere AVX, Vulkan 1.3 y, preferiblemente, 6 GB de VRAM. El audio no necesita un archivo de firmware de la consola; no se incluyen archivos del juego.

**Qué está disponible:** v1.0 sigue siendo la descarga estable recomendada para Linux x86-64 (glibc 2.39+) y Windows 10/11 x64. beta-rc1 es una versión preliminar descargable por separado para las mismas plataformas, no su sustituta estable. La tasa de fotogramas y los gráficos siguen siendo irregulares. La compatibilidad con RX 580/Polaris en Windows es experimental. beta-rc1 enumera texturas negras del suelo al reescalar, FSR poco nítido a 3x y reescalado en Linux sin probar; el lanzador no ofrece las betas como actualizaciones normales. RemakeList no ha instalado ni jugado ninguna de las dos versiones.

**Licencia del código:** [GPL-2.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/HayatoG/iss_pc/blob/main/port/LICENSE)  
**Autor:** HayatoG  
[Documentación oficial](https://github.com/HayatoG/iss_pc#readme) · Fuentes revisadas: 2026-10-28

</details>

### [LAS Recomp](https://github.com/peiikai/LASRecomp)

Compila localmente una adaptación nativa para escritorio a partir de tus propios archivos de Link’s Awakening para Switch 1.0.0, 1.0.1 o 1.1.0, con pantalla panorámica y opciones de aleatorización. Sigue en beta.

Original o referencia: **The Legend of Zelda: Link’s Awakening** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/peiikai/LASRecomp/releases/tag/beta_5.4) · [Explorar RemakeList](https://remakelist.com/es/remakes/las-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=las-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / macOS con Apple silicon / Linux x64; Linux ARM64 experimental

**Estado:** beta_5.4 · Beta · requiere archivos originales

**Qué necesitas:** Aporta tus propios archivos exefs y romfs de Link’s Awakening para Switch 1.0.0, 1.0.1 o 1.1.0, obtenidos legalmente, y selecciona su carpeta para compilar localmente. Mac requiere Apple silicon y macOS 15+. Windows 10/11 y Linux x64 necesitan AVX2, FMA, Vulkan 1.3, al menos 8 GB de RAM y unos 12 GB para la configuración. No se proporcionan archivos de juego ni claves.

**Qué está disponible:** beta_5.4 es la descarga general para Windows, Mac con Apple silicon y Linux; corrige el renderizado de BowWow, líneas de hierba, la selección de mando y varios fallos del aleatorizador. La compilación posterior test-462-arc-2 sirve solo para probar problemas con Intel Arc; su corrección no forma parte de beta_5.4. Aún pueden producirse cierres, semillas sin solución y fallos de pantalla panorámica, especialmente al mezclar salas. Linux ARM64 no tiene pruebas en hardware; los Mac Intel y las GPU integradas Intel antiguas no son compatibles. Los ID de semillas anteriores a Beta-5 producen resultados distintos. RemakeList no ha compilado, instalado ni jugado esta versión.

**Licencia del código:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/peiikai/LASRecomp/blob/main/LICENSE)  
**Autor:** peiikai  
[Documentación oficial](https://github.com/peiikai/LASRecomp#readme) · Fuentes revisadas: 2026-10-30

</details>

### [Lets Go Recomp](https://github.com/raulzrrs/letsgo-recomp)

Lets Go Recomp — Exploración, capturas y combates de entrenadores. Una adaptación independiente de Pokémon: Let’s Go, Eevee! / Pikachu! para los dispositivos indicados.

Original o referencia: **Pokémon: Let’s Go, Eevee! / Pikachu!** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/raulzrrs/letsgo-recomp/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/lets-go-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=lets-go-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10–11 x64 · Vulkan 1.3 · AVX2

**Estado:** Versión preliminar jugable o experimental.

**Qué necesitas:** Aporta tus propios archivos obtenidos legalmente: Nintendo Switch · exefs + romfs · Eevee 1.0.0. El proyecto es gratuito; el juego original va aparte. Aquí no se ofrecen archivos del juego, claves ni paquetes listos para jugar.

**Qué está disponible:** Vía oficial: Windows 10–11 x64 · Vulkan 1.3 · AVX2. Versión preliminar jugable o experimental. No se ha verificado el juego completo. Eevee 1.0.0 es la versión más probada; Pikachu y las actualizaciones tienen menos pruebas. Elige el paquete oficial adecuado para tu sistema.

**Licencia del código:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/raulzrrs/letsgo-recomp/blob/main/LICENSE)  
**Autor:** raulzrrs  
[Documentación oficial](https://github.com/raulzrrs/letsgo-recomp#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Muscle March Recomp](https://github.com/tmcleroy/muscle-march-recomp)

Muscle March Recomp — Controles con palancas, táctiles y de teclado. Una adaptación independiente de Muscle March para los dispositivos indicados.

Original o referencia: **Muscle March** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/tmcleroy/muscle-march-recomp/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/muscle-march-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=muscle-march-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10–11 / macOS 13+ Apple silicon / Linux / Android 8+ ARM64

**Estado:** Beta; quedan errores y pruebas incompletas.

**Qué necesitas:** Aporta tus propios archivos obtenidos legalmente: WiiWare · USA WAD + clave común de tu propia Wii. El proyecto es gratuito; el juego original va aparte. Aquí no se ofrecen archivos del juego, claves ni paquetes listos para jugar.

**Qué está disponible:** Vía oficial: Windows 10–11 / macOS 13+ Apple silicon / Linux / Android 8+ ARM64. Beta; quedan errores y pruebas incompletas. El rendimiento publicado corresponde a pocos dispositivos. Según el autor, los paquetes incluyen código del juego traducido, aunque no archivos de datos. Elige el paquete oficial adecuado para tu sistema.

**Licencia del código:** [GPL-3.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/tmcleroy/muscle-march-recomp/blob/main/LICENSE)  
**Autor:** tmcleroy  
[Documentación oficial](https://github.com/tmcleroy/muscle-march-recomp#readme) · Fuentes revisadas: 2026-10-19

</details>

### [NSMB Wii Multiplayer Recompilation](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation)

NSMB Wii Multiplayer Recompilation — Controles táctiles y multijugador LAN entre móviles y PC. Una adaptación independiente de New Super Mario Bros. Wii para los dispositivos indicados.

Original o referencia: **New Super Mario Bros. Wii** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation/releases/tag/v0.3.1) · [Explorar RemakeList](https://remakelist.com/es/remakes/nsmb-wii-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nsmb-wii-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Android 9+ ARM64 · Windows 10/11 x64 · Linux x86-64 (validación limitada en hardware)

**Estado:** v0.3.1 · Versión preliminar jugable o experimental.

**Qué necesitas:** Aporta tus propios archivos obtenidos legalmente: Wii · USA SMNE01 · revisión 1. El proyecto es gratuito; el juego original va aparte. Aquí no se ofrecen archivos del juego, claves ni paquetes listos para jugar.

**Qué está disponible:** v0.3.1 ofrece paquetes para Windows x64, Linux x64 y Android ARM64 y corrige los elementos de nivel incorrectos introducidos en 0.3.0. La actualización subyacente traslada el trabajo gráfico a un segundo núcleo de CPU en dispositivos compatibles; las mejoras dependen del dispositivo. Se conservan partidas, ajustes y datos del juego importados. Sigue siendo una versión preliminar. Linux solo tiene pruebas de renderizado por software en WSL; las GPU de equipos Linux/Steam Deck reales y los teléfonos Mali carecen de validación. Las versiones incluyen código del juego traducido, aunque excluyen los archivos de datos del juego. RemakeList no lo ha compilado, instalado ni jugado.

**Licencia del código:** [GPL-3.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation/blob/main/LICENSE)  
**Autor:** WitherBlitz  
[Documentación oficial](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation#readme) · Fuentes revisadas: 2026-10-30

</details>

### [OpenSA2](https://github.com/kittycache9/OpenSA2)

OpenSA2 — Entorno nativo, controles táctiles Android y ajustes opcionales. Una adaptación independiente de Sonic Adventure 2 para los dispositivos indicados.

Original o referencia: **Sonic Adventure 2** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/kittycache9/OpenSA2/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/opensa2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=opensa2-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / Linux / Android

**Estado:** Versión preliminar jugable o experimental.

**Qué necesitas:** Aporta tus propios archivos obtenidos legalmente: PC · Sonic Adventure 2 (2012) · ejecutable y recursos. El proyecto es gratuito; el juego original va aparte. Aquí no se ofrecen archivos del juego, claves ni paquetes listos para jugar.

**Qué está disponible:** Vía oficial: Windows / Linux / Android. Versión preliminar jugable o experimental. No se ha verificado el juego completo. Elige el paquete oficial adecuado para tu sistema. Los paquetes oficiales incluyen lógica del juego recompilada y el entorno del port. Debes aportar mediante el instalador el ejecutable y los recursos de tu edición PC 2012 compatible; no son simples paquetes vacíos.

**Licencia del código:** [GPL-3.0-only applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/kittycache9/OpenSA2/blob/main/LICENSE)  
**Autor:** kittycache9  
[Documentación oficial](https://github.com/kittycache9/OpenSA2#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Ottsel](https://github.com/chrissotraidis/ottsel)

Ottsel — Controles táctiles, mandos y pantalla externa. Una adaptación independiente de Jak and Daxter: The Precursor Legacy para los dispositivos indicados.

Original o referencia: **Jak and Daxter: The Precursor Legacy** · Proyecto basado en descompilación  
[Compilar y aportar tus archivos del juego](https://github.com/chrissotraidis/ottsel#readme) · [Explorar RemakeList](https://remakelist.com/es/remakes/ottsel/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ottsel-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** iPadOS 18.5+ / macOS Apple silicon

**Estado:** Versión para desarrolladores; requiere compilar o firmar.

**Qué necesitas:** Aporta tus propios archivos obtenidos legalmente: PS2 · USA SCUS-97124 · Black Label. El proyecto es gratuito; el juego original va aparte. Aquí no se ofrecen archivos del juego, claves ni paquetes listos para jugar.

**Qué está disponible:** Vía oficial: iPadOS 18.5+ / macOS Apple silicon. Versión para desarrolladores; requiere compilar o firmar. Hay ejecuciones documentadas en iPad y Mac; iPhone físico sin verificar. Compila localmente según las instrucciones oficiales.

**Licencia del código:** [ISC applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/chrissotraidis/ottsel/blob/main/LICENSE)  
**Autor:** chrissotraidis  
[Documentación oficial](https://github.com/chrissotraidis/ottsel#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Phantom Hourglass Recomp](https://github.com/dguillot-gh/phantom-hourglass-recomp)

Phantom Hourglass Recomp — Diseños de pantalla flexibles con ARM9 recompilado y núcleo de hardware melonDS. Una adaptación independiente de The Legend of Zelda: Phantom Hourglass para los dispositivos indicados.

Original o referencia: **The Legend of Zelda: Phantom Hourglass** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/dguillot-gh/phantom-hourglass-recomp#readme) · [Explorar RemakeList](https://remakelist.com/es/remakes/phantom-hourglass-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=phantom-hourglass-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / Android

**Estado:** Versión preliminar jugable o experimental.

**Qué necesitas:** Aporta tus propios archivos obtenidos legalmente: Nintendo DS · USA · ROM SHA-1: 4c8f52dd719918bbcd46e73a8bae8628139c1b85 / 7e0d26d143992f1eee182b24f1abb9e7f038eacf. El proyecto es gratuito; el juego original va aparte. Aquí no se ofrecen archivos del juego, claves ni paquetes listos para jugar.

**Qué está disponible:** Vía oficial: Windows / Android. Versión preliminar jugable o experimental. Las aplicaciones y archivos derivados del juego son privados; no los redistribuyas. Compila localmente según las instrucciones oficiales.

**Licencia del código:** [GPL-3.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/dguillot-gh/phantom-hourglass-recomp/blob/main/LICENSE)  
**Autor:** dguillot-gh  
[Documentación oficial](https://github.com/dguillot-gh/phantom-hourglass-recomp#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Pinyon Shift](https://github.com/arcanite24/pinyon-shift)

Pinyon Shift — Lanzador, opciones gráficas y vía para Steam Deck. Una adaptación independiente de Forza Horizon para los dispositivos indicados.

Original o referencia: **Forza Horizon** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/arcanite24/pinyon-shift/releases/tag/v0.7.1) · [Explorar RemakeList](https://remakelist.com/es/remakes/pinyon-shift/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pinyon-shift-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / Linux x86-64·SteamOS / macOS 13+ Apple silicon / Android 13+ alfa

**Estado:** v0.7.1 · compilación local · Android alfa

**Qué necesitas:** Aporta tu propio disco comercial estadounidense de Forza Horizon para Xbox 360 (MS-2505, ID 4D5309C9) o una carpeta extraída compatible sin modificar; TU4 y los DLC propios van por separado. El autor estima entre 20 y 60 minutos para la primera compilación y unos 30 GB libres. En escritorio se requiere Vulkan 1.3. La alfa de Android necesita Android 13+ y Vulkan 1.3, y está ajustada para Snapdragon 8 Gen 2+ con 8 GB de RAM.

**Qué está disponible:** v0.7.1 ofrece lanzadores para Windows, Linux x86-64 y Mac con Apple silicon. Cada uno compila el juego a partir de tus archivos; actualizar vuelve a compilar conservando partidas, ajustes y DLC. Android no tiene una APK de lanzamiento lista: créala en el PC mediante el lanzador y transfiérela al dispositivo. Persisten fallos gráficos y ralentizaciones. Las GPU AMD/Intel de PC aún no están validadas; v4 en Linux/Mac solo tiene pruebas de recorridos automatizados. Android es alfa y las GPU ajenas a Qualcomm requieren activación expresa. DLSS solo está en Windows; DualSense por Bluetooth o fuera de Windows no se ha probado. El UDLC comunitario cubre pocos coches y tiene derechos de contenido independientes. RemakeList no lo ha compilado ni jugado.

**Licencia del código:** [BSD-3-Clause applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/arcanite24/pinyon-shift/blob/main/LICENSE)  
**Autor:** arcanite24  
[Documentación oficial](https://github.com/arcanite24/pinyon-shift#readme) · Fuentes revisadas: 2026-10-28

</details>

### [Red Alert 2 Recomp](https://github.com/sp00nznet/redalert2-recomp)

Utiliza un instalador para construir localmente una versión nativa a partir de tus propios archivos de Red Alert 2 / Yuri’s Revenge, con pantalla panorámica y opciones de presentación modernas. Es distinto de OpenRA, RA2WEB y Vanguard.

Original o referencia: **Red Alert 2 / Yuri’s Revenge** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/sp00nznet/redalert2-recomp/releases/tag/v0.1.3) · [Explorar RemakeList](https://remakelist.com/es/remakes/redalert2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=redalert2-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / Linux x64 / macOS ARM64

**Estado:** Instalador disponible · Compilación local · Requiere el juego original

**Qué necesitas:** Aporta tu propia instalación de Steam o EA App (Origin) con game.exe 1.006 y gamemd.exe 1.001. El instalador detecta los archivos, genera y compila localmente e instala herramientas de compilación cuando hace falta. El código generado del juego original y sus datos permanecen en tu equipo.

**Qué está disponible:** v0.1.3 ofrece instaladores para Windows x64, Linux x64 y macOS ARM64 que generan y compilan localmente a partir de tus archivos originales. Corrige algunos fallos de inicio en Windows y procesos que permanecían abiertos al salir en Linux/macOS. El autor calcula entre 30 y 60 minutos y unos 6 GB para la primera compilación. Los instaladores no están firmados y el sistema operativo puede bloquearlos. Requieren compilación local y no incluyen archivos originales. Las comprobaciones programadas del autor cubren menús, escaramuzas y entrada a la campaña, no una verificación del juego completo por RemakeList. MIT cubre el código propio del proyecto; el código y los recursos de los juegos de EA tienen derechos independientes. RemakeList no lo ha compilado, instalado ni ejecutado.

**Licencia del código:** [MIT for project-authored tooling only; EA game code and assets retain separate rights.](https://github.com/sp00nznet/redalert2-recomp/blob/main/LICENSE)  
**Autor:** sp00nznet  
[Documentación oficial](https://github.com/sp00nznet/redalert2-recomp#readme) · Fuentes revisadas: 2026-10-27

</details>

### [Road Trip Recomp](https://github.com/silentsudin/RoadTripAdventure-recomp)

Road Trip / Choro Q HG2 en ordenador y Android con pantalla panorámica y estados guardados. El primer inicio prepara tu propia imagen de disco estadounidense.

Original o referencia: **Road Trip / Choro Q HG2** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/silentsudin/RoadTripAdventure-recomp/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/road-trip-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=road-trip-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Android

**Estado:** Vista previa · requiere juego original

**Qué necesitas:** Aporta tus archivos obtenidos legalmente que correspondan a: Road Trip USA · SLUS-20398 · CUE/BIN/ISO/CHD. El contenido comercial es independiente y RemakeList no lo proporciona.

**Qué está disponible:** Se enlazan ZIP de Windows, DMG de Mac y APK de Android. El autor indica que funcionan aventura y carrera rápida. Mac necesita Apple Silicon, macOS 13+ y Command Line Tools; Android 12+ y Vulkan.

**Licencia del código:** [GPL-3.0; third-party notices separate](https://github.com/silentsudin/RoadTripAdventure-recomp#readme)  
**Autor:** silentsudin  
[Documentación oficial](https://github.com/silentsudin/RoadTripAdventure-recomp#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Rogue Squadron 64 Recomp](https://github.com/MikeSemicolonD/RogueSquadron64Recomp)

Recompilación estática de Star Wars: Rogue Squadron N64 con pantalla ancha y ratón, mando y joystick de vuelo modernos. Aporta la ROM USA indicada; Mac solo tiene compilación verificada.

Original o referencia: **Star Wars: Rogue Squadron** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/MikeSemicolonD/RogueSquadron64Recomp#readme) · [Explorar RemakeList](https://remakelist.com/es/remakes/rogue-squadron64-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rogue-squadron64-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / Linux / Android

**Estado:** Compilación desde código · requiere juego original

**Qué necesitas:** Tu ROM Star Wars Rogue Squadron N64 USA v1.0 de 16 MB. No distribuye datos ROM.

**Qué está disponible:** Documenta compilación Windows, Linux y Android; el autor afirma que puede completarse. No enumera archivos publicados: compila desde código con tu ROM USA v1.0. Trazado de rayos, interpolación y multijugador experimentales siguen limitados. macOS solo se ha compilado, sin ejecutarse en Mac; Linux x86 solo se probó en PC de 64 bits con Vulkan por software. GPL-3.0 cubre código propio de entorno/mods/herramientas, no derechos del juego. RemakeList no lo ha compilado ni jugado.

**Licencia del código:** [GPL-3.0 for host runtime, patches, hooks, mods, tools and docs; ROM-derived code and game assets are separate](https://github.com/MikeSemicolonD/RogueSquadron64Recomp/blob/main/LICENSE)  
**Autor:** MikeSemicolonD  
[Documentación oficial](https://github.com/MikeSemicolonD/RogueSquadron64Recomp#readme) · Fuentes revisadas: 2026-10-28

</details>

### [Silent Hill — Native PC Port](https://github.com/SlickAmogus/silent-hill-decomp)

Port nativo de Silent Hill basado en la descompilación de PS1, con mejoras opcionales. Windows es la plataforma principal y necesitas los datos de tu disco.

Original o referencia: **Silent Hill** · Proyecto basado en descompilación  
[Descargar y aportar tus archivos del juego](https://github.com/SlickAmogus/silent-hill-decomp/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/silent-hill-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=silent-hill-native-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows

**Estado:** Vista previa · requiere juego original

**Qué necesitas:** Aporta tus archivos obtenidos legalmente que correspondan a: PlayStation · Silent Hill disc image · SLUS-00707 USA. El contenido comercial es independiente y RemakeList no lo proporciona.

**Qué está disponible:** La vía de PC sigue siendo independiente de xbox360-alpha-1, un nuevo paquete de prueba para Xbox 360/homebrew acompañado de una compilación para la Xbox original. Esa alfa solo reporta escenas iniciales, interacciones básicas y carga de algunas partidas; no acredita una partida completa en Xbox. Las compilaciones Realtime de PC/móvil son un canal de actualización independiente y sin probar. Windows sigue siendo la vía principal de PC; Linux/Mac son versiones inestables en desarrollo y el soporte móvil es inicial. Aporta tu propia imagen del disco original de Silent Hill de PS1; la GPL de la capa del port no cubre los datos de Konami ni el código del juego descompilado. RemakeList no ha compilado, instalado ni jugado esta versión.

**Licencia del código:** [GPL-3.0 for port layer only; decompilation and Konami material not relicensed](https://github.com/SlickAmogus/silent-hill-decomp#readme)  
**Autor:** Chris Hardin / KushAstronaut / SlickAmogus  
[Documentación oficial](https://github.com/SlickAmogus/silent-hill-decomp#readme) · Fuentes revisadas: 2026-10-30

</details>

### [SpeedBreaker](https://github.com/speedbreakerproject/speedbreaker)

Ejecuta tu propio Need for Speed: Most Wanted de Xbox 360 en dispositivos modernos, con pantalla panorámica, pantalla dividida y opciones de imagen. La instalación externa en iPhone y iPad sigue siendo experimental, y Windows está en beta.

Original o referencia: **Need for Speed: Most Wanted (2005)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/speedbreakerproject/speedbreaker/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/speedbreaker/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=speedbreaker-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Linux / SteamOS / macOS Apple silicon / iOS·iPadOS experimentales / Windows beta

**Estado:** v0.2.0 publicada · Windows beta · Instalación externa experimental en iOS

**Qué necesitas:** Aporta tu propia ISO, XISO o carpeta extraída de Most Wanted para Xbox 360, de Estados Unidos NTSC-U o de Europa PAL en español, obtenida legalmente. No utiliza Title Update; no admite otras regiones, Games on Demand ni la edición de PC. Reserva unos 7,2 GB. Windows y Linux x64 requieren AVX2 y Vulkan 1.2; Mac necesita Apple silicon y macOS 15+; iOS/iPadOS requieren 17+, un chip de clase A15 o posterior, mando o teclado y tu propia firma para instalación externa.

**Qué está disponible:** La versión principal v0.2.0 ofrece paquetes para SteamOS/Linux x86-64, Steam Frame ARM64 y Mac con Apple silicon, además de una IPA experimental para iOS. Windows utiliza la versión preliminar independiente v0.2.0-windows-beta.2; no hay versión Android. Las dos arquitecturas de SteamOS no son intercambiables. El autor probó la beta de Windows en una selección limitada de equipos con gráficos integrados Intel. La propia IPA adjunta para iOS no se ha instalado en un dispositivo; las pruebas del autor usaron compilaciones firmadas con Xcode, y los permisos de firma o los límites de memoria pueden impedir la ejecución mediante instalación externa. La app de Mac no está notarizada; macOS 15 solo se probó en una máquina virtual. Steam Frame muestra una pantalla plana, no VR; el paquete ARM64 no se ha probado en otros dispositivos Linux. Configura Steam Deck OLED a 60 Hz; el modelo LCD no se ha probado. No se promete una tasa de fotogramas universal. RemakeList no lo ha ejecutado.

**Licencia del código:** [Project-authored code is GPL-3.0-or-later; bundled libraries retain their own licenses, and original game content is excluded.](https://github.com/speedbreakerproject/speedbreaker#readme)  
**Autor:** project(u) / SpeedBreakerProject  
[Documentación oficial](https://github.com/speedbreakerproject/speedbreaker#readme) · Fuentes revisadas: 2026-10-27

</details>

### [Renegade Squadron — PC](https://github.com/gtteancum/starwars-renegadesquadron-pc)

Un port nativo de Star Wars Battlefront: Renegade Squadron de PSP con controles modernos de doble stick y renderizado de mayor resolución. Windows dispone de una opción Vulkan; el paquete de Linux tiene requisitos estrictos de bibliotecas y validación limitada en hardware.

Original o referencia: **Star Wars Battlefront: Renegade Squadron** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/GTTeancum/StarWars-RenegadeSquadron-PC/releases/tag/v0.9.1) · [Explorar RemakeList](https://remakelist.com/es/remakes/renegade-squadron-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=renegade-squadron-pc-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · Vulkan 1.1 / DirectX 12; Linux x64 (generación Ubuntu 26.04, glibc 2.43+)

**Estado:** v0.9.1 · Windows / compilación de Linux con restricciones

**Qué necesitas:** Tu Star Wars Battlefront Renegade Squadron PSP USA ULUS10292, con PSP_GAME extraído en data/.

**Qué está disponible:** v0.9.1 establece Vulkan nativo como opción predeterminada en Windows, mantiene DirectX 12 opcional, corrige texturas de modelos y extrae automáticamente tu ISO USA ULUS10292. Un archivo adicional de Linux x64 está dirigido solo a sistemas de la generación Ubuntu 26.04, con glibc 2.43+, FFmpeg 8 y Vulkan 1.1. Se reportan pruebas básicas en Hoth para Windows y con Vulkan por software en WSL2 para Linux; el rendimiento con GPU real de Linux, los controles físicos y la cobertura del juego completo siguen sin verificar. La iluminación mejorada, las sombras y el bloom siguen siendo exclusivos de DirectX 12. El antiguo paquete HD opcional no se ha vuelto a validar con Vulkan. Haz una copia de los ajustes personalizados y conserva las partidas al actualizar.

**Licencia del código:** [MIT for framework/port, third-party notices separate](https://github.com/GTTeancum/StarWars-RenegadeSquadron-PC/blob/main/work/project/source/LICENSE)  
**Autor:** gtteancum  
[Documentación oficial](https://github.com/gtteancum/starwars-renegadesquadron-pc#readme) · Fuentes revisadas: 2026-10-29

</details>

### [Super Mario Bros. Wonder Recomp](https://github.com/BelmanteGu/SuperMarioWonderRecomp)

Recompila Super Mario Bros. Wonder para ordenador y Android. Requiere compilar el código y aportar tu juego, claves y firmware.

Original o referencia: **Super Mario Bros. Wonder** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/BelmanteGu/SuperMarioWonderRecomp#readme) · [Explorar RemakeList](https://remakelist.com/es/remakes/super-mario-wonder-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=super-mario-wonder-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux / Android

**Estado:** Compilación propia · requiere juego original

**Qué necesitas:** Aporta tus archivos obtenidos legalmente que correspondan a: Switch · Wonder 1.0.0 · 010015100B514000 · own keys + firmware. El contenido comercial es independiente y RemakeList no lo proporciona.

**Qué está disponible:** Requiere compilar con tu juego, claves y firmware. El autor documenta Mac, Windows, Linux y Galaxy S23; persisten problemas de GPU y un fallo de Windows tras elegir personaje.

**Licencia del código:** [MIT authored code; Nintendo game and derivatives excluded](https://github.com/BelmanteGu/SuperMarioWonderRecomp#readme)  
**Autor:** Projeto Belmante / BelmanteGu  
[Documentación oficial](https://github.com/BelmanteGu/SuperMarioWonderRecomp#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Super Street Fighter II Turbo HD Remix — PC Port](https://github.com/saulob/ssf2t-hd-remix-recompiled)

Port nativo para Windows de Super Street Fighter II Turbo HD Remix de Xbox Live Arcade. Necesita tu paquete de la versión exacta; no hay juego en línea.

Original o referencia: **Super Street Fighter II Turbo HD Remix** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/saulob/ssf2t-hd-remix-recompiled/releases/tag/v0.2.2) · [Explorar RemakeList](https://remakelist.com/es/remakes/ssf2t-hd-remix-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ssf2t-hd-remix-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows

**Estado:** v0.2.2 · Windows / Linux experimental

**Qué necesitas:** Aporta tu propio paquete del juego XBLA y Title Update #1 para Title ID 584108A4, Media ID 37B7D7D3. El lanzador requiere default.xex 0.0.1.3 más default.xexp para obtener la versión 0.0.2.3 del juego. No se incluye ninguno de los dos paquetes; quitar la actualización hace que esta versión no se pueda jugar.

**Qué está disponible:** v0.2.2 ofrece descargas para Windows x64 y un AppImage experimental para Linux. Ahora requiere el juego XBLA original más Title Update #1, con instaladores separados y validación de versión. La actualización cambia el ejecutable requerido de 0.0.1.3 a 0.0.2.3. Solo sin conexión; los paquetes de Linux/Steam Deck tienen comprobaciones automatizadas, pero ninguna prueba en hardware real. El juego se mantiene en 60 actualizaciones por segundo. Solo se admite el juego 0.0.1.3 más Title Update #1 (que da como resultado 0.0.2.3). Windows no está firmado. Archivos originales / configuración: Aporta tu propio paquete del juego XBLA y Title Update #1 para Title ID 584108A4, Media ID 37B7D7D3. El lanzador requiere default.xex 0.0.1.3 más default.xexp para obtener la versión 0.0.2.3 del juego. No se incluye ninguno de los dos paquetes; quitar la actualización hace que esta versión no se pueda jugar.

**Licencia del código:** [Project code is GPL-2.0-only; v0.2.2 now includes the TRG Launcher MIT notice in THIRD-PARTY-LICENSES.txt. Dependencies keep their own terms. None of these grants cover the original game or title-update content.](https://github.com/saulob/ssf2t-hd-remix-recompiled#readme)  
**Autor:** saulob  
[Documentación oficial](https://github.com/saulob/ssf2t-hd-remix-recompiled#readme) · Fuentes revisadas: 2026-10-29

</details>

### [The Last Guardian — PC](https://github.com/hayatog/tlg_pc)

Port de compatibilidad para PC de The Last Guardian. El autor probó Linux; Windows aún no tiene pruebas dentro del juego. Requiere tus archivos de PS4.

Original o referencia: **The Last Guardian** · Capa de compatibilidad entre plataformas  
[Descargar y aportar tus archivos del juego](https://github.com/HayatoG/tlg_pc/releases/tag/v2026.10.27-4825a99) · [Explorar RemakeList](https://remakelist.com/es/remakes/last-guardian-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=last-guardian-pc-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Linux x86-64 (glibc 2.39+) / Windows 10–11 x64 (juego sin verificar)

**Estado:** v2026.10.27-4825a99 · vista previa · archivos originales de PS4

**Qué necesitas:** Aporta tus archivos obtenidos legalmente que correspondan a: PS4 · CUSA03627 / CUSA03745 · update 01.03 · own libSceNgs2.sprx. El contenido comercial es independiente y RemakeList no lo proporciona.

**Qué está disponible:** v2026.10.27-4825a99 ofrece archivos para Linux y Windows sin datos del juego. El autor informa de juego en Linux, con 30 FPS por defecto y opciones experimentales de 60 FPS o sin límite. Windows tiene una compilación automática, pero el autor no ha verificado el juego. Las tasas superiores siguen siendo experimentales y no se ha establecido la cobertura del juego completo. macOS está previsto, sin descarga. RemakeList no lo ha compilado, instalado ni jugado.

**Licencia del código:** [GPL-2.0 per port/LICENSE and README; game/firmware excluded](https://github.com/HayatoG/tlg_pc/blob/main/port/LICENSE)  
**Autor:** HayatoG  
[Documentación oficial](https://github.com/hayatog/tlg_pc#readme) · Fuentes revisadas: 2026-10-28

</details>

### [Tiberian Sun Recomp](https://github.com/sp00nznet/tiberiansun-recomp)

Genera una versión nativa de tu instalación Tiberian Sun/Firestorm con pantalla ancha y ajustes gráficos. Versión temprana con pruebas de escaramuza e inicio de campaña; completar el juego sigue sin verificar.

Original o referencia: **Tiberian Sun / Firestorm** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/sp00nznet/tiberiansun-recomp/releases/tag/v0.1.0-alpha.2) · [Explorar RemakeList](https://remakelist.com/es/remakes/tiberian-sun-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=tiberian-sun-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / Linux; macOS mediante CrossOver (sin probar)

**Estado:** Instalador alfa · compila desde tu juego

**Qué necesitas:** Tu instalación Steam de Tiberian Sun + Firestorm con Game.exe, Language.dll y archivos MIX.

**Qué está disponible:** v0.1.0-alpha.2 ofrece instaladores que descargan herramientas y compilan localmente; Linux añade menú F10 y resoluciones. Usan tus archivos Steam de Tiberian Sun + Firestorm, sin incluir el juego. La primera preparación requiere unos 30–60 minutos y 6 GB y puede instalar herramientas con permiso. Los instaladores no están firmados. Hay pruebas documentadas Windows/Linux; macOS usa CrossOver y el autor no lo probó. La campaña completa sigue sin verificar. RemakeList no lo ha compilado, instalado ni jugado.

**Licencia del código:** [MIT authored tooling; EA game and generated C excluded](https://github.com/sp00nznet/tiberiansun-recomp/blob/main/LICENSE)  
**Autor:** sp00nznet  
[Documentación oficial](https://github.com/sp00nznet/tiberiansun-recomp#readme) · Fuentes revisadas: 2026-10-28

</details>

### [Wind Waker HD Android — Plus](https://github.com/Nycolazs/WindWakerHD-Android-Plus)

Fork Android de Wind Waker HD con traducción portuguesa y ajustes táctiles. Requiere tu propio juego de Wii U.

Original o referencia: **The Legend of Zelda: The Wind Waker HD** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/Nycolazs/WindWakerHD-Android-Plus/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/wind-waker-hd-android-plus/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wind-waker-hd-android-plus-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Android

**Estado:** Vista previa · requiere juego original

**Qué necesitas:** Aporta tus archivos obtenidos legalmente que correspondan a: Wii U · Wind Waker HD · WUD/WUX + own keys / own WUA. El contenido comercial es independiente y RemakeList no lo proporciona.

**Qué está disponible:** Se enlaza una APK; necesita Android 11+, ARM64 y Vulkan. Las capturas publicadas proceden de un Galaxy S20 FE 5G con Snapdragon 865.

**Licencia del código:** [MPL-2.0 code; translation/third-party notices separate](https://github.com/Nycolazs/WindWakerHD-Android-Plus#readme)  
**Autor:** Nycolazs  
[Documentación oficial](https://github.com/Nycolazs/WindWakerHD-Android-Plus#readme) · Fuentes revisadas: 2026-10-19

</details>

### [Wind Waker HD — Mods Fork](https://github.com/asadsi/wwhd-recomp-mods)

Fork no oficial de Wind Waker HD con sucesos marítimos opcionales y un barco pirata navegable. Requiere tu juego; el cooperativo es experimental.

Original o referencia: **The Legend of Zelda: The Wind Waker HD** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/asadsi/wwhd-recomp-mods/releases) · [Explorar RemakeList](https://remakelist.com/es/remakes/wind-waker-hd-mods/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wind-waker-hd-mods-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / macOS / Linux

**Estado:** Vista previa · requiere juego original

**Qué necesitas:** Aporta tus archivos obtenidos legalmente que correspondan a: Wii U USA/EUR · Wind Waker HD · own disc dump + keys / WUA. El contenido comercial es independiente y RemakeList no lo proporciona.

**Qué está disponible:** Se documentan paquetes de escritorio; Android se compila por cuenta propia. Las modificaciones son opcionales, el cooperativo es experimental y se necesitan tus datos Wii U.

**Licencia del código:** [MPL-2.0 code; Nintendo assets excluded](https://github.com/asadsi/wwhd-recomp-mods#readme)  
**Autor:** AsadSi / asadsi  
[Documentación oficial](https://github.com/asadsi/wwhd-recomp-mods#readme) · Fuentes revisadas: 2026-10-19

</details>

### [nxnative](https://github.com/seedds/nxnative)

Crea en un Mac apps para iPhone, iPad o Mac con Apple silicon a partir de tus propios archivos de juegos Switch compatibles. La compatibilidad depende del perfil del juego y de la compilación.

Original o referencia: **Juegos de Nintendo Switch** · Capa de compatibilidad entre plataformas  
[Compilar y aportar tus archivos del juego](https://github.com/seedds/nxnative#pack-an-ipa) · [Explorar RemakeList](https://remakelist.com/es/remakes/nxnative/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nxnative-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** iPhone / iPad · iOS / iPadOS 26+; Mac con Apple silicon · compilación local

**Estado:** Requiere compilación local · compatibilidad según el autor

**Qué necesitas:** Aporta los NSP de tu propio juego, las actualizaciones o DLC necesarios y tu propio prod.keys. Compila localmente en un Mac con Xcode y Homebrew. La vía para iPhone/iPad genera un IPA sin firmar, que debe firmarse e instalarse por carga lateral en pasos separados; los Mac con Apple silicon usan la vía de la app para Mac. Los paquetes generados contienen código y recursos derivados del juego para uso personal, no para redistribuir. Aquí no se ofrecen juegos comerciales, claves ni paquetes de juego listos para instalar; comprueba tus derechos sobre los archivos que aportas.

**Qué está disponible:** Consulta la tabla actual de estado de los juegos del autor y el perfil de cada juego antes de compilar. Según el autor, Tears of the Kingdom ya es jugable en iPhone; su opción de 60 fps requiere la actualización 1.4.3 y no garantiza esa tasa en todos los dispositivos. La vía para crear una app de Mac usa --platform mac-app y permite abrirla desde Finder en un Mac con Apple silicon. Un informe de iPhone no confirma la compatibilidad con Mac.

**Licencia del código:** [MIT project code · game rights and third-party licenses separate](https://github.com/seedds/nxnative/blob/main/LICENSE)  
**Autor:** seedds and contributors  
[Documentación oficial](https://github.com/seedds/nxnative/blob/main/README.md) · Fuentes revisadas: 2026-10-25

</details>

### [Zelda-Mobile · Tears of the Kingdom](https://github.com/OJZen/totk-mobile)

Port nativo experimental de Tears of the Kingdom v1.4.3 para Apple silicon. Requiere tu juego y compilar el código; no se ha verificado jugar en iPhone.

Original o referencia: **The Legend of Zelda: Tears of the Kingdom** · Capa de compatibilidad entre plataformas  
[Compilar y aportar tus archivos del juego](https://github.com/OJZen/totk-mobile/blob/main/docs/getting-started.md) · [Explorar RemakeList](https://remakelist.com/es/remakes/totk-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=totk-mobile-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Mac Apple silicon; iPad M1+; iPhone 15 Pro · experimental

**Estado:** Experimental · compilación desde código · sin lanzamiento formal

**Qué necesitas:** Necesitas tu juego de Switch, actualización v1.4.3 en .nsz y prod.keys correspondientes, extraídos de tu propia consola. Solo se admite esa versión. Prepara un Mac Apple silicon con Xcode completo, herramientas de línea de comandos, Homebrew y unos 60 GB libres. iPhone/iPad requiere además iOS/iPadOS 26+, firma de desarrollo, modo de desarrollador, USB y unos 25 GB libres en el dispositivo. El repositorio y esta ficha no proporcionan juegos, claves, apps firmadas ni paquetes de sombreadores derivados. La licencia del código no concede derechos sobre el contenido de Nintendo.

**Qué está disponible:** Compilación experimental desde código, sin Releases formales. El autor informa de cargar partidas y jugar escenas en Mac con Apple silicon; no ha validado completar el juego. Los iPad M1 o posteriores están muy por debajo de 60 FPS a resolución original; los mandos no están plenamente verificados. En iPhone 15 Pro solo se verificaron instalación con firma de desarrollo, transferencia de recursos y arranque con caché hasta la pantalla de título. No se han medido juego, FPS, memoria ni temperatura. Otros iPhone, incluido el 13 Pro, no están probados. Las escenas nuevas pueden dar tirones al compilar sombreadores.

**Licencia del código:** [Original code: Apache-2.0 · reused components retain their own licenses](https://github.com/OJZen/totk-mobile/blob/main/LICENSE)  
**Autor:** JZen (@JZennm)  
[Documentación oficial](https://github.com/OJZen/totk-mobile/blob/510d95b8da159c0a7da467ad51b10a5a7c7ac133/README.md) · Fuentes revisadas: 2026-10-20

</details>

### [Melee Unlocked](https://github.com/Hero88go/melee-unlocked)

Una adaptación nativa para PC de Super Smash Bros. Melee con juego en línea mediante Slippi y visualización a alta frecuencia de actualización. Requiere tu propia ISO NTSC 1.02.

Original o referencia: **Super Smash Bros. Melee (NTSC 1.02)** · Capa de compatibilidad entre plataformas  
[Descargar y aportar tus archivos del juego](https://github.com/Hero88go/melee-unlocked/releases/tag/v0.9.72) · [Explorar RemakeList](https://remakelist.com/es/remakes/melee-unlocked/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=melee-unlocked-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 / Linux x86-64 (AVX2, OpenGL 4.5)

**Estado:** Beta v0.9.72 · Linux experimental · requiere tu propia ISO

**Qué necesitas:** Debes aportar una ISO de Super Smash Bros. Melee NTSC 1.02 obtenida legalmente, limpia y sin comprimir. No se incluyen datos del juego original; la licencia del código no cubre los recursos del juego.

**Qué está disponible:** v0.9.72 ofrece paquetes para Windows x64 y Linux x64. Corrige los reflejos de Fountain of Dreams en pantalla panorámica real y evita que las proyecciones de cámara no compatibles de discos modificados cierren el juego. Usa tu propia ISO NTSC 1.02; cierra el juego y el lanzador antes de actualizar. Sigue siendo software beta. Linux es experimental y requiere AVX2/OpenGL 4.5; Static Recomp es exclusivo de Windows y la compatibilidad de mods depende del motor. RemakeList no ha compilado, instalado ni jugado esta versión.

**Licencia del código:** [GPL-3.0-or-later · port code; third-party components keep their own terms.](https://github.com/Hero88go/melee-unlocked/blob/main/LICENSE)  
**Autor:** Hero88go / Melee Unlocked contributors  
[Documentación oficial](https://github.com/Hero88go/melee-unlocked#readme) · Fuentes revisadas: 2026-10-30

</details>

### [Brawl Recompiled](https://github.com/josiahg2502-glitch/BrawlRecompiled)

Una adaptación nativa para PC de Super Smash Bros. Brawl para Windows y Linux, creada mediante recompilación estática. Requiere tu propia imagen de disco USA RSBE01 revision 1.

Original o referencia: **Super Smash Bros. Brawl (Wii, USA RSBE01 revision 1)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/josiahg2502-glitch/BrawlRecompiled/releases/tag/v0.5.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/brawl-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=brawl-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / Linux de 64 bits (glibc 2.35+, Vulkan)

**Estado:** v0.5.0 · versión inicial

**Qué necesitas:** Requiere tu propia imagen de disco de Brawl obtenida legalmente: USA, RSBE01, revision 1 (ISO, CISO o WBFS). La extracción necesita unos 7 GB. Convierte primero las imágenes RVZ, WIA, GCZ o NKit a ISO estándar. RemakeList no proporciona imágenes de disco.

**Qué está disponible:** v0.5.0 ofrece paquetes para Windows y Linux. Añade interpolación visual opcional a 240 fps, con tasas adaptativas inferiores, y transfiere la partida guardada completa para el juego en línea para corregir un fallo que podía sobrescribir la del anfitrión. La mayor tasa de visualización es interpolación, no 240 actualizaciones por segundo de la lógica del juego. En desarrollo: solo se reportan pruebas del inicio de Classic y Subspace. La interpolación a 120/180/240 fps sigue siendo experimental. Algunas redes bloquean las conexiones directas; la vía probada es el juego en línea sin mods, y los participantes con mods necesitan el mismo contenido SD. Los mods de menú interpretados pueden funcionar a menos de 60 fps.

**Licencia del código:** [GPLv3 · project code only; original game artwork and third-party components have separate rights and terms.](https://github.com/josiahg2502-glitch/BrawlRecompiled/blob/v0.4.0/wiicompiled/LICENSE)  
**Autor:** JosiahG  
[Documentación oficial](https://github.com/josiahg2502-glitch/BrawlRecompiled/blob/master/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [Splinter Cell: Double Agent — Xbox Recomp](https://github.com/TGP482/SCDA-XBERecomp)

Port nativo para Windows de Splinter Cell: Double Agent de Xbox original. Añade teclado y ratón, resolución y FPS ajustables y juego cooperativo; requiere tus propios archivos de Xbox.

Original o referencia: **Splinter Cell: Double Agent (original Xbox, 2006)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/TGP482/SCDA-XBERecomp/releases/tag/V3) · [Explorar RemakeList](https://remakelist.com/es/remakes/scda-xbe-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=scda-xbe-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10+ x64 · Direct3D 12

**Estado:** Versión V3 · requiere archivos originales de Xbox

**Qué necesitas:** Tu propia copia obtenida legalmente de Double Agent para Xbox original. La versión descargable acepta ISO o archivos extraídos: default.xbe y sc4_adv.xbe junto a las carpetas Default, Media y adv. Compilar desde el código requiere archivos extraídos. Los archivos de PC o Xbox 360 no sirven como sustitutos. No se incluyen recursos del juego.

**Qué está disponible:** V3 ofrece un paquete para Windows que compila tus archivos de Double Agent de la Xbox original en el primer inicio. Añade extracción y sustitución de texturas, sensibilidades de apuntado separadas, apuntado giroscópico y modos para daltonismo, y corrige el comportamiento del agua y de las físicas de cuerpos a tasas altas de fotogramas. RemakeList no ha compilado, instalado ni jugado esta versión.

**Licencia del código:** [MIT for the project code; original game content and third-party components retain their own rights.](https://github.com/TGP482/SCDA-XBERecomp/blob/main/LICENSE)  
**Autor:** TGP482  
[Documentación oficial](https://github.com/TGP482/SCDA-XBERecomp#readme) · Fuentes revisadas: 2026-10-30

</details>

### [P.T. for PC](https://github.com/LoreanXavier/pt-pc)

Una adaptación para ordenador del teaser P.T. de PS4, con controles de teclado, mando y modo foto. Requiere tus propios datos del juego de PS4.

Original o referencia: **P.T. (PS4, 2014)** · Capa de compatibilidad entre plataformas  
[Descargar y aportar tus archivos del juego](https://github.com/LoreanXavier/pt-pc/releases/tag/v1.0.8) · [Explorar RemakeList](https://remakelist.com/es/remakes/pt-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pt-pc-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 / Linux x86-64 / macOS 14+

**Estado:** v1.0.8 · Adaptación temprana · Requiere archivos originales

**Qué necesitas:** Aporta tus propios datos de P.T. para PS4, obtenidos legalmente. El autor prueba la edición estadounidense CUSA01127; los PKG cifrados de la tienda no son utilizables. La adaptación y el instalador no incluyen los archivos del juego original.

**Qué está disponible:** v1.0.8 ofrece instaladores y paquetes portátiles para Windows y Linux, además de versiones para Mac con Apple silicon e Intel. Linux requiere glibc 2.38+; los gráficos requieren Vulkan 1.3, con MoltenVK incluido en macOS. RemakeList no ha ejecutado estas versiones. Las versiones para Mac Intel no se han probado en un Mac Intel físico. La VR solo se ha comprobado con un entorno simulado. Algunos efectos y técnicas de reescalado no están disponibles en macOS; la compatibilidad del hardware varía.

**Licencia del código:** [MIT for project code; original game content and third-party components retain their own rights and terms.](https://github.com/LoreanXavier/pt-pc/blob/main/LICENSE)  
**Autor:** LoreanXavier  
[Documentación oficial](https://github.com/LoreanXavier/pt-pc/blob/main/README.md) · Fuentes revisadas: 2026-10-26

</details>

### [GT4Recomp](https://github.com/moesuito/gt4-staticrecomp)

Una adaptación de Gran Turismo 4 para Windows con ajustes de resolución, mandos y paquetes de texturas. Requiere tu propia imagen de disco de PS2 compatible.

Original o referencia: **Gran Turismo 4 (PS2)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/moesuito/gt4-staticrecomp/releases/tag/v1.3.0-rc6) · [Explorar RemakeList](https://remakelist.com/es/remakes/gt4-staticrecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gt4-staticrecomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · Vulkan / Direct3D 12 / Direct3D 11

**Estado:** v1.3.0-rc6 · Versión preliminar · Requiere archivos originales

**Qué necesitas:** Requiere una ISO sin comprimir de Gran Turismo 4 USA v2.00 (SCUS-97328) obtenida legalmente. Spec II necesita además tu propia imagen Spec II 1.10. El proyecto no proporciona archivos del juego ni del mod.

**Qué está disponible:** v1.3.0-rc6 es una versión pública de pruebas con instalador de Windows y ZIP portátil, no la versión final 1.3.0. Vulkan es la opción predeterminada probada; Direct3D 12 y 11 son alternativas más recientes. Linux y Android siguen previstos. Versión candidata: algunas demostraciones de licencias y fondos de menús no se reproducen. Los volantes no son compatibles y las sesiones largas no se han probado por completo. El modo Rendimiento elimina los halos de luz y el resplandor solar. Persisten problemas del HUD ultrapanorámico de Spec II; el rendimiento depende del hardware.

**Licencia del código:** [MIT for original project code; the separate PCSX2 GS process is GPL-3.0-or-later. Original game and mod content have separate rights.](https://github.com/moesuito/gt4-staticrecomp/blob/main/LICENSE)  
**Autor:** moesuito  
[Documentación oficial](https://github.com/moesuito/gt4-staticrecomp/blob/main/README.md) · Fuentes revisadas: 2026-10-26

</details>

### [God of War PSP Recomp](https://github.com/DrummingBird1/gow-psp-recomp)

Un lanzador para Windows que recompila localmente los dos God of War de PSP a partir de tus propias imágenes de discos estadounidenses, con ajustes modernos de pantalla y controles.

Original o referencia: **God of War: Chains of Olympus / Ghost of Sparta (PSP)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/DrummingBird1/gow-psp-recomp/releases/tag/v1.3.1) · [Explorar RemakeList](https://remakelist.com/es/remakes/gow-psp-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gow-psp-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows · Linux / Steam Deck previstos

**Estado:** v1.3.1 · Adaptación temprana · Requiere archivos originales

**Qué necesitas:** Aporta tus propias imágenes de discos estadounidenses de PSP obtenidas legalmente, en CHD o ISO: Chains of Olympus UCUS98653 y/o Ghost of Sparta UCUS98737. El proyecto no incluye datos de los juegos originales.

**Qué está disponible:** v1.3.1 proporciona un ZIP del lanzador para Windows. La primera operación Build pide permiso para descargar herramientas portátiles y después compila localmente el juego seleccionado. Windows es la plataforma publicada actualmente; no se ha verificado una partida completa de ninguno de los dos juegos. Versión de prueba: puede haber fallos en niveles avanzados, jefes y finales. Linux y Steam Deck están previstos. El lanzador no está firmado y las herramientas de compilación requieren una descarga inicial. Los recorridos automáticos de niveles no demuestran que se puedan completar los juegos.

**Licencia del código:** [GPL-3.0-or-later for project code; original game content and third-party components retain their own rights and terms.](https://github.com/DrummingBird1/gow-psp-recomp/blob/main/LICENSE)  
**Autor:** DrummingBird1  
[Documentación oficial](https://github.com/DrummingBird1/gow-psp-recomp/blob/main/README.md) · Fuentes revisadas: 2026-10-26

</details>

### [PrimeRecomp](https://github.com/gminustwo/primerecomp)

Una adaptación temprana para ordenador de Metroid Prime Remastered con control mediante ratón. La configuración requiere tus propios archivos extraídos de Switch v1.0.0.

Original o referencia: **Metroid Prime Remastered (Switch)** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/gminustwo/primerecomp/releases/tag/v0.0.4) · [Explorar RemakeList](https://remakelist.com/es/remakes/primerecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=primerecomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / Linux x86-64 / macOS 15+ Apple Silicon

**Estado:** v0.0.4 · Beta inicial · requiere archivos originales

**Qué necesitas:** Aporta tus propios archivos de Metroid Prime Remastered v1.0.0 para Switch obtenidos legalmente, sin actualizaciones y extraídos en las carpetas exefs y romfs. No se incluyen datos del juego original.

**Qué está disponible:** v0.0.4 ofrece descargas de ZIP para Windows, AppImage para Linux y DMG para Mac con Apple silicon. La decodificación ASTC en GPU y menos cargas de iluminación reducen las pausas al atravesar puertas en la escena medida por el autor. La instalación compila localmente a partir de tus propios archivos extraídos de Metroid Prime Remastered 1.0.0. Windows/Linux requieren AVX2 y Vulkan 1.3; Linux necesita glibc 2.35+. Persisten fallos visuales, y las zonas posteriores a Magmoor Caverns no están probadas y pueden cerrarse o bloquearse. Las mediciones de Steam Deck cubren escenas concretas, no el juego completo. Mac no está notarizado y persisten los tirones iniciales por shaders. RemakeList no lo ha compilado, instalado ni jugado.

**Licencia del código:** [MIT for project code; original game content and third-party components retain their own rights and terms.](https://github.com/gminustwo/primerecomp/blob/main/LICENSE)  
**Autor:** gminustwo  
[Documentación oficial](https://github.com/gminustwo/primerecomp/blob/main/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [Wario Land: Shake It! Native PC](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC)

Una adaptación para Windows del Wario Land de Wii, con entrada de teclado/mando y gráficos configurables. Requiere tu propia imagen estadounidense del juego compatible.

Original o referencia: **Wario Land: Shake It! (Wii)** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC/releases/tag/v0.2.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/wario-land-shake-it-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wario-land-shake-it-pc-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · Direct3D 12 / Vulkan

**Estado:** v0.2.0 · versión de pruebas · requiere compilación local

**Qué necesitas:** Aporta una imagen estadounidense sin modificar de Wario Land: Shake It! para Wii (RWLE01), obtenida legítimamente, o sus carpetas sys/files extraídas. El lanzador valida el main.dol original. Reserva unos 3 GB para compilar y 4,4 GB adicionales para extraer la imagen. No se proporcionan datos, ejecutable ni código traducido del juego original.

**Qué está disponible:** v0.2.0 ofrece un lanzador Windows y un ZIP con herramientas de compilación, no un juego ya compilado. Tras importar tu imagen Wii estadounidense compatible, compila localmente en unos 15–45 minutos; se recomiendan 16 GB de RAM. Requiere Windows 10/11 x64 y D3D12 o Vulkan. Sigue siendo una versión de pruebas aunque GitHub no active la marca de preliminar. Las pruebas del juego completo, jefes, vídeos y movimiento DualSense son incompletas; puede haber fallos gráficos y cierres. La pantalla ancha y la interpolación son experimentales. RemakeList no lo ha instalado ni jugado.

**Licencia del código:** [GPL-3.0 for project code; original game content and third-party components retain their own rights and terms.](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC/blob/main/LICENSE)  
**Autor:** santiagovalencia109  
[Documentación oficial](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [PGR4 Native](https://github.com/shaunsingh/pgr4-native)

Una recompilación de Project Gotham Racing 4 con renderizador nativo Direct3D 12. Funciona en Windows o mediante Proton con tu propio juego y Title Update #2.

Original o referencia: **Project Gotham Racing 4 (Xbox 360)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/shaunsingh/pgr4-native/releases/tag/v0.3.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/pgr4-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pgr4-native-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / Linux y Steam Deck mediante Proton

**Estado:** v0.3.0 · Windows; Proton en Linux

**Qué necesitas:** Aporta los datos extraídos de tu propio disco de PGR4 obtenido legalmente, junto con el paquete o los archivos de Title Update #2. Según el autor, el contenido de los discos PAL y NTSC coincide. No se incluyen datos del juego original.

**Qué está disponible:** v0.3.0 ofrece un ZIP para Windows x64 con renderizado 16:10, ajustes dentro del juego, resolución dinámica y generación de fotogramas FidelityFX opcional. Linux y SteamOS usan Proton. Aporta tu propio disco de PGR4 extraído y Title Update 2, además de tus propios DLC opcionales. La generación de fotogramas puede mostrar 90 a partir de 45 renderizados; las mediciones de rendimiento del autor no son una garantía para cada Steam Deck o GPU. RemakeList no lo ha jugado.

**Licencia del código:** [MIT for project code; original game content and third-party components retain their own rights and terms.](https://github.com/shaunsingh/pgr4-native/blob/main/LICENSE)  
**Autor:** shaunsingh  
[Documentación oficial](https://github.com/shaunsingh/pgr4-native/blob/main/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [Sky Recomp](https://github.com/Apolinario-coder/SkyRecomp)

Una adaptación experimental para ordenador de Skyward Sword HD, con controles de teclado/ratón y ajustes gráficos. Requiere tus propios archivos de Switch v1.0.0.

Original o referencia: **The Legend of Zelda: Skyward Sword HD (Switch)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/Apolinario-coder/SkyRecomp/releases/tag/v2.0.2) · [Explorar RemakeList](https://remakelist.com/es/remakes/skyrecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=skyrecomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / Linux / macOS

**Estado:** v2.0.2 · Adaptación temprana · Requiere archivos originales

**Qué necesitas:** Aporta tus propios archivos de Skyward Sword HD v1.0.0 para Switch obtenidos legalmente, sin actualizaciones. No se proporcionan los archivos del juego original. Los paquetes visuales opcionales conservan las condiciones independientes de sus autores.

**Qué está disponible:** v2.0.2 ofrece paquetes para Windows, Linux y macOS. Windows/Linux necesitan hardware compatible con Vulkan 1.3; las versiones x86 requieren AVX2. macOS utiliza el backend Metal del proyecto. No se ha establecido la estabilidad durante todo el juego. Experimental: siguen investigándose cierres, bloqueos en menús y diferencias de renderizado. Los modos de alta frecuencia de imágenes son experimentales y dependen del hardware. RemakeList no ha instalado ni jugado estos paquetes.

**Licencia del código:** [MIT for original code; LAS Recomp and third-party components retain their notices. Texture packs and presets have separate authors and terms.](https://github.com/Apolinario-coder/SkyRecomp/blob/main/LICENSE)  
**Autor:** Apolinario-coder  
[Documentación oficial](https://github.com/Apolinario-coder/SkyRecomp/blob/main/README.md) · Fuentes revisadas: 2026-10-26

</details>

### [Madden NFL 08 Recompiled](https://github.com/anishchandra24/MaddenNFL08-Recompiled)

Una adaptación temprana para Windows de Madden NFL 08 de Xbox 360. La instalación descarga las herramientas y compila localmente a partir de tus propios archivos extraídos del juego.

Original o referencia: **Madden NFL 08 (Xbox 360)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/anishchandra24/MaddenNFL08-Recompiled/releases/tag/v0.1.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/madden-nfl08-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=madden-nfl08-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · Direct3D 12 con ROV

**Estado:** v0.1.0 · Versión preliminar · Requiere archivos originales

**Qué necesitas:** Aporta tu propia copia de Madden NFL 08 para Xbox 360 (Title ID 4541081D) obtenida legalmente, extraída con default.xex junto a los demás archivos del juego. Solo es compatible la revisión del ejecutable indicada en la README.

**Qué está disponible:** v0.1.0 es un ejecutable de instalación preliminar, no un juego listo para jugar. La instalación requiere archivos compatibles del juego, acceso a Internet, Git y Visual Studio 2022 Community con las herramientas C++, y unos 10 GB para compilar. Requiere una CPU rápida y Rasterizer-Ordered Views (ROV) de Direct3D 12. En el PC de gama baja del autor los partidos no eran jugables; solo se probaron dos PC. Persisten tirones de shaders, algunos problemas visuales y de sonido y la falta de servicios en línea.

**Licencia del código:** [GPL-3.0 for project code; original game content and third-party components retain their own rights and terms.](https://github.com/anishchandra24/MaddenNFL08-Recompiled/blob/main/LICENSE)  
**Autor:** anishchandra24  
[Documentación oficial](https://github.com/anishchandra24/MaddenNFL08-Recompiled/blob/main/README.md) · Fuentes revisadas: 2026-10-26

</details>

### [CPS-2 Recomp](https://github.com/tmcleroy/cps2recomp)

Una colección de adaptaciones no oficiales de juegos arcade CPS-2 y CPS-1, con un único lanzador, herramientas de entrenamiento para juegos de lucha y beat ’em ups para tres jugadores. Requiere los conjuntos exactos de ROM compatibles de tus propias placas arcade.

Original o referencia: **Juegos arcade de Capcom CPS-2 / CPS-1** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/tmcleroy/cps2recomp/releases/tag/v1.0.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/cps2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=cps2-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · macOS 13+ (Apple Silicon / Intel) · Linux x86_64 / ARM64 / SteamOS

**Estado:** v1.0.0 · versión completa · 17 juegos

**Qué necesitas:** Aporta la revisión exacta de ROM compatible de una placa arcade que poseas y, para los juegos CPS-2, su archivo de clave. El lanzador comprueba las sumas de verificación y rechaza otras regiones o revisiones; algunos conjuntos también necesitan su conjunto principal. No se proporcionan archivos de juegos ni claves.

**Qué está disponible:** v1.0.0 es la primera versión completa no beta del autor, con paquetes para Windows x64, macOS universal y Linux x64/ARM64. Añade juego en línea con rollback y tres juegos, elevando la selección compatible a 17. Cada jugador debe aportar los conjuntos exactos de ROM y las claves compatibles; no se incluye ningún juego. El estado de la versión declarado por el autor no acredita pruebas completas en todos los equipos y juegos. Windows no está firmado y macOS no está notarizado. Se requieren revisiones exactas de las ROM; RemakeList no lo ha instalado ni jugado.

**Licencia del código:** [Project code is GPL-3.0-only; third-party components retain their own notices. This license does not grant rights to Capcom or other rights holders’ game code, ROMs, keys, music or artwork.](https://github.com/tmcleroy/cps2recomp/blob/main/LICENSE)  
**Autor:** tmcleroy  
[Documentación oficial](https://github.com/tmcleroy/cps2recomp/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [Free Riders Recompiled](https://github.com/YuutaTsubasa/Free-Riders-Recompiled)

Una adaptación no oficial de Sonic Free Riders de Xbox 360 que permite jugar con mando o teclado sin Kinect. Importa los datos desde tu propia imagen de disco estadounidense o europea y sigue en desarrollo.

Original o referencia: **Sonic Free Riders (Xbox 360)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/YuutaTsubasa/Free-Riders-Recompiled/releases/tag/v0.10.38) · [Explorar RemakeList](https://remakelist.com/es/remakes/free-riders-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=free-riders-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows / Linux x64 · Android arm64 · macOS Apple Silicon / iOS experimentales

**Estado:** v0.10.38 · En desarrollo · requiere disco original

**Qué necesitas:** Aporta tu propia imagen de disco (.iso) de Sonic Free Riders para Xbox 360, de Estados Unidos o Europa, obtenida legalmente. El lanzador importa de ella modelos, texturas, audio y vídeos. El autor indica que los paquetes incluyen el programa recompilado, pero no los archivos de datos originales; la licencia GPL del proyecto no concede derechos sobre el contenido de SEGA.

**Qué está disponible:** v0.10.38 añade seguimiento corporal opcional mediante cámara a Android y Linux; Android solo pide permiso de cámara cuando esa función abre una cámara. Hay paquetes para Windows, Linux, Mac con Apple silicon, Android e iOS. El juego real con cámara en Android/Linux sigue sin probarse; la validación usó imágenes guardadas y el Thor probado no tiene cámara. Muchos modos y el soporte en línea/Kinect v2 aún requieren validación. El soporte Apple es experimental, Mac no está notarizado e iOS requiere instalación externa. RemakeList no ha compilado, instalado ni jugado esta versión.

**Licencia del código:** [Project code is GPL-3.0-or-later. The original game’s code and data remain SEGA’s and are outside that grant; third-party components and models retain their separate licenses.](https://github.com/YuutaTsubasa/Free-Riders-Recompiled/blob/main/COPYING)  
**Autor:** YuutaTsubasa  
[Documentación oficial](https://github.com/YuutaTsubasa/Free-Riders-Recompiled/blob/main/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [James Pond 2 Recompiled](https://github.com/griches/JamesPond2RobocodRecomp)

Una adaptación comunitaria de James Pond 2 de Amiga con pantalla panorámica, ranuras de guardado y movimiento visual más fluido. Requiere tu propia imagen de disco Kixx compatible o una instalación WHDLoad.

Original o referencia: **James Pond 2: Codename RoboCod (Amiga)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/griches/JamesPond2RobocodRecomp/releases/tag/v1.0.4) · [Explorar RemakeList](https://remakelist.com/es/remakes/james-pond-2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=james-pond-2-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · macOS 13+ (Apple Silicon / Intel) · Linux x86_64 / Steam Deck · Android 7+ ARM64 (sin probar) · PS5 homebrew

**Estado:** Windows v1.0.4 · otras plataformas por separado

**Qué necesitas:** Aporta tu propia reedición Kixx de Amiga obtenida legalmente, como imagen estándar .adf, opcionalmente comprimida con gzip como .adz o dentro de un .zip, o una instalación WHDLoad compatible. No se admiten la edición original de Millennium con protección anticopia, ADF extendido ni imágenes .dms o .ipf. Aquí no se ofrece ninguna descarga del disco original.

**Qué está disponible:** v1.0.4 es una corrección exclusiva de Windows para los guardados repetidos y los ajustes que dejaban de guardarse tras la primera vez, incluidas las rutas de carpetas de usuario con caracteres no ingleses. Las demás plataformas mantienen sus propias versiones: macOS/Linux 1.0.0, PS5 1.0.2 y Android 1.0.3. Aporta una copia de Amiga compatible obtenida legalmente; no se incluyen datos del juego. Android 1.0.3 es una primera versión de prueba que el autor no ha jugado en un dispositivo Android; requiere Android 7+ ARM64 y controles físicos integrados o externos. PS5 requiere un entorno homebrew ya existente. RemakeList no lo ha instalado ni jugado, ni ha verificado de forma independiente la compatibilidad del juego completo.

**Licencia del código:** [The project’s own code is GPL-3.0. SDL3, Musashi, fonts and other dependencies retain their separate licenses; the original game’s code, artwork and music are not granted under the project license.](https://github.com/griches/JamesPond2RobocodRecomp/blob/main/LICENSE)  
**Autor:** griches  
[Documentación oficial](https://github.com/griches/JamesPond2RobocodRecomp/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [recvx-enhanced-port](https://github.com/aikatore/recvx-enhanced-port)

Adaptación mejorada de Code: Veronica X con cooperativo para dos, apuntado opcional en tercera persona y pantalla ancha. Lee tu propia imagen de disco PS2.

Original o referencia: **Resident Evil Code: Veronica X (PS2)** · Adaptación de la comunidad  
[Descargar y aportar tus archivos del juego](https://github.com/aikatore/recvx-enhanced-port/releases/tag/v0.6.10) · [Explorar RemakeList](https://remakelist.com/es/remakes/recvx-enhanced-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=recvx-enhanced-port-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10+ x86 · Linux i686 · OpenGL 3.3

**Estado:** v0.6.10 · preliminar · cooperativo para dos

**Qué necesitas:** Tu propia ISO legítima de Code: Veronica X para PS2 NTSC-U, SLUS-20184. No incluye datos del juego ni las texturas HD opcionales.

**Qué está disponible:** v0.6.10 es preliminar: ofrece clientes Windows x86 y Linux i686 y un servidor cooperativo Linux x86_64 separado. Linux requiere glibc 2.34+ y bibliotecas gráficas y de audio de 32 bits; ambos clientes necesitan OpenGL 3.3. El intercambio de modelos en escenas sigue en fase inicial; combinar cooperativo y mods puede causar fallos.

**Licencia del código:** [MIT for the port and credited decompilation code; third-party components and Capcom game content have separate terms.](https://github.com/aikatore/recvx-enhanced-port/blob/main/LICENSE)  
**Autor:** aikatore  
[Documentación oficial](https://github.com/aikatore/recvx-enhanced-port/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [Code Veronica PS3 HD Recomp](https://github.com/kastieloficial/RE-Code-Veronica-PS3-HD-Recomp-PC)

Adaptación de Code: Veronica X HD de PS3 con interpolación, herramientas de speedrun y HUD de combate moderno. Requiere tu edición PSN compatible.

Original o referencia: **Resident Evil Code: Veronica X HD (PS3)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/kastieloficial/RE-Code-Veronica-PS3-HD-Recomp-PC/releases/tag/v1.1.11) · [Explorar RemakeList](https://remakelist.com/es/remakes/code-veronica-ps3-hd-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=code-veronica-ps3-hd-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · Direct3D 12

**Estado:** v1.1.11 · Windows · requiere tus propios archivos de PS3

**Qué necesitas:** Tu edición base PS3 PSN 01.00: NPEB00553 (Europa), NPUB30467 (EE. UU.) o NPJB00135 (Japón), con PARAM.SFO y USRDIR/EBOOT.BIN. Europa/EE. UU. requieren además la licencia .rap de la cuenta compradora. No admite actualizaciones ni ediciones en disco; el lanzador no abre PKG directamente.

**Qué está disponible:** v1.1.11 ofrece el archivo para PC Windows y una herramienta de extracción de PKG, mejora el inicio del lanzador y el cambio de texturas, y mantiene separadas las descargas opcionales de texturas. Para compilar se usó el juego USA; las identidades europea/japonesa se comprobaron por sus nombres de archivo, sin probarlas jugando. Aporta tus propios archivos del juego PS3 PSN y las licencias requeridas. Los paquetes opcionales de texturas de terceros o ampliadas con IA tienen derechos independientes y no quedan cubiertos automáticamente por la licencia MIT del código del port. RemakeList no lo ha compilado ni jugado.

**Licencia del código:** [MIT for port/ps3recomp code; third-party terms and Capcom’s original game rights are separate.](https://github.com/kastieloficial/RE-Code-Veronica-PS3-HD-Recomp-PC/blob/code-veronica/LICENSE)  
**Autor:** kastieloficial  
[Documentación oficial](https://github.com/kastieloficial/RE-Code-Veronica-PS3-HD-Recomp-PC/blob/code-veronica/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [OpenRAC](https://github.com/OpenRAC/OpenRAC)

Adaptación nativa de Ratchet &amp; Clank con lanzador común, mejoras gráficas y herramientas de mods. El primer juego es jugable; las secuelas siguen en desarrollo.

Original o referencia: **Ratchet &amp; Clank (PS2)** · Adaptación de la comunidad  
[Descargar y aportar tus archivos del juego](https://github.com/OpenRAC/OpenRAC/releases/tag/launcher-v0.9.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/openrac/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openrac-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 · Linux x64 / ARM64 · macOS universal · Android ARM64

**Estado:** launcher-v0.9.0 · primer juego jugable · secuelas en desarrollo

**Qué necesitas:** Tu disco PS2 del primer juego en ISO o CHD: PAL SCES_509.16 v2.00 o NTSC-U SCUS_971.99 v1.00. El lanzador lo verifica; otras regiones o ediciones pueden no coincidir. No descarga datos del juego.

**Qué está disponible:** launcher-v0.9.0 sigue siendo la versión general del lanzador. sdk-v1.10.0 actualiza el SDK para desarrollar mods, no la versión jugable del juego. launcher-dev-master contiene una compilación de desarrollo 0.9.1 independiente y no debe presentarse como el lanzador estable. Solo el primer Ratchet &amp; Clank figura como jugable. Los juegos posteriores están incompletos; Android se distribuye como APK de depuración y los gráficos mejorados son experimentales.

**Licencia del código:** [Top-level launcher/tools use GPL-3.0-or-later; game modules and the MIT SDK/editor retain their own notices. None of these licenses grant original game-content rights.](https://github.com/OpenRAC/OpenRAC/blob/master/LICENSE.md)  
**Autor:** OpenRAC  
[Documentación oficial](https://github.com/OpenRAC/OpenRAC/blob/master/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [The Umbrella Chronicles Recompiled](https://github.com/solleo95/reuc-recomp)

Adaptación Windows de The Umbrella Chronicles con apuntado por ratón, opciones gráficas modernas y cooperativo en línea inicial para dos.

Original o referencia: **Resident Evil: The Umbrella Chronicles (Wii)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/solleo95/reuc-recomp/releases/tag/0.0.12) · [Explorar RemakeList](https://remakelist.com/es/remakes/reuc-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=reuc-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · AVX2 · Vulkan 1.3

**Estado:** 0.0.12 · versión inicial · cooperativo experimental

**Qué necesitas:** Tu imagen Wii NTSC-U, ID RBUE08. Extráela con Wit incluido en el lanzador o aporta la carpeta DATA extraída. No admite PAL RBUP08 ni Japón RBUJ08. Los componentes propietarios y paquetes de texturas opcionales tienen condiciones propias.

**Qué está disponible:** 0.0.12 ofrece un paquete para Windows con mejores límites de apuntado y zonas de recarga, una tecla de aceleración configurable y menos interrupciones falsas por desincronización cooperativa. El apuntado con pistola de luz/Wii Remote solo tiene pruebas de entradas simuladas. La divergencia transitoria subyacente del cooperativo sigue sin resolverse; esta actualización tolera una sola aparición. Sigue siendo una compilación inicial probada principalmente en un PC con RTX 4080/Windows 11; no se ha establecido el rendimiento mínimo. El cooperativo en línea puede no conectar, desincronizarse o bloquearse; el trazado de rayos solo cubre sombras. RemakeList no ha compilado, instalado ni jugado esta versión.

**Licencia del código:** [GPL-3.0 for project code; vendor DLSS/FidelityFX runtimes and other dependencies keep their own licenses. Capcom game code and assets are excluded.](https://github.com/solleo95/reuc-recomp/blob/main/LICENSE)  
**Autor:** solleo95  
[Documentación oficial](https://github.com/solleo95/reuc-recomp/blob/main/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [G-Diffuser 3DS](https://github.com/cruxxxxxx/gdx-3ds)

Adaptación nativa de F-Zero X para la familia 3DS, con 3D estereoscópico, panel inferior y carreras para dos a cuatro jugadores. Requiere tu volcado compatible y una consola preparada para homebrew.

Original o referencia: **F-Zero X (Nintendo 64)** · Proyecto basado en descompilación  
[Descargar y aportar tus archivos del juego](https://github.com/cruxxxxxx/gdx-3ds/releases/tag/v1.1.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/g-diffuser-3ds/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=g-diffuser-3ds-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** familia Old/New Nintendo 3DS y 2DS · homebrew

**Estado:** v1.1.0 · consola homebrew · requiere cartucho original

**Qué necesitas:** Aporta tu volcado F-Zero X USA revisión 0, conviértelo en el ordenador a dos archivos .o2r y usa tu volcado del firmware DSP de la consola para el audio. EK necesita el disco comercial japonés 64DD compatible; no admite traducciones de aficionados. No se incluyen ROM, discos ni recursos convertidos.

**Qué está disponible:** v1.1.0 ofrece ZIP, .3dsx y .cia separados para Old/New 3DS, versiones EK opcionales y extractores para ordenador. Prepara los recursos en el ordenador; el script extractor requiere una copia git con el submódulo de descompilación. Se retiraron las descargas v1.0.0. Elige la versión de tu consola. La pantalla ancha y el nuevo búfer de pistas solo se probaron en emulador; no se probaron todas las parejas de consolas en multijugador. Old 3DS limita el multijugador 3D a 30 FPS y su EK tiene tirones, música entrecortada y editores lentos. Persisten problemas de memoria y audio; no se garantizan 60 FPS. El servidor en línea es temporal.

**Licencia del código:** [MIT covers original G-Diffuser and 3DS-port additions, unless a file says otherwise. Dependencies, decompiled Nintendo/N64 SDK code and game content have separate rights; the MIT license does not grant rights to those materials.](https://github.com/cruxxxxxx/gdx-3ds/blob/main/LICENSE)  
**Autor:** cruxxxxxx  
[Documentación oficial](https://github.com/cruxxxxxx/gdx-3ds/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [Metroid Dread Recomp — Linux fork](https://github.com/DaniSald/Metroid-Dread-Recomp)

Bifurcación de Metroid Dread Recomp centrada en Linux que compila una versión nativa de PC desde tus archivos Switch 2.1.0. Ofrece AppImage Linux y paquete Windows.

Original o referencia: **Metroid Dread (Nintendo Switch)** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/DaniSald/Metroid-Dread-Recomp/releases/tag/v0.4.0-linux.2) · [Explorar RemakeList](https://remakelist.com/es/remakes/metroid-dread-recomp-linux/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=metroid-dread-recomp-linux-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / Linux x86-64 (glibc 2.38+, OpenGL 4.3) / Steam Deck

**Estado:** v0.4.0-linux.2 · vista previa temprana · compilación local

**Qué necesitas:** Aporta ExeFS y RomFS de tu copia legítima de Metroid Dread 2.1.0, con la actualización combinada o separada. RomFS solo no basta. No distribuye código, datos ni claves del juego.

**Qué está disponible:** v0.4.0-linux.2 ofrece AppImage Linux x86-64 y ZIP Windows. Al iniciar verifica tus archivos y compila localmente; Linux necesita unos 7 GB libres, glibc 2.38+, OpenGL 4.3, SDL2 y selector de carpetas. Conserva el EXE Windows junto a su carpeta de recompilación. Aunque GitHub no la marca como preliminar, el autor llama a todas las 0.x vistas previas tempranas y advierte de cierres y problemas de instalación. Linux carece de Vulkan nativo, actualizador integrado, apuntado libre por ratón y grabación F7. La prueba Steam Deck OLED duró nueve minutos: no demuestra juego completo ni 60 FPS universales.

**Licencia del código:** [SwitchRecomp code is Apache-2.0; the README identifies the combined Windows executable with the ScarletNX renderer as GPL-3.0. Linux and bundled toolchain/libraries have their own notices. Nintendo game files and keys are excluded.](https://github.com/DaniSald/Metroid-Dread-Recomp/blob/main/README.md#licences)  
**Autor:** DaniSald  
[Documentación oficial](https://github.com/DaniSald/Metroid-Dread-Recomp/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [Odin Sphere Leifthrasir PC](https://github.com/saulob/odin-sphere-leifthrasir-pc)

Ejecuta tu paquete compatible de Odin Sphere Leifthrasir de PS4 en Windows, con lanzador, ajustes gráficos y trofeos locales. Linux y Steam Deck son experimentales.

Original o referencia: **Odin Sphere Leifthrasir (PlayStation 4)** · Capa de compatibilidad entre plataformas  
[Descargar y aportar tus archivos del juego](https://github.com/saulob/odin-sphere-leifthrasir-pc/releases/tag/v0.1.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/odin-sphere-leifthrasir-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=odin-sphere-leifthrasir-pc-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10 1903+/11 x64 / Linux x86-64 y Steam Deck (experimentales)

**Estado:** v0.1.0 · versión Windows · Linux experimental

**Qué necesitas:** Aporta tu .pkg PS4 legítimo descifrado: USA CUSA05083 base 1.00, Japón CUSA01290 base 1.00 o actualización 1.02, o Europa CUSA05262 base 1.00 o actualización 1.01. Cada actualización requiere su base regional. Rechaza paquetes cifrados por consola u otras versiones; no proporciona juego ni claves.

**Qué está disponible:** v0.1.0 es la primera versión pública: ZIP Windows x64 y AppImage Linux x86-64 experimental. Importa tu .pkg PS4 descifrado compatible en Play. Requiere Vulkan 1.3 y sus extensiones indicadas y unos 4 GB; Linux necesita glibc 2.31+ y X11/Wayland. Solo 16:9 Original conserva las proporciones: ultrapanorámica estira el juego sin mostrar más mundo, y otras relaciones lo comprimen; HUD, menús y vídeos no se adaptan. Linux/Steam Deck pasaron comprobaciones automatizadas, sin pruebas en hardware real. Descargas sin firma, trofeos locales y sin PSN ni juego en línea.

**Licencia del código:** [GPL-2.0-or-later covers original project code. The shadPS4-derived renderer and other third-party components retain their notices; the original game and its assets are excluded.](https://github.com/saulob/odin-sphere-leifthrasir-pc/blob/main/LICENSE)  
**Autor:** saulob  
[Documentación oficial](https://github.com/saulob/odin-sphere-leifthrasir-pc/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [Rogue Galaxy Recompiled](https://github.com/victor-takai/rogue-galaxy-recomp)

Compila Rogue Galaxy USA de PS2 de forma nativa en Windows desde tu disco, con pantalla ancha, escalado de resolución y ajustes de juego.

Original o referencia: **Rogue Galaxy (PlayStation 2)** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/victor-takai/rogue-galaxy-recomp/releases/tag/v0.1.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/rogue-galaxy-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rogue-galaxy-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64

**Estado:** v0.1.0 preliminar · compilación local Windows · solo disco USA

**Qué necesitas:** Tu imagen legítima de Rogue Galaxy USA PS2, SCUS-97490. No admite otras regiones. No distribuye datos, BIOS ni archivos derivados del disco; conserva localmente el juego generado.

**Qué está disponible:** v0.1.0 es un ZIP instalador preliminar para Windows. Ejecuta Install.bat con tu disco USA: descarga unos 300 MB de herramientas y compila localmente. Reserva unos 16 GB y 20–60 minutos según el PC. La descarga no es el juego completo compilado. El autor informa de título, introducción, Salgin y combates, no de una partida completa. Persiste un bloqueo raro tras cargar Story; escenas pesadas pueden bajar a unos 50 FPS y la pantalla ancha estira menús y texto. El antivirus puede bloquear el compilador local; no implica garantía de seguridad.

**Licencia del código:** [GPL-3.0 covers the project, matching the linked PS2Recomp framework. Dependencies retain their own notices; original game data, BIOS and disc-derived files are not included or relicensed.](https://github.com/victor-takai/rogue-galaxy-recomp/blob/main/LICENSE)  
**Autor:** victor-takai  
[Documentación oficial](https://github.com/victor-takai/rogue-galaxy-recomp/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [PaxDino](https://github.com/wootbeer/PaxDino)

Adaptación PC de Turok: Rage Wars con apuntado por ratón, pantalla ancha y hasta cuatro jugadores locales.

Original o referencia: **Turok: Rage Wars (Nintendo 64)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/wootbeer/PaxDino/releases/tag/v0.1.6) · [Explorar RemakeList](https://remakelist.com/es/remakes/paxdino/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=paxdino-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 / Linux x86_64 y Steam Deck (experimentales)

**Estado:** v0.1.6 · beta · requiere ROM original

**Qué necesitas:** Aporta tu ROM compatible USA de Turok: Rage Wars; el README enumera hashes .n64/.z64 y acepta .v64. La corrección de la prueba cooperativa usa USA 1.0. No incluye datos del juego.

**Qué está disponible:** v0.1.6 ofrece archivos Windows y Linux. Sigue en beta; Linux y Steam Deck son experimentales. El lanzador importa tu ROM. RemakeList no lo ha instalado ni jugado.

**Licencia del código:** [GPL-3.0 applies to project code; original game content and third-party components retain separate rights and terms.](https://github.com/wootbeer/PaxDino/blob/main/COPYING)  
**Autor:** wootbeer  
[Documentación oficial](https://github.com/wootbeer/PaxDino/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [KirbyRecomp](https://github.com/xtamqispeak/KirbyRecomp)

Adaptación experimental de Super Kirby Clash que se compila localmente desde tus archivos Switch.

Original o referencia: **Super Kirby Clash (Switch)** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/xtamqispeak/KirbyRecomp/releases/tag/v0.3.0-alpha) · [Explorar RemakeList](https://remakelist.com/es/remakes/kirby-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=kirby-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · AVX2/FMA · Vulkan 1.3

**Estado:** v0.3.0-alpha · compilación local

**Qué necesitas:** Aporta ExeFS/RomFS coincidentes de Super Kirby Clash, título 01003FB00C5A8000. El ID main probado empieza por c9649e053bd7be2751ef0b00e7c03f5d59695b94; otras revisiones no están verificadas. No ofrece importación ni descifrado NSP/XCI.

**Qué está disponible:** v0.3.0-alpha ofrece un EXE de instalación para Windows y un kit de código fuente. Corrige el renderizado de la tienda y el perfil y añade resolución personalizada y una opción de 120 fps. La instalación traduce y compila localmente tus propios ExeFS/RomFS coincidentes; no incluye un juego precompilado. Las batallas completas y los niveles posteriores siguen sin validar. La ausencia de servicios o las instrucciones no compatibles pueden detener la ejecución; no se ha acreditado el juego completo ni la compra en línea. Requiere Windows x64, AVX2/FMA y el hardware compatible con Vulkan documentado.

**Licencia del código:** [MIT applies to project code; original game content and third-party components retain separate rights and terms.](https://github.com/xtamqispeak/KirbyRecomp/blob/main/LICENSE)  
**Autor:** xtamqispeak  
[Documentación oficial](https://github.com/xtamqispeak/KirbyRecomp/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [1080° Snowboarding: Recompiled](https://github.com/thebradshaw/1080-Snowboarding-decomp)

Adaptación PC de 1080° Snowboarding con pantalla ancha, mayor tasa de fotogramas opcional y distancia de dibujado.

Original o referencia: **1080° Snowboarding (Nintendo 64)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/thebradshaw/1080-Snowboarding-decomp/releases/tag/1.01) · [Explorar RemakeList](https://remakelist.com/es/remakes/1080-snowboarding-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=1080-snowboarding-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 / Linux x64 experimental

**Estado:** 1.01 · Windows / Linux experimental

**Qué necesitas:** Aporta una ROM USA .z64 sin modificar, MD5 fa27089c425dbab99f19245c5c997613. No incluye ROM. Los redibujados opcionales de tablas y el arte del lanzador derivan del juego y quedan fuera de la licencia del código.

**Qué está disponible:** 1.01 ofrece paquetes para Windows x64 y Linux x64 experimental. Corrige la barra oscura parpadeante de la cueva de Mountain Village y añade control de VSync. Se conservan las partidas y ajustes de 1.0; sigue siendo necesaria tu ROM USA .z64 compatible. Linux es experimental y no se ha probado en hardware. El envío a RetroAchievements está pendiente de aprobación; los desbloqueos siguen siendo locales.

**Licencia del código:** [GPL-3.0 applies to project code; original game content and third-party components retain separate rights and terms.](https://github.com/thebradshaw/1080-Snowboarding-decomp/blob/main/LICENSE)  
**Autor:** thebradshaw  
[Documentación oficial](https://github.com/thebradshaw/1080-Snowboarding-decomp/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [Mission: Impossible — PC Recomp](https://github.com/nickallevato/mi_n64_exe)

Adaptación Linux de Mission: Impossible de N64 con apuntado por ratón, pantalla ancha y cámara analógica moderna.

Original o referencia: **Mission: Impossible (Nintendo 64)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/nickallevato/mi_n64_exe/releases/tag/v0.1.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/mi-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mi-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Linux x86_64 · glibc 2.35+ · Vulkan

**Estado:** v0.1.0 · versión Linux · partida completa sin verificar

**Qué necesitas:** Aporta tu ROM USA .z64 con SHA-1 7546d5df1fc93fed8205a066f1333fd7dd50c1e1. No incluye ROM ni recursos originales.

**Qué está disponible:** v0.1.0 ofrece AppImage y tar.gz Linux x64 basados en Ubuntu 22.04; requiere Vulkan y glibc 2.35+. El autor informa de que los 20 niveles cargan y se pueden jugar, sin verificar partidas completas. No hay paquete Windows ni macOS. RemakeList no lo ha instalado ni jugado. Elegir 60 FPS no garantiza ese rendimiento en todos los dispositivos.

**Licencia del código:** [GPL-3.0 applies to project code; original game content and third-party components retain separate rights and terms.](https://github.com/nickallevato/mi_n64_exe/blob/main/COPYING)  
**Autor:** nickallevato  
[Documentación oficial](https://github.com/nickallevato/mi_n64_exe/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [Ascension](https://github.com/arnaldolima1/gow-ascension-pc)

Port Windows experimental de God of War: Ascension desde tu disco PS3 europeo. El autor informa del primer nivel y jefe, no de una partida completa.

Original o referencia: **God of War: Ascension (PS3)** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/arnaldolima1/gow-ascension-pc/blob/main/docs/README.en.md#building) · [Explorar RemakeList](https://remakelist.com/es/remakes/god-of-war-ascension-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=god-of-war-ascension-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · compilación manual desde código

**Estado:** Compilación desde código · experimento de juego inicial

**Qué necesitas:** Tu disco legítimo europeo BCES-01741 v1.00, incluido EBOOT.ELF preparado localmente y las claves personales necesarias. El contenido opcional en portugués brasileño se genera desde tu disco estadounidense. No incluye juego ni claves.

**Qué está disponible:** No hay paquete publicado. Requiere compilación manual con Visual Studio 2022, CMake, Ninja, Vulkan SDK, ps3recomp modificado y .env local; el autor estima 20–40 minutos y 16 GB de RAM. Windows es la ruta documentada y probada; macOS está pausado. Persisten bajo rendimiento, gráficos duplicados y bloqueos de tareas SPU; no se ha establecido que los niveles posteriores sean jugables. RemakeList no lo ha compilado ni jugado.

**Licencia del código:** [MIT covers this repository’s code. The author states that builds using RPCS3’s RSX renderer are GPL-2.0; original game code and assets retain their owners’ rights.](https://github.com/arnaldolima1/gow-ascension-pc/blob/main/LICENSE)  
**Autor:** arnaldolima1  
[Documentación oficial](https://github.com/arnaldolima1/gow-ascension-pc/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [LostWorldNative](https://github.com/snicolast/LostWorldNative)

Port Windows compilado desde código del arcade de pistolas de 1997, con pantalla ancha, gráficos modernos y apuntado por ratón o mando. Requiere el conjunto japonés exacto de ROM.

Original o referencia: **The Lost World: Jurassic Park (arcade)** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/snicolast/LostWorldNative/blob/master/README.md#install) · [Explorar RemakeList](https://remakelist.com/es/remakes/lost-world-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=lost-world-native-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · Vulkan 1.3 · compilación local

**Estado:** Compilación desde código · requiere ROM arcade original

**Qué necesitas:** Tu lostwsga.zip legítimo, conjunto Japón Rev. A de Sega Model 3 Step 1.5, con las ROM indicadas. No admite otras revisiones ni incluye datos originales.

**Qué está disponible:** No hay binario publicado. En Windows se ejecuta build.bat con tu ROM, Python 3 y herramientas C++ Visual Studio 2022; la primera compilación descarga dependencias. Las capturas del autor muestran el port, sin verificar independientemente el juego completo, todos los dispositivos ni el rendimiento a alta frecuencia. Las funciones gráficas opcionales dependen de la GPU. RemakeList no lo ha compilado ni jugado.

**Licencia del código:** [MIT covers the repository’s authored code. Third-party libraries and fonts retain their own licenses; the original arcade game’s ROM, code and data retain their owners’ rights.](https://github.com/snicolast/LostWorldNative/blob/master/LICENSE)  
**Autor:** snicolast  
[Documentación oficial](https://github.com/snicolast/LostWorldNative/blob/master/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [HarmonyRecomp](https://github.com/Wrexxial/HarmonyRecomp)

Port Windows de Harmony of Despair desde tu paquete XBLA, con ajustes gráficos y cooperativo de hasta seis jugadores por LAN o LAN virtual.

Original o referencia: **Castlevania: Harmony of Despair (Xbox 360)** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/Wrexxial/HarmonyRecomp/releases/tag/v0.3.5) · [Explorar RemakeList](https://remakelist.com/es/remakes/harmony-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=harmony-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · compilación local

**Estado:** v0.3.5 · compilación local en Windows

**Qué necesitas:** Aporta tu propio paquete Xbox 360 XBLA 58410A7A. Los DLC opcionales requieren tus propios paquetes de contenido y Title Update 2 (juego 2.04); la instalación actual omite los DLC sin la actualización. No se deben redistribuir el código del juego generado ni los recursos extraídos.

**Qué está disponible:** v0.3.5 ofrece un EXE de instalación para Windows y archivos de herramientas auxiliares para compilar localmente a partir de tu propio paquete XBLA (unos 10–30 minutos y 10 GB de espacio temporal). Corrige el cierre de resultados en línea; las clasificaciones siguen vacías porque no existe un servidor. El cierre al salir se corrigió en v0.3.3. Los DLC opcionales requieren tus propios paquetes y Title Update 2; la instalación actual omite los DLC sin esa actualización. No se ha jugado cada nivel de DLC. El cooperativo necesita versiones de lanzamiento y del juego coincidentes por LAN o LAN virtual, no Xbox Live. RemakeList no lo ha compilado ni jugado.

**Licencia del código:** [The project code is BSD-3-Clause; the extractor includes MIT-licensed NocturneRecomp code. Runtime dependencies retain their terms, and original game code/data are outside these grants.](https://github.com/Wrexxial/HarmonyRecomp/blob/main/LICENSE)  
**Autor:** Wrexxial  
[Documentación oficial](https://github.com/Wrexxial/HarmonyRecomp/blob/main/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [Underground 2 Android Evolved](https://github.com/codepdbh/nfsu2-recompiled)

Adaptación Android nativa de Underground 2 para PC, con controles táctiles y gráficos configurables. Requiere tus archivos PC compatibles.

Original o referencia: **Need for Speed: Underground 2 (PC)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/codepdbh/nfsu2-recompiled/releases/tag/v0.14.11) · [Explorar RemakeList](https://remakelist.com/es/remakes/nfsu2-android-evolved/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nfsu2-android-evolved-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Android 10+ (ARM64 / ARMv7), Vulkan 1.1+; Windows x86 compilación desde código

**Estado:** v0.14.11 APK Android · Windows desde código

**Qué necesitas:** Tu instalación PC compatible y el SPEED2.EXE exacto admitido (4.800.512 bytes), con sus datos. Otros ejecutables o ediciones pueden no coincidir con el recompilador.

**Qué está disponible:** v0.14.11 ofrece APK ARM64/ARMv7 con hashes publicados. Sus notas describen correcciones menores, expresamente sin cambios de rendimiento o juego. Windows tiene compilación documentada desde código, no binario en esta publicación. La compatibilidad varía según dispositivo y controlador. Windows requiere compilación local con sus herramientas. El README aún menciona v0.14.9; se comprobó v0.14.11.

**Código visible; sujeto a restricciones de licencia:** [The README declares MIT for the author’s original tooling. No standalone project license was verified. This statement does not license the original executable, game code or assets.](https://github.com/codepdbh/nfsu2-recompiled/blob/main/README.md)  
**Autor:** codepdbh  
[Documentación oficial](https://github.com/codepdbh/nfsu2-recompiled/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [LASRecomp Android](https://github.com/mamcjr/LASRecompAndroid)

Bifurcación Android de LASRecomp con controles móviles y compilación en el dispositivo. Requiere tus archivos compatibles de Link’s Awakening para Switch.

Original o referencia: **The Legend of Zelda: Link’s Awakening (Switch)** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/mamcjr/LASRecompAndroid/releases/tag/v0.5.7) · [Explorar RemakeList](https://remakelist.com/es/remakes/las-recomp-android/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=las-recomp-android-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Android 11+ ARM64; GPU/controlador Vulkan compatible

**Estado:** v0.5.7 preliminar · Android · compilación en el dispositivo

**Qué necesitas:** Tus ExeFS/RomFS de Link’s Awakening Switch 1.0.0, 1.0.1 o 1.1.0. Mantén compatibles las versiones del ejecutable y los datos.

**Qué está disponible:** v0.5.7 es una APK preliminar para Android 11+ ARM64. Necesita unos 12 GB libres y compila en el teléfono. Hay rutas alternativas Vulkan 1.1/1.2, con resultados variables. Se valida principalmente en POCO F7 Ultra, Snapdragon 8 Elite/Adreno 830. Buenos resultados Adreno pueden requerir Turnip; forzar rutas alternativas no demuestra soporte Mali real. v0.5.7 no se probó en un Mali físico.

**Licencia del código:** [The Android port and upstream project code have scoped MIT notices. Third-party components retain their licenses; original Nintendo data and generated game code are outside that grant.](https://github.com/mamcjr/LASRecompAndroid/blob/main/LICENSE)  
**Autor:** mamcjr  
[Documentación oficial](https://github.com/mamcjr/LASRecompAndroid/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [Project Stonehenge](https://github.com/Onaga00/ProjectStonehenge)

Reconstrucción nativa Windows de Ace Combat 04 con ajustes gráficos modernos. Requiere tu imagen PS2 USA.

Original o referencia: **Ace Combat 04: Shattered Skies (PS2)** · Proyecto basado en descompilación  
[Descargar y aportar tus archivos del juego](https://github.com/Onaga00/ProjectStonehenge/releases/tag/Beta) · [Explorar RemakeList](https://remakelist.com/es/remakes/project-stonehenge/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=project-stonehenge-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64; Vulkan 1.2

**Estado:** Paquete 0.9.6 · etiqueta Beta · Windows

**Qué necesitas:** Tu disco PS2 USA SLUS-20152 en imagen ISO9660 estándar de sectores de 2048 bytes. No admite BIN/CUE raw.

**Qué está disponible:** La etiqueta de publicación es Beta y el paquete Windows adjunto es 0.9.6. El autor informa de campaña completa jugable; sigue siendo beta. Compatibilidad y alta frecuencia son afirmaciones del autor, no garantías para cada sistema. La ausencia de marca preliminar en GitHub no la convierte en versión final.

**Licencia del código:** [Project code is GPL-3.0. The license does not cover original game assets, trademarks or disc data; dependencies retain their own terms.](https://github.com/Onaga00/ProjectStonehenge/blob/main/LICENSE)  
**Autor:** Onaga00  
[Documentación oficial](https://github.com/Onaga00/ProjectStonehenge/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [Project 8 Plus](https://github.com/MaxLeiter/project-8-plus)

Adaptación nativa de escritorio de Tony Hawk’s Project 8 con gráficos modernos y herramientas de mods. Requiere tu juego PS3 compatible y actualización.

Original o referencia: **Tony Hawk’s Project 8 (PS3)** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/MaxLeiter/project-8-plus/releases/tag/v0.9.2) · [Explorar RemakeList](https://remakelist.com/es/remakes/project-8-plus/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=project-8-plus-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64, Direct3D 12; Linux x86_64 experimental

**Estado:** v0.9.2 · Windows · Linux experimental

**Qué necesitas:** Tu carpeta PS3 USA BLUS30011 con actualización 01.02 y la preparación RPCS3 documentada. El paquete HD opcional no aporta las texturas originales.

**Qué está disponible:** v0.9.2 ofrece preparación Windows, archivo Linux experimental y paquete opcional de modelos HD/herramientas. Windows necesita internet y unos 4 GB; el autor estima 20–25 minutos. Linux sigue experimental. Las instalaciones existentes deben recompilar para adoptar las partidas compartidas de v0.9.2. El reescalado opcional requiere procesamiento local y no garantiza una mejora visual o de rendimiento universal verificada.

**Licencia del código:** [Project code is MIT; the optional upscaling model is CC-BY-4.0 and dependencies have their own notices. Original game content is excluded.](https://github.com/MaxLeiter/project-8-plus/blob/master/LICENSE)  
**Autor:** MaxLeiter  
[Documentación oficial](https://github.com/MaxLeiter/project-8-plus/blob/master/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [2014 FIFA World Cup Brazil: Recompiled](https://github.com/HossEz/fifa-world-cup-2014-recompiled)

Port Windows no oficial del juego de fútbol Xbox 360, con lanzador para importar tu disco o carpeta extraída.

Original o referencia: **2014 FIFA World Cup Brazil** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/HossEz/fifa-world-cup-2014-recompiled/releases/tag/v0.1.10) · [Explorar RemakeList](https://remakelist.com/es/remakes/fifa-world-cup-2014-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fifa-world-cup-2014-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · Direct3D 12 · SSE4.2

**Estado:** v0.1.10 · vista previa · requiere recursos originales

**Qué necesitas:** Tu copia Xbox 360 como ISO o carpeta con default.xex. El proyecto no proporciona datos del juego.

**Qué está disponible:** v0.1.10 ofrece instalador Windows y ZIP portátil; el lanzador verifica tu juego. Se mantienen los requisitos CPU/GPU. Intel UHD e Iris Xe usan un renderizador más lento; vídeos, repeticiones y celebraciones a alta resolución pueden bajar de 60 FPS. Son informes del autor, no pruebas independientes del juego completo.

**Licencia del código:** [BSD-3-Clause covers the author's launcher, fixes, SDK patches and tools. It excludes the original game and recompiled game code; dependencies retain their own licenses.](https://github.com/HossEz/fifa-world-cup-2014-recompiled/blob/main/LICENSE)  
**Autor:** HossEz  
[Documentación oficial](https://github.com/HossEz/fifa-world-cup-2014-recompiled/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [Smash 4 PC](https://github.com/josiahg2502-glitch/Smash4PC)

Port Windows nativo de Super Smash Bros. for Wii U con lanzador para tus archivos de juego, actualización y DLC opcionales.

Original o referencia: **Super Smash Bros. for Wii U** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/josiahg2502-glitch/Smash4PC/releases/tag/v0.1.1) · [Explorar RemakeList](https://remakelist.com/es/remakes/smash4pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=smash4pc-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · Vulkan 1.3

**Estado:** v0.1.1 · port inicial · juego en red por streaming en beta

**Qué necesitas:** Tu volcado Wii U USA; se recomienda v304 y el DLC debe proceder de tu volcado. Pretendo necesita además tus archivos de consola Wii U y cuenta.

**Qué está disponible:** v0.1.1 ofrece un ZIP para Windows con compatibilidad con CPU antiguas y correcciones de entradas y tirones. Sus nuevas salas beta de juego en red transmiten la partida de un anfitrión a hasta siete invitados a 1080p/60, devolviendo las entradas de los invitados al anfitrión. Es streaming de juego remoto, no ocho instancias nativas del juego sincronizadas. La nueva vía de streaming se probó en un solo PC, no entre domicilios distintos; las redes restrictivas pueden impedir conexiones directas. El anfitrión necesita los archivos originales del juego USA de Wii U. Las tasas de visualización altas usan interpolación; el código del juego generado en el repositorio tiene derechos independientes. RemakeList no lo ha probado.

**Licencia del código:** [Project-authored code is MIT; Cemu-derived network code is MPL-2.0 and other components retain their notices. None of these licenses grants rights to Nintendo game code or assets.](https://github.com/josiahg2502-glitch/Smash4PC/blob/main/LICENSE)  
**Autor:** josiahg2502-glitch  
[Documentación oficial](https://github.com/josiahg2502-glitch/Smash4PC/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [Glassline](https://github.com/MoonCellar-Team/Glassline)

Lleva Mirror’s Edge para iPad a escritorio, Android y navegador, con controles modernos y partidas opcionales uno contra uno en red.

Original o referencia: **Mirror's Edge for iPad** · Proyecto basado en descompilación  
[Descargar y aportar tus archivos del juego](https://github.com/MoonCellar-Team/Glassline/releases/tag/v1.4.1) · [Explorar RemakeList](https://remakelist.com/es/remakes/glassline/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=glassline-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 · Linux x64 / Steam Deck · Android 9+ · Web

**Estado:** v1.4.1 · escritorio, Android y navegador

**Qué necesitas:** Tu IPA de Mirror’s Edge para iPad v1.1.48 o posterior; no admite la edición iPhone. No proporciona datos originales.

**Qué está disponible:** v1.4.1 ofrece paquetes para Windows, Linux, Android y web y corrige los controles táctiles/de equilibrio y un cierre al iniciar en navegador. Requiere tu propio IPA 1.1.48+ de Mirror’s Edge para iPad; el juego de iPhone no es compatible. El uno contra uno en línea y las cuentas usan servicios de MoonCellar, no de EA; la clasificación solo para amigos sigue vacía. No existe paquete nativo de macOS. Borrar el almacenamiento del navegador elimina los archivos y las partidas locales del juego, y los efectos mejorados requieren OpenGL ES 3.0. Las condiciones del código fuente disponible restringen la redistribución y el uso comercial.

**Código visible; sujeto a restricciones de licencia:** [The custom license permits specified personal noncommercial use of the author's work. Redistribution, modified builds and commercial use need separate permission. EA's original code and assets are excluded; dependencies retain their licenses.](https://github.com/MoonCellar-Team/Glassline/blob/main/LICENSE)  
**Autor:** MoonCellar-Team  
[Documentación oficial](https://github.com/MoonCellar-Team/Glassline/blob/main/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [RE: Outbreak](https://github.com/Ninjacornix/reo)

Un port de Resident Evil Outbreak para Windows con compilación local guiada, controles configurables y cooperativo opcional mediante openSNAP. File #1 tiene una versión estable; File #2 es una opción experimental en versión candidata.

Original o referencia: **Resident Evil Outbreak File #1** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/Ninjacornix/reo/releases/tag/v1.0.20-rc0) · [Explorar RemakeList](https://remakelist.com/es/remakes/reo-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=reo-native-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 · .NET 8 Desktop Runtime · Vulkan

**Estado:** v1.0.20-rc0 · versión candidata · File #2 experimental

**Qué necesitas:** v1.0.20-rc0 acepta tu propia ISO File #1 NTSC-U v2.00 (SLUS-20765) o la experimental File #2 NTSC-U v1.05 (SLUS-20984). La estable v1.0.19 solo admite File #1. Conserva la ISO y los ZIP build-inputs de la versión para compilar localmente. No se admiten versiones PAL, japonesas, modificadas ni otras revisiones; no se suministran datos del juego ni BIOS de PS2.

**Qué está disponible:** v1.0.20-rc0 es una versión candidata con un lanzador portátil de Windows, entorno de ejecución .NET incluido y configuración automática del compilador. Compila localmente a partir de tu disco File #1 NTSC-U v2.00 o del experimental File #2 NTSC-U v1.05. v1.0.19 sigue siendo la versión estable de File #1. RC0 copia automáticamente los datos, cachés, ajustes y partidas anteriores del lanzador al usar una carpeta de datos nueva. Haz una copia de las partidas y sigue las instrucciones de instalación limpia de la versión antes de abrir una extracción nueva. File #2 es experimental; el soporte en RC no implica una versión estable.

**Licencia del código:** [This fork's original contributions use GPL-3.0-only. Upstream and third-party code retains its own notices. Original game content and generated game code are not licensed by this grant.](https://github.com/Ninjacornix/reo/blob/main/LICENSE)  
**Autor:** Ninjacornix  
[Documentación oficial](https://github.com/Ninjacornix/reo/blob/main/README.md) · Fuentes revisadas: 2026-10-29

</details>

### [SegaSonic Native Port](https://github.com/cheviman/segasonic-port)

Port nativo del arcade Sega para tres jugadores, con opciones de escritorio y portátiles, desde tu conjunto exacto de ROM.

Original o referencia: **SegaSonic The Hedgehog (arcade)** · Proyecto basado en descompilación  
[Descargar y aportar tus archivos del juego](https://github.com/cheviman/segasonic-port/releases/tag/v1.3.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/segasonic-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=segasonic-port-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows x64 · Linux x64 · macOS 11+ · Anbernic H700 · Android/Switch generados localmente

**Estado:** v1.3.0 · importación local de recursos

**Qué necesitas:** Tu sonic.zip SegaSonic The Hedgehog Japón revisión C, con los 18 archivos esperados. Importar crea segasonic.assets; los paquetes móviles/consola generados contienen tus recursos extraídos y no deben compartirse.

**Qué está disponible:** v1.3.0 ofrece paquetes para Windows, Linux, macOS y Anbernic con nuevos ajustes de trackball y asignación de mandos. Aporta tu propio sonic.zip (Japón rev. C, 18 archivos) o importa tu segasonic.assets extraído. El APK para Android 7+ y el NSP de Switch se generan localmente; generar el de Switch también requiere tus propias claves. Estos paquetes personales contienen recursos originales y no deben compartirse. El multijugador es local para hasta tres jugadores. Las compilaciones de macOS no están firmadas; las comparaciones del autor con MAME no son pruebas de juego de RemakeList.

**Licencia del código:** [Project code uses BSD-3-Clause; MAME/ymfm-derived components, SDL and Kenney assets have their own BSD, zlib or CC0 terms. Original Sega ROMs and assets are not licensed by the project.](https://github.com/cheviman/segasonic-port/blob/main/LICENSE)  
**Autor:** cheviman  
[Documentación oficial](https://github.com/cheviman/segasonic-port/blob/main/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [Stunt Race FX DECOMP](https://github.com/Mabec-games/Stunt-Race-FX-DECOMP)

Port Linux experimental del juego de carreras SNES Super FX, con lógica original y gráficos más fluidos y de mayor resolución.

Original o referencia: **Stunt Race FX** · Proyecto basado en descompilación  
[Descargar y aportar tus archivos del juego](https://github.com/Mabec-games/Stunt-Race-FX-DECOMP/releases/tag/beta-0.1) · [Explorar RemakeList](https://remakelist.com/es/remakes/stunt-race-fx-decomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=stunt-race-fx-decomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Linux x86-64

**Estado:** beta-0.1 · vista previa · requiere recursos originales

**Qué necesitas:** Tu ROM Stunt Race FX USA revisión 1, SHA-1 781e376ff453a83c7bcf72339abe6b842efd9c86. No incluye datos del juego.

**Qué está disponible:** beta-0.1 ofrece AppImage Linux x86-64. La promesa del README de publicarlo más adelante está desactualizada: el archivo ya existe. También documenta compilación desde código. Beta temprana: Speed Trax, especialmente pistas principiantes, tiene mayor cobertura. Otros circuitos y modos siguen incompletos; menús, selección de coche y batalla para dos conservan resolución original sin interpolación. Ver 60 FPS fluidos no cambia la simulación original.

**Licencia del código:** [The upstream decompilation and this fork are offered under CC0-1.0. Nintendo/Argonaut's original game and ROM contents remain separately protected and are not supplied.](https://github.com/Mabec-games/Stunt-Race-FX-DECOMP/blob/main/LICENSE)  
**Autor:** Mabec-games  
[Documentación oficial](https://github.com/Mabec-games/Stunt-Race-FX-DECOMP/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [2010 FIFA World Cup South Africa: Recompiled](https://github.com/CalinGraphics/fifa-world-cup-2010-recompiled)

Port Windows del juego del Mundial de Xbox 360, disponible mediante compilación local documentada desde tu disco compatible.

Original o referencia: **2010 FIFA World Cup South Africa** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/CalinGraphics/fifa-world-cup-2010-recompiled/blob/main/README.md) · [Explorar RemakeList](https://remakelist.com/es/remakes/fifa-world-cup-2010-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fifa-world-cup-2010-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · Direct3D 12 · SSE4.2

**Estado:** Temprano · compilación local y recursos originales

**Qué necesitas:** Tu edición exacta Xbox 360 europea con inglés, español y neerlandés, con hashes coincidentes de default.xex y fifadllzf.xex. No admite PS3 ni otras regiones.

**Qué está disponible:** El 28 de octubre de 2026 no había versiones GitHub publicadas pese al botón del README. Usa BUILDING.md y build.ps1; el autor estima una hora para SDK y primera compilación. No funciona el modo en línea/Xbox Live. Menús y vídeos siguen a 30 FPS; el autor no probó todos los modos de principio a fin. La imagen localizada muestra el lanzador del autor, no demuestra juego.

**Licencia del código:** [BSD-3-Clause covers the author's launcher, app, hooks, SDK patches and tools. Original and recompiled game code are excluded, and third-party components keep their licenses.](https://github.com/CalinGraphics/fifa-world-cup-2010-recompiled/blob/main/LICENSE)  
**Autor:** CalinGraphics  
[Documentación oficial](https://github.com/CalinGraphics/fifa-world-cup-2010-recompiled/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [BotW Recompiled for Windows](https://github.com/ryderclanky/BotW-Native)

Port Windows temprano de Breath of the Wild de Wii U, con traducción local del juego y gráficos Vulkan.

Original o referencia: **The Legend of Zelda: Breath of the Wild (Wii U)** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/ryderclanky/BotW-Native/releases/tag/v0.1.1) · [Explorar RemakeList](https://remakelist.com/es/remakes/botw-native-windows/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=botw-native-windows-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · Vulkan 1.1 · compilación local

**Estado:** v0.1.1 · temprano · compilación local y recursos originales

**Qué necesitas:** Tu juego Wii U USA ya extraído con actualización v208 (1.5.0), carpetas code/content/meta y hash U-King.rpx compatible. No incluye claves ni juego.

**Qué está disponible:** v0.1.1 ofrece ZIP Windows con lanzador y código. Compila localmente tu juego; la ruta desde código usa MSYS2 UCRT64. No es una versión del juego completo. El autor comprobó escenas concretas de inicio, combate, mapa, viaje y Hateno en un portátil NVIDIA reciente. Mandos, efectos, texto de vídeos, DLC y sesiones largas siguen incompletos o sin verificar. El README se contradice sobre audio, por lo que no se confirma sonido funcional. No se ha establecido jugabilidad Linux/Apple en este fork.

**Licencia del código:** [Project-authored code is MIT; Cemu-derived components stay MPL-2.0, with other dependencies under their own licenses. Nintendo's original game, assets and extracted files are excluded.](https://github.com/ryderclanky/BotW-Native/blob/main/LICENSE)  
**Autor:** ryderclanky  
[Documentación oficial](https://github.com/ryderclanky/BotW-Native/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [358/2 Days for Android](https://github.com/sonofskywalker3/khdays-358-android)

Fork Android del port nativo Kingdom Hearts 358/2 Days de Yokimitsuro, con dos pantallas en AYN Thor y pantalla compartida en teléfonos.

Original o referencia: **Kingdom Hearts 358/2 Days** · Proyecto basado en descompilación  
[Descargar y aportar tus archivos del juego](https://github.com/sonofskywalker3/khdays-358-android/releases/tag/android-0.1.4-beta8) · [Explorar RemakeList](https://remakelist.com/es/remakes/khdays-358-android/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=khdays-358-android-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Android 10+ · ARM64 · Vulkan · dos pantallas AYN Thor

**Estado:** android-0.1.4-beta8 · Mali experimental

**Qué necesitas:** Tu ROM de cartucho DS europeo o norteamericano. Vídeos/menús HD opcionales requieren tus copias HD 1.5+2.5 ReMIX y, para menús, HD 2.8; no se incluyen.

**Qué está disponible:** android-0.1.4-beta8 ofrece un APK para Android y corrige los cierres de paneles de Mission Mode y la disposición de la pantalla inferior. El soporte de GPU Mali es experimental y no se ha probado en hardware Mali; las escenas 3D cargadas siguen siendo lentas en el AYN Odin antiguo. Requiere Android 10+, ARM64/Vulkan y tu propia ROM europea o norteamericana de DS. El EXE de Windows que lo acompaña prepara contenido HD opcional a partir de tus propias colecciones HD; no es una compilación de Android. Las carpetas personalizadas de HD/mods necesitan acceso a todos los archivos. Exporta las partidas antes de desinstalar, ya que esto elimina los datos locales de la aplicación. Las afirmaciones sobre el juego completo son del autor, no pruebas de RemakeList.

**Licencia del código:** [Project code uses MIT with upstream and third-party notices retained. This does not grant rights to Square Enix/Disney game files or optional HD collection assets.](https://github.com/sonofskywalker3/khdays-358-android/blob/master/LICENSE)  
**Autor:** sonofskywalker3  
[Documentación oficial](https://github.com/sonofskywalker3/khdays-358-android/blob/master/.github/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [F.E.A.R. 360 Recompiled](https://github.com/Juansolo457/fear360-recomp)

Un port nativo de F.E.A.R. y F.E.A.R. Files de Xbox 360 para Linux y Steam Deck que se compila desde el código fuente, con un menú de colección y controles de tasa de fotogramas ajustados a la pantalla.

Original o referencia: **F.E.A.R. / F.E.A.R. Files (Xbox 360)** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/Juansolo457/fear360-recomp/blob/master/docs/SETUP.md) · [Explorar RemakeList](https://remakelist.com/es/remakes/fear360-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fear360-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Código actual: Linux x86-64 / Steam Deck nativos · AVX2/FMA · Vulkan 1.3; estable v0.1.5: Windows Direct3D 12 / Proton

**Estado:** Compilación desde el código · estable v0.1.5 / línea de desarrollo nativa de Linux 0.9

**Qué necesitas:** Aporta tus propios discos compatibles de Xbox 360: F.E.A.R. Title ID 565507D9 y F.E.A.R. Files 565507E8, con los valores SHA-256 de ejecutables indicados en SETUP.md. Los ejecutables generados y el paquete local de Steam Deck incluyen código y datos derivados del disco; mantenlos privados. No se suministran recursos originales ni un paquete del juego listo para usar.

**Qué está disponible:** El endpoint de GitHub de la última versión estable sigue devolviendo v0.1.5, una versión de código fuente para Windows con una vía mediante Proton para Steam Deck y sin archivos ejecutables. Por separado, la documentación de la rama predeterminada actual denomina su línea de desarrollo 0.9 y ofrece compilaciones Vulkan nativas para Linux/Steam Deck sin Proton, con informes del autor de pruebas de juego y rendimiento. Verificamos las instrucciones de compilación, no una etiqueta de versión v0.9.0. Las compilaciones de Windows con el código actual no están probadas. Completar las campañas sigue siendo un objetivo de pruebas de v1.0; RemakeList no ha compilado ni jugado ninguna de las dos vías. Actualmente renderiza a 1280×720 y no admite el paquete de texturas de PC. Los tiroteos a cámara lenta pueden no alcanzar 120 fps; faltan las marcas de sangre en Steam Deck y los autoguardados de la historia pueden desconectar brevemente el mando. Aún requieren validación los 120 Hz en modo conectado a una base, la misión adicional Holiday y las campañas completas. Las compilaciones de Windows de la línea de desarrollo 0.9 documentada no están probadas; Android y Windows ARM64 siguen siendo trabajo futuro. Archivos originales / configuración: Aporta tus propios discos compatibles de Xbox 360: F.E.A.R. Title ID 565507D9 y F.E.A.R. Files 565507E8, con los valores SHA-256 de ejecutables indicados en SETUP.md. Los ejecutables generados y el paquete local de Steam Deck incluyen código y datos derivados del disco; mantenlos privados. No se suministran recursos originales ni un paquete del juego listo para usar.

**Licencia del código:** [Own tools and glue are MIT, fear-nx-derived runtime parts are GPL-3.0-or-later, and renderer/SDK components have MIT/BSD terms. Linked builds include GPL obligations. Original game code, assets and generated private builds must not be redistributed as project downloads.](https://github.com/Juansolo457/fear360-recomp/blob/master/LICENSE)  
**Autor:** Juansolo457  
[Documentación oficial](https://github.com/Juansolo457/fear360-recomp/blob/master/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [ReStreet](https://github.com/samuelit0davila/fifa-street-pc-port)

Recompilación Windows de FIFA Street (2012), con lanzador, carrera local y servidores comunitarios opcionales, desde tu juego Xbox 360.

Original o referencia: **FIFA Street (2012)** · Recompilación estática  
[Descargar y aportar tus archivos del juego](https://github.com/samuelit0davila/fifa-street-pc-port/releases/tag/v2.1.3-online-beta) · [Explorar RemakeList](https://remakelist.com/es/remakes/restreet-fifa-street/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=restreet-fifa-street-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · lanzador Linux con Proton (beta)

**Estado:** v2.1.3-online-beta · vista previa · requiere recursos originales

**Qué necesitas:** Tu ISO Xbox 360 de FIFA Street (2012). No hay descarga separada de datos originales; el autor declara incluir binarios del juego generados en el instalador.

**Qué está disponible:** v2.1.3-online-beta ofrece instalador Windows y lanzador Linux nativo; Linux ejecuta el juego con Proton. El 2.0.8 del README está desactualizado. Windows añade restauración de World Tour, aún ausente en el lanzador Linux. Salas e invitaciones Linux siguen en pruebas y el autor no probó Steam Deck. Vulkan puede dar tirones o cerrarse en AMD; resolución interna actual 1280×720. Los servidores comunitarios tienen condiciones propias. Si desaparece una carrera World Tour, deja de jugar antes de restaurar: solo conserva las diez últimas partidas. No se afirman derechos de distribución de los binarios generados.

**Licencia del código:** [MIT covers the author's installer, launcher and scripts only; dependencies keep their licenses. The installer contains generated game binaries, and the author explicitly says MIT does not establish redistribution rights or legal clearance for them.](https://github.com/samuelit0davila/fifa-street-pc-port/blob/main/LICENSE)  
**Autor:** samuelit0davila  
[Documentación oficial](https://github.com/samuelit0davila/fifa-street-pc-port/blob/main/README.md) · Fuentes revisadas: 2026-10-28

</details>

### [NX2Apple](https://github.com/LNPANDY/NX2Apple)

Biblioteca y lanzador de juegos para Mac y herramienta gráfica de compilación para nxnative. Crea apps personales para Mac o iPhone/iPad desde tus archivos Switch compatibles; es una bifurcación comunitaria independiente, no una colección de juegos incluidos.

Original o referencia: **Compilación y gestión de bibliotecas de juegos Nintendo Switch en dispositivos Apple** · Capa de compatibilidad entre plataformas  
[Compilar y aportar tus archivos del juego](https://github.com/LNPANDY/NX2Apple/releases/tag/v0.7.1) · [Explorar RemakeList](https://remakelist.com/es/remakes/nx2apple/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nx2apple-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Herramienta de compilación: Mac Apple silicon, macOS 13+ · destinos: Mac / iPhone / iPad

**Estado:** v0.7.1 · herramienta de compilación local guiada

**Qué necesitas:** Aporta tus propios volcados de juegos de Switch, las actualizaciones y DLC requeridos y prod.keys. El lanzador abre en Mac con Apple silicon y macOS 13+; las compilaciones de juegos NVN necesitan Xcode 27.1 en macOS 26.6+, salvo que se use la sustitución de Metal alternativa documentada. La aplicación incluye Python y herramientas de compilación e instala .NET SDK 10. Las compilaciones de iPhone se dirigen a iOS 26+; los dispositivos antiguos no están probados. El código y los recursos derivados del juego no deben redistribuirse.

**Qué está disponible:** v0.7.1 ofrece la herramienta de compilación para Mac con Apple silicon. El modo consola ahora inicia los juegos a pantalla completa en la pantalla del lanzador, los fallos de compilación ofrecen acciones de recuperación y los DLC seleccionados se incorporan a las compilaciones reducidas de iOS. v0.7.0 también añade sincronización de partidas entre Mac/iPhone mediante una carpeta de iCloud Drive. Los cambios del juego requieren recompilar a partir de tus propios volcados. Se ofrece una herramienta de compilación, no aplicaciones de juego listas para jugar. Los perfiles no acreditan compatibilidad completa; los mods reales siguen sin probarse. Windows no tiene un proceso de publicación verificado. Los juegos grandes dependen de la memoria del dispositivo y de los permisos de firma; la firma gratuita con Apple ID caduca a los siete días. RemakeList no ha compilado, instalado ni jugado esta versión.

**Licencia del código:** [MIT covers project code, with upstream attribution and separate third-party notices. It grants no rights to Nintendo game code, assets, keys or the game-derived packages you build.](https://github.com/LNPANDY/NX2Apple/blob/main/LICENSE)  
**Autor:** LNPANDY and contributors  
[Documentación oficial](https://github.com/LNPANDY/NX2Apple/blob/main/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [NHL 2K8 Recompiled](https://github.com/anishchandra24/NHL2K8-Recompiled)

Adaptación no oficial para Windows del juego de hockey de Xbox 360, reconstruida localmente con tus propios archivos de NHL 2K8, con multijugador local y música personalizada.

Original o referencia: **NHL 2K8** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/anishchandra24/NHL2K8-Recompiled/releases/tag/v1.1.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/nhl2k8-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nhl2k8-recompiled-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 · Direct3D 12 · compilación local; Windows 11 sin probar

**Estado:** v1.1.0 · compilación local · multijugador local · sin funciones en línea

**Qué necesitas:** Debes aportar tu copia legal de NHL 2K8 para Xbox 360, ID de título 54540809, versión 0.0.0.3, extraída con default.xex y los demás archivos juntos. El README especifica el hash del ejecutable admitido; otras ediciones no son compatibles. Reserva espacio adicional para los archivos extraídos. RemakeList no proporciona datos del juego.

**Qué está disponible:** v1.1.0 ofrece un programa de configuración que descarga herramientas y compila localmente, además de una vía manual desde el código fuente. Junto con tus archivos de una versión compatible del juego, requiere Windows 10/11 x64, Direct3D 12, Visual Studio 2022 C++ con Clang/CMake, Git, internet durante la configuración y unos 10 GB para compilar. El autor solo ha probado Windows 10. Las funciones en línea no funcionan; puede haber tirones con mucho público o al encontrar un shader por primera vez. El botón Save to config de los ajustes F4 escribe una configuración ilegible. RemakeList no lo ha instalado ni jugado; la afirmación del autor sobre falsos positivos del antivirus no es una verificación de seguridad independiente.

**Licencia del código:** [GPL-3.0 covers the project-owned files only. ReXGlue/Xenia patches retain their BSD licenses. Original game files, generated game code, artwork and screenshots are excluded.](https://github.com/anishchandra24/NHL2K8-Recompiled/blob/main/LICENSE)  
**Autor:** anishchandra24  
[Documentación oficial](https://github.com/anishchandra24/NHL2K8-Recompiled/blob/main/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [Virtua Fighter 2 Recomp](https://github.com/mr-finster/vf2-recomp)

Adaptación no oficial de Virtua Fighter 2 para escritorio, con renderizado de mayor resolución, pantalla panorámica y juego en línea experimental con rollback mediante tu propia ROM arcade.

Original o referencia: **Virtua Fighter 2** · Adaptación de la comunidad  
[Descargar y aportar tus archivos del juego](https://github.com/mr-finster/vf2-recomp/releases/tag/v0.1.16) · [Explorar RemakeList](https://remakelist.com/es/remakes/virtua-fighter-2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=virtua-fighter-2-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10/11 x64 / macOS 11+ Intel y Apple silicon / Linux x64 y ARM64 / Steam Deck

**Estado:** v0.1.16 · descargas para escritorio · juego en línea experimental con rollback

**Qué necesitas:** Se necesita tu propio conjunto de ROM MAME vf2 Version 2.1, vf2.zip, obtenido legalmente. El proyecto no incluye ROM ni material generado a partir de ellas. Los rivales en línea deben usar el mismo conjunto. Las instrucciones Linux ARM64 están dirigidas a Raspberry Pi 5 y Ubuntu 22.04, Debian 12 o Raspberry Pi OS Bookworm y posteriores.

**Qué está disponible:** v0.1.16 ofrece archivos para Windows 10/11 x64, macOS 11+ Universal, Linux x64/Steam Deck y Linux ARM64. Debes aportar el conjunto de ROM MAME vf2 Version 2.1, vf2.zip. Las compilaciones para Mac y Windows no están firmadas. El juego en línea es experimental y ambos jugadores necesitan ROM idénticas y versiones compatibles; las partidas directas revelan tu IP al rival, mientras que Hide my IP address utiliza un servidor de retransmisión. La instalación nativa en Steam Deck debe seguir la guía de Linux. RemakeList no lo ha instalado ni jugado.

**Licencia del código:** [MIT for the project’s own code; MAME components retain BSD-3-Clause and other dependencies retain their terms. The author’s app icon and painted selection-screen sides use CC BY 4.0. SEGA game code and assets are not granted by these licenses.](https://github.com/mr-finster/vf2-recomp/blob/main/LICENSE)  
**Autor:** mr-finster  
[Documentación oficial](https://github.com/mr-finster/vf2-recomp/blob/main/README.md) · Fuentes revisadas: 2026-10-30

</details>

### [FM4 Static Recomp](https://github.com/i2kiselev/fm4-static-recomp)

Adaptación no oficial de Forza Motorsport 4 para Windows, compilada localmente desde tu disco de Xbox 360, con renderizado Vulkan, ajustes gráficos modernos y reescalado DLSS/FSR.

Original o referencia: **Forza Motorsport 4** · Recompilación estática  
[Compilar y aportar tus archivos del juego](https://github.com/i2kiselev/fm4-static-recomp/releases/tag/v0.3.0) · [Explorar RemakeList](https://remakelist.com/es/remakes/fm4-static-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fm4-static-recomp-es)

<details>
<summary>Requisitos y capturas</summary>

**Plataformas:** Windows 10 versión 2004+ x64 · Vulkan · compilación local

**Estado:** v0.3.0 · compilación local experimental para Windows · requiere tu Disc 1

**Qué necesitas:** Aporta tu copia legal de Forza Motorsport 4 para Xbox 360, Disc 1 versión 1.0: ID de medio PAL 61D62D9F o USA 26FF1101, ID de título 4D530910. Disc 1 Rev 1/1.1 no es compatible. Tus propios Disc 2 y DLC son opcionales y requieren unos 5 GB adicionales. El lanzador compila localmente; RemakeList no proporciona datos del juego.

**Qué está disponible:** La versión experimental v0.3.0 ofrece un lanzador gratuito para Windows que compila el juego desde tu ISO o datos GOD de un Disc 1 compatible. Requiere Windows 10 versión 2004+ x64, un controlador Vulkan actualizado, internet inicial y unos 10 GB de espacio. La configuración descarga componentes de compilación de Microsoft tras aceptar sus licencias; no incluye el juego precompilado. Solo admite Disc 1 comercial PAL/USA versión 1.0, no Rev 1/1.1. Linux y los volantes están previstos; Xbox LIVE y Kinect no son compatibles. El parpadeo del reescalado sigue siendo un problema conocido. RemakeList no lo ha instalado ni jugado.

**Licencia del código:** [BSD-3-Clause for this project’s source. Pinyon Shift-derived code retains its notices and dependencies keep their terms. The original game, assets, generated translation and resulting game executable are excluded and must not be redistributed.](https://github.com/i2kiselev/fm4-static-recomp/blob/main/LICENSE)  
**Autor:** i2kiselev  
[Documentación oficial](https://github.com/i2kiselev/fm4-static-recomp/blob/main/README.md) · Fuentes revisadas: 2026-10-30

</details>

## Acerca de esta lista

Esta lista se genera a partir de las fichas publicadas en RemakeList. Las incorporaciones, modificaciones y retiradas se revisan primero en el sitio web y después se sincronizan automáticamente con GitHub. Las descripciones de los proyectos se mantienen en un solo lugar. [Notas sobre datos y sincronización](docs/data.md)

Las alternativas funcionales, las reimplementaciones y las adaptaciones describen relaciones diferentes. La licencia del código no concede derechos sobre los recursos del juego original. Las afirmaciones de compatibilidad y rendimiento proceden de las fuentes citadas y no implican pruebas realizadas por RemakeList. Este repositorio no ofrece archivos de juegos, claves ni paquetes de instalación. Algunos proyectos permiten consultar su código con restricciones de licencia y no son de código abierto.

Puedes sugerir proyectos o comunicar errores mediante una Issue. Consulta la guía de contribución para saber qué fuentes aportar. Los datos generados y las entradas del README se actualizan a través de RemakeList. [Sugerir un proyecto](CONTRIBUTING.md)

Los textos originales de la lista se publican bajo CC BY 4.0 y los scripts de generación bajo MIT. Los proyectos y materiales de terceros conservan sus propias licencias. Consulta LICENSE y NOTICE.md.

[CC BY 4.0](LICENSE) · [MIT](scripts/LICENSE) · [NOTICE](NOTICE.md)
