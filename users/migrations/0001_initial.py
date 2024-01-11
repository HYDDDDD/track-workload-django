# Generated by Django 5.0.1 on 2024-01-11 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('H', 'health'), ('C', 'Culture')], max_length=1)),
                ('updateDate', models.DateField()),
                ('hour', models.IntegerField()),
                ('status', models.CharField(choices=[('P', 'pass'), ('N', 'no pass'), ('D', 'doing')], max_length=1)),
                ('image', models.ImageField(upload_to='activites')),
                ('activityUser', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('phone', models.CharField(max_length=10)),
                ('role', models.CharField(choices=[('Admin', 'admin'), ('Personnel', 'users'), ('Officer', 'officer')], max_length=10)),
                ('branch', models.CharField(blank=True, choices=[('', ''), ('DB', 'สาขาวิชาธุรกิจดิจิทัล'), ('IT', 'สาขาวิชาเทคโนโลยีสารสนเทศ'), ('GIS', 'สาขาวิชาภูมิสารสนเทศศาสตร์'), ('CS', 'สาขาวิชาวิทยาการคอมพิวเตอร์'), ('DSA', 'สาขาวิชาวิทยาการข้อมูลและการประยุกต์'), ('CPE', 'สาขาวิชาวิศวกรรมคอมพิวเตอร์'), ('SE', 'สาขาวิชาวิศวกรรมซอฟต์แวร์'), ('CG', 'สาขาวิชาคอมพิวเตอร์กราฟิกและมัลติมีเดีย'), ('OFFICE', 'สำนักงานคณะ')], max_length=40, null=True)),
                ('totalHour', models.IntegerField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
