from sito.models import Persona, Alumno, AlumnoClase, AlumnoGrupo, Grupo
from static.utils import dd


def persona(request):
   user = request.user
   if user.is_authenticated:
       persona = Persona.objects.get(cve_persona=user.cve_persona)
       return {'persona': persona}
   else:
       return {'persona': ''}



def user_permissions_and_groups(request):
   # Check if the user is authenticated
   if request.user.is_authenticated:
       # Get the user's permissions and groups
       permissions = request.user.get_all_permissions()
       groups = request.user.groups.values_list('name', flat=True)
   else:
       permissions = set()
       groups = []


   return {
       'user_permissions': permissions,
       'user_groups': groups,
   }

def group_permission(request):
    user = request.user
    groups_list = ['Alumno', 'Administrador']
    # Verifica que el usuario este autenticado
    if user.is_authenticated:
        # Retorna el listado de todos los grupos en los que pertenece el usuario
        groups = user.groups.values_list('name', flat=True)
        # Recorre el listado de grupos
        for i in range(0, len(groups)):
            # Valida que el grupo este dentro de los permitidos
            for g in range(0, len(groups_list)):
                if groups[i] == groups_list[g]:
                    # Si el grupo es permitido se retorna
                    return {"grupo": groups[i]}
    else:
        # Si el usuario no esta autenticado, se retorna una variable vacía
        return {"grupo": ""}

def get_alumnos_clase(request):
    user = request.user
    r = []
    if user.is_authenticated:
        alumnos = AlumnoClase.objects.filter(matricula=user.login).values_list('cve_docente', flat=True)
        for al in alumnos:
            if al not in r:
                r.append(al)
        return {'profesor': r}
    else:
        return {'profesor': ''}

def get_grupo(request):
    user = request.user
    if user.is_authenticated and user.login != 'ramon':
        grupos = []
        cve_grupo = AlumnoGrupo.objects.filter(matricula=user.login).values_list('cve_grupo', flat=True)
        for cve in cve_grupo:
            grupo_name = Grupo.objects.get(cve_grupo=cve)
            grupos.append(grupo_name.nombre)
        for name_grupo in grupos[::-1]:
            if name_grupo:
                break
        return {'grupo_name': name_grupo}
    else:
        return {'grupo_name': ''}
