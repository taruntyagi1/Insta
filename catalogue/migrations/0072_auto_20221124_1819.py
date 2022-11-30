# Generated by Django 2.2.13 on 2022-11-24 12:49

import catalogue.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0071_questionaire_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogmain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Description')),
                ('main_heading', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Main_Heading')),
                ('image', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_blog_image_path, verbose_name='Image')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Client_logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_client_logo_image_path, verbose_name='Image')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_logo_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_blog_image_path, verbose_name='Image')),
                ('title', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Title')),
                ('button', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Button')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consult_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='FaqIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_faqicon_image_path, verbose_name='Image')),
                ('step', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Step')),
                ('title', models.CharField(blank=True, max_length=20000, null=True, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=100000, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='faqicon_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='FAQSproduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True, verbose_name='Question')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Answer')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='faqsproduct_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_header_image_path, verbose_name='Image')),
                ('footer', models.CharField(blank=True, choices=[('Left_section', 'Left_section'), ('Quick_links', 'Quick_links'), ('More_links', 'More_links'), ('Contact_us', 'Contact_us')], max_length=1000, null=True, verbose_name='Footer')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('links', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Links')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='Icon')),
                ('hyperlink', models.URLField(blank=True, null=True, verbose_name='Hyperlink')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='footer_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Frame1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frames', models.CharField(blank=True, choices=[('Frame 1', 'Frame 1'), ('Frame 2', 'Frame 2'), ('Frame 3', 'Frame 3'), ('Frame 4', 'Frame 4'), ('Frame 5', 'Frame 5')], max_length=30, null=True, verbose_name='Frames')),
                ('image', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_about_us_image_path, verbose_name='Image')),
                ('title', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='frame1_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(blank=True, max_length=100, null=True, verbose_name='Menu')),
                ('hyperlink', models.URLField(blank=True, null=True, verbose_name='Hyperlink')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='head_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_header_image_path, verbose_name='Image')),
                ('image_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Image_Title')),
                ('image_hyperlink', models.URLField(blank=True, null=True, verbose_name='Image_Hyperlink')),
                ('menu', models.CharField(blank=True, max_length=100, null=True, verbose_name='Menu')),
                ('hyperlink', models.URLField(blank=True, null=True, verbose_name='Hyperlink')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='header_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='How_it_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Main_Title')),
                ('title', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('title2', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Title2')),
                ('description2', models.TextField(blank=True, null=True, verbose_name='Description2')),
                ('title3', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Title3')),
                ('description3', models.TextField(blank=True, null=True, verbose_name='Description3')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='how_it_work_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Micronutrientdeficiency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Heading')),
                ('description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='micronutrient_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Our_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_our_products_image_path, verbose_name='Image')),
                ('title', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Title')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='our_products_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Question')),
                ('answer', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Answer')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Who_we_are',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_who_we_are_image_path, verbose_name='Image')),
                ('image1', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_who_we_are_image_path, verbose_name='Image1')),
                ('image2', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_who_we_are_image_path, verbose_name='Image2')),
                ('image3', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_who_we_are_image_path, verbose_name='Image3')),
                ('image4', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_who_we_are_image_path, verbose_name='Image4')),
                ('hyperlink', models.URLField(blank=True, null=True, verbose_name='Hyperlink')),
            ],
        ),
        migrations.DeleteModel(
            name='FAQS',
        ),
    ]