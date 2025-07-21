from django.db import migrations

def enforce_default_categories(apps, schema_editor):
    Category = apps.get_model('todo', 'Category')
    default_categories = [
        'General Tasks',
        'Appliances',
        'Home Automation',
        'Entertainment',
    ]
    # Delete all categories not in the default list
    Category.objects.exclude(name__in=default_categories).delete()
    # Ensure all default categories exist
    for category_name in default_categories:
        Category.objects.get_or_create(name=category_name)

class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_remove_task_action_remove_task_device_type_and_more'),
    ]

    operations = [
        migrations.RunPython(enforce_default_categories),
    ]
