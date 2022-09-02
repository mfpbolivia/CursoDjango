from django.db import models

# Create your models here.
class Autores(models.Model):
    idAutor =models.BigAutoField(primary_key=True)
    autor = models.CharField(max_length=50)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.autor)

class Categorias(models.Model):
    idCategoria =models.BigAutoField(primary_key=True)
    Categoria = models.CharField(max_length=50)    

    def __str__(self):
        txt = "{0}"
        return txt.format(self.Categoria)

class Editoriales(models.Model):
    idEditorial =models.BigAutoField(primary_key=True)
    Editorial = models.CharField(max_length=50)    

    def __str__(self):
        txt = "{0}"
        return txt.format(self.Editorial)

class Libros(models.Model):
    idAsin = models.BigAutoField(primary_key=True)
    Titulo = models.CharField(max_length=50)
    Fecha_Lanzamiento = models.DateField(auto_now=False, auto_now_add=False)
    Autor = models.ForeignKey(Autores,null=False,blank=False, on_delete=models.CASCADE)
    Categoria = models.ForeignKey(Categorias,null=False,blank=False, on_delete=models.CASCADE)
    Editorial = models.ForeignKey(Editoriales,null=False,blank=False, on_delete=models.CASCADE)
    Idiomas = [
        ('Esp', 'Español'),
        ('Ing', 'Ingles'),
        ('Fra', 'Frances'),
        ('Ale', 'Aleman'),
        ('Chi', 'Chino')
    ]
    Idioma = models.CharField(max_length=3,choices=Idiomas,default='ESP')
    Paginas = models.IntegerField()
    Descripcion = models.TextField()

    def __str__(self):
        txt = "ASIN:{0}, {1},Lanzamiento: {2}, Autor: {3}, Categoria:{4}, Editorial: {5},Idioma={6}"
        fechaLan = self.Fecha_Lanzamiento.strftime("%d/%m/%Y")    
        return txt.format(self.idAsin,self.Titulo,fechaLan,self.Autor,self.Categoria,self.Editorial,self.Idioma)    