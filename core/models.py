from django.db import models
from django.utils.translation import gettext_lazy as _

class JobStatus(models.TextChoices):
    DRAFT = 'draft', _('Draft')
    ACTIVE = 'active', _('Active')
    EXPIRED = 'expired', _('Expired')
    DELETED = 'deleted', _('Deleted')

class BoostStatus(models.TextChoices):
    PENDING = 'pending', _('Pending')
    PAID = 'paid', _('Paid')
    FAILED = 'failed', _('Failed')
    CANCELED = 'canceled', _('Canceled')

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
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    max_post_limit = models.IntegerField()
    website = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    voen = models.CharField(max_length=20)
    summary = models.CharField(max_length=400, blank=True, null=True)
    founded_at = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    employees_count = models.IntegerField()
    status = models.BooleanField(default=False)
    activated_by = models.ForeignKey(User, models.SET_NULL, related_name='activated_companies', blank=True, null=True)
    activated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'companies'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

class Candidate(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate')
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
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'

class Moderator(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, models.CASCADE, related_name='moderator')
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moderators'
        verbose_name = 'Moderator'
        verbose_name_plural = 'Moderators'

class TranslatableModel(models.Model):
    class Meta:
        abstract = True

    def get_translation(self):
        if not hasattr(self, 'translations'):
            return f"{self._meta.verbose_name} {self.pk}"
        t = self.translations.filter(locale='az').first()
        if t: return t.name
        t = self.translations.filter(locale='en').first()
        if t: return t.name
        t = self.translations.first()
        if t: return t.name
        return f"{self._meta.verbose_name} {self.pk}"

class Industry(TranslatableModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.get_translation()

    class Meta:
        managed = False
        db_table = 'industries'
        verbose_name_plural = 'Industries'
        verbose_name = 'Industry'

class IndustryTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    industry = models.ForeignKey(Industry, models.CASCADE, related_name='translations')
    locale = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'industry_translations'
        unique_together = (('industry', 'locale'),)

class Occupation(TranslatableModel):
    id = models.BigAutoField(primary_key=True)
    industry = models.ForeignKey(Industry, models.CASCADE) # Belongs to industry
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.get_translation()

    class Meta:
        managed = False
        db_table = 'occupations'
        verbose_name = 'Occupation'
        verbose_name_plural = 'Occupations'

class OccupationTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    occupation = models.ForeignKey(Occupation, models.CASCADE, related_name='translations')
    locale = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'occupation_translations'
        unique_together = (('occupation', 'locale'),)

class EmploymentType(TranslatableModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.get_translation()

    class Meta:
        managed = False
        db_table = 'employment_types'
        verbose_name = 'Employment Type'
        verbose_name_plural = 'Employment Types'

class EmploymentTypeTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    employment_type = models.ForeignKey(EmploymentType, models.CASCADE, related_name='translations')
    locale = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'employment_type_translations'
        unique_together = (('employment_type', 'locale'),)

class EducationLevel(TranslatableModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.get_translation()

    class Meta:
        managed = False
        db_table = 'education_levels'
        verbose_name = 'Education Level'
        verbose_name_plural = 'Education Levels'

class EducationLevelTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    education_level = models.ForeignKey(EducationLevel, models.CASCADE, related_name='translations')
    locale = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'education_level_translations'
        unique_together = (('education_level', 'locale'),)

class Level(TranslatableModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        if not hasattr(self, 'translations'):
            return f"Level {self.pk}"
        t = self.translations.filter(locale='az').first()
        if t: return t.label
        t = self.translations.filter(locale='en').first()
        if t: return t.label
        t = self.translations.first()
        if t: return t.label
        return f"Level {self.pk}"

    class Meta:
        managed = False
        db_table = 'levels'
        verbose_name = 'Level'
        verbose_name_plural = 'Levels'

class LevelTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    level = models.ForeignKey(Level, models.CASCADE, related_name='translations')
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
    company = models.ForeignKey(Company, models.CASCADE, related_name='job_posts')
    occupation = models.ForeignKey(Occupation, models.CASCADE, related_name='job_posts')
    employment_type = models.ForeignKey(EmploymentType, models.SET_NULL, null=True, related_name='job_posts')
    education_level = models.ForeignKey(EducationLevel, models.SET_NULL, null=True, related_name='job_posts')
    created_by = models.ForeignKey(User, models.CASCADE, related_name='created_job_posts')
    status = models.CharField(max_length=255, choices=JobStatus.choices, default=JobStatus.DRAFT)
    view_count = models.BigIntegerField(default=0)
    published_at = models.DateTimeField(blank=True, null=True)
    expired_at = models.DateTimeField(blank=True, null=True)
    # searchable_text = models.TextField(blank=True, null=True) # Generated column, cannot insert
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'job_posts'
        verbose_name = 'Job Post'
        verbose_name_plural = 'Job Posts'

class JobApplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    job_post = models.ForeignKey(JobPost, models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(Candidate, models.CASCADE, related_name='applications')
    applied_by = models.ForeignKey(User, models.CASCADE, related_name='job_applications')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_applications'
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'

class Boost(models.Model):
    id = models.BigAutoField(primary_key=True)
    job_post = models.ForeignKey(JobPost, models.CASCADE, related_name='boosts')
    booster = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    order_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, choices=BoostStatus.choices, default=BoostStatus.PENDING)
    valid_until = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boosts'
        verbose_name = 'Boost'
        verbose_name_plural = 'Boosts'

class PricingPlans(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    paypal_plan_id = models.CharField(unique=True, max_length=255)
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    features = models.JSONField(null=True,blank=True)  # This field type is a guess.
    max_post_limit = models.IntegerField(blank=True, null=True)
    duration_months = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pricing_plans'

class Skill(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'skills'
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

class CandidateSkill(models.Model):
    id = models.BigAutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, models.CASCADE)
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

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'languages'
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

class CandidateLanguageLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, models.CASCADE, related_name='languages')
    language = models.ForeignKey(Language, models.CASCADE)
    level = models.ForeignKey(Level, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_language_level'
        unique_together = (('candidate', 'language'),)

