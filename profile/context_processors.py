from .models import Electrician

def global_electricians(request):
    """
    Fetches all electricians globally and makes them available in all templates.
    """
    electricians = Electrician.objects.all()
    return {'electricians': electricians}
