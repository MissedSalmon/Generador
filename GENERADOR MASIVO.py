import csv
from faker import Faker
import os

fake = Faker()
directory = 'C:/directory'

def generate_docente_csv(filename, num_rows):
    legajos = []
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['legajo', 'DNI', 'nombre', 'estado_civil', 'email', 'sexo', 'fecha_nacimiento'])
        for _ in range(num_rows):
            legajo = fake.unique.random_int(min=1000, max=99999999999)
            legajos.append(legajo)
            writer.writerow([
                legajo,
                fake.unique.random_int(min=10000000, max=99999999),
                fake.name(),
                fake.random_element(['Soltero', 'Casado', 'Divorciado']),
                fake.email(),
                fake.random_element(['M', 'F']),
                fake.date_of_birth(minimum_age=25, maximum_age=65)
            ])
    return legajos

def generate_contactos_csv(filename, num_rows):
    numeros = []
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['numero', 'tipo', 'medio'])
        for _ in range(num_rows):
            numero = fake.unique.random_int(min=1, max=99999999999)
            tipo = fake.random_element(['Telefono', 'Email', 'Celular'])
            if tipo == 'Email':
                medio = fake.email()
            else:
                medio = fake.phone_number()
            numeros.append(numero)
            writer.writerow([
                numero,
                tipo,
                medio
            ])
    return numeros

def generate_publicaciones_csv(filename, num_rows):
    publicaciones = []
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['titulo', 'año', 'ref_biblio'])
        for _ in range(num_rows):
            publi = fake.sentence(nb_words=6)
            publicaciones.append(publi)
            writer.writerow([
                publi,
                fake.year(),
                fake.url()
            ])
    return publicaciones

def generate_idiomas_csv(filename, num_rows):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id_idioma', 'nivel', 'idioma', 'institucion', 'certificacion'])
        for _ in range(num_rows):
            writer.writerow([
                fake.unique.random_int(min=1, max=100000),
                fake.random_element(['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']),
                fake.language_name(),
                fake.company(),
                fake.word()
            ])

def generate_docente_posee_contactos_csv(filename, docente_legajos, contacto_numeros):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['legajo', 'numero'])
        for legajo in docente_legajos:
            numero = fake.random_element(contacto_numeros)
            writer.writerow([legajo, numero])

def generate_docente_tiene_publicaciones_csv(filename, docente_legajos, publicaciones):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['legajo', 'titulo'])
        for legajo in docente_legajos:
            publicacion = fake.random_element(publicaciones)
            writer.writerow([legajo, publicacion])

def generate_reuniones_cientificas(filename, num_rows):
    reuniones = []
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id_reunion', 'titulo', 'fecha', 'participacion'])
        for _ in range(num_rows):
            reu = fake.unique.random_int(min=1000, max=99999999)
            reuniones.append(reu)
            writer.writerow([
                reu,
                fake.sentence(nb_words=6),
                fake.date(),
                fake.random_element(['Disertante', 'Colaborador', 'Oyente'])
            ])
    return reuniones

def generate_docente_participa_reuniones_csv(filename, docente_legajos, reuniones):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['legajo', 'id_reunion'])
        for legajo in docente_legajos:
            reunion = fake.random_element(reuniones)
            writer.writerow([legajo, reunion])


def generate_pasividad_obtenida_csv(filename, docente_legajos, num_rows):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id_pasividad', 'regimen', 'fecha_inicio', 'suspendido', 'causa', 'legajo'])
        for _ in range(num_rows):
            writer.writerow([
                fake.unique.random_int(min=1000, max=999999999),
                fake.random_element(['Ordinario', 'Extraordinario']),
                fake.date(),
                fake.boolean(),
                fake.sentence(nb_words=6),
                fake.random_element(docente_legajos)
            ])

def generate_ubicacion_csv(filename, num_rows):
    ubicaciones=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['CP', 'Provincia', 'ciudad'])
        for _ in range(num_rows):
            ubi=fake.unique.random_int(min=1000, max=99999999)
            ubicaciones.append(ubi)
            writer.writerow([
                ubi,
                fake.state(),
                fake.city()
            ])
    return ubicaciones

def generate_domicilio_csv(filename, ubicaciones, num_rows):
    domicilios =[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id_domicilio', 'barrio', 'calle', 'numero', 'piso', 'depto', 'cp'])
        for _ in range(num_rows):
            domi=fake.unique.random_int(min=1000, max=99999999)
            domicilios.append(domi)
            writer.writerow([
                domi,
                fake.street_name(),
                fake.street_address(),
                fake.building_number(),
                fake.random_int(min=1, max=10),
                fake.random_element(['A', 'B', 'C', 'D']),
                fake.random_element(ubicaciones)
            ])
    return domicilios

def generate_institucion_csv(filename, domicilios, num_rows):
    cuit=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['CUIT', 'razon_social', 'id_domicilio'])
        for _ in range(num_rows):
            cuits=fake.unique.random_int(min=10000000000, max=9999999999999)
            cuit.append(cuits)
            writer.writerow([
                cuits,
                fake.company(),
                fake.random_element(domicilios)
            ])
    return cuit

def generate_universidad_csv(filename, num_rows, insti_cuits):
    universidades_cuits=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['cuit', 'dependencia', 'unidad_academica'])
        for _ in range(num_rows):
            uni=fake.random_element(insti_cuits)
            universidades_cuits.append(uni)
            writer.writerow([
                uni,
                fake.company(),
                fake.word()
            ])
    return universidades_cuits

def generate_empresa_csv(filename, num_rows, uni_cuits):
    empresa_cuit=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['cuit', 'ActividadPrincipal', 'tipo'])
        
        for _ in range(num_rows):
            emp = fake.unique.random_int(min=10000000000, max=99999999999)
            while emp == uni_cuits:
                emp = fake.unique.random_int(min=10000000000, max=99999999999)
            
            empresa_cuit.append(emp)
            writer.writerow([
                emp,
                fake.job(),
                fake.random_element(['SA', 'SRL', 'SAS'])
            ])
    return empresa_cuit

def generate_tareas_no_oficiales_csv(filename, institucion_cuits, num_rows):
    tarea=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id_tarea', 'fecha_inicio', 'RelacionDependencia', 'FuncionDesempeñada', 'institucion'])
        for _ in range(num_rows):
            tareas=fake.unique.random_int(min=1000, max=9999999)
            tarea.append(tareas)
            writer.writerow([
                tareas,
                fake.date(),
                fake.word(),
                fake.job(),
                fake.random_element(institucion_cuits)
            ])
    return tarea        

def generate_docente_realiza_tarea_no_oficiales_csv(filename, docente_legajos, tareas_no_oficiales):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['legajo', 'id_tarea'])
        for legajo in docente_legajos:
            tarea = fake.random_element(tareas_no_oficiales)
            writer.writerow([legajo, tarea])

def generate_antecedentes_csv(filename, docente_legajos, num_rows):
    antecedentes_id=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id_antecedentes', 'id_docentes', 'nombre_cargo', 'funcion', 'reparticion', 'fecha_inicio', 'fecha_fin'])
        for _ in range(num_rows):
            antecedentes=fake.unique.random_int(min=1000, max=99999999)
            antecedentes_id.append(antecedentes)
            desde = fake.date()
            hasta = fake.date()
            while hasta < desde:
                hasta = fake.date()
            writer.writerow([
                antecedentes,
                fake.random_element(docente_legajos),
                fake.job(),
                fake.sentence(nb_words=6),
                fake.random_int(min=1, max=10),
                desde,
                hasta
            ])
    return antecedentes_id

def generate_antecedentes_docentes_csv(filename, antecedentes_ids, universidades_cuits, num_rows):
    antecedentes_docentesids=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id_antecedentes', 'materia', 'id_corresponde'])
        for _ in range(num_rows):
            doc=fake.random_element(antecedentes_ids)
            antecedentes_docentesids.append(doc)
            writer.writerow([
                doc,
                fake.word(),
                fake.random_element(universidades_cuits)
            ])
    return antecedentes_docentesids

def generate_antecedentes_profesionales_csv(filename, antecedentes_ids, empresas_cuits, num_rows):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id_antecedentes', 'tipo_act', 'id_corresponde'])
        for _ in range(num_rows):
            writer.writerow([
                fake.random_element(antecedentes_ids),
                fake.job(),
                fake.random_element(empresas_cuits)
            ])

def generate_horas_csv(filename, antecedentes_docentes_ids, num_rows):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id_hora', 'hora_entrada', 'hora_salida', 'dia', 'id_antecedentes'])
        for _ in range(num_rows):
            hora1 = fake.time()
            hora2 = fake.time()
            while hora2<hora1:
                hora2 = fake.time()

            writer.writerow([
                fake.unique.random_int(min=1, max=10000000),
                hora1,
                hora2,
                fake.random_int(min=1, max=7),
                fake.random_element(antecedentes_docentes_ids)
            ])

def generate_seguro_csv(filename, docente_legajos, institucion_cuits, num_rows):
    Seguro=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['nro_seguro', 'nombre_aseguradora', 'cod_compania', 'tipo', 'Legajo', 'CUIT'])
        for _ in range(num_rows):
            segu=fake.unique.random_int(min=1000, max=9999999)
            Seguro.append(segu)
            writer.writerow([
                segu,
                fake.company(),
                fake.random_int(min=1000, max=9999999),
                fake.word(),
                fake.random_element(docente_legajos),
                fake.random_element(institucion_cuits)
            ])
    return Seguro

def generate_obra_social_csv(filename, docente_legajos, institucion_cuits, num_rows):
    Osocial=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nro_Obra', 'Nombre_obra', 'Plan', 'Legajo', 'CUIT'])
        for _ in range(num_rows):
            Social = fake.unique.random_int(min=1000, max=99999999)
            Osocial.append(Social)
            writer.writerow([
                Social,
                fake.company(),
                fake.word(),
                fake.random_element(docente_legajos),
                fake.random_element(institucion_cuits)
            ])
    return Osocial

def generate_familiar_csv(filename, domicilio_ids, num_rows):
    Fami=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['nro_documento', 'NombreCompleto', 'tipo_documento', 'id_domicilio'])
        for _ in range(num_rows):
            fam=fake.unique.random_int(min=10000000, max=999999999)
            Fami.append(fam)
            writer.writerow([
                fam,
                fake.name(),
                fake.random_element(['DNI', 'Pasaporte', 'Cedula']),
                fake.random_element(domicilio_ids)
            ])
    return Fami

def generate_docente_afilia_familiar_csv(filename, docente_legajos, familiar_nros, num_rows):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['nro_documento', 'parentesco', 'Legajo'])
        for _ in range(num_rows):
            writer.writerow([
                fake.random_element(familiar_nros),
                fake.random_element(['Padre', 'Madre', 'Hijo', 'Hija', 'Conyuge']),
                fake.random_element(docente_legajos)
            ])

def generate_seguro_beneficia_familiar_csv(filename, seguro_nros, familiar_nros, num_rows):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['nro_seguro', 'nro_documento', 'porcentaje'])
        for _ in range(num_rows):
            writer.writerow([
                fake.random_element(seguro_nros),
                fake.random_element(familiar_nros),
                fake.random_int(min=1, max=100)
            ])

def generate_obra_afilia_familiar_csv(filename, obra_nros, familiar_nros, num_rows):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['nro_obra', 'nro_documento'])
        for _ in range(num_rows):
            writer.writerow([
                fake.random_element(obra_nros),
                fake.random_element(familiar_nros)
            ])

def generate_docente_tiene_domicilio_csv(filename, docente_legajos, domicilio_ids, num_rows):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['legajo', 'id_domicilio', 'tipo'])
        for _ in range(num_rows):
            writer.writerow([
                fake.random_element(docente_legajos),
                fake.random_element(domicilio_ids),
                fake.random_element(['Particular', 'Laboral'])
            ])

def generate_curso_oconf_csv(filename, institucion_cuits, num_rows):
    Confe=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['curso_Conf', 'descripcion', 'cuit'])
        for _ in range(num_rows):
            conf=fake.word()
            Confe.append(conf)
            writer.writerow([
                conf,
                fake.sentence(nb_words=6),
                fake.random_element(institucion_cuits)
            ])
    return Confe

def generate_docente_dicta_conferencia_csv(filename, docente_legajos, cursos_confs, num_rows):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['curso_Conf', 'legajo', 'desde', 'hasta'])
        for _ in range(num_rows):
            desde = fake.date()
            hasta = fake.date()
            while hasta < desde:
                hasta = fake.date()
            writer.writerow([
                fake.random_element(cursos_confs),
                fake.random_element(docente_legajos),
                desde,
                hasta
            ])

def generate_actividades_investigacion_csv(filename, institucion_cuits, num_rows):
    Investigacion=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['investigacion', 'area_principal', 'categoria', 'institucion'])
        for _ in range(num_rows):
            inv=fake.unique.random_int(min=1000, max=99999999)
            Investigacion.append(inv)
            writer.writerow([
                inv,
                fake.word(),
                fake.word(),
                fake.random_element(institucion_cuits)
            ])
    return Investigacion

def generate_docente_participa_investigacion_csv(filename, docente_legajos, investigaciones, num_rows):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Legajo', 'investigacion', 'desde', 'hasta', 'dedicación'])
        for _ in range(num_rows):
            desde = fake.date()
            hasta = fake.date()
            while hasta < desde:
                hasta = fake.date()

            writer.writerow([
                fake.random_element(docente_legajos),
                fake.random_element(investigaciones),
                desde,
                hasta,
                fake.random_int(min=1, max=40)
            ])

def generate_titulos_csv(filename, num_rows):
    Titulo=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['idtitulo', 'nivel', 'nombre'])
        for _ in range(num_rows):
            Tit=fake.unique.random_int(min=1, max=10000000)
            Titulo.append(Tit)
            writer.writerow([
                Tit,
                fake.word(),
                fake.word()
            ])
    return Titulo

def generate_docente_obtiene_titulo_csv(filename, docente_legajos, titulos_ids, num_rows):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['idTitulo', 'Legajo', 'Desde', 'Hasta'])
        for _ in range(num_rows):
            desde = fake.date()
            hasta = fake.date()
            while hasta < desde:
                hasta = fake.date()

            writer.writerow([
                fake.random_element(titulos_ids),
                fake.random_element(docente_legajos),
                desde,
                hasta
            ])

def generate_universidad_brinda_titulo_csv(filename, titulos_ids, universidades_cuits, num_rows):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['idTitulo', 'Universidad'])
        for _ in range(num_rows):
            writer.writerow([
                fake.random_element(titulos_ids),
                fake.random_element(universidades_cuits)
            ])

def generate_actividades_extension_universitaria_csv(filename, universidades_cuits, num_rows):
    Extension=[]
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['idActividad', 'acciones', 'cargo', 'CUIT'])
        for _ in range(num_rows):
            Ext=fake.unique.random_int(min=1000, max=99999999)
            Extension.append(Ext)
            writer.writerow([
                Ext,
                fake.sentence(nb_words=6),
                fake.job(),
                fake.random_element(universidades_cuits)
            ])
    return Extension

def generate_docente_impulsa_actividad_ext_csv(filename, docente_legajos, actividades_ext_ids, num_rows):
    with open(os.path.join(directory, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['desde', 'hasta', 'id_actividad_ext', 'Legajo', 'dedicación'])
        for _ in range(num_rows):
            desde = fake.date()
            hasta = fake.date()
            while hasta < desde:
                hasta = fake.date()

            writer.writerow([
                desde,
                hasta,
                fake.random_element(actividades_ext_ids),
                fake.random_element(docente_legajos),
                fake.random_int(min=1, max=40)
            ])








# Generar archivos CSV
docente_legajos = generate_docente_csv('Docente.csv', 1000000)
contacto_numeros = generate_contactos_csv('Contactos.csv', 20000)
publicaciones_publi = generate_publicaciones_csv('Publicaciones.csv', 20000)
reuniones_reu = generate_reuniones_cientificas('Reuniones.csv', 20000)
generate_idiomas_csv('Idiomas.csv', 20000)
generate_docente_posee_contactos_csv('DocenteContacto.csv', docente_legajos, contacto_numeros)
generate_docente_participa_reuniones_csv('DocentesReuniones.csv', docente_legajos, reuniones_reu)
generate_docente_tiene_publicaciones_csv('DocentePublicaciones.csv', docente_legajos, publicaciones_publi)
generate_pasividad_obtenida_csv('PasividadObtenida.csv',docente_legajos, 20000)
ubicaciones = generate_ubicacion_csv('Ubicaciones.csv', 20000)
domicilios = generate_domicilio_csv('Domicilio.csv', ubicaciones, 20000)
institucion_cuits=generate_institucion_csv('Institucion.csv', domicilios, 20000)
universidades_cuits=generate_universidad_csv('Universidad.csv', 20000, institucion_cuits)
empresa_cuits=generate_empresa_csv('Empresa.csv', 20000, institucion_cuits)
tareas_no_oficiales=generate_tareas_no_oficiales_csv('tareasnooficiales.csv', institucion_cuits, 20000)
generate_docente_realiza_tarea_no_oficiales_csv('DocenteRealizaTareasNoOficiales.csv', docente_legajos, tareas_no_oficiales)
antecedentes_ids=generate_antecedentes_csv('Antecedentes.csv', docente_legajos, 20000)
antecedentes_docentesids=generate_antecedentes_docentes_csv('AntecedentesDocentes.csv', antecedentes_ids, universidades_cuits, 20000)
generate_antecedentes_profesionales_csv('AntecedentesProfesionales.csv', antecedentes_ids, empresa_cuits, 20000)
generate_horas_csv('Horas.csv', antecedentes_docentesids, 20000)
seguro = generate_seguro_csv('Seguro.csv', docente_legajos, institucion_cuits, 20000)
Obra_Social=generate_obra_social_csv('ObraSocial.csv', docente_legajos, institucion_cuits, 20000)
Familiar=generate_familiar_csv('Familiar.csv', domicilios, 20000)
generate_docente_afilia_familiar_csv('DocenteAfiliaFamiliar.csv', docente_legajos, Familiar, 20000)
generate_seguro_beneficia_familiar_csv('SeguroBeneficiaFamiliar.csv', seguro, Familiar, 20000)
generate_obra_afilia_familiar_csv('DocenteObraAfiliaFamiliar.csv', Obra_Social, Familiar, 20000)
generate_docente_tiene_domicilio_csv('DocenteTieneDomicilio.csv', docente_legajos, domicilios, 20000)
Curso_Conf=generate_curso_oconf_csv('Curso_Conferencia.csv', institucion_cuits, 20000)
generate_docente_dicta_conferencia_csv('DocenteDicataConferencia.csv', docente_legajos, Curso_Conf, 20000)
investigacion=generate_actividades_investigacion_csv('ActividadesInvestigacion.csv', institucion_cuits, 20000)
generate_docente_participa_investigacion_csv('DocenteParticipaInvestigacion.csv', docente_legajos, investigacion, 20000)
Titulo=generate_titulos_csv('Titulo.csv', 20000)
generate_docente_obtiene_titulo_csv('DocenteObtieneTitutlo.csv', docente_legajos, Titulo, 20000)
generate_universidad_brinda_titulo_csv('UniversidadBrindaTitulo.csv', Titulo, universidades_cuits, 20000)
Extension=generate_actividades_extension_universitaria_csv('ActividadesExtensionUniversitaria.csv', universidades_cuits, 20000)
generate_docente_impulsa_actividad_ext_csv('DocenteImpulsaActividadExt.csv', docente_legajos, Extension, 20000)

print("Archivos CSV generados exitosamente en:", directory)
