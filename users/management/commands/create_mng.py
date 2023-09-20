from django.core.management import BaseCommand
from users.models import User
from django.contrib.auth.models import Group, Permission
from blog.models import Article
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='test@test.ru',
            first_name='test',
            last_name='test_',
            is_staff=True,
            is_active=True
        )
        user.set_password('test')
        user.save()

        user1 = User.objects.create(
            email='test1@test.ru',
            first_name='test1',
            last_name='test1_',
            is_staff=True,
            is_active=True
        )
        user1.set_password('test1')
        user1.save()

        manager = Group.objects.create(name='manager')
        content_manager = Group.objects.create(name='content_manager')

        add_permission = Permission.objects.get(codename='add_article')
        change_permission = Permission.objects.get(codename='change_article')
        delete_permission = Permission.objects.get(codename='delete_article')
        view_permission = Permission.objects.get(codename='view_article')

        content_manager.permissions.add(add_permission, change_permission, delete_permission, view_permission)

        manager.user_set.add(user)
        content_manager.user_set.add(user1)





        # manager = Group.objects.create(name='manager')
        # content_manager = Group.objects.create(name='content_manager')
        #
        # permissions = ['add', 'change', 'delete', 'view']
        # for permission in permissions:
        #     codename = f'blog.{permission}_{Article}'
        #     content_type = ContentType.objects.get_for_model(Article)
        #     p, created = Permission.objects.get_or_create(codename=codename, content_type=content_type)
        #     if created:
        #         p.name = f'Can {permission} article'
        #         p.save()
        #
        # # Добавьте разрешения в группы
        # content_manager.permissions.add(*Permission.objects.filter(codename__icontains='blog'))
        #
        # # Добавьте пользователей в группы
        # manager.user_set.add(user)
        # content_manager.user_set.add(user1)
        #
        # self.stdout.write(self.style.SUCCESS('Группы и разрешения созданы и настроены успешно.'))
