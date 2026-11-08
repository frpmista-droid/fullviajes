# FULL VIAJES MARKETING PRO — Auditoría previa y plan de trabajo

**Fecha:** 8 de noviembre de 2026
**Responde a:** sección 19 del prompt maestro (`PROMPT_MAESTRO_MARKETING_PRO.md`).
**Estado:** no se programó nada, no se tocó producción y el pull request sigue en borrador.

---

## 1. Auditoría del proyecto actual

### Repositorio `frpmista-droid/fullviajes`

| Rama | Contenido | Relación con Marketing Pro |
|---|---|---|
| `main` (producción del repositorio) | 5 imágenes de Instagram y un README de 12 bytes. | Ninguna. **No hay código ni sistema.** |
| `claude/kind-allen-iqdiqx` (PR #2) | Solo documentos: el prompt maestro, este plan y las versiones anteriores en `docs/anteriores/`. | Es la especificación. |
| `claude/wonderful-hamilton-8qgj9v` | Proyecto de video de Año Nuevo en Camboriú. | Ninguna. No se toca. |

### FULL VIAJES 360 (otra sesión de trabajo)

- Sistema de gestión de la agencia con **26 pantallas**: CRM, clientes, viajes, vendedoras y más.
- Se está adaptando para el hosting de **Ferozo** en `fullviajesyturismo.com/app/`:
  - interfaz en archivos estáticos;
  - API en **PHP 8.4**;
  - base de datos **MySQL**;
  - sin procesos permanentes.
- Convive con el **WordPress** del sitio principal.
- **Su código no está en GitHub.** No se pudo auditar en detalle: lo que figura acá sale de lo visible en esa sesión.

### Producción real

- `fullviajesyturismo.com` (WordPress) y la cuenta de Ferozo **no fueron tocados** en ninguna etapa.

---

## 2. Revisión del Pull Request #2

- Solo agrega documentos (Markdown). No modifica ni borra nada existente.
- Sin conflictos con `main`. El repositorio no tiene controles automáticos (CI).
- **Si se mezclara, no rompería nada**, porque no hay código. Igual queda en borrador hasta tu aprobación, como pediste.
- Reorganización hecha en este paso:
  - `PROMPT_MAESTRO_MARKETING_PRO.md` → documento definitivo (tu texto, sin cambios de contenido).
  - Documentos anteriores → `docs/anteriores/` (se conservan como historial, no se borró nada).

---

## 3. Comparación con `PROMPT_GRUPOS_FACEBOOK.md` (versión anterior)

### 3.1 Lo que el prompt maestro mejora

- Proceso **grupo por grupo** en 7 etapas, bien definido.
- Categoría nueva **APTO**, entre "prioritario" y "en observación".
- **CRM** con estados claros.
- Las 13 secciones del dashboard.
- Regla clave: **no inventar atribuciones** (origen "desconocido").
- Asociación imagen ↔ promoción (nunca Mendoza con texto de Brasil).
- Enfoques de redacción (informativo, emocional, familiar, etc.).

### 3.2 Detalles que quedaron afuera y conviene recuperar

Propongo sumarlos como **anexo técnico** del prompt maestro, sin cambiar tu texto:

| # | Detalle de la versión anterior | Por qué importa |
|---|---|---|
| 1 | **Concepción del Uruguay primero dentro de la prioridad máxima** (puntaje 100 contra 90 de Colón, Gualeguaychú y Concordia). | En el maestro, Concepción del Uruguay comparte nivel con 5 ciudades. Tu estrategia es "primero dominar Concepción del Uruguay". |
| 2 | **Puntaje final**: geografía + actividad + reglas + tipo + tamaño + resultados, con más peso de los resultados cuando hay historial. | El maestro dice que el sistema "aprenda de los resultados", pero no cómo combinarlos con la geografía. |
| 3 | **"Salidas confirmadas desde"**: no decir "salida desde Colón" si no está confirmada. | Evita prometer algo falso en textos por localidad. |
| 4 | **Textos por localidad** ("¡Desde La Histórica…!"). | Es una de las mejores herramientas comerciales que habías definido. |
| 5 | **Control de duplicados explícito**: la misma promoción no se publica dos veces en el mismo grupo (ni si está pendiente). | El maestro dice "evitar repetir"; conviene que sea una regla dura de la base de datos. |
| 6 | **Exclusión por palabra completa** y "revisar" en lugar de excluir para compra y venta. | Evita descartar por error un grupo de compra y venta donde venden "microondas". |
| 7 | **Estado "detenido por seguridad"**, distinto de "pausado", que solo se levanta con tu revisión. | El maestro dice "detener y esperar la resolución"; el estado lo hace verificable. |
| 8 | **Frecuencia máxima**: una publicación por grupo por semana, salvo reglas del grupo. | El maestro dice "no saturar", pero sin un número. |
| 9 | **Unirse a grupos de a pocos por día**, decidido por vos. | Sumarse a muchos grupos de golpe es de lo que más rápido genera restricciones. |
| 10 | **Canales oficiales** (Página de Facebook, Instagram, anuncios, web). | Son los únicos donde la publicación puede ser 100 % autónoma (ver punto 5). |

### 3.3 Diferencias de criterio que hay que decidir

- **Abandono automático de grupos (sección 7).** El maestro lo permite si está habilitado. No hay forma oficial de abandonar un grupo desde un sistema, así que solo podría hacerse manejando Chrome. **Recomendación:** opción deshabilitada por defecto, y abandono con un toque tuyo desde una lista "sugeridos para abandonar".
- **Zonas.** El maestro movió Gualeguay a complementaria y Liebig a alta (antes estaba al revés). Se toma el maestro como válido.

---

## 4. Funcionalidades duplicadas

| Función del prompt maestro | Ya existe en FULL VIAJES 360 | Decisión recomendada |
|---|---|---|
| **CRM comercial** (sección 14) | Sí: módulo CRM y clientes. | **No crear un segundo CRM.** Usar el existente y agregarle el origen (grupo, campaña, canal) y los estados que falten. |
| Reservas y ventas | Sí: viajes y reservas. | Vincular, no duplicar. Las ventas por grupo salen de las reservas reales. |
| Promociones (sección 8) | Parcial: los viajes ya tienen destino, fechas y precio. | La promoción **apunta a un viaje** existente y suma imágenes, textos, WhatsApp y vigencia. Así precios y fechas no se cargan dos veces ni se desincronizan. |
| Usuarios y permisos | Sí. | Reutilizar el mismo inicio de sesión. |
| Copias de seguridad | Previstas en FULL VIAJES 360. | Incluir las tablas nuevas en ese mismo respaldo. |
| Dashboard (sección 15) | El panel existe. | Las 13 secciones se agregan como un menú "Marketing Pro" dentro del panel. **Imágenes** y **Textos** pueden ir dentro de **Promociones** para evitar pantallas repetidas (a confirmar). |

**Conclusión:** Marketing Pro se construye como **módulo de FULL VIAJES 360**. Hacerlo aparte duplicaría CRM, reservas, usuarios y promociones.

---

## 5. Limitaciones de las integraciones de Meta

| Acción | ¿Hay vía oficial? | Qué hace el sistema |
|---|---|---|
| Listar los grupos donde participa la cuenta | **No** | Lectura en sesión supervisada con Claude en Chrome, o carga manual. |
| Leer reglas, actividad y publicaciones de un grupo | **No** | Igual: sesión supervisada, de a un grupo, solo lectura. |
| **Publicar en un grupo** | **No** (Meta eliminó `publish_to_groups` en abril de 2024) | **Siempre "preparada para intervención manual"** (etapa 5 del maestro): cola "publicar en un toque", unos 20 segundos por grupo. |
| Saber si quedó pendiente, aprobada o rechazada | **No** | Marcado con un toque al publicar y ronda semanal de revisión. |
| Unirse a un grupo o abandonarlo | **No** | Lo hacés vos; el sistema sugiere. |
| Detectar advertencias de Facebook | **No** para grupos | Claude las ve en pantalla en las sesiones supervisadas; botón "Facebook me mostró una advertencia" en la cola. |
| Publicar en la **Página** de Full Viajes | **Sí** (`pages_manage_posts`) | 100 % autónomo. |
| Publicar en **Instagram** profesional | **Sí** (`instagram_content_publish`) | 100 % autónomo. |
| **Anuncios pagos** | **Sí** (API de Marketing) | Autónomo, con presupuesto máximo. |

**Un riesgo que hay que tener presente:** las condiciones de Meta también restringen la **lectura automatizada** de Facebook (no solo la publicación). Por eso la lectura de grupos con Claude en Chrome tiene que ser en sesiones supervisadas, de bajo volumen y un grupo por vez, como pide el maestro. Ni así se puede garantizar que Meta no restrinja la cuenta. Es el mismo motivo por el que el maestro prioriza la seguridad.

**Qué significa en la práctica:** con las reglas del propio prompt maestro ("publicar únicamente mediante mecanismos autorizados"), **toda publicación en grupos queda como intervención manual**. La autonomía real está en todo lo demás: análisis, selección, armado, registro, medición y los canales oficiales.

---

## 6. Copia de seguridad

| Qué | Estado |
|---|---|
| Este repositorio | Todo está versionado en Git: cada estado anterior se puede recuperar. No se borró ningún archivo (las versiones anteriores están en `docs/anteriores/`). |
| WordPress y hosting de Ferozo | No se tocaron. **Antes de instalar cualquier cosa en el hosting**, hay que hacer una copia completa (archivos + base de WordPress) desde el panel de Ferozo. Es el paso 0 de la implementación. |
| Base de FULL VIAJES 360 | Antes de agregar tablas, respaldo completo con la herramienta de copias de ese sistema y prueba de restauración. |

---

## 7. Plan de trabajo por módulos

Cada módulo se desarrolla en una rama separada, se prueba con datos de ejemplo y se muestra antes de pasar al siguiente. **Nada va a producción sin tu autorización.**

| # | Módulo | Contenido | Cómo se comprueba | Depende de |
|---|---|---|---|---|
| 0 | **Preparación** | Copias de seguridad del hosting y de FULL VIAJES 360; código de FULL VIAJES 360 en GitHub. | Restauración de prueba. | Otra sesión y vos. |
| 1 | **Base de datos** | Tablas de grupos, localidades y puntajes, promociones (vinculadas a viajes), imágenes, textos, campañas, publicaciones, incidencias, estado del sistema. Regla de duplicados en la base. | Pruebas automáticas sobre una copia de la base. | 0 |
| 2 | **Grupos** | Carga (manual o desde una sesión supervisada), clasificación de 5 categorías, puntaje geográfico, exclusiones por palabra completa, lista de excluidos con motivo. | Cargar 20 grupos reales de Concepción del Uruguay y revisar la clasificación con vos. | 1 |
| 3 | **Promociones y creatividades** | Ficha vinculada al viaje, imágenes y textos asociados, bloqueo de precios y fechas, vigencia automática. | Intentar asociar una imagen a la promoción equivocada debe fallar. | 1 |
| 4 | **Campañas** | Activar, pausar, reanudar, finalizar, "detenido por seguridad"; armado de la cola diaria respetando prioridad, frecuencia y duplicados. | Simulación de una campaña de 2 semanas con datos de prueba. | 2 y 3 |
| 5 | **Cola "publicar en un toque"** | Pantalla para el celular: copiar texto, guardar imagen, abrir grupo, marcar resultado. Reparto entre vendedoras (si lo aprobás). | Prueba real con 3 a 5 grupos de Concepción del Uruguay. | 4 |
| 6 | **Consultas y CRM** | Enlaces de WhatsApp con código por grupo, origen en el CRM existente, origen "desconocido" cuando no se sabe, vínculo con reservas. | Una consulta de prueba de punta a punta hasta una reserva. | 5 |
| 7 | **Dashboard y estadísticas** | Las 13 secciones e indicadores, ranking de grupos por pasajeros, mapa de cobertura por localidad. | Revisión con vos. | 6 |
| 8 | **Sesiones supervisadas con Claude en Chrome** | Guía de trabajo grupo por grupo (etapas 1 a 4 y 6), conectada a la API con un usuario de permisos mínimos; freno ante advertencias. | Sesión real supervisada con 5 grupos. | 2 y 7 |
| 9 | **Canales oficiales (opcional)** | Página de Facebook, Instagram y web automáticos; anuncios con presupuesto máximo. | Publicación de prueba en la Página. | 4 y tu aprobación |

**Orden de valor:** con los módulos 1 a 6 ya se sabe **qué grupos traen pasajeros**, que es la métrica de éxito del prompt maestro.

---

## 8. Decisiones pendientes

1. **Toque manual en grupos:** ¿aceptás que publicar en grupos quede como intervención manual (unos 20 segundos por grupo), que es lo que exige el propio prompt maestro al no haber una vía autorizada?
2. **Vendedoras:** ¿se puede repartir la cola entre ellas?
3. **Canales oficiales:** ¿sumamos Página de Facebook, Instagram y web automáticos? ¿Anuncios pagos? ¿Con qué presupuesto máximo por día?
4. **Abandono de grupos:** ¿lo dejamos deshabilitado y con un toque tuyo, como se recomienda?
5. **Anexo técnico:** ¿agrego los 10 detalles del punto 3.2 como anexo del prompt maestro?
6. **Módulo de FULL VIAJES 360:** ¿confirmás que se construye ahí, reutilizando CRM, viajes y usuarios?
7. **Código de FULL VIAJES 360:** hace falta subirlo a GitHub para auditarlo antes de empezar el módulo 1.
