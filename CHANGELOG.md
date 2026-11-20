# Registro de cambios

## [0.5.0] — 2026-11-21 · Misiones ocultas

### Añadido
- **Misiones ocultas por capítulo** (15): contenido que no aparece en el mapa del juego hasta que lo descubres (folletos, llamadas, lugares escondidos y encuentros). Incluye cómo activarlas, dónde, cuándo, recompensa, estado y fuente.
- En la guía interactiva: bloque de ocultas en cada capítulo con casillas, aviso en «Tu próxima parada», capa «Misiones ocultas» en el mapa y botón «Ver en el mapa».
- En la guía en texto: sección 3.6 y checklist 2b.
- Nuevas misiones de Billy, Andy, Yasmani, Moses y Pete en las cadenas secundarias.
- Pistas de inicio para *Get Shirley's Rum*, *Donnie's Lost Drugs* y Kirk.

### Corregido
- Resuelta la duda de trofeos: *Hometown Heroes* (Billy) da *The Lone Rider* y *Puff Puff Pass* (Andy) da *Road to Rehabilitation*.

## [0.4.0] — 2026-11-20 · Mapa interactivo y castellano

### Añadido
- Mapa interactivo de Leonida: esquema propio (no oficial, no a escala) con las 6 regiones anunciadas por Rockstar y condados conocidos, zoom con rueda, botones y pellizco, arrastre, marcadores de secretos e inicio de secundarias, ficha al pulsar y botón «Ver en el mapa» en cada secreto.
- Lista «Aún sin situar en el mapa» para que la comunidad ayude a ubicarlos.
- Nombres en castellano de todas las misiones opcionales y tareas, y de las misiones de cada cadena secundaria, con el nombre original al lado y opción «Nombres originales».
- Validación en `build.py` de áreas y posiciones del mapa.

### Cambiado
- En los secretos, `region` es el texto de ubicación y `area` la región del mapa.

## [0.3.0] — 2026-11-20 · Guía abierta

### Añadido
- Repositorio público con guía de colaboración (`CONTRIBUTING.md`), plantillas de issue (corrección, perdible, secreto, dato nuevo) y de pull request.
- Licencias: CC BY-SA 4.0 para el contenido y MIT para el código (`LICENSE.md`).
- Publicación automática en GitHub Pages: guía interactiva en la raíz y guía en texto en `/guia/`. Validación automática de cada pull request.
- Enlace «Colabora» en la guía interactiva.

## [0.2.0] — 2026-11-20 · Guía interactiva

### Añadido
- `web/`: guía interactiva en un único archivo HTML con portada ilustrada, cuatro secciones (Historia, Mapa secreto, Misiones perdibles, 100 % completado) y progreso guardado en el navegador.
- Motor de avisos «Tu próxima parada»: ALTO antes de *Tourist Trap*, *Checking Out*, *The Cartel Heist* y la misión final; aviso de perdibles disponibles y de reloj de arena.
- Modo sin spoilers, filtros, buscador, contadores del 100 % y copia de seguridad del progreso.
- `web/data/guia.json` como fuente única de datos y `web/build.py` con validación.

## [0.1.0] — 2026-11-20 · Edición de lanzamiento

**Fases completadas**: 1 (investigación), 2 (índice y estructura), 3 (sistema de progresión). Fase 4 iniciada.

### Añadido
- Portada, índice maestro, sistema de etiquetas (✅/🔍/❓/⬜) y de alertas (⚠️/🔒/⏳/⭐).
- Cap. 0: datos confirmados, fuentes y tabla de discrepancias.
- Cap. 1: consejos iniciales, configuración, mecánicas y errores comunes.
- Cap. 2: lista de misiones del Prólogo y los Capítulos 1–5 con protagonista, desbloqueos y alertas.
- Cap. 3: tabla de cadenas secundarias con clasificación, perdibles y orden recomendado.
- Caps. 4–5: primeras ubicaciones especiales y easter eggs descubiertos.
- Cap. 6: trucos conocidos, dinero, combate y conducción.
- Cap. 7: requisitos del 100 %, recompensas de coleccionables y resumen de trofeos.
- Cap. 8: protagonistas y contactos por capítulo.
- Cap. 9: ruta cronológica al 100 % con paradas de guardado.
- Cap. 10: checklist marcable.
- Plantillas de ficha de misión y de ubicación; guía de mantenimiento; `mkdocs.yml`.

### Pendiente
- Fichas detalladas por misión (12 campos).
- Ubicaciones de coleccionables, eventos aleatorios y mapas propios.
- Decisiones y finales (sin documentación fiable aún).
