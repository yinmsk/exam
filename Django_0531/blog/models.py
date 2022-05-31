#user/models.py
from django.db import models

# Models.py 에 <글 제목, 글 카테고리, 글 내용>이 들어갈 수 있는 Article 이라는 모델을 만들어보세요.
class UserModel(models.Model):
    class Article:
        db_table = "my_user"
    # ForeignKey
    # author = models.ForeignKey(blog, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=20, null=False)
    article_category = models.CharField(max_length=256, null=False)
    article_content = models.CharField(max_length=256, default='')

# Models.py 에 <카테고리 이름, 설명>이 들어갈 수 있는 Category 라는 모델을 만들어보세요.
class UserModel(models.Model):
    class Category:
        db_table = "my_user"
    article_name = models.CharField(max_length=20, null=False)
    article_description = models.CharField(max_length=256, null=False)