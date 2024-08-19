from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def get_recipe(request, recipe):
    try:
        servings = int(request.GET.get('servings', 1))
    except ValueError:
        servings = 0

    context_recipe = DATA.get(recipe, None)
    if context_recipe is not None:
        context_recipe = {ingredient: amount * servings for ingredient,
                          amount in context_recipe.items()}

    context = {'recipe': context_recipe}
    return render(request, 'calculator/index.html', context)
