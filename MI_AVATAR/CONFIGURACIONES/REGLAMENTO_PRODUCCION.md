# Reglamento permanente de producción audiovisual — Doble digital

Este reglamento se aplica **automáticamente** a todo video que se pida con el avatar.
El pedido del usuario define el **contenido**; este documento define el **estándar de producción**.

## Identidad (no negociable)
- La fuente de verdad son las fotos, videos y audios originales del usuario que figuran en `VERSIONES_APROBADAS/`.
- No inventar rasgos, no embellecer, no aplicar filtros de belleza, no generar "piel de plástico". Conservar poros, textura y pequeñas imperfecciones.
- No mezclar la identidad con la de otras personas. Nunca usar a terceros que aparezcan en las fotos.
- Voz: solamente la voz clonada aprobada (ver `CONFIGURACIONES/avatar.json`). Si no existe, decirlo; nunca reemplazarla por una voz genérica parecida.

## Rostro y cuerpo
- Parpadeos naturales e irregulares, microexpresiones, cambios de mirada, cejas y mejillas con movimiento, respiración.
- No mantener una sonrisa permanente, no congelar la mirada, no repetir ciclos de animación evidentes.
- Gestos de manos y cabeza que acompañen el sentido del texto (entusiasmo para promociones, seriedad para temas serios). Nada de gestos al azar.
- Lip-sync prioritario. Boca en reposo natural durante las pausas.

## Escenario e integración
- Escenarios vivos: personas, vehículos, viento, agua, nubes, sombras dinámicas, según corresponda.
- Si el escenario representa un lugar real (hotel, ciudad, playa), buscar antes referencias reales y no inventar características.
- La luz, la temperatura de color, las sombras, la escala y la perspectiva del avatar tienen que coincidir con el escenario. Nunca un fondo "pegado".

## Cámara
- Variar los planos con intención narrativa: primer plano, plano medio, general y detalle; travelling, paneo, cambio de foco.
- Sin movimientos imposibles ni transiciones gratuitas.

## Audio
- La voz siempre por encima: música entre −18 y −24 dB por debajo de la voz; voz normalizada a −14 LUFS para redes.
- Sonido ambiente coherente con el escenario.
- No inventar diálogos ni cambiar el sentido del mensaje del usuario.

## Ahorro de créditos
1. Guion y plan de planos **antes** de generar.
2. Informar el costo estimado y **esperar la aprobación** antes de cualquier operación paga.
3. Probar en borrador (480p o el modo *draft*) y finalizar en 1080p solo lo aprobado.
4. No regenerar lo ya aprobado; reutilizar referencias y configuraciones.
5. Edición, música, subtítulos y montaje: siempre locales (ffmpeg), sin costo.
6. Nunca comprar créditos ni contratar servicios sin autorización explícita.

## Privacidad
- No publicar ni compartir fotos, videos, audios, la voz clonada ni el avatar.
- Antes de enviar datos a un proveedor nuevo: informar quién es, qué se envía, cómo se guarda, si se usa para entrenamiento y cómo se borra. Esperar la autorización.

## Flujo para un pedido nuevo
Ejemplo de pedido: *"Creame un video de 30 segundos promocionando un viaje a Brasil"*.
1. Interpretar la intención, el público y el mensaje.
2. Escribir un guion con la forma de hablar del usuario (rioplatense, cercano) → mostrarlo para aprobar.
3. Plan de planos (2–4 clips de 8–15 s) + escenarios + música → mostrar el costo estimado.
4. Con la aprobación: audio con la voz clonada → clips de video con las referencias aprobadas → montaje local → exportación (9:16 para redes, 16:9 para web).
5. Control de calidad: parecido, voz, lip-sync, continuidad y niveles de audio. No entregar un resultado defectuoso como terminado.
6. Guardar en `PROYECTOS/<fecha>_<nombre>/` el guion, los parámetros y los IDs de las generaciones.
