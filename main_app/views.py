from django.shortcuts import render

finches = [
    {
        'name': 'Gouldian Finch',
        'species': 'Chloebia gouldiae',
        'description': 'Brightly colored with a distinctive rainbow pattern',
        'habitat': 'Grasslands and savannas of northern Australia',
        'diet': 'Seeds, grains, and some insects',
        'conservation_status': 'Near Threatened'
    },
    {
        'name': 'Zebra Finch',
        'species': 'Taeniopygia guttata',
        'description': 'Small finch with distinctive black and white stripes',
        'habitat': 'Arid and semi-arid regions of Australia',
        'diet': 'Seeds, grains, and some insects',
        'conservation_status': 'Least Concern'
    },
    {
        'name': 'Canary',
        'species': 'Serinus canaria',
        'description': 'Small yellow songbird, popular as a pet',
        'habitat': 'Originally from the Canary Islands, now domesticated',
        'diet': 'Seeds, fruits, and some insects',
        'conservation_status': 'Domesticated'
    },
    {
        'name': 'Hawfinch',
        'species': 'Coccothraustes coccothraustes',
        'description': 'Large finch with a massive beak for cracking seeds',
        'habitat': 'Woodlands and forests across Europe and Asia',
        'diet': 'Seeds, nuts, and berries',
        'conservation_status': 'Least Concern'
    },
    {
        'name': "Darwin's Ground Finch",
        'species': 'Geospiza fortis',
        'description': 'One of Darwin\'s finches, with a beak adapted for eating seeds',
        'habitat': 'Galapagos Islands',
        'diet': 'Seeds, insects, and plant matter',
        'conservation_status': 'Least Concern'
    }
]


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    return render(request, 'index.html', {
        'finches': finches
    })
