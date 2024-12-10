from django.test import TestCase
from .models import Product, Order

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Test Product", description="Test Description", price=10.00)

    def test_product_creation(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.description, "Test Description")

class OrderTestCase(TestCase):
    def setUp(self):
        product = Product.objects.create(name="Test Product", description="Test Description", price=10.00)
        Order.objects.create(product=product, quantity=2)

    def test_order_creation(self):
        order = Order.objects.get(product__name="Test Product")
        self.assertEqual(order.quantity, 2)
