# -*- coding: utf-8 -*-
"""Contenido del CV de Maurice Valdés Bermúdez, en español e inglés.

TODO lo de aquí sale del CV original (doPDF, 5 jul 2021) o se deriva de él.
NADA SE INVENTA. Las palabras que faltan y que probablemente son ciertas
—Prism, vSphere, Kubernetes, Terraform, Prometheus— NO están aquí: están en
el documento de revisión, en una lista para que Maurice confirme. Es la
diferencia entre un CV que aguanta una entrevista y uno que se cae en la
primera pregunta.

Lo que se corrigió del original, y por qué:

  · «20 años»: el CV decía «Experience 16 years» en julio de 2021, lo que
    sitúa el inicio a mediados de 2005. Se usa 2006 —el año en que empieza su
    formación técnica, el dato más temprano documentado— porque es MÁS
    conservador que su propia afirmación.
  · «Safety Engineer» se corrige a Security Engineer: en inglés «safety» es
    seguridad física. En un CV internacional dice lo contrario de lo que hizo.
  · NCP / NCAP / NSS se dejan como siglas: expandirlas sería suponer.

EL CAMBIO DE ESTA VERSIÓN: ALIGERAR. La anterior tenía razón en el fondo y se
equivocaba en la cantidad — perfil de siete renglones, cinco logros, siete
líneas de competencias y seis o siete viñetas por puesto. Todo cierto, todo
junto, y cansa antes de llegar a lo bueno.

Lo que se quitó y por qué:
  · La sección de logros entera. Repetía los 8 PB y los 38 proyectos que ya
    dicen las cifras y las viñetas. Tres sitios para el mismo dato es ruido.
  · El perfil pasa de siete renglones a cuatro.
  · Las competencias, de siete líneas a cinco, con las listas podadas.
  · Las viñetas, de seis o siete por puesto a CUATRO. Las que quedan llevan
    más palabras clave que las que se fueron, porque se fusionaron.

Lo que se añadió: una banda de CIFRAS arriba. Un reclutador da doce segundos
a la primera pantalla y un filtro automático busca términos; cuatro números
con su frase al lado sirven a los dos a la vez —se leen de un vistazo y se
extraen como oraciones completas, no como dígitos sueltos—.
"""

DATOS = {
    "nombre": "Maurice Valdés Bermúdez",
    "correo": "mauro.boss@gmail.com",
    "tel": "+52 55 4767 7080",
    "ciudad_es": "Ciudad de México, México",
    "ciudad_en": "Mexico City, Mexico",
    "sitio": "valdes-bermudez.vercel.app",
    "retrato": "img/retrato-cv.png",
}

ES = {
    "titulo": "Senior Site Reliability Engineer",
    "bajada": "Infraestructura crítica · Nube híbrida · Seguridad ofensiva",

    # Cada cifra se extrae como una oración entera, no como un dígito suelto.
    "cifras": [
        ("20", "años en infraestructura crítica"),
        ("4", "regiones en la rotación global"),
        ("8 PB", "migrados y configurados en Azure"),
        ("+38", "proyectos de nube entregados"),
    ],

    "h_perfil": "Perfil",
    "perfil": (
        "Veinte años manteniendo en pie infraestructura crítica: hoy en el equipo global "
        "de Nutanix, sobre cuatro regiones y en inglés; antes como arquitecto de nube, con "
        "8 PB migrados y más de 38 proyectos entregados en Azure. Mi formación de origen "
        "es ofensiva —hacking ético certificado por EC-Council—: diseño alta disponibilidad "
        "sabiendo por dónde se rompe."
    ),

    "h_comp": "Competencias técnicas",
    "comp": [
        ("Confiabilidad",
         "Site Reliability Engineering, alta disponibilidad HA, DRP, BCP, continuidad del "
         "negocio, recuperación ante desastres, protección de datos, gestión de "
         "incidentes, análisis de causa raíz, análisis de rendimiento"),
        ("Virtualización",
         "Nutanix AHV, Nutanix Leap, VMware, Microsoft Hyper-V, Citrix"),
        ("Nube",
         "Microsoft Azure, IaaS, arquitectura de nube, migración Lift & Shift, "
         "almacenamiento a escala de petabytes"),
        ("Seguridad",
         "Hacking ético, pruebas de penetración, arquitectura segura, endurecimiento de "
         "Linux, firewalls, AAA y AAA+, Novell Identity Manager, eDirectory, Sentinel"),
        ("Idiomas",
         "Español nativo · Inglés profesional, de uso diario en un equipo de cuatro regiones"),
    ],

    "h_exp": "Experiencia",
    "exp": [
        {
            "puesto": "Site Reliability Engineer",
            "empresa": "Nutanix México, S.A. de C.V.",
            "lugar": "Ciudad de México",
            "fechas": "ago 2019 – actualidad",
            "puntos": [
                "Soporte de producción de infraestructura hiperconvergida en el equipo "
                "global de Nutanix, en inglés y sobre cuatro regiones.",
                "Diagnóstico y análisis de causa raíz sobre Nutanix AHV, VMware, Microsoft "
                "Hyper-V y Citrix; equipo virtual de rendimiento.",
                "Instructor interno de diagnóstico de rendimiento: formo a otros ingenieros "
                "en el método, no sólo cierro el caso.",
                "Arquitecturas HA, DRP y BCP; recuperación ante desastres, incidentes de "
                "nube sobre Nutanix Leap y Azure, y endurecimiento de Linux.",
            ],
        },
        {
            "puesto": "Arquitecto de Soluciones TI — Open Source y Seguridad",
            "empresa": "bSide · Microsoft Gold Partner",
            "lugar": "Ciudad de México",
            "fechas": "abr 2018 – ago 2019",
            "puntos": [
                "Más de 38 proyectos corporativos y de gobierno entregados en Microsoft "
                "Azure, entre ellos Pemex, IMSS y Actica.",
                "Migración Lift & Shift de máquinas virtuales con 8 PB de almacenamiento "
                "migrado y configurado.",
                "Diseño, construcción e implementación de arquitectura de nube; operación "
                "de IaaS en Azure y on-premise.",
                "Evaluación de arquitectura segura y pruebas de penetración; "
                "arquitecturas HA, DRP y BCP.",
            ],
        },
        {
            "puesto": "Ingeniero de Seguridad Especializado (Clase 3)",
            "empresa": "Grupo Elektra, S.A. de C.V. · Oficina de Seguridad de la Información",
            "lugar": "Ciudad de México",
            "fechas": "dic 2013 – abr 2018",
            "puntos": [
                "Hacking ético sobre los sistemas de un grupo financiero y comercial, "
                "desde su Oficina de Seguridad de la Información.",
                "Certificación de seguridad de aplicaciones y sistemas operativos antes de "
                "su paso a producción.",
                "Novell Identity Manager, eDirectory y Sentinel; servidores AAA y AAA+ de "
                "alta transaccionalidad.",
                "Análisis de arquitectura segura, atención a incidentes y endurecimiento "
                "de Linux y firewalls sobre arquitecturas HA.",
            ],
        },
    ],

    "h_cert": "Certificaciones",
    "cert": [
        ("CEH — Certified Ethical Hacker", "EC-Council · 2018"),
        ("NCP, NCAP y NSS", "Nutanix"),
    ],

    "h_edu": "Formación",
    "edu": [
        ("MBA — Dirección y Administración de Empresas",
         "Universidad del Valle de México · U. Europea de Madrid", "2013 – 2015"),
        ("Ingeniería en Sistemas Computacionales",
         "Universidad del Valle de México", "2008 – 2013"),
        ("Técnico en Operación de Microcomputadoras", "", "2006 – 2008"),
    ],
}

EN = {
    "titulo": "Senior Site Reliability Engineer",
    "bajada": "Critical infrastructure · Hybrid cloud · Offensive security",

    "cifras": [
        ("20", "years in critical infrastructure"),
        ("4", "regions in the global rotation"),
        ("8 PB", "migrated and configured on Azure"),
        ("+38", "cloud projects delivered"),
    ],

    "h_perfil": "Summary",
    "perfil": (
        "Twenty years keeping critical infrastructure standing: today in Nutanix's global "
        "team, across four regions and in English; before that as a cloud architect, with "
        "8 PB migrated and more than 38 projects delivered on Azure. My original training "
        "is offensive —EC-Council certified ethical hacker—: I design high availability "
        "knowing exactly where it breaks."
    ),

    "h_comp": "Core competencies",
    "comp": [
        ("Reliability",
         "Site Reliability Engineering, high availability HA, DRP, BCP, business "
         "continuity, disaster recovery, data protection, incident management, root cause "
         "analysis, performance analysis"),
        ("Virtualisation",
         "Nutanix AHV, Nutanix Leap, VMware, Microsoft Hyper-V, Citrix"),
        ("Cloud",
         "Microsoft Azure, IaaS, cloud architecture, Lift & Shift migration, "
         "petabyte-scale storage"),
        ("Security",
         "Ethical hacking, penetration testing, secure architecture, Linux hardening, "
         "firewalls, AAA and AAA+, Novell Identity Manager, eDirectory, Sentinel"),
        ("Languages",
         "Spanish native · English professional, in daily use across a four-region team"),
    ],

    "h_exp": "Experience",
    "exp": [
        {
            "puesto": "Site Reliability Engineer",
            "empresa": "Nutanix Mexico, S.A. de C.V.",
            "lugar": "Mexico City",
            "fechas": "Aug 2019 – Present",
            "puntos": [
                "Production support for hyperconverged infrastructure within Nutanix's "
                "global team, in English and across four regions.",
                "Troubleshooting and root cause analysis across Nutanix AHV, VMware, "
                "Microsoft Hyper-V and Citrix; performance virtual team.",
                "Internal trainer for performance troubleshooting: I teach other engineers "
                "the method, not just close the case.",
                "HA, DRP and BCP architectures; disaster recovery, cloud incident response "
                "on Nutanix Leap and Azure, and Linux hardening.",
            ],
        },
        {
            "puesto": "IT Solutions Architect — Open Source and Security",
            "empresa": "bSide · Microsoft Gold Partner",
            "lugar": "Mexico City",
            "fechas": "Apr 2018 – Aug 2019",
            "puntos": [
                "More than 38 enterprise and government projects delivered on Microsoft "
                "Azure, including Pemex, IMSS and Actica.",
                "Lift & Shift virtual machine migration with 8 PB of storage migrated and "
                "configured.",
                "Design, build and implementation of cloud architecture; Azure IaaS and "
                "on-premise operation.",
                "Secure architecture assessment and penetration testing; HA, DRP and BCP "
                "architectures.",
            ],
        },
        {
            "puesto": "Specialized Security Engineer (Class 3)",
            "empresa": "Grupo Elektra, S.A. de C.V. · Information Security Office",
            "lugar": "Mexico City",
            "fechas": "Dec 2013 – Apr 2018",
            "puntos": [
                "Ethical hacking across the systems of a financial and retail group, from "
                "its Information Security Office.",
                "Security certification of applications and operating systems before "
                "production release.",
                "Novell Identity Manager, eDirectory and Sentinel; high-transaction AAA "
                "and AAA+ servers.",
                "Secure architecture analysis, incident response and Linux and firewall "
                "hardening on HA architectures.",
            ],
        },
    ],

    "h_cert": "Certifications",
    "cert": [
        ("CEH — Certified Ethical Hacker", "EC-Council · 2018"),
        ("NCP, NCAP and NSS", "Nutanix"),
    ],

    "h_edu": "Education",
    "edu": [
        ("MBA — Management and Business Administration",
         "Universidad del Valle de México · U. Europea de Madrid", "2013 – 2015"),
        ("B.Eng. in Computer Systems Engineering",
         "Universidad del Valle de México", "2008 – 2013"),
        ("Technician in Microcomputer Operation", "", "2006 – 2008"),
    ],
}
