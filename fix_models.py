import os

content = """from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        managed = False
        db_table = 'users'

class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='company')
    max_post_limit = models.IntegerField()
    website = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    voen = models.CharField(max_length=20)
    summary = models.CharField(max_length=400, blank=True, null=True)
    founded_at = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    employees_count = models.IntegerField()
    status = models.BooleanField(default=False)
    activated_by = models.ForeignKey(User, models.DO_NOTHING, related_name='activated_companies', blank=True, null=True)
    activated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'companies'

class Candidate(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='candidate')
    name = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    summary = models.TextField()
    salary_expectation = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'candidates'

class Moderator(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, models.DO_NOTHING, related_name='moderator')
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moderators'

class Industry(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Industry {self.id}"

    class Meta:
        managed = False
        db_table = 'industries'
        verbose_name_plural = 'Industries'

class IndustryTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    industry = models.ForeignKey(Industry, models.DO_NOTHING, related_name='translations')
    locale = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'industry_translations'
        unique_together = (('industry', 'locale'),)

class Occupation(models.Model):
    id = models.BigAutoField(primary_key=True)
    industry = models.ForeignKey(Industry, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occupations'

class OccupationTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    occupation = models.ForeignKey(Occupation, models.DO_NOTHING, related_name='translations')
    locale = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'occupation_translations'
        unique_together = (('occupation', 'locale'),)

class EmploymentType(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employment_types'

class EmploymentTypeTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    employment_type = models.ForeignKey(EmploymentType, models.DO_NOTHING, related_name='translations')
    locale = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'employment_type_translations'
        unique_together = (('employment_type', 'locale'),)

class EducationLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'education_levels'

class EducationLevelTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    education_level = models.ForeignKey(EducationLevel, models.DO_NOTHING, related_name='translations')
    locale = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'education_level_translations'
        unique_together = (('education_level', 'locale'),)

class Level(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'levels'

class LevelTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    level = models.ForeignKey(Level, models.DO_NOTHING, related_name='translations')
    locale = models.CharField(max_length=255)
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'level_translations'
        unique_together = (('level', 'locale'),)

class JobPost(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=70)
    experience = models.CharField(max_length=70)
    salary = models.CharField(max_length=30)
    info = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()
    company = models.ForeignKey(Company, models.DO_NOTHING, related_name='job_posts')
    occupation = models.ForeignKey(Occupation, models.DO_NOTHING, related_name='job_posts')
    employment_type = models.ForeignKey(EmploymentType, models.DO_NOTHING, related_name='job_posts')
    education_level = models.ForeignKey(EducationLevel, models.DO_NOTHING, related_name='job_posts')
    created_by = models.ForeignKey(User, models.DO_NOTHING, related_name='created_job_posts')
    status = models.CharField(max_length=255)
    view_count = models.BigIntegerField(default=0)
    published_at = models.DateTimeField(blank=True, null=True)
    expired_at = models.DateTimeField(blank=True, null=True)
    searchable_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'job_posts'

class JobApplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    job_post = models.ForeignKey(JobPost, models.DO_NOTHING, related_name='applications')
    candidate = models.ForeignKey(Candidate, models.DO_NOTHING, related_name='applications')
    applied_by = models.ForeignKey(User, models.DO_NOTHING, related_name='job_applications')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_applications'

class Boost(models.Model):
    id = models.BigAutoField(primary_key=True)
    job_post = models.ForeignKey(JobPost, models.DO_NOTHING, related_name='boosts')
    booster = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    order_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    valid_until = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boosts'

class Skill(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills'

class CandidateSkill(models.Model):
    id = models.BigAutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, models.DO_NOTHING, related_name='skills')
    skill = models.ForeignKey(Skill, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_skill'
        unique_together = (('candidate', 'skill'),)

class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'

class CandidateLanguageLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, models.DO_NOTHING, related_name='languages')
    language = models.ForeignKey(Language, models.DO_NOTHING)
    level = models.ForeignKey(Level, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_language_level'
        unique_together = (('candidate', 'language'),)
"""

try:
    if os.path.exists('core/models.py'):
        os.remove('core/models.py')
    with open('core/models.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully re-created core/models.py")
except Exception as e:
    print(f"Error: {e}")
