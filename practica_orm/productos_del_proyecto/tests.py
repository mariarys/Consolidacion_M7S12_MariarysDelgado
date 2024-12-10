from django.test import TestCase
from django.urls import reverse

class ProductosURLsTests(TestCase):
    def test_url_producto_insertar_status_code(self):
        response = self.client.get('/agregar/')
        self.assertEqual(response.status_code, 200)

    def test_url_insertar_producto_reversa(self):
        url = reverse('agregar_productos')  # Cambiado a 'agregar_productos'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_correct_template_for_producto_insertar(self):
        response = self.client.get(reverse('agregar_productos'))  # Cambiado a 'agregar_productos'
        self.assertTemplateUsed(response, 'supermercado/agregar_producto.html')

    def test_template_content(self):
        response = self.client.get(reverse('agregar_productos'))  # Cambiado a 'agregar_productos'
        self.assertContains(response, '<label for="nombre" class="form-label">Nombre del Producto</label>')
        self.assertContains(response, '<input type="text" class="form-control" id="nombre" name="nombre" required placeholder="Ingresar el nombre del Producto">')
