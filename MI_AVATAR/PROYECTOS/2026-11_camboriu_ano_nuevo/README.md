# Año Nuevo en Camboriú — video publicitario Full Viajes

## Entrega (`ENTREGA/`)
| Archivo | Uso |
|---|---|
| `FullViajes_Camboriu_AnoNuevo_1080x1920.mp4` | Máster: 1080×1920, 30 fps, H.264, 40,4 s, alta calidad |
| `FullViajes_Camboriu_AnoNuevo_REELS.mp4` | Versión optimizada para Instagram, Facebook y TikTok (≈ 5,4 Mbps, faststart) |
| `Portada_Camboriu_AnoNuevo.jpg` | Portada vertical 1080×1920 con el destino y el precio |

## Estructura del video
| Tiempo | Escena | Origen |
|---|---|---|
| 0,0–5,1 | Vista aérea de Balneário Camboriú de noche + "ESTE AÑO NUEVO SE VIVE EN BRASIL" | IA (Seedance 2.5) |
| 5,1–12,1 | Mariano en la playa con amigos + "IMAGINATE RECIBIR EL 2027 FRENTE AL MAR..." | IA con referencias reales de Mariano |
| 12,1–22,2 | Ronda de turistas, cuenta regresiva 5→0 con números sincronizados a los gritos. La música se corta justo antes del cero | IA con referencias de Mariano |
| 18,6 | **CERO**: primeros fuegos artificiales + "¡FELIZ AÑO NUEVO!" | — |
| 22,2–28,3 | Gran show de fuegos sobre la bahía y la multitud | IA |
| 28,3–34,3 | Mariano: "¡Vos qué estás esperando para ir a pasar Año Nuevo así!" (con subtítulo) | Doble digital (Higgsfield Intone + voz clonada de su video) |
| 34,3–40,4 | Cierre con el flyer oficial + "RESERVÁ TU LUGAR Y VIVÍ UN AÑO NUEVO INOLVIDABLE" | Flyer original, sin retipear datos |

Audio: ambiente de cada escena (mar, gente, conteo, fuegos), música instrumental generada (ElevenLabs Music vía Higgsfield, sin derechos de terceros), mezclada a ≈ −13 LUFS.

## Lo que NO se usó y por qué
- **Video de eltrece** (Camboriú real): tiene marca de agua de un canal de TV, así que hay riesgo de reclamo en anuncios pagos. Se reemplazó por escenas generadas.
- **Video de Río de Janeiro**: no es Camboriú y la protagonista es una persona que no dio su autorización.

## Costos (créditos de Higgsfield)
Saldo antes: 2.143,4 → después: 1.844,89. **Total gastado: 298,5 créditos** (presupuesto aprobado: unos 320).
- 4 escenas Seedance 2.5, 720p, 28 s en total: 196 (escaladas a 1080p en la edición)
- Clip del coordinador, Intone 1080p: 96
- Frase con la voz clonada (Seed Audio): 1,2
- Música (ElevenLabs Music v2.5): 6,1

## IDs para reutilizar
- Referencias de cara (de su video del escritorio): `0929741c-5cd4-4add-a2b2-cedddcd171b3`, `62bc8052-d099-4073-aa59-842776401244`, `5a3043e9-fbdc-4d2d-9f4c-a94c432ffd10`
- Referencia de voz (29 s limpios de su video): `64bc49ea-5355-4e9a-a726-f6dfda455d3a`
- Trabajos: escenas `5fe85619…`, `acdedbbd…`, `2d4643c1…`, `f8bbd1ad…` · coordinador `18e688de…` · voz `bde97629…` · música `54d6db6c…`

Los recortes de la cara y el audio de referencia de la voz **no** se suben a este repositorio, porque es público. Están solo en la cuenta de Higgsfield.

## Pendientes y notas
- La remera oficial de Full Viajes: no había una foto real de Mariano con la remera, así que aparece con su **gorra Full Viajes real** y la remera verde de su video. Para no inventar un logo, no se generó una remera falsa.
- Volver a renderizar: `python3 SCRIPTS/mktext.py && python3 SCRIPTS/build.py` (desde una carpeta con s1–s5.mp4, music.mp3, endcard.png y txt/).
