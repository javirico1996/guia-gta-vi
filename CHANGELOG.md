# Registro de cambios

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
