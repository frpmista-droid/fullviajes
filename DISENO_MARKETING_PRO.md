# FULL VIAJES MARKETING PRO — Análisis y diseño de la Campaña automática

**Fecha:** 8 de noviembre de 2026
**Estado:** análisis y diseño. No hay código, no se tocó producción y el pull request sigue en borrador.

---

## 1. Resumen en una frase

Se puede automatizar **casi todo el trabajo**: armar la campaña, elegir grupos, combinar imágenes y textos, evitar duplicados, publicar en los canales oficiales, medir consultas y ventas, y frenar ante problemas. Lo único que **no se puede automatizar de forma autorizada** es el acto de publicar dentro de un grupo de Facebook. Ese paso queda como un **"publicar en un toque"** que lleva unos 20 segundos por grupo y que puede hacer cualquier persona del equipo.

---

## 2. El dato que define todo: Facebook y los grupos

- Hasta abril de 2024, Meta permitía que una aplicación publicara en grupos (permiso `publish_to_groups`).
- **Meta eliminó esa función.** Hoy no existe ninguna forma oficial de que un sistema externo publique en un grupo de Facebook, ni de leer sus reglas, ni de saber si una publicación quedó pendiente o aprobada.
- Cualquier herramienta que hoy "publique sola en grupos" lo hace manejando un navegador como si fuera una persona. Eso va contra las condiciones de Meta y es justamente lo que provoca restricciones y bloqueos de cuentas.

**Consecuencia:** en los grupos, el sistema hace todo el trabajo previo y posterior, pero el clic de publicar lo da una persona. No hay manera legítima de evitarlo.

---

## 3. Qué se puede automatizar y qué no

### 3.1 Automatizable al 100 % (sin intervención)

| Función | Cómo |
|---|---|
| Cargar la campaña una sola vez | Sección CAMPAÑA AUTOMÁTICA: imágenes, textos, viaje, enlace de WhatsApp, exclusiones. |
| Excluir grupos de micros y fútbol | Filtro por palabras clave en el nombre y la descripción ("micro", "colectivo", "pasajes de micro", "fútbol", "hinchas", nombres de clubes, etc.), editable. Además de la lista de exclusión manual. |
| Clasificar grupos aptos para turismo | Puntaje por tipo de grupo (compra y venta, barrial, viajes, jubilados), ciudad, cantidad de miembros, resultados anteriores. |
| Interpretar las reglas | Claude lee el texto de las reglas (una vez por grupo, y cada 30 días) y decide: permite / permite con condiciones / prohíbe. |
| Elegir imagen y texto para cada grupo | Según el público del grupo y lo que ya se publicó ahí. |
| Alternar creatividades | Rotación para no mostrarle siempre la misma pieza a los mismos miembros. **Precios, fechas y condiciones quedan bloqueados:** salen siempre de la ficha del viaje y no se pueden alterar. |
| Evitar duplicados | La base no permite dos publicaciones activas o pendientes de la misma promoción en el mismo grupo. |
| No insistir donde rechazan | Lista negra comercial automática (reglas del módulo 16). |
| Planificar el calendario | Respeta días permitidos y frecuencia máxima por grupo; reparte la carga en el día. |
| Publicar en la **Página de Facebook** de Full Viajes | API oficial de Meta (`pages_manage_posts`). |
| Publicar en **Instagram** (cuenta profesional) | API oficial de Meta (`instagram_content_publish`). |
| **Anuncios pagos** en Facebook e Instagram | API de Marketing de Meta, con presupuesto diario máximo que fijás vos. Es el canal más escalable y totalmente autorizado. |
| Publicar la promo en la **web** (WordPress) | API de WordPress. |
| Atribuir consultas | Enlace de WhatsApp con código distinto por grupo y por canal. |
| Estadísticas de consultas y ventas | Vinculando el código con el CRM y las reservas de FULL VIAJES 360. |
| Pausar y reanudar | Interruptor general y por campaña. |
| Reportes | Semanales, automáticos. |

### 3.2 Requiere un toque humano (no hay vía autorizada)

| Función | Por qué | Cómo se reduce al mínimo |
|---|---|---|
| Publicar en un grupo | Meta eliminó la publicación por API. | **Cola "publicar en un toque"** (ver punto 4). |
| Saber si quedó pendiente, aprobada o rechazada | Facebook no lo informa a sistemas externos. | Un botón por publicación: "Publicada / Quedó pendiente / Rechazada". Una ronda semanal para actualizar las pendientes. |
| Obtener la lista de grupos donde estás y sus reglas | No hay API. | Carga inicial única: pegar la lista o hacer una sesión de lectura supervisada con Claude en Chrome. Después se mantiene sola con los resultados. |
| Detectar advertencias de Facebook | Facebook no avisa a sistemas externos. | Botón rojo "Facebook me mostró una advertencia" en la cola: detiene todo al instante. Los canales por API (Página, Instagram, anuncios) sí detectan los errores solos. |
| Responder consultas | Es una conversación comercial. | Claude prepara respuestas sugeridas; las envía la vendedora. |

### 3.3 Lo que el sistema no va a hacer

- Manejar Chrome solo para publicar en grupos sin supervisión.
- Simular comportamiento humano, rotar cuentas o perfiles, ni usar herramientas para no ser detectado.
- Superar CAPTCHAs o verificaciones.
- Cambiar textos para engañar a los filtros antispam (la rotación es para no cansar al público, no para disfrazar repeticiones).

---

## 4. Cómo queda tu trabajo y el del equipo

### Tu trabajo

1. Cargar la promoción una sola vez (imágenes, textos, ficha del viaje, WhatsApp).
2. Tocar **ACTIVAR CAMPAÑA**.
3. Mirar los resultados.

### Lo que hace el sistema solo

- Publica en la Página de Facebook, Instagram y la web.
- Lanza los anuncios con el presupuesto que fijaste (si lo activás).
- Arma la cola de grupos del día: elige grupos, imagen y texto, evita duplicados y respeta reglas y frecuencias.

### El "toque" en los grupos (puede hacerlo cualquier persona del equipo)

Desde el celular, en la pantalla **Cola de grupos de hoy**, cada tarjeta trae todo listo:

1. Botón **Copiar texto y guardar imagen**.
2. Botón **Abrir grupo** (abre la app de Facebook en ese grupo).
3. Pegar, elegir la imagen y publicar.
4. Volver y tocar **Publicada** o **Quedó pendiente**.

Son unos **20 segundos por grupo**. Con 20 grupos por día, son unos 7 minutos, y se puede repartir entre las vendedoras. Cada persona publica desde su propia cuenta y en los grupos donde ya es miembro, lo que además reparte el riesgo y no concentra todo en una sola cuenta.

No hay que aprobar cada publicación: el contenido ya está validado en la campaña. El toque es solamente el clic que Meta no permite automatizar.

---

## 5. Diseño de la sección CAMPAÑA AUTOMÁTICA

### Carga

- **Viaje:** se elige de FULL VIAJES 360 (destino, fechas, precio, cupos, condiciones). Esos datos no se escriben a mano en los textos: se insertan solos y quedan bloqueados.
- **Imágenes:** de 1 a 20.
- **Textos:** varios, con marcadores como `{precio}`, `{fecha}`, `{whatsapp}`.
- **WhatsApp:** número; el sistema genera un enlace con código por canal y por grupo.
- **Exclusiones:** grupos puntuales y palabras clave (por defecto: micros, colectivos, pasajes, fútbol, hinchadas, clubes).
- **Canales:** Página de Facebook, Instagram, anuncios (con presupuesto máximo), web, grupos.
- **Fechas:** inicio y fin; se corta sola si el viaje vence o se agota.

### Estados de la campaña

`Borrador → Activa → Pausada → Finalizada`, más **Detenida por seguridad** (solo se sale con una revisión tuya).

### Panel de resultados

- Consultas y reservas por campaña, canal, grupo, imagen y texto.
- Ranking de grupos que traen pasajeros.
- Qué imagen y qué texto convierten mejor.
- Costo por consulta y por reserva en los anuncios.
- Grupos en lista negra y por qué.
- Salud de la cuenta e incidencias.

---

## 6. Arquitectura

Un módulo dentro de **FULL VIAJES 360** (PHP 8.4 + MySQL en Ferozo), que ya tiene usuarios, CRM y reservas.

```
           ┌──────────── FULL VIAJES 360 / MARKETING PRO ────────────┐
           │  Campañas · Creatividades · Grupos · Lista negra         │
 Vos  ───▶ │  Cola de grupos · Estadísticas · Estado de seguridad     │
           └───────┬──────────────┬──────────────┬───────────────┬────┘
                   │ API oficial  │ API oficial  │ API WordPress │ Cola en el celular
                   ▼              ▼              ▼               ▼
           Página FB + IG   Anuncios Meta     Web propia     Grupos de Facebook
           (automático)     (automático,      (automático)   (un toque por grupo)
                             con tope de $)
                   │              │              │               │
                   └──────────────┴──── WhatsApp con código ─────┘
                                          │
                                   CRM → Reserva → Estadísticas
```

**Detalle técnico importante:** el hosting compartido no tiene procesos permanentes. Las publicaciones programadas se disparan con la **tarea programada (cron)** del panel de Ferozo cada pocos minutos. Hay que confirmar que el plan lo permite (el diagnóstico de hosting de la otra sesión lo verifica).

**Escalable:** varias campañas en paralelo, cientos de grupos y varias personas publicando desde la cola, sin cambiar la arquitectura.

---

## 7. Qué hace falta para los canales automáticos

| Canal | Requisito |
|---|---|
| Página de Facebook e Instagram | Una aplicación de Meta propia (gratis), Página e Instagram profesional vinculados, y un usuario de sistema en el administrador comercial de Meta. Puede requerir verificación del negocio. |
| Anuncios | Cuenta publicitaria con medio de pago y un presupuesto máximo que vos definís. |
| Web | Usuario de WordPress con permiso para publicar y una "contraseña de aplicación". |
| Grupos | Ningún permiso técnico: solo estar en los grupos. |

Las claves se guardan cifradas en el servidor, nunca en el código ni en el chat.

---

## 8. Cambios respecto del prompt actual

Si aprobás este diseño, hay que ajustar `PROMPT_GRUPOS_FACEBOOK.md`:

- **15 y 20.7 (aprobación de cada publicación):** se reemplaza por **aprobación por campaña**. Al activar la campaña aprobás su contenido; las publicaciones individuales ya no piden confirmación.
- **19 (Claude manejando Chrome):** pasa a ser opcional, solo para la carga inicial de grupos y las rondas de revisión, siempre supervisadas. No se usa para publicar sin supervisión.
- Se suman los canales automáticos (Página, Instagram, anuncios, web) y la cola "publicar en un toque".

---

## 9. Plan por etapas

| Etapa | Qué incluye | Resultado para vos |
|---|---|---|
| 1 | FULL VIAJES 360 instalado en Ferozo (otra sesión). | Base lista. |
| 2 | Campañas, creatividades, grupos, exclusiones, lista negra, duplicados. | Cargás una promo una vez. |
| 3 | Cola "publicar en un toque" en el celular + estados. | Grupos en 20 segundos cada uno. |
| 4 | WhatsApp con código + vínculo con CRM y reservas + estadísticas. | Sabés qué grupo trae pasajeros. |
| 5 | Publicación automática en Página de Facebook, Instagram y web. | Canales oficiales sin intervención. |
| 6 | Anuncios automáticos con tope de presupuesto. | Escala real y medible. |

Las etapas 2 a 4 ya dan el valor principal (saber qué grupos venden). La 5 y la 6 suman la parte 100 % automática.

---

## 10. Decisiones que necesito de vos

1. ¿Aprobás que en los grupos quede el "toque" de 20 segundos, sabiendo que no hay vía autorizada para evitarlo?
2. ¿Querés que el toque se pueda repartir entre las vendedoras?
3. ¿Sumamos Página de Facebook, Instagram y web como canales automáticos?
4. ¿Querés anuncios pagos automáticos? Si es así, ¿con qué presupuesto máximo diario?
5. ¿Confirmás que se construye como módulo de FULL VIAJES 360?
