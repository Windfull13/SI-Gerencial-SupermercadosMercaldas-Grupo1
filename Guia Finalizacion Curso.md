**Guia de Finalizacion del Curso — Entrega Final Sprint **6** y **6**** Entrega Final  |  Sprint 6 y 6  |  45%
|||||
| :- | :- | :- | :- |
||**UNIVERSIDAD DE CALDAS**|||
||Facultad de Ingenierias  |  Dpto. Sistemas e Informatica|||
||**GUIA DE FINALIZACION DEL CURSO**|||
||**Entrega Final del Proyecto de Aula**|||
||**Sprint 2 y Sprint 3  —  45% de la nota**|||
||Sistema funcional + documentacion completa en Git y Drive|||
||**Asignatura:**|Sistemas de Informacion Gerencial![ref1]||
||**Evaluacion:**|**Sprint 2 y Sprint 3 — Valor: 45% de la nota final del curso![ref1]**||
||**Modalidad:**|Trabajo en grupo  |  3 a 4 integrantes![ref1]||
||**Entregables:**|Repositorio Git + carpeta Drive + software funcional con datos![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.002.png)||
||**Sustentacion:**|Demostracion en vivo + revision de trazabilidad![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.003.png)||
**Objetivo de la entrega final** ![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.004.png)

Esta es la entrega que cierra el curso. Reune TODO el trabajo del semestre: el sistema funcional construido para tu empresa caso, mas toda la documentacion generada (SRS, mockups, modelo de datos, diagramas UML, auditoria UX, plan de proyecto). El docente revisara la TRAZABILIDAD: que el software construido corresponda fielmente a lo que se documento. Vale el 45% de la nota final del curso.

**1. DISTRIBUCION DE LA NOTA — SPRINT 2 Y 3![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.005.png)**

**Valor de cada Sprint** 

La entrega final corresponde al Sprint 2 y al Sprint 3, que en conjunto valen el 45% de la nota del curso: 



|**Sprint**|**Que cubre**|**Valor**|**Acumulado**|
| - | - | - | - |
|**Sprint 2**|Diseno completo: mockups aprobados, modelo de base de datos, diagramas UML y backend funcional con datos.|**22.5%**|**22.5%**|
|**Sprint 3**|Sistema completo: frontend integrado, software funcional con datos de prueba, reportes/informes, documentacion final.|**22.5%**|**45%**|
|**TOTAL ENTREGA FINAL**|**45%**|**45%**||

**Como se reparte el 45% internamente** ![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.006.png)

Sprint 2 (22.5%): se evalua al final de la etapa de diseno. Sprint 3 (22.5%): se evalua en la sustentacion final. Ambos sprints deben estar versionados en Git y respaldados en Drive. Una entrega incompleta de cualquiera de los dos sprints afecta proporcionalmente la nota.



|**2. QUE ENTREGAR EN CADA SPRINT**|
| - |

**Sprint 2 — Diseno y backend (22.5%) ![ref2]**



|**Entregable**|**Detalle de lo que se espera**||
| - | - | :- |
|**Mockups aprobados**|Todas las pantallas del sistema en alta fidelidad, validadas con el cliente. Exportadas a PDF o imagen y subidas al Drive.||
|**Modelo de base de datos**|Diagrama entidad-relacion + script SQL de creacion de tablas. La BD debe estar creada y poblada con datos de prueba.||
|**Diagramas UML**|Los 4 diagramas: casos de uso, clases, secuencia y actividades. Coherentes con el SRS.||
|**Backend funcional**|API REST con los endpoints principales funcionando. Autenticacion implementada. Conectado a la base de datos.||
|**Documentacion parcial**|SRS actualizado + diccionario de datos + manual tecnico preliminar. Todo versionado en Git.||

**Sprint 3 — Sistema completo y cierre (22.5%)** 



|**Entregable**|**Detalle de lo que se espera**|
| - | - |
|**Software funcional completo**|Frontend integrado con backend. Todas las funciones operativas. Desplegado o ejecutable con instrucciones claras.|
|**Base de datos con datos**|La BD debe tener datos reales de prueba suficientes para generar reportes (minimo 20-30 registros por tabla principal).|
|**Modulo de reportes/informes**|El sistema debe generar al menos 2 reportes utiles para el cliente (ej: ordenes por mecanico, ingresos por periodo).|
|**Documentacion final completa**|Manual de usuario + manual tecnico + documentacion de la API + script de BD + lecciones aprendidas.|
|**Repositorio Git ordenado**|Commits descriptivos, ramas organizadas, README completo, .gitignore correcto. Historial que muestre el avance.|
|**Carpeta Drive estructurada**|Todos los documentos organizados en carpetas. Acceso compartido con el docente.|
|**Auditoria UX aplicada**|Resultados de la auditoria heuristica + SUS aplicada al propio sistema construido.|



|**3. REPOSITORIO GIT — ESTRUCTURA OBLIGATORIA**|
| - |

**Como organizar el repositorio** 

El repositorio en GitHub (o GitLab) debe seguir esta estructura de carpetas: 



|**Carpeta / Archivo**|**Que contiene**|
| - | - |
|**/README.md![ref3]**|Descripcion del proyecto, integrantes, como instalar y ejecutar, tecnologias usadas.|
|**/docs/**|Toda la documentacion: SRS, manuales, diagramas UML, modelo BD, auditoria UX.|
|**/frontend/![ref3]**|Codigo fuente del frontend (interfaz de usuario).|
|**/backend/**|Codigo fuente del backend (API, logica de negocio).|
|**/database/![ref4]**|Scripts SQL: creacion de tablas + datos de prueba (seed).|
|**/mockups/**|Mockups exportados en imagen o PDF.|
|**/reports/![ref4]**|Ejemplos de los reportes/informes que genera el sistema.|
|**/.gitignore**|Excluir node\_modules, archivos de entorno, credenciales.|

**Requisitos del historial de commits ![ref2]**



|**Requisito**|**Que se espera**||
| - | - | :- |
|**Commits frecuentes**|Minimo 2-3 commits por semana por integrante. Refleja trabajo continuo, no todo el ultimo dia.||
|**Mensajes descriptivos**|'Agregar endpoint de crear OT' es bueno. 'cambios' o 'fix' solos son malos.||
|**Todos contribuyen**|El grafico de contribuciones debe mostrar aporte de TODOS los integrantes.||
|**Ramas organizadas**|Usar rama main estable + ramas de desarrollo. No trabajar todo en main.||
|**Tags por sprint**|Crear un tag git al cerrar cada sprint: v1.0-sprint2, v2.0-sprint3.||

⚠️  **Sobre el control de versiones** ![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.010.png)

El docente revisara el historial de Git. Un repositorio con un solo commit gigante el ultimo dia tendra penalizacion. El proposito de Git es demostrar el proceso de construccion, no solo el resultado final. Todos los integrantes deben aparecer como contribuyentes.



|**4. CARPETA DRIVE — DOCUMENTACION COMPLETA**|
| - |

**Estructura de la carpeta compartida** 

Ademas del Git, debe existir una carpeta en Google Drive compartida con el docente, organizada asi: 



|**Carpeta**|**Documentos que debe contener**|
| - | - |
|**01\_Requisitos![ref5]**|SRS IEEE 830 completo. Lista de requerimientos funcionales y no funcionales.|
|**02\_Diseno**|Mockups de todas las pantallas. Sitemap navegacional. Guia de estilo.|
|**03\_Modelo\_Datos![ref5]**|Diagrama entidad-relacion. Diccionario de datos. Script SQL.|
|**04\_Diagramas\_UML**|Casos de uso, clases, secuencia, actividades.|
|**05\_Auditoria\_UX![ref5]**|Resultados de heuristicas Nielsen + SUS aplicados al sistema propio.|
|**06\_Plan\_Proyecto**|Excel del plan: WBS, cronograma, sprints, EVM, riesgos.|
|**07\_Manuales![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.012.png)**|Manual de usuario + manual tecnico + documentacion de la API.|
|**08\_Reportes**|Capturas o PDF de los informes que genera el sistema.|
|**09\_Sustentacion**|Presentacion final + video demo (opcional pero recomendado).|

💡 **Sobre el acceso compartido** ![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.013.png)

La carpeta Drive debe estar compartida con permiso de LECTURA para el correo institucional del docente. Verifica el acceso ANTES de la fecha de entrega — un documento que el docente no puede abrir cuenta como no entregado. Recomendacion: probar el enlace desde una sesion de incognito.



|**5. REVISION DE TRAZABILIDAD — EL CRITERIO CLAVE**|
| - |

**Que es la revision comparativa** 

**Concepto: trazabilidad** ![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.014.png)

La trazabilidad es la capacidad de seguir un requisito desde que se documenta hasta que se construye. El docente NO solo revisara que el software funcione. Revisara que lo que se construyo CORRESPONDA fielmente a lo que se documento en cada etapa del curso. Cada requisito debe poder rastrearse: requisito en el SRS → mockup → modelo de datos → diagrama UML → codigo → funcionalidad real.![ref2]

**Cadena de trazabilidad que se revisara ![ref6]![ref7]**

Para una muestra de funcionalidades, el docente seguira esta cadena completa: 



|**Paso**|**Artefacto**|**Pregunta de verificacion**|
| - | - | - |
|**1**|**Requisito (SRS)**|¿El requisito esta claramente escrito en el SRS con su identificador?|
|**2**|**Mockup**|¿Existe una pantalla disenada que implementa ese requisito?|
|**3**|**Modelo de datos![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.017.png)**|¿Las tablas y campos necesarios para ese requisito existen en la BD?|
|**4**|**Diagrama UML**|¿El caso de uso / clase / secuencia refleja ese requisito?|
|**5**|**Codigo fuente**|¿Hay codigo en el repositorio que implementa esa funcionalidad?|
|**6**|**Software funcional**|¿La funcionalidad realmente FUNCIONA en el sistema ejecutado?|
|**7**|**Datos y reporte**|¿Se puede generar un reporte/informe usando datos reales de esa funcionalidad?|

**Matriz de trazabilidad — debes incluirla en la documentacion** 

Tu grupo debe entregar una matriz que demuestre la trazabilidad. Ejemplo del formato (con datos MotoExpres): 



|**ID Req.**|**Requisito**|**Mockup**|**Tabla BD**|**Caso de uso**|**Estado**|
| - | - | - | - | - | - |
|**RF-01**|Crear orden de trabajo|P-11|ordenes|CU-01|✓ **OK![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.018.png)**|
|**RF-02**|Listar ordenes|P-20|ordenes|CU-02|✓ **OK![ref8]**|
|**RF-03**|Buscar por placa|P-30|vehiculos|CU-03|✓ **OK![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.020.png)**|
|**RF-04**|Asignar mecanico|P-21|mecanicos|CU-04|✓ **OK![ref8]**|
|**RF-05**|Generar reporte|P-41|ordenes|CU-05|✓ **OK**|



|**6. SOFTWARE CON DATOS, REPORTES E INFORMES**|
| - |

**La base de datos debe tener datos reales** 

**Por que datos de prueba son obligatorios** ![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.021.png)

Un sistema vacio no se puede evaluar. La base de datos debe estar poblada con datos de prueba realistas para que el docente pueda: ejecutar funciones, generar reportes, analizar la informacion y verificar que el sistema realmente funciona end-to-end. Minimo 20-30 registros por tabla principal.

**Datos minimos requeridos (ejemplo MotoExpres)** 



|**Tabla**|**Cantidad minima**|**Para que sirve**|
| - | - | - |
|**Clientes![ref9]**|**20 registros![ref10]**|Probar busquedas, historial de cliente.![ref11]|
|**Vehiculos / Motos**|**25 registros**|Probar busqueda por placa, asociacion con cliente.|
|**Ordenes de trabajo![ref9]**|**30 registros![ref10]**|Generar reportes, filtros por estado, por mecanico.![ref11]|
|**Mecanicos / Usuarios**|**5 registros**|Probar asignacion, login por roles, productividad.|
|**Servicios / Catalogo**|**15 registros**|Probar creacion de OT con distintos servicios.|

**Reportes / informes que debe generar el sistema ![ref2]**

El sistema debe poder generar minimo 2 reportes utiles para la gerencia. Ejemplos para MotoExpres: ![ref6]![ref7]



|**Reporte**|**Que muestra y para que sirve**|
| - | - |
|**Ordenes por mecanico**|Cuantas OT atendio cada mecanico en un periodo. Sirve para medir productividad.|
|**Ingresos por periodo**|Total facturado por dia/semana/mes. Sirve para la gestion financiera del taller.|
|**Ordenes por estado**|Cuantas OT estan recibidas, en proceso, listas, entregadas. Sirve para el control operativo.|
|**Historial de un vehiculo**|Todas las OT de una placa. Sirve para dar seguimiento al cliente.|
|**Servicios mas solicitados**|Ranking de servicios. Sirve para decisiones de inventario y personal.|

💡 **Sobre el analisis de la base de datos** ![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.025.png)

Documenta en el manual tecnico: el modelo entidad-relacion final, el diccionario de datos (cada tabla, cada campo, su tipo y proposito) y al menos 3 consultas SQL de ejemplo que alimentan los reportes. Esto demuestra que entiendes la estructura de datos que construiste.

**7. SUSTENTACION FINAL![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.026.png)**

**Como sera la sustentacion** 



|**Momento**|**Tiempo**|**Que se espera**|
| - | - | - |
|**Presentacion![ref12]**|**8 min![ref13]**|Contexto del proyecto, decisiones de diseno, arquitectura del sistema.![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.029.png)|
|**Demo en vivo**|**10 min**|Demostrar el sistema funcionando con datos reales. Recorrer flujos principales.|
|**Trazabilidad![ref12]**|**7 min![ref13]**|Mostrar la cadena requisito → mockup → modelo → codigo de 2-3 funcionalidades.|
|**Reportes**|**3 min**|Generar un reporte en vivo y explicarlo.|
|**Preguntas**|**7 min**|El docente pregunta a CUALQUIER integrante sobre CUALQUIER parte. Todos deben ![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.030.png)saber.|

⚠️  **Todos deben dominar el proyecto** ![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.031.png)

En la sustentacion el docente puede preguntar a cualquier integrante sobre cualquier parte del sistema, incluso codigo o documentacion que no escribio. La nota es grupal pero el conocimiento debe ser de todos. Si un integrante no puede responder sobre su propio proyecto, afecta la nota del grupo.



|**8. RUBRICA DE EVALUACION — 45%**|
| - |

**Como se distribuye el 45% ![ref2]**



|**Criterio**|**Peso**|**Excelente**|**Aceptable**|**Insuf.**||
| - | - | - | - | - | :- |
|**Software funcional**|**12%**|Funciona completo, sin errores, con datos.|Funciona con fallos ![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.032.png)menores.|No funciona o muy ![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.033.png)incompleto.||
|**Trazabilidad**|**10%**|Cadena requisito-codigo perfecta y documentada.|Trazabilidad parcial.|Sin matriz de trazabilidad.||
|**Documentacion Drive**|**7%**|Completa, organizada, accesible.|Algunos documentos faltan.|Desorganizada o sin ![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.034.png)acceso.||
|**Repositorio Git**|**6%**|Historial limpio, todos contribuyen.|Commits irregulares.|Un solo commit o sin Git.||
|**Base de datos + reportes**|**6%**|BD poblada, reportes utiles funcionando.|Datos escasos, 1 reporte.|Sin datos o sin reportes.||
|**Sustentacion**|**4%**|Todos dominan, demo fluida.|Demo con tropiezos.|No dominan el proyecto.||
|**TOTAL**|**45%**|**Sprint 2: 22.5%  +  Sprint 3: 22.5%**||||



|**9. LISTA DE VERIFICACION FINAL**|
| - |

**Antes de la entrega, verifica TODO** 



|✓|**Item a verificar**|
| - | - |
|☐|El software funciona completo en una maquina limpia (probado, no solo 'en mi maquina').|
|||
|☐|La base de datos tiene datos de prueba suficientes (20-30 registros por tabla principal).|
|||
|☐|El sistema genera minimo 2 reportes utiles y funcionan.|
|||
|☐|El repositorio Git tiene historial limpio con commits de TODOS los integrantes.|
|||
|☐|El repositorio tiene README con instrucciones de instalacion y ejecucion.|
|||
|☐|La carpeta Drive esta organizada en las 9 subcarpetas y compartida con el docente.|
|||
|☐|Probaste el acceso al Drive desde una sesion de incognito (el docente puede abrirlo).|
|||
|☐|La matriz de trazabilidad esta completa: requisito-mockup-BD-UML-codigo.|
|||
|☐|Los mockups corresponden a las pantallas reales del sistema construido.|
|||
|☐|El modelo de datos coincide con las tablas reales de la base de datos.|
|||
|☐|Los diagramas UML reflejan la arquitectura real del sistema.|
|||
|☐|Aplicaste la auditoria UX (heuristicas + SUS) al sistema propio y documentaste resultados.|
|||
|☐|El manual de usuario y el manual tecnico estan completos.|
|||
|☐|Todos los integrantes pueden explicar cualquier parte del proyecto.|
|||
|☐|Creaste los tags de Git: v1.0-sprint2 y v2.0-sprint3.|
|||
|☐|El nombre de los archivos sigue convencion clara y profesional.|
|||
**Mensaje de cierre del curso** ![](Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.035.png)

Esta entrega final integra TODO lo aprendido en el semestre: requerimientos, diseno, modelado, desarrollo, usabilidad, auditoria y planificacion. No es solo una nota — es la evidencia de que pueden llevar un sistema de informacion desde la idea hasta un producto funcional documentado. Esa es exactamente la competencia que se espera de un Ingeniero en Informatica de la Universidad de Caldas. Mucho exito en la entrega final.![ref2]
Sistemas de Informacion Gerencial  |  Ing. Cesar Barahona  |  Universidad de Caldas Pag. 6

[ref1]: Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.001.png
[ref2]: Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.007.png
[ref3]: Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.008.png
[ref4]: Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.009.png
[ref5]: Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.011.png
[ref6]: Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.015.png
[ref7]: Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.016.png
[ref8]: Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.019.png
[ref9]: Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.022.png
[ref10]: Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.023.png
[ref11]: Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.024.png
[ref12]: Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.027.png
[ref13]: Aspose.Words.923ef093-778d-40e0-ac8c-432ae96741a3.028.png
