# Cómo colaborar en la Guía Definitiva de GTA VI

¡Gracias por querer mejorar la guía! El objetivo es que **ningún jugador se pierda misiones, secretos o contenido perdible**, así que cada aporte cuenta.

## 🥇 La regla de oro: nada inventado

Cada dato nuevo necesita **una fuente**: tu propia partida (mejor con captura), un post oficial de Rockstar o una guía especializada. Si no estás seguro, márcalo como **No confirmado** y lo verificaremos entre todos.

| Etiqueta | Cuándo usarla |
|---|---|
| ✅ Confirmado (`C`) | Rockstar lo dice o lo han comprobado varias fuentes independientes |
| 🔍 Descubierto (`D`) | Lo has comprobado tú en partida o lo publica una guía especializada |
| ❓ No confirmado (`N`) | Rumor, teoría o dato que aún nadie ha podido repetir |

⏳ **Solo se marca algo como perdible si está demostrado.** Indica en qué momento exacto deja de estar disponible.

## 🗣️ Opción fácil: abrir un issue (no hace falta saber programar)

Ve a la pestaña **Issues → New issue** y elige una plantilla:
- **🐛 Corrección**: algo está mal o desactualizado.
- **⏳ Contenido perdible**: has descubierto algo que se pierde al avanzar.
- **🗺️ Secreto o easter egg**: ubicación nueva.
- **📝 Dato nuevo**: misión, recompensa, coleccionable, truco…

Rellena los campos y alguien lo incorporará.

## 🛠️ Opción completa: proponer el cambio tú mismo (pull request)

1. Haz un **fork** del repositorio y crea una rama: `git checkout -b ficha-gone-fishing`.
2. Edita lo que corresponda:
   - **Guía en texto**: `docs/*.md` (usa las [plantillas](plantillas/)).
   - **Guía interactiva**: `web/data/guia.json` (formato explicado en [docs/mantenimiento.md](docs/mantenimiento.md)).
3. Si tocas el JSON, ejecuta `python3 web/build.py`: valida los datos y regenera `web/index.html`.
4. Añade tu cambio en [`CHANGELOG.md`](CHANGELOG.md) dentro de una sección «Sin publicar».
5. Abre el **pull request** rellenando la plantilla (incluye siempre la fuente).

Cada pull request pasa una **comprobación automática** que valida el JSON y que la web se genera bien.

### ⚠️ Importante en `guia.json`
- **No cambies el `id` de una misión existente**: el progreso de los jugadores se guarda por ID.
- Si añades un perdible, añade también su punto de control en `gates` cuando haya un punto sin retorno claro.

## 🗺️ Ayuda con el mapa y las traducciones

- **Situar un secreto**: si sabes en qué región está, añade `"area"`; si quieres afinar el punto, añade `"pos": [x, y]` (lienzo de 1000 × 1000, norte arriba) y explica en el pull request cómo lo has calculado.
- **Nombres oficiales en castellano**: si juegas con el juego en español y la misión aparece con otro nombre, abre un issue de «Corrección» con una captura y lo cambiamos por el oficial.

## ✍️ Estilo

- Español claro y cercano, tuteando al jugador.
- Nombres de misiones en su idioma original del juego (en cursiva en los `.md`).
- Marca los spoilers importantes con 🔴 **SPOILER**.
- Redacta con tus palabras: **no copies** textos, tablas ni imágenes de otras guías. Cítalas por nombre.
- Imágenes: solo **capturas propias**, en `assets/`.

## 🤝 Convivencia

Sé amable, asume buena fe y discute datos, no personas. Los aportes que inventen información o copien contenido de terceros se rechazarán.

## 📜 Licencia de tus aportes

Al contribuir aceptas que tu aporte se publique bajo las licencias del proyecto (ver [LICENSE.md](LICENSE.md)).
