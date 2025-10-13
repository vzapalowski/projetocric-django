from event.models import EventBond, EventHowknew

def seed_event_aux_tables():
    # EventBond
    bonds = [
        {'name': 'Cicloturista'},
        {'name': 'Atleta Amador'},
        {'name': 'Profissional'},
        {'name': 'Iniciante'},
        {'name': 'Lazer'}
    ]
    
    for bond_data in bonds:
        EventBond.objects.create(**bond_data)

    # EventHowknew
    how_knew_options = [
        {'name': 'Redes Sociais'},
        {'name': 'Amigos'},
        {'name': 'Site'},
        {'name': 'Outro Ciclista'},
        {'name': 'Panfleto'},
        {'name': 'Jornal'}
    ]
    
    for option_data in how_knew_options:
        EventHowknew.objects.create(**option_data)

    print("Event auxiliary tables seeded successfully!")