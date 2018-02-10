from django.db import models

# Create your models here.
class Person(models.Model):

    MAN = 0
    WOMAN = 1

    HOKKAIDO = 0
    TOHOKU = 5
    TOKYO = 10
    CHIBA = 11
    KANAGAWA = 12
    SAITAMA = 13
    TOCHIGI = 14
    IBARAGI = 15
    CHUBU = 20
    KANSAI = 25
    CHUGOKU = 30
    SHIKOKU = 35
    KYUSHU = 40
    OKINAWA = 45

    # ���O
    name = models.CharField(max_length=128)
    # �a����
    birthday = models.DateTimeField()
    # ����
    sex = models.IntegerField(editable=False)
    # �o�g�n
    address_from = models.IntegerField()
    # ���Z��
    current_address = models.IntegerField()
    # ���[���A�h���X
    email = models.EmailField()


class Manager(models.Model):

    # �����̒萔
    DEP_ACCOUNTING = 0  # �o��
    DEP_SALES = 5  # �c��
    DEP_PRODUCTION = 10  # ����
    DEP_DEVELOPMENT = 15  # �J��
    DEP_HR = 20  # �l��
    DEP_FIN = 25  # ����
    DEP_AFFAIRS = 30  # ����
    DEP_PLANNING = 35  # ���
    DEP_BUSINESS = 40  # �Ɩ�
    DEP_DISTR = 45  # ����
    DEP_IS = 50  # ���V�X�e��

    # �l
    person = models.ForeignKey('Person')
    # ����
    department = models.IntegerField()
    # ���C����
    joined_at = models.DateTimeField()
    # ��߂�����
    quited_at = models.DateTimeField(null=True, blank=True)


class Worker(models.Model):

    # �l
    person = models.ForeignKey('Person')
    # ���C����
    joined_at = models.DateTimeField()
    # ��߂�����
    quited_at = models.DateTimeField(null=True, blank=True)
    # �S����i
    manager = models.ForeignKey('Manager')
