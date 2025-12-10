from .models import Collaborators, URL

def run():
    # Criação dos colaboradores
    mateus = Collaborators.objects.create(name='Mateus Peres', position='Front-End & UI Dev')
    jeremias = Collaborators.objects.create(name='Jeremias Piontkoski', position='Back-End Dev & PMO')
    vanius = Collaborators.objects.create(name='Vanius Zapalowski', position='Orientador')
    andre = Collaborators.objects.create(name='André del Mestre', position='Professor Adjunto')
    rodrigo = Collaborators.objects.create(name='Rodrigo Baptista', position='Apoiador do Projeto')
    pedro_R = Collaborators.objects.create(name='Pedro Rodrigues', position='Front-End Dev')
    regis = Collaborators.objects.create(name='Regis Brasil', position='Front-End Dev')
    marcelo = Collaborators.objects.create(name='Marcelo Augusto', position='Back-End Dev')
    pedro_A = Collaborators.objects.create(name='Pedro Ambrosini', position='Front-End Dev')
    gabriel = Collaborators.objects.create(name='Gabriel Umann', position='Front-End Dev')

    # URLs de cada colaborador
    URL.objects.create(collaborator=mateus, url='https://www.linkedin.com/in/mateuspereslopes/')
    URL.objects.create(collaborator=mateus, url='https://www.instagram.com/yperessx/')
    URL.objects.create(collaborator=mateus, url='https://github.com/mateussperess')

    URL.objects.create(collaborator=jeremias, url='https://www.linkedin.com/in/jeremias-piontkoski-740a8a267/')
    URL.objects.create(collaborator=jeremias, url='https://www.instagram.com/jeremias_piontkoski/')
    URL.objects.create(collaborator=jeremias, url='https://github.com/JeremiasPiontkoski')

    URL.objects.create(collaborator=vanius, url='https://www.linkedin.com/in/vzapalowski/')
    URL.objects.create(collaborator=vanius, url='https://github.com/vzapalowski')
    URL.objects.create(collaborator=vanius, url='https://www.facebook.com/vzapalowski')

    URL.objects.create(collaborator=andre, url='https://www.linkedin.com/in/andr%C3%A9-lu%C3%ADs-del-mestre-martins-421b43a1/')
    URL.objects.create(collaborator=andre, url='https://www.instagram.com/andredelmestre/')
    URL.objects.create(collaborator=andre, url='https://github.com/andredelmestre')

    URL.objects.create(collaborator=rodrigo, url='https://www.instagram.com/ulbra.saojeronimo')
    URL.objects.create(collaborator=rodrigo, url='https://www.facebook.com/ulbrasaojeronimo')
    URL.objects.create(collaborator=rodrigo, url='https://www.ulbra.br/sao-jeronimo')

    URL.objects.create(collaborator=pedro_R, url='https://www.linkedin.com/in/pedro-rodrigues-da-cunha-523137252/')
    URL.objects.create(collaborator=pedro_R, url='https://www.instagram.com/roddriguespedro/')
    URL.objects.create(collaborator=pedro_R, url='https://github.com/rodriguespedro22')

    URL.objects.create(collaborator=regis, url='https://www.linkedin.com/in/regis-brasil/')
    URL.objects.create(collaborator=regis, url='https://www.instagram.com/regiswolfs/')
    URL.objects.create(collaborator=regis, url='https://github.com/regisbrasil')

    URL.objects.create(collaborator=marcelo, url='https://www.linkedin.com/in/marcelo-augusto-costa-oliveira-384610245/')
    URL.objects.create(collaborator=marcelo, url='https://www.instagram.com/marcelo_a504/')
    URL.objects.create(collaborator=marcelo, url='https://github.com/Marcelo-Augustto')

    URL.objects.create(collaborator=pedro_A, url='https://www.linkedin.com/in/pedro-ambrosini')
    URL.objects.create(collaborator=pedro_A, url='https://www.instagram.com/pedro_ambrosini/')
    URL.objects.create(collaborator=pedro_A, url='https://github.com/roxxedo')
    
    URL.objects.create(collaborator=gabriel, url='https://www.linkedin.com/in/gabriel-umann-machado-7406582b7/')
    URL.objects.create(collaborator=gabriel, url='https://www.instagram.com/umann.g/')
    URL.objects.create(collaborator=gabriel, url='https://github.com/gabrielumann')