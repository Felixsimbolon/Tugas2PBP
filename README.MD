# Toko Musik John Lennon
# Deployment link
http://jeremi-felix-tokomusikjohnlennon.pbp.cs.ui.ac.id/

Sebuah proyek Django sederhana sebagai Tugas Mata Kuliah Pemrograman Berbasis Platform oleh Jeremi Felix Adiyatma 2306219575 kelas PBP B. 
## Tugas 2

### Proses Pembuatan Projek Django
1. Membuat sebuah _repository_ Github baru bernama ```Tugas2PBP```
2. Membuat inisial push ke dalam repo itu dalam bentuk readme.md
3. Di direktori asal Membuat _virtual environment_ Python baru dengan command:

    ```bash
    python -m venv env
    ```
4. Menyalakan _virtual environment_ Python baru dengan command:
    ```bash
    source env/bin/activate
    ```
5. terdapat error Execution_Policy, sehingga saya harus menjalankan command 
    ``` bash
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ``` 
    di windows powershell agar dapat mengaktivasikan virtual environment.

6. Membuat berkas _requirements_ dengan 
    isi dari requirements.txt
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
7. Meng-_install requirements_ dengan pip
    ```bash
    Python -m pip install -r requirements.txt
    ```
    
8. Membuat proyek Django baru dengan command:
    ```bash
    django-admin startproject toko_musik_john_lennon .
    ```
9. Mengubah ```ALLOWED_HOSTS``` di file ```settings.py``` dengan menambahkan ```"localhost"``` dan ```"127.0.0.1"```agar proyek ini bisa 
    dijalankan di host lokal

9. Membuat aplikasi ```main``` dengan command:
    ```bash
    python manage.py startapp main
    ```
10. Menambahkan ```main```  ke ```INSTALLED_APPS``` pada file ```settings.py``` di direktori ```toko_musik_john_lennon``` 

11. Modifikasi ```models.py``` menjadi:
    ```python
    from django.db import models

    class Product(models.Model):
        item = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
    ```
12. Melakukan migrasi dengan command:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
13. Membuat direktori templates dan menambahkan file ```main.html``` serta memodifikasi file tersebut

14. Menambahkan fungsi show_main untuk me-_render_ laman main pada file ```views.py```:
    ```python
    from django.shortcuts import render

    def show_main(request):
        context = {
           'name' : 'Jeremi Felix Adiyatma',
            'npm' : '2306219575',
            'kelas' : 'PBP B',
            'item Name' : 'Gitar Michael Jackson',
            'price': 6000000,
            'description': 'This was the guitar Michael Used on his tour in early 2009 months before he died'
        }

        return render(request, "main.html", context)

    ```
15. Me-_routing_ url pada file ```urls.py``` di direktori ```toko_musik_john_lennon``` sehingga isi file ```urls.py``` menjadi:
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```

16. Melakukan routing pada aplikasi ```main``` pada file ```urls.py``` di direktori main:
    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

17. Mengetest aplikasi pada localhost dengan command:
    ```
    python manage.py runserver
    ```
    kemudian membuka ```http://localhost:8000/``` di _browser_

18. Membuat proyek baru di pws dengan nama tokomusikjohnlennon
19. menambahkan allowed host dengan url depoloyment pws 
    ```
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "jeremi-felix-tokomusikjohnlennon.pbp.cs.ui.ac.id"]
    ```
20. add branch pws dengan command :
    ```
    git remote add pws https://pbp.cs.ui.ac.id/jeremi.felix/tokomusikjohnlennon
    ```
21. melakukan push ke repo git serta ke pws untuk deploy dengan command:
    ```
    git add .
    git commit -m "pesan"
    git push origin main
    git push pws main:master
    ```


### Jawaban dari Pertanyaan

2. **Bagan Arsitektur Django**
![](static/images/raster/Bagan.png)
Permintaan _request_ dari pengguna terlebih dahulu diproses untuk diarahkan ke View yang tepat. Setelah itu, View akan berinteraksi dengan Model untuk mengambil atau memperbarui data, dan kemudian menggunakan Template untuk menampilkan informasi yang diperlukan. Akhirnya, hasil tersebut dikirim kembali ke pengguna dalam bentuk _response_.

3. **Fungsi Git dalam Pengembangan Perangkat Lunak:**

Git dalam pengembangan perangkat lunak berfungsi sebagai alat yang sangat penting untuk mengelola dan melacak perubahan pada kode. Sebagai sistem kontrol versi terdistribusi, Git memungkinkan pengembang untuk bekerja secara bersamaan pada proyek yang sama tanpa khawatir tentang konflik perubahan. Setiap perubahan yang dilakukan pada kode atau file dilacak secara detail, memungkinkan tim untuk melihat riwayat versi, menguji perubahan, dan memulihkan versi sebelumnya jika diperlukan.

Git juga mendukung kolaborasi tim dengan memfasilitasi pembuatan cabang (branch) yang memungkinkan pengembang bekerja secara terpisah pada fitur baru atau perbaikan bug tanpa memengaruhi kode utama. Setelah perubahan siap, cabang tersebut dapat digabungkan (merge) ke cabang utama. Setiap perubahan teratribusi pada pengembang yang melakukannya, sehingga memudahkan pelacakan kontribusi individu. Selain itu, Git memungkinkan pembalikan perubahan dengan mudah jika terjadi kesalahan, dan mendukung kesesuaian waktu, di mana beberapa pengembang dapat mengerjakan kode secara bersamaan tanpa saling mengganggu. Dengan semua fitur ini, Git membantu menjaga integritas proyek perangkat lunak, memastikan kolaborasi yang efisien, dan mempermudah pengelolaan proyek.

4. **Mengapa Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?**

Django sering dipilih sebagai framework awal untuk pengembangan perangkat lunak karena menyederhanakan banyak tugas yang kompleks, memungkinkan pengembang pemula fokus pada logika aplikasi. Fitur "batteries included"-nya menyediakan solusi bawaan untuk kebutuhan umum seperti autentikasi pengguna, manajemen basis data, dan routing URL, sehingga tidak perlu terlalu banyak alat tambahan.

Selain itu, Django sangat skalabel dan cocok untuk proyek kecil maupun besar, menjadikannya platform belajar yang fleksibel. Dokumentasinya yang lengkap juga mempermudah pemula dalam mempelajari cara membangun aplikasi web.

5. **Mengapa Model pada Django Disebut Sebagai ORM?**

Model dalam Django disebut sebagai ORM (Object-Relational Mapping) karena fungsinya yang menghubungkan antara objek dalam kode Python dengan tabel dalam basis data relasional. Dengan ORM, pengembang dapat berinteraksi dengan basis data menggunakan objek Python tanpa harus menulis kueri SQL manual, sehingga mempermudah proses manipulasi data seperti membuat, membaca, memperbarui, atau menghapus data dalam tabel. ORM juga memberikan abstraksi dari basis data, artinya pengembang tidak perlu memikirkan detail-detail kompleks SQL dan bisa fokus pada logika bisnis aplikasi. Django ORM juga mendukung kompatibilitas antar berbagai sistem manajemen basis data, seperti SQLite, MySQL, dan PostgreSQL, sehingga pengembang bisa beralih antar platform basis data tanpa mengubah kode. Hal ini menjadikan ORM sebagai alat yang sangat efisien dan fleksibel dalam pengelolaan basis data di Django.


## Tugas 3

2. memodifikasi settings.py di direktori toko_musik_john_lennon di bagian TEMPLATES:
```
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
'APP_DIRS': True,
```
3. mengubah main.html menjadi:
```
 {% extends 'base.html' %}
 {% block content %}
 <h1>Mental Health Tracker</h1>

 <h5>NPM: </h5>
 <p>{{ npm }}<p>

 <h5>Name:</h5>
 <p>{{ name }}</p>

 <h5>Class:</h5>
 <p>{{ class }}</p>
 {% endblock content %}
 ```
4. delete file db.sqlite3
5. Mengubah models.py menjadi
```
from django.db import models
import uuid 

class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    item = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    item_satisfactory = models.IntegerField()
```
6. make migrations and migrate

7. Membuat forms.py di direktori main dengan isi
```
from django.forms import ModelForm
from main.models import ProductEntry

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["item", "description", "item_satisfactory"]
```
8. menambahkan bagian import di views.py:
```
from django.shortcuts import render, redirect   
from main.forms import MoodEntryForm
from main.models import MoodEntry
```

9. Menambahkan Method create_product_entry untuk menambah entri database di file views.py di direktori main
```
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
10. Routing URL ke laman yang bersangkutan di file urls.py di direktori main
```
urlpatterns = [
    ...
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    ...
]
```
11. Membuat file baru bernama create_product_entry.html di main/templates/

12. Menambahkan folder templates di direktori utama dan base.html sebagai basis dari laman-laman lain



Mengimplementasikan database ke dalam laman utama main.html dan juga menjadi perpanjangan dari base.html di direktori utama

...
<table>
    <tr>
        <th>Name</th>
        <th>Amount</th>
        <th>Description</th>
        <th></th>
    </tr>

    {% for salt in salts %}
        <tr>
            <td>{{salt.name}}</td>
            <td>{{salt.amount}}</td>
            <td>{{salt.description}}</td>
            <td id="delete">
                <a href="{% url 'main:delete' salt.id %}">
                    <button class="tablebutton">
                        Delete
                    </button>
                </a>
            </td>
        </tr>
    {% endfor %}
</table>
...
Menggunakan folder static untuk mengorganisir aset-aset yang digunakan seperti gambar dan stylesheet CSS untuk mempercantik laman

Membuat app baru bernama debug untuk melihat tampilan JSON dan XML dari app main

Menambahkan fungsi-fungsi yang diperlukan untuk menampilkan JSON dan XML baik secara keseluruhan maupun per entri database

def show_xml(request):
    data = Salts.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Salts.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Salts.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Salts.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
Merouting kembali URL yang bersangkutan di file urls.py di direktori debug

urlpatterns = [
    path('json/', show_json, name='json'),
    path('xml/', show_xml, name='xml'),
    path('json/<int:id>/', show_json_by_id, name='json_by_id'),
    path('xml/<int:id>/', show_xml_by_id, name='xml_by_id'),
]
Mengetest aplikasi pada localhost dengan command:

python manage.py runserver
kemudian membuka http://localhost:8000/ di browser
