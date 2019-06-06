from rest_framework import serializers

from core.models import Tag, Ingredient, Recipe, Diet, Allergy, Course, Cousine, Holiday, Nutritions
""""""
class DietSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diet
        fields = ('id', 'name')
        read_only_fields = ('id',)


class AllergySerializer(serializers.ModelSerializer):

    class Meta:
        model = Allergy
        fields = ('id', 'name')
        read_only_fields = ('id',)


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name')
        read_only_fields = ('id',)


class CousineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cousine
        fields = ('id', 'name')
        read_only_fields = ('id',)


class HolidaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Holiday
        fields = ('id', 'name')
        read_only_fields = ('id',)

class NutritionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nutritions
        fields = ('id', 'name','calories', 'fat_calories', 'total_fat', 'sat_fat', 'trans_fat', 'sodium', 'total_carb', 'fibers', 'sugar', 'proteins', 'vitamins','calcium', 'iron' )
        read_only_fields = ('id',)

""""""
class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset= Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset= Tag.objects.all()
    )
    """"""
    diet = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset= Diet.objects.all()
    )

    allergy= serializers.PrimaryKeyRelatedField(
        many = True,
        queryset= Allergy.objects.all()
    )

    course = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset= Course.objects.all()
    )

    cousine = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset= Cousine.objects.all()
    )
    
    holiday = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset= Holiday.objects.all()
    )

    nutritions = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset= Nutritions.objects.all()
    )

    """"""


    class Meta:
        model = Recipe
        fields = ('id', 'title', 'ingredients', 'tags','diet', 'allergy' ,'course', 'cousine', 'holiday', 'nutritions', 'time_minutes', 'price', 'link', 'description', 'list_date', 'is_published')
        read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    ingredients = IngredientSerializer(many=True,read_only=True)
    tags = TagSerializer(many=True,read_only=True)
    """"""
    diet = DietSerializer(many=True,read_only=True)
    allergy = AllergySerializer(many=True,read_only=True)
    course = CourseSerializer(many=True,read_only=True)
    cousine = CousineSerializer(many=True,read_only=True)
    holiday = HolidaySerializer(many=True,read_only=True)
    nutritions = NutritionsSerializer(many=True,read_only=True)




class RecipeImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id', 'image')
        read_only_fields = ('id',)



