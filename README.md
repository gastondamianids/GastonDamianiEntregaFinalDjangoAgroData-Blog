AgroDataBlog



Es un blog en Django sobre Data Science aplicada al agro en Uruguay donde los usuarios pueden compartir estados de sus cultivos, rendimientos, situación sanitaria, etc.



Funcionalidades

\- Home (`/`)

\- About (`/about/`)

\- Pages (`/pages/`): listado, búsqueda por título, detalle, crear/editar/borrar (solo autor logueado)

\- Accounts (`/accounts/`): signup, login, logout, perfil, editar perfil (avatar/bio), cambio de password

\- Messenger (`/messenger/`): inbox (recibidos/enviados), enviar, detalle (marca leído), borrar



Modelos

\- pages.Page (modelo principal con 2 charfields, contenido con ckeditor, imagen y fecha)

\- accounts.Profile (avatar, bio, birth\_date)

\- messenger.Message

\- interactions.Comment



\## Cómo correr el proyecto

1\. Crear entorno virtual (opcional) e instalar dependencias:

&nbsp;  - `pip install -r requirements.txt`

2\. Migraciones:

&nbsp;  - `python manage.py migrate`

3\. Crear superusuario (opcional):

&nbsp;  - `python manage.py createsuperuser`

4\. Correr servidor:

&nbsp;  - `python manage.py runserver`



\## Notas

\- `db.sqlite3` y `media/` están ignorados por `.gitignore`.



