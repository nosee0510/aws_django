import os
from PIL import Image
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile


class ThumbnailImageFieldFile(ImageFieldFile): #이미지 파일을 저장
    def _add_thumb(self, s):  #이메소드는 썸네일 이미지 파일 이름 만들기
        parts = s.split('.')
        parts.insert(-1, 'thumb') #-1은 마지막 위치를 전을 말함 따라서 '경로','thumb','확장자' 순이 됨
        if parts[-1].lower() not in ('jpeg', 'jpg'):
            parts[-1] = 'jpg'
        return '.'.join(parts)

    @property
    def thumb_path(self): #이메소드는 반환 path
        return self._add_thumb(self.path)

    @property
    def thumb_url(self): #url을 받아서 thumb를 붙여서 반환
        return self._add_thumb(self.url)

    def save(self, name, content, save=True): #이메소드는 원래이쓴ㄴ 메소드지만 밑에서 재정의함
        super().save(name, content, save)

        img = Image.open(self.path) #PIL라이브러리로 IMAGE 핸들링
        size = (self.field.thumb_width, self.field.thumb_height) #앞에 128 뒤에 128이 들어감 즉 이미지크기
        img.thumbnail(size) #원본이미지를 저 사이즈크기만큼 섬네일을 만들어라.
        background = Image.new('RGB', size, (255, 255, 255)) #128x128 크기의 흰색 백그라운드를 만든다
        box = (int((size[0]-img.size[0])/2), int((size[1]-img.size[1])/2))
        background.paste(img, box) #박스의 위치에서 섬네일을 붙여라.
        background.save(self.thumb_path, 'JPEG')

    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)


class ThumbnailImageField(ImageField): #경로만저장
    attr_class = ThumbnailImageFieldFile #이분을 통해 FIELDFILE을 연결시킨다. Fieldfile에서 파일을 저장하고 데이터베이스에
    # 경로를 저장하는것이 이클래스이다

    def __init__(self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs):
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verbose_name, **kwargs)