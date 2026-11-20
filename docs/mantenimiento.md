# Cómo mantener la guía viva

[← Índice](index.md)

## Estructura del repositorio

```
guia-gta-vi/
├── README.md              ← portada, índice maestro, etiquetas y alertas
├── CHANGELOG.md           ← registro de cambios por versión
├── mkdocs.yml             ← configuración para publicarla como web
├── docs/
│   ├── 00-metodologia-y-fuentes.md
│   ├── 01 … 10            ← los 10 capítulos
│   ├── mantenimiento.md
│   ├── misiones/          ← (futuro) una ficha por misión
│   └── coleccionables/    ← (futuro) ubicaciones por región
├── plantillas/            ← fichas reutilizables
└── assets/mapas/          ← (futuro) capturas y mapas propios
```

## Flujo de actualización

1. **Encuentra un dato** (partida propia, parche oficial, guía especializada).
2. **Etiquétalo**: ✅ / 🔍 / ❓ según los criterios del [Cap. 0](00-metodologia-y-fuentes.md).
3. **Edita el capítulo** o crea la ficha con la plantilla.
4. Si cambia una alerta ⏳, **actualiza también** el README, el [Cap. 3](03-misiones-secundarias.md), la [ruta](09-ruta-100.md) y el [checklist](10-checklist.md).
5. Anota el cambio en el `CHANGELOG.md` y sube la versión (0.1.0 → 0.2.0 para contenido nuevo; 0.1.1 para correcciones).
6. Haz commit con un mensaje claro: `misiones: ficha de Gone Fishing`.

## Prioridades para las próximas entregas

1. Fichas completas de las misiones del Capítulo 1 (las más consultadas).
2. Resolver discrepancias del [Cap. 0](00-metodologia-y-fuentes.md).
3. Lista completa de los ~35 requisitos del 100 % y de los 55 trofeos.
4. Ubicaciones de coleccionables por región, con capturas propias.
5. Confirmar qué cadenas cuentan para *Strangers & Freaks*.
6. Revisar tras cada parche oficial de Rockstar.

## Actualizar la guía interactiva (`web/`)

| Archivo | Para qué |
|---|---|
| `web/data/guia.json` | **Todos los datos**: misiones, perdibles, puntos sin retorno, secretos y requisitos del 100 % |
| `web/src/template.html` | Diseño y lógica (normalmente no hace falta tocarlo) |
| `web/build.py` | Valida los datos y genera `web/index.html` |
| `web/index.html` | Resultado final, autocontenido. **No lo edites a mano** |

**Campos de una misión**: `n` nombre · `w` protagonista (`J`, `L`, `JL`, `S`) · `t` tipo (`P` principal, `O` opcional, `T` tarea) · `note` · `unlock` · `reward` · `rec: true` recomendada · `missable` texto del aviso · `hourglass: true` tiempo limitado · `after` ID tras el que aparece · `noreturn` texto del punto sin retorno · `id` (opcional).

**Traducción**: `es` = nombre en castellano. La web lo muestra como nombre principal y debajo el original (`n`), que es como aparece en el juego. Si se confirma el nombre oficial de la versión española del juego, sustituye el valor de `es` por el oficial.

**Mapa** (`map.regions`, `secrets`, `sideChains`):
- Cada región tiene `id`, `name`, `sub`, centro `x`/`y` y tamaño `rx`/`ry` en un lienzo de 1000 × 1000 (norte arriba). `labelDy` y `markerDy` ajustan dónde van el texto y los marcadores.
- Un secreto o una cadena secundaria aparece en el mapa si tiene `area` (id de región: se coloca de forma aproximada en esa región) o `pos: [x, y]` (posición exacta en el esquema).
- `region` es solo el texto de ubicación que lee el jugador.
- Lo que no tiene `area` ni `pos` aparece en «Aún sin situar en el mapa».

**Misiones ocultas** (`hidden`): `ch` capítulo · `id` · `n` original · `es` castellano · `who` · `how` cómo activarla · `where` · `when` · `reward` · `kind` (`flyer`, `hidden`, `encounter`, `phone`) · `s` estado · `src` fuente · `area` región del mapa (opcional) · `lostAfter` ID de la misión tras la que se pierde (opcional).

**Puntos de control** (`gates`): `before` = ID de la misión sin retorno; `requires` = IDs que deben estar hechos (lanza el ALTO); `recommended` y `tips` = consejos.

⚠️ **No cambies el `id` de una misión ya publicada**: el progreso de los jugadores se guarda por ID. Si renombras una misión sin `id` explícito, añádele `"id"` con el valor antiguo.

```bash
python3 web/build.py   # valida y genera web/index.html; avisa de IDs rotos o duplicados
```

## Publicar como web

```bash
pip install mkdocs-material
mkdocs serve      # vista previa en http://127.0.0.1:8000
mkdocs build      # genera la web estática en site/
```

- **Publicación automática**: cada cambio en `main` ejecuta `.github/workflows/web.yml`, que valida los datos, genera la guía interactiva (raíz del sitio) y la guía en texto (`/guia/`) y las publica en GitHub Pages.
- Los pull requests pasan la misma validación sin publicar nada.

## Exportar a PDF

```bash
pandoc README.md docs/0*.md docs/10-checklist.md -o guia-gta-vi.pdf --toc
```

## Imágenes y copyright

- Usa **capturas propias** del juego. No copies mapas ni imágenes de otras guías.
- Las fuentes se citan por nombre; los datos se redactan con palabras propias.
