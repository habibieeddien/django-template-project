*** Created By habibie@bnpb.go.id ***

### Django Start Project ###

Untuk membuat project Django, ketik di terminal:

`$ django-admin startproject your_project_name`


### Django Start App ###

Untuk membuat `application` baru dalam project `Django`, ketik di terminal:

`$ cd applications`

`$ python ../manage.py startapp app1`

maka akan terbentuk folder `app1` yang otomatis berisi file:

    * __init__.py

    * admin.py

    * apps.py

    * models.py

    * tests.py

    * views.py

### Django Create Model (Create Table on DB) ###

Setelah mendefinisikan `models.py` lakukan sintak berikut di terminal:

`$ python manage.py makemigrations`

`$ python manage.py migrate`

maka akan otomatis update struktur / schema isi DB

### Run Development Server ###

Untuk run server development, ketik di terminal:

`$ python manage.py runserver`

### Deployment with Apache + mod_wsgi ###

* install apache2-lib-mod_wsgi
* enable mod_wsgi: `$ sudo a2enmod wsgi`
* setting apache di `sudo vi /etc/apache2/site-available/000-default.conf` :

<apache-script>
    <VirtualHost *:80>
        ... ### your_settings_apache2 above ###
        
        Alias /static /home/your_name/your_project/core/static
        
        <Directory /home/your_name/your_project/core/static>
                Require all granted
        </Directory>

        <Directory /home/your_name/your_project/core>
                <Files wsgi.py>
                       Require all granted
                </Files>
       </Directory>

        WSGIDaemonProcess your_project python-home=/home/your_name/your_project/your_projectenv python-path=/home/your_name/your_project
        WSGIProcessGroup your_project
        WSGIScriptAlias /your_url_name /home/your_name/your_project/core/wsgi.py
    </VirtualHost>
</apache-script>

### Django Template Language (DTL) ###

* `{{ your_variable }}` --> untuk input variabel dari code Python ke HTML
* `{% block your_variable_htmlTag %} Some_Text_Will_Replace_Here {% endblock your_variable_htmlTag %}` --> untuk override antar template HTML yang berbeda content.