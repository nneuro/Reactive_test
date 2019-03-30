
from reactive_app import create_app
from reactive_app.model import Reactives, db

app = create_app()

with app.app_context():
    reactive_name = input('Введите название реактива: ')
    react_count = input('Введите количество упаковок: ')

    new_reactive = Reactives(title = reactive_name, reactive_count = react_count)
    
    db.session.add(new_reactive)
    db.session.commit()
    print('Reactive with id {} added'.format(new_reactive.id))
