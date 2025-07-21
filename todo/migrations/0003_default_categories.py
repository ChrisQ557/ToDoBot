from django.db import migrations

def create_default_categories(apps, schema_editor):
    Category = apps.get_model('todo', 'Category')
    default_categories = [
        'General Tasks',
        'Appliances',
        'Home Automation',
        'Entertainment',
    ]
    for category_name in default_categories:
        Category.objects.get_or_create(name=category_name)

class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_category_task_category'),
    ]

    operations = [
        migrations.RunPython(create_default_categories),
    ]
