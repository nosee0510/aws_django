from django.contrib import admin
from photo1.models import Album1, Photo1


class PhotoInline(admin.StackedInline): #세로로 보여주는 클래스  StackedInline은 세로 TabularInline을 쓰면 포토를 가로로 나열해줌
    model = Photo1
    extra = 2 #디폴트로 2개입력  한화면에 2개의 테이블을  입력할수있게. 3으로하면 3개


@admin.register(Album1)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,) #튜플형식으로 저장
    list_display = ('id', 'name', 'description')


@admin.register(Photo1)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')
