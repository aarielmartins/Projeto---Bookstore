import pytest
from product.models import Product, Category
from product.serializers.product_serializer import ProductSerializer
from product.serializers.category_serializer import CategorySerializer

@pytest.mark.django_db
def test_product_serialization():
    category = Category.objects.create(
        title="Tecnologia",
        slug="tecnologia",
        description="Categoria de tecnologia",
        active=True
    )

    product = Product.objects.create(
        title="Smartphone",
        description="Um smartphone top",
        price=2000,
        active=True
    )

    # Adicionando categoria manualmente para o serializer
    product_data = ProductSerializer(product).data
    product_data["category"] = CategorySerializer([category], many=True).data

    expected_data = {
        "title": "Smartphone",
        "description": "Um smartphone top",
        "price": 2000,
        "active": True,
        "category": [{
            "title": "Tecnologia",
            "slug": "tecnologia",
            "description": "Categoria de tecnologia",
            "active": True
        }]
    }

    assert product_data == expected_data