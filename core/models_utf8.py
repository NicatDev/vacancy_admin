# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admins(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admins'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Boosts(models.Model):
    id = models.BigAutoField(primary_key=True)
    job_post = models.ForeignKey('JobPosts', models.DO_NOTHING)
    booster = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    order_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boosts'


class Cache(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cache'


class CacheLocks(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    owner = models.CharField(max_length=255)
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cache_locks'


class CandidateLanguageLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    candidate = models.ForeignKey('Candidates', models.DO_NOTHING)
    language = models.ForeignKey('Languages', models.DO_NOTHING)
    level = models.ForeignKey('Levels', models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_language_level'
        unique_together = (('candidate', 'language'),)


class CandidateService(models.Model):
    id = models.BigAutoField(primary_key=True)
    candidate = models.ForeignKey('Candidates', models.DO_NOTHING)
    service = models.ForeignKey('Services', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_service'


class CandidateSkill(models.Model):
    id = models.BigAutoField(primary_key=True)
    candidate = models.ForeignKey('Candidates', models.DO_NOTHING)
    skill = models.ForeignKey('Skills', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_skill'
        unique_together = (('candidate', 'skill'),)


class Candidates(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    summary = models.TextField()
    salary_expectation = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidates'


class Companies(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    max_post_limit = models.IntegerField()
    website = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    voen = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField()
    activated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='companies_activated_by_set', blank=True, null=True)
    activated_at = models.DateTimeField(blank=True, null=True)
    summary = models.CharField(max_length=400, blank=True, null=True)
    founded_at = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    employees_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'companies'


class CompanyPhoneNumbers(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    number = models.CharField(max_length=255)
    label = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_phone_numbers'


class Contacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    comment = models.CharField(max_length=1000)
    read_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='read_by', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    read_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EducationLevelTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    education_level = models.ForeignKey('EducationLevels', models.DO_NOTHING)
    locale = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'education_level_translations'
        unique_together = (('education_level', 'locale'),)


class EducationLevels(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'education_levels'


class EmploymentTypeTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    employment_type = models.ForeignKey('EmploymentTypes', models.DO_NOTHING)
    locale = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'employment_type_translations'
        unique_together = (('employment_type', 'locale'),)


class EmploymentTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employment_types'


class ExternalLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=255)
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_links'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Industries(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industries'


class IndustryTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    industry = models.ForeignKey(Industries, models.DO_NOTHING)
    locale = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'industry_translations'
        unique_together = (('industry', 'locale'),)


class JobApplications(models.Model):
    id = models.BigAutoField(primary_key=True)
    job_post = models.ForeignKey('JobPosts', models.DO_NOTHING)
    candidate = models.ForeignKey(Candidates, models.DO_NOTHING)
    applied_by = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_applications'


class JobBatches(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    total_jobs = models.IntegerField()
    pending_jobs = models.IntegerField()
    failed_jobs = models.IntegerField()
    failed_job_ids = models.TextField()
    options = models.TextField(blank=True, null=True)
    cancelled_at = models.IntegerField(blank=True, null=True)
    created_at = models.IntegerField()
    finished_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_batches'


class JobPosts(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=70)
    experience = models.CharField(max_length=70)
    salary = models.CharField(max_length=30)
    info = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    occupation = models.ForeignKey('Occupations', models.DO_NOTHING)
    employment_type = models.ForeignKey(EmploymentTypes, models.DO_NOTHING)
    education_level = models.ForeignKey(EducationLevels, models.DO_NOTHING)
    created_by = models.ForeignKey('Users', models.DO_NOTHING)
    status = models.CharField(max_length=255)
    published_at = models.DateTimeField(blank=True, null=True)
    expired_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    searchable_text = models.TextField(blank=True, null=True)  # This field type is a guess.
    view_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'job_posts'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255)
    payload = models.TextField()
    attempts = models.SmallIntegerField()
    reserved_at = models.IntegerField(blank=True, null=True)
    available_at = models.IntegerField()
    created_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class JwtTokenBlacklist(models.Model):
    id = models.BigAutoField(primary_key=True)
    jwt_token = models.ForeignKey('JwtTokens', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jwt_token_blacklist'


class JwtTokens(models.Model):
    id = models.UUIDField(primary_key=True)
    tokenable_type = models.CharField(max_length=255)
    tokenable_id = models.BigIntegerField()
    token = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jwt_tokens'


class Languages(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'


class LevelTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    level = models.ForeignKey('Levels', models.DO_NOTHING)
    locale = models.CharField(max_length=255)
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'level_translations'
        unique_together = (('level', 'locale'),)


class Levels(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'levels'


class Media(models.Model):
    id = models.BigAutoField(primary_key=True)
    model_type = models.CharField(max_length=255)
    model_id = models.BigIntegerField()
    uuid = models.UUIDField(unique=True, blank=True, null=True)
    collection_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=255, blank=True, null=True)
    disk = models.CharField(max_length=255)
    conversions_disk = models.CharField(max_length=255, blank=True, null=True)
    size = models.BigIntegerField()
    manipulations = models.TextField()  # This field type is a guess.
    custom_properties = models.TextField()  # This field type is a guess.
    generated_conversions = models.TextField()  # This field type is a guess.
    responsive_images = models.TextField()  # This field type is a guess.
    order_column = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class ModelHasPermissions(models.Model):
    pk = models.CompositePrimaryKey('permission_id', 'model_id', 'model_type')
    permission = models.ForeignKey('Permissions', models.DO_NOTHING)
    model_type = models.CharField(max_length=255)
    model_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_permissions'


class ModelHasRoles(models.Model):
    pk = models.CompositePrimaryKey('role_id', 'model_id', 'model_type')
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    model_type = models.CharField(max_length=255)
    model_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_roles'


class ModelInfoPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    model_info = models.ForeignKey('ModelInfos', models.DO_NOTHING)
    permission = models.ForeignKey('Permissions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'model_info_permission'


class ModelInfos(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_infos'


class Moderators(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moderators'


class OccupationTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    occupation = models.ForeignKey('Occupations', models.DO_NOTHING)
    locale = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'occupation_translations'
        unique_together = (('occupation', 'locale'),)


class Occupations(models.Model):
    id = models.BigAutoField(primary_key=True)
    industry = models.ForeignKey(Industries, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occupations'


class PasswordResetTokens(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_reset_tokens'


class Permissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    guard_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'
        unique_together = (('name', 'guard_name'),)


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=255)
    tokenable_id = models.BigIntegerField()
    name = models.TextField()
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class PricingPlans(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    paypal_plan_id = models.CharField(unique=True, max_length=255)
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    features = models.TextField()  # This field type is a guess.
    max_post_limit = models.IntegerField(blank=True, null=True)
    duration_months = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pricing_plans'


class RoleHasPermissions(models.Model):
    pk = models.CompositePrimaryKey('permission_id', 'role_id')
    permission = models.ForeignKey(Permissions, models.DO_NOTHING)
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_has_permissions'


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    guard_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'
        unique_together = (('name', 'guard_name'),)


class Services(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'


class Sessions(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    user_id = models.BigIntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    payload = models.TextField()
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Skills(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills'


class Subscriptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    paypal_process_id = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    pricing_plan = models.ForeignKey(PricingPlans, models.DO_NOTHING)
    subscribed_by = models.ForeignKey('Users', models.DO_NOTHING)
    status = models.CharField(max_length=255)
    started_at = models.DateTimeField(blank=True, null=True)
    suspended_at = models.DateTimeField(blank=True, null=True)
    expired_at = models.DateTimeField(blank=True, null=True)
    cancelled_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriptions'


class TelescopeEntries(models.Model):
    sequence = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(unique=True)
    batch_id = models.UUIDField()
    family_hash = models.CharField(max_length=255, blank=True, null=True)
    should_display_on_index = models.BooleanField()
    type = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telescope_entries'


class TelescopeEntriesTags(models.Model):
    pk = models.CompositePrimaryKey('entry_uuid', 'tag')
    entry_uuid = models.ForeignKey(TelescopeEntries, models.DO_NOTHING, db_column='entry_uuid', to_field='uuid')
    tag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'telescope_entries_tags'


class TelescopeMonitoring(models.Model):
    tag = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'telescope_monitoring'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
