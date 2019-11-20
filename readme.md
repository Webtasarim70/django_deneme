https://tutorial.djangogirls.org/tr/django_start_project/

# çalışma ortamı (linux), sanal makina kurulumu, django kurulumu
  - python3 kurulu, sadece python komutu varsayılan başka bir sürümü çalıştırabilir

- sanal ortam oluşturma $ python3 -m venv myvenv çalışmaz ise $ sudo apt install python3-venv
- sanal ortamı aktif etmek $ source myvenv/bin/activate
- jango yüklemek için kullanacağımız yazılım olan pip'in en son versiyonuna sahip olduğundan emin olmalıyız
(myvenv) ~$ python3 -m pip install --upgrade pip
- requirements.txt ve içine Django~=2.2.4 ekleyerek kaydettik
- Django kurmak için pip install -r requirements.txt komutunu çalıstırın
- blog oluşturalım (myvenv) ~/djangogirls$ django-admin startproject mysite .
- yapı
            djangogirls
            ├───manage.py
            ├───mysite
            │        settings.py
            │        urls.py
            │        wsgi.py
            │        __init__.py
            └───requirements.txt
- manage.py site yönetimine yardımcı olan bir komut dosyasıdır. Bu dosya sayesinde, başka herhangi bir şey kurmadan bilgisayarımızda bir web sunucusunu başlatabileceğiz.

- settings.py dosyası, web sitesinizin ayarlarını içerir.
- urls.py dosyası urlresolver(urlçözümleyici) tarafından kullanılan kalıpların bir listesini içerir.

# sublime text için eklenti
  

      try SublimeJEDI

      step 1: ctrl+shift+p search - install package

      step 2: Wait for few seconds until drop down box to appear

      step 3: search Jedi - Python autocompletion and press enter

      now auto completion for python will work in sublime..

      Note: you can try Anaconda instead Jedi using same step.


# django ayarları

  mysite/settings.py TIME_ZONE = 'Europe/Istanbul'
  LANGUAGE_CODE = 'en-us'
  STATIC_URL = '/static/'
  STATIC_ROOT = os.path.join(BASE_DIR, 'static')
  ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

# veritabanı kurulumu

varsayılan sqlite3 ayarlarda kurulu
mysite/settings.py

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
     }

python manage.py migrate

# sunucuyu çalıştırma ve görme
    (myvenv) ~/djangogirls$ python manage.py runserver
  http://127.0.0.1:8000/

# blog kurulumu
    
    python manage.py startapp blog

Uygulamamızı oluşturduktan sonra, Django'ya bunu kullanmasını söylememiz lazım. Bunu mysite/settings.py dosyasından yapacağız -- kod editörümüzde açalım. INSTALLED_APPS'ı bulup ] karakterinin üzerindeki satıra 'blog', yazmamız lazım. Sonuç aşağıdaki gibi görünmeli:

  mysite/settings.py

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',
    ]

# model

Şimdi blog/models.py dosyasını açalım ve içindeki her şeyi silip şu kodu yazalım:

            blog/models.py

            from django.db import models
            from django.utils import timezone


            class Post(models.Model):
                author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
                title = models.CharField(max_length=200)
                text = models.TextField()
                created_date = models.DateTimeField(
                        default=timezone.now)
                published_date = models.DateTimeField(
                        blank=True, null=True)

                def publish(self):
                    self.published_date = timezone.now()
                    self.save()manage.py migrate blog

                def __str__(self):
                    return self.title

#modeller icin veritabanı tablo oluşturma

    python manage.py makemigrations blog
    python manage.py migrate blog

# django admin

Şimdi blog/admin.py dosyasını açarak içeriğini aşağıdaki şekilde değiştirelim:

        blog/admin.py

        from django.contrib import admin
        from .models import Post

        admin.site.register(Post)


superkullanıcı oluşturma      
  
      python manage.py createsuperuser
    #git ve github
    $ sudo apt install git

# git repo oluşturma
 
   Hatırlatma: Kullanıcı adı seçerken Türkçe karakter kullanmayın.
      $ git init
      Initialized empty Git repository in ~/djangogirls/.git/
      $ git config --global user.name "Adınız"
      $ git config --global user.email you@example.com

Git bu dizindeki tüm dizin ve dosyalardaki değişiklikleri kaydedecek, ama takip etmemesini istediğimiz bazı dosyalar var. Bunu dizinin dibinde .gitignore adında bir dosya oluşturarak yapıyoruz. Editörünüzü açın ve aşağıdaki içeriklerle yeni bir dosya yaratın:

.gitignore

          *.pyc
          *~
          __pycache__
          myvenv
          db.sqlite3
          /static
          .DS_Store

   Ve onu .gitignore ismi ile "djangogirls" dizinine kaydedin.

          $ git status
          $ git add --all .
          $ git commit -m "Django Girls uygulamam, ilk commit"
          $ git remote add origin https://github.com/<github-kullanıcı-adınız>/repoadi.git
          $ git push -u origin master
          
# pyton any where için kurulumu
          PythonAnywhere command-line
          $ pip3.6 install --user pythonanywhere
          $ pa_autoconfigure_django.py https://github.com/<github-kullanıcı-adınız>/my-first-blog.git

          (<kullanici-adiniz>.pythonanywhere.com) $ python manage.py createsuperuser

