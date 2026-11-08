# Análisis de viabilidad — Herramienta de captación en grupos de Facebook

**Fecha:** 8 de noviembre de 2026
**Estado:** solo análisis. No se implementó nada, no se tocó producción y el pull request sigue en borrador.

---

## 1. Qué hay hoy

### En este repositorio (`frpmista-droid/fullviajes`)

| Rama | Contenido |
|---|---|
| `main` | 5 imágenes y un README. **No hay código ni sistema.** |
| `claude/kind-allen-iqdiqx` (este PR) | Los documentos del prompt y este análisis. |
| `claude/wonderful-hamilton-8qgj9v` | Proyecto de video de Camboriú (no tiene relación con este tema). |

**Conclusión:** el repositorio actual no permite implementar ninguna de las funciones, porque no hay una aplicación. Tampoco hay nada que se pueda romper.

### FULL VIAJES 360 (en desarrollo en otra sesión)

Hay otra sesión de Claude Code trabajando en **FULL VIAJES 360**, el sistema de gestión de la agencia. Según lo que se ve en esa sesión:

- **26 pantallas** (CRM, clientes, viajes, vendedoras, etc.).
- Se está adaptando para el hosting de **Ferozo** en `fullviajesyturismo.com/app/`:
  - interfaz en archivos estáticos;
  - API en **PHP 8.4**;
  - base de datos **MySQL**;
  - sin procesos permanentes (hosting compartido).
- Convive con el WordPress del sitio, en una carpeta separada.
- **Ese código todavía no está subido a GitHub**, así que no se pudo revisar en detalle.

**Esta es la base correcta para la herramienta de grupos:** ya tiene usuarios, base de datos, CRM y registro de viajes y ventas. La herramienta de grupos debería ser un **módulo nuevo de FULL VIAJES 360**, no un sistema aparte.

---

## 2. Viabilidad de cada requisito

| # | Requisito | ¿Se puede? | Cómo |
|---|---|---|---|
| 1 | Historial permanente | **Sí** | Tablas nuevas en la base MySQL de FULL VIAJES 360. No depende de Chrome. Se suma a las copias de seguridad que ya prevé ese sistema. |
| 2 | Lista negra | **Sí** | Campo de estado en la ficha del grupo, con motivo y fecha. La clasificación del módulo 16 se calcula en el servidor. Solamente un administrador puede sacar un grupo de la lista. |
| 3 | Consultas y ventas por grupo | **Sí, con una condición** | Enlace de WhatsApp con código por grupo (`G-045`). Al cargar la consulta en el CRM se elige o se detecta el grupo de origen. La venta se vincula a la reserva que ya existe en FULL VIAJES 360. **Condición:** alguien tiene que cargar el código en el CRM cuando llega la consulta; WhatsApp no lo informa solo. |
| 4 | Control de duplicados | **Sí** | Restricción en la base: una promoción no puede tener dos publicaciones activas o pendientes en el mismo grupo. Comparación de textos para detectar casi duplicados. |
| 5 | Dashboard | **Sí** | Pantallas nuevas dentro del panel de FULL VIAJES 360, con el mismo inicio de sesión y permisos. |
| 6 | Pausar y reanudar | **Sí** | Un estado global (activo / pausado / detenido por seguridad) guardado en la base. Claude lo consulta antes de cada paso. |
| 7 | Nada sin autorización | **Sí** | Cola de aprobación en el dashboard. Además, el clic final en "Publicar" lo hacés vos en Chrome. |
| 8 | Freno ante advertencias | **Parcial** | El freno en el sistema (estado "detenido por seguridad") **sí** se puede hacer. Lo que **no** se puede automatizar es *detectar* la advertencia desde el servidor: Facebook no avisa a sistemas externos. La detecta Claude al ver la pantalla mientras trabaja con vos, o la cargás vos. |

---

## 3. Límites reales que conviene saber antes de aprobar

1. **Facebook no ofrece una forma oficial de publicar en grupos.** Meta dio de baja en 2024 la API que permitía publicar en grupos desde otras aplicaciones. Por eso:
   - el servidor **no puede** publicar ni leer los grupos;
   - la parte de Facebook la hace Claude en tu Chrome, mirando la pantalla, en sesiones supervisadas;
   - el clic final lo das vos.
2. **El estado de las publicaciones (pendiente, aprobada, rechazada) no se actualiza solo.** Hay que entrar al grupo para verlo. Se puede hacer en una "ronda de revisión" semanal con Claude en Chrome, que actualiza el registro.
3. **Claude no trabaja las 24 horas.** Funciona cuando abrís una sesión en tu computadora con la app de escritorio (Computer use activado) o con Claude en Chrome. El hosting de Ferozo no puede manejar un navegador.
4. **Incluso con supervisión, Meta puede restringir la cuenta** si considera que hay automatización o demasiadas publicaciones comerciales. Los límites conservadores y la aprobación manual reducen el riesgo, pero no lo eliminan.
5. **La atribución de ventas depende de la carga en el CRM.** Si una consulta llega sin código y nadie registra de qué grupo vino, esa venta no se le atribuye a ningún grupo.

---

## 4. Arquitectura propuesta

```
┌──────────────────────────────┐        ┌─────────────────────────────────┐
│  Tu PC (Chrome con tu sesión │        │  fullviajesyturismo.com/app/    │
│  de Facebook)                │        │  FULL VIAJES 360 (PHP + MySQL)  │
│                              │        │                                 │
│  Claude (Computer use /      │◀──────▶│  Módulo "Grupos de Facebook":   │
│  Claude en Chrome)           │  API   │   · grupos y lista negra        │
│   · lee reglas               │ segura │   · promociones y vigencia      │
│   · prepara la publicación   │        │   · cola de aprobación          │
│   · vos hacés clic final     │        │   · historial de publicaciones  │
│   · registra el resultado    │        │   · consultas → CRM → reservas  │
│   · frena ante advertencias  │        │   · estado: activo/pausado/     │
│                              │        │     detenido por seguridad      │
└──────────────────────────────┘        │   · dashboard y reportes        │
                                        └─────────────────────────────────┘
```

### Tablas nuevas (borrador)

- `fb_grupos`: ficha del grupo, reglas resumidas, categoría, lista negra, motivo.
- `fb_promociones`: o se reutilizan los viajes/paquetes que ya existen en FULL VIAJES 360, sumando imagen, texto base y vigencia.
- `fb_publicaciones`: grupo, promoción, texto, imagen, aprobación (usuario y fecha), estado, fechas de revisión. Índice único para el control de duplicados.
- `fb_consultas`: vínculo con el CRM existente (grupo de origen, código, promoción).
- `fb_incidencias`: advertencias de Facebook, con captura y resolución.
- `fb_estado_sistema`: activo / pausado / detenido por seguridad, con historial de cambios.
- `fb_reglas_clasificacion`: umbrales del módulo 16, editables.

### Acceso de Claude al sistema

- Un usuario técnico con **permisos mínimos** (leer el estado, leer la cola aprobada, registrar resultados e incidencias).
- **Sin** permiso para aprobar publicaciones, sacar grupos de la lista negra ni reanudar después de una detención por seguridad: eso queda solamente para tu usuario.

---

## 5. Plan sugerido por etapas

| Etapa | Qué incluye | Requiere |
|---|---|---|
| **0. Revisión** | Revisás este documento y el prompt, y corregís los módulos 1 a 14. | Tu revisión. |
| **1. Base** | FULL VIAJES 360 instalado y funcionando en Ferozo (lo está haciendo la otra sesión). | Terminar esa instalación. |
| **2. Datos** | Tablas nuevas, carga inicial de grupos y promociones, lista negra, control de duplicados. | Etapa 1. |
| **3. Dashboard** | Pantallas de grupos, promociones, cola de aprobación, estado y pausa. | Etapa 2. |
| **4. Claude en Chrome** | Flujo supervisado del módulo 19 conectado a la API, con freno de seguridad. Prueba con 3 a 5 grupos. | Etapa 3 y Computer use o Claude en Chrome en tu PC. |
| **5. Medición** | Códigos de WhatsApp por grupo, vínculo consulta → reserva, reportes de rentabilidad. | Etapa 4 y uso del CRM. |

Cada etapa se prueba aparte, en una rama separada, sin tocar el WordPress ni la instalación en producción hasta tu aprobación.

---

## 6. Qué necesito de vos para avanzar

1. Revisar los módulos 1 a 14 reconstruidos y corregir lo que no coincida con el original (o pasarme el original si lo encontrás).
2. Confirmar que la herramienta va como **módulo de FULL VIAJES 360**.
3. Que el código de FULL VIAJES 360 se suba a GitHub (lo maneja la otra sesión), para poder revisar sus tablas y su API antes de diseñar el módulo.
4. Una lista inicial de grupos (aunque sea parcial) y las promociones vigentes.
