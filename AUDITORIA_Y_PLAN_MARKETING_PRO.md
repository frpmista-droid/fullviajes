# FULL VIAJES MARKETING PRO — Auditoría y plan de trabajo (proyecto independiente)

**Fecha:** 8 de noviembre de 2026
**Responde a:** sección 19 del prompt maestro (`PROMPT_MAESTRO_MARKETING_PRO.md`), con el alcance definitivo de proyecto **completamente independiente**.
**Alcance de esta auditoría:** solamente este proyecto (repositorio `frpmista-droid/fullviajes` y su Pull Request #2). No se revisó, tocó ni conectó ningún otro sistema de Full Viajes.
**Estado:** no se programó nada, no se tocó producción y el pull request sigue en borrador.

---

## 1. Auditoría del proyecto

### Contenido del repositorio

| Rama | Contenido | Decisión |
|---|---|---|
| `main` | 5 imágenes y un README de 12 bytes. | No hay código. No se toca. |
| `claude/kind-allen-iqdiqx` (PR #2) | Documentos: prompt maestro, esta auditoría y versiones anteriores en `docs/anteriores/`. | Es la especificación del proyecto. |
| `claude/wonderful-hamilton-8qgj9v` | Video de Camboriú. | Fuera del alcance. No se toca. |

**Conclusión:** Marketing Pro **se construye desde cero**. No hay funciones existentes que se puedan romper ni que haya que conservar.

### Pull Request #2

- Solo documentos. Sin conflictos con `main`. Sin controles automáticos (CI).
- Queda en borrador hasta tu aprobación.

### Cambios aplicados al prompt maestro en este paso

- Se agregó el bloque **"Proyecto completamente independiente"** con el alcance definitivo de 10 puntos.
- **Sección 13:** la medición se limita a consultas generadas, sin datos personales, reservas ni ventas.
- **Sección 14 (CRM):** eliminada.
- **Sección 15:** se quitó "CRM" del menú (quedan 12 secciones) y se cambiaron los indicadores de reservas y ventas por aprobadas, rechazadas y consultas por publicación.
- **Sección 16:** almacenamiento propio, separado de otros sistemas.
- **Principio final:** la métrica de éxito pasa a ser **consultas** generadas.

---

## 2. Funcionalidades duplicadas

- **Con otros sistemas:** ninguna, por definición. Marketing Pro no reutiliza ni replica el CRM, las reservas ni los usuarios de otros proyectos.
- **Dentro del prompt maestro** (para no construir lo mismo dos veces):

| Duplicación | Recomendación |
|---|---|
| Secciones "Imágenes" y "Textos" separadas de "Promociones". | Que sean pestañas dentro de cada promoción, porque cada imagen y cada texto pertenecen a una promoción (regla "nunca Mendoza con texto de Brasil"). A confirmar. |
| "Publicaciones" e "Historial". | Una sola tabla de publicaciones; "Historial" es la vista con filtros de fechas y estados. |
| "Grupos excluidos" y la categoría "No recomendado". | Una sola lista de exclusión con el motivo (rechazos, pendientes, reglas, micros/fútbol, manual). |

---

## 3. Limitaciones de las integraciones de Meta

| Acción | ¿Hay vía oficial? | Qué hace Marketing Pro |
|---|---|---|
| Listar los grupos donde está unida la cuenta | **No** | Sesión supervisada con Claude en Chrome (solo lectura) o carga manual. |
| Leer temática, actividad y reglas de un grupo | **No** | Sesión supervisada, de a un grupo (etapas 1 a 4 del maestro). |
| **Publicar en un grupo** | **No** (Meta eliminó `publish_to_groups` en abril de 2024) | **Preparada para intervención manual** (etapa 5 del maestro): cola "publicar en un toque", unos 20 segundos por grupo. |
| Saber si quedó aprobada, pendiente o rechazada | **No** | Marcar con un toque al publicar + ronda semanal de revisión. |
| Abandonar un grupo | **No** | Lista "sugeridos para abandonar"; salís vos con un toque. |
| Detectar advertencias de Meta | **No** | Claude las ve en pantalla durante las sesiones supervisadas; botón "Facebook me mostró una advertencia" que detiene todo. |

**Lo que esto significa:**

- La publicación en grupos nunca va a ser 100 % autónoma de forma autorizada. Con la regla del propio maestro ("publicar únicamente mediante mecanismos autorizados"), queda siempre como intervención manual.
- La autonomía real está en todo lo demás: analizar, clasificar, priorizar, excluir, elegir imagen y texto, evitar duplicados, armar la cola, registrar y medir.
- Meta también restringe la **lectura automatizada**. Las sesiones con Claude en Chrome deben ser supervisadas, de bajo volumen y de a un grupo. Aun así, no hay garantía de que Meta no restrinja la cuenta.

---

## 4. Cómo medir consultas sin CRM

El alcance pide contar consultas generadas sin gestionar clientes. Propuesta:

1. **Enlace de seguimiento propio por grupo y promoción**, por ejemplo `.../w/G045-P12`. Al tocarlo, el sistema suma un clic y redirige a WhatsApp con el mensaje precargado ("Hola Full Viajes, vi su publicación…" + código).
   - Mide **intención de consulta** (clics), de forma automática.
2. **Botón "registrar consulta"**: quien atiende WhatsApp anota solo el código que vino en el mensaje. Sin nombre, sin teléfono, sin datos del cliente.
   - Mide **consultas reales**.
3. Si no hay código: origen **desconocido** (regla de la sección 13).

No se guarda ningún dato personal y no se conecta con ningún otro sistema.

---

## 5. Arquitectura propuesta (independiente)

| Componente | Propuesta |
|---|---|
| Interfaz | Panel web propio "FULL VIAJES MARKETING PRO", usable desde la computadora y el celular. |
| Servidor | Carpeta o subdominio propio (por ejemplo, `marketing.fullviajesyturismo.com`), separado del WordPress y de cualquier otro sistema. |
| Almacenamiento | **Base de datos propia** (MySQL nueva y exclusiva), con usuario propio. No comparte tablas ni credenciales con nada. |
| Usuarios | Propios del proyecto. |
| Tareas programadas | Cron del hosting para armar la cola diaria y recalcular clasificaciones. |
| Claude en Chrome | En tu computadora, en sesiones supervisadas, con un usuario técnico de permisos mínimos en Marketing Pro (lee la cola y registra resultados; no puede reanudar después de una detención por seguridad). |
| Copias de seguridad | Respaldo diario propio de la base de Marketing Pro. |

**Alternativa:** si preferís no usar tu hosting actual, Marketing Pro puede funcionar en otro servidor económico. Lo importante es que tenga su propia base y su propio dominio o carpeta. A decidir.

### Datos que guarda

- **Grupos:** nombre, enlace, localidad, puntaje, tipo, reglas, categoría, motivo de exclusión, historial.
- **Promociones:** destino, fecha, precio, duración, hotel, comidas, servicios, condiciones, vigencia, imágenes, textos, WhatsApp.
- **Campañas:** estado (activa, pausada, finalizada o detenida por seguridad).
- **Publicaciones:** grupo, promoción, imagen y texto usados, fechas, estado. Regla de no duplicar.
- **Consultas:** código, fecha, origen. Sin datos personales.
- **Incidencias de Meta.**
- **Registro de acciones:** quién hizo qué y cuándo.

---

## 6. Copia de seguridad

| Qué | Estado |
|---|---|
| Este repositorio | Versionado en Git; no se borró nada (versiones anteriores en `docs/anteriores/`). |
| Otros sistemas de Full Viajes | **No se tocan.** |
| Hosting | Antes de crear la carpeta y la base de Marketing Pro, copia completa del hosting desde su panel, para que la web actual no se vea afectada. |

---

## 7. Plan de trabajo por módulos

Cada módulo en una rama separada, probado y mostrado antes de seguir. **Nada va a producción sin tu autorización.**

| # | Módulo | Contenido | Cómo se comprueba |
|---|---|---|---|
| 0 | **Preparación** | Elegir dónde se aloja; copia de seguridad del hosting; base de datos y usuario nuevos. | La web actual sigue funcionando igual. |
| 1 | **Base y estructura** | Tablas propias, inicio de sesión, registro de acciones, respaldo diario. | Pruebas automáticas. |
| 2 | **Grupos** | Carga, 5 tipos, prioridad geográfica, exclusiones (micros, fútbol, sin relación), categorías del maestro, lista de exclusión con motivo. | Cargar 20 grupos reales de Concepción del Uruguay y revisar la clasificación con vos. |
| 3 | **Contenido** | Promociones con imágenes y textos asociados, precios y fechas bloqueados, vencimiento automático. | Asociar una imagen a una promoción equivocada debe ser imposible. |
| 4 | **Campañas** | Activar, pausar, reanudar, finalizar y "detenido por seguridad"; cola diaria grupo por grupo con prioridad, frecuencia y control de duplicados; alternancia de creatividades. | Simulación de 2 semanas con datos de prueba. |
| 5 | **Cola "publicar en un toque"** | Pantalla para el celular con texto, imagen, enlace al grupo y botones de resultado; depuración automática según los parámetros del maestro. | Prueba real con 3 a 5 grupos. |
| 6 | **Consultas y estadísticas** | Enlaces de seguimiento, registro de consultas por código, dashboard con los indicadores del maestro. | Una consulta de prueba de punta a punta. |
| 7 | **Sesiones supervisadas con Claude en Chrome** | Guía de trabajo grupo por grupo (etapas 1 a 7) conectada a Marketing Pro; freno ante advertencias. | Sesión real supervisada con 5 grupos. |

**Quedan fuera del alcance:** CRM, reservas, ventas, conexión con cualquier otro sistema, Página de Facebook, Instagram y anuncios pagos.

---

## 8. Decisiones pendientes

1. **Toque manual en grupos:** ¿aceptás que publicar en grupos quede como intervención manual (unos 20 segundos por grupo), que es lo que exige el propio maestro al no haber una vía autorizada?
2. **Dónde se aloja:** ¿carpeta o subdominio propio en tu hosting actual, con base de datos nueva y exclusiva, u otro servidor?
3. **Quién publica:** ¿solo vos, o también personas del equipo desde sus cuentas?
4. **Abandono de grupos:** ¿deshabilitado y con un toque tuyo, como se recomienda?
5. **Medición de consultas:** ¿te sirve la propuesta del punto 4 (clics automáticos + registro del código, sin datos personales)?
6. **Ajustes técnicos dentro del alcance:** ¿sumamos estos detalles de la versión anterior?
   - Concepción del Uruguay primero dentro de la prioridad máxima.
   - Una publicación por grupo por semana como máximo.
   - Exclusión por palabra completa (para no descartar "microondas").
   - Textos por localidad sin prometer salidas no confirmadas.
