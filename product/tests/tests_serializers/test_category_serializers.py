import pytest
from product.models import Category
from product.serializers.category_serializer import CategorySerializer


@pytest.mark.django_db
def test_category_serialization():
    category = Category.objects.create(
        title="Tecnologia",
        slug="tecnologia",
        description="Categoria de tecnologia",
        active=True,
    )

    serializer = CategorySerializer(category)
    assert serializer.data == {
        "title": "Tecnologia",
        "slug": "tecnologia",
        "description": "Categoria de tecnologia",
        "active": True,
    }
