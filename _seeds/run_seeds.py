import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

def run_all_seeds():
    print("Starting complete database seeding...")
    
    # Ordem CRUCIAL devido às dependências
    from anchorpoint_category_seed import seed_anchorpoint_categories
    from city_seed import seed_cities
    from anchorpoint_seed import seed_anchorpoints
    from route_seed import seed_routes
    from event_aux_seed import seed_event_aux_tables
    from event_seed import seed_events
    from warning_seed import seed_warnings
    from user_seed import seed_users
    from relationship_seed import seed_relationships
    from form_response_seed import seed_form_responses
    from auth_seed import seed_auth_data
    
    seed_anchorpoint_categories()
    seed_cities()
    seed_anchorpoints()
    seed_routes()
    seed_event_aux_tables()
    seed_events()
    seed_warnings()
    seed_users()
    seed_relationships()
    seed_form_responses()
    seed_auth_data()
    
    print("✅ ALL SEEDS COMPLETED SUCCESSFULLY!")
    print("📊 Estatísticas:")
    from django.apps import apps
    for model in apps.get_models():
        if model._meta.app_label == 'your_app_name':  # substitua pelo nome do seu app
            print(f"  {model._meta.model_name}: {model.objects.count()} registros")

if __name__ == '__main__':
    run_all_seeds()