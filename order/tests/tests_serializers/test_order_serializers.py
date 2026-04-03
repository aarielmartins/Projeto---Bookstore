import pytest
from django.contrib.auth.models import User
from order.models import Order
from product.models import Product, Category
from order.serializers import OrderSerializer
from product.serializers import ProductSerializer, CategorySerializer


@pytest.mark.django_db
def test_order_serialization():
    user = User.objects.create_user(username="testuser", password="password")

    category = Category.objects.create(
        title="Tecnologia",
        slug="tecnologia",
        description="Categoria de tecnologia",
        active=True,
    )

    product1 = Product.objects.create(
        title="Smartphone", description="Um smartphone top", price=2000, active=True
    )
    product2 = Product.objects.create(
        title="Tablet", description="Um tablet top", price=1500, active=True
    )

    product1.category.add(category)
    product2.category.add(category)

    order = Order.objects.create(user=user)
    order.product.add(product1, product2)

    serializer = OrderSerializer(order)

    # Montando os produtos serializados
    serialized_products = []
    for prod in order.product.all():
        data = ProductSerializer(prod).data
        data["category"] = CategorySerializer(prod.category.all(), many=True).data
        serialized_products.append(data)

    expected_data = {
        "product": serialized_products,
        "total": 3500,
        "user": order.user.id,
    }

    assert serializer.data == expected_data
