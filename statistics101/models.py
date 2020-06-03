# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django_pandas.io import read_frame


class Actions(models.Model):
    type = models.CharField(max_length=200)
    completed_at = models.DateTimeField(blank=True, null=True)
    user_id = models.UUIDField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)  # This field type is a guess.
    data = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'actions'


class Addresses(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.UUIDField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    delivery_time = models.IntegerField(blank=True, null=True)
    kitchen_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'addresses'


class Admins(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    roles = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    fired_at = models.DateTimeField(blank=True, null=True)
    is_online = models.BooleanField(blank=True, null=True)
    kitchen_id = models.IntegerField(blank=True, null=True)
    avatar = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admins'


class AgentSalaries(models.Model):
    day = models.DateField(blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    salary_type = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_salaries'
        unique_together = (('day', 'agent_id', 'amount'),)


class AgentSalaryItems(models.Model):
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.UUIDField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    day = models.DateField(blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'agent_salary_items'
        unique_together = (('source_type', 'source_id'),)


class AppVersions(models.Model):
    platform = models.CharField(max_length=200, blank=True, null=True)
    native_version = models.CharField(max_length=200, blank=True, null=True)
    bundle_url = models.CharField(max_length=200, blank=True, null=True)
    urgent = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    devs_only = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    admin_user_id = models.IntegerField(blank=True, null=True)
    package = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_versions'


class Bonuses(models.Model):
    amount = models.IntegerField(blank=True, null=True)
    user_id = models.UUIDField(blank=True, null=True)
    is_referral = models.BooleanField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bonuses'
# Unable to inspect table 'change_item_requests'
# The error was: permission denied for relation change_item_requests



class Companies(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    permalink = models.CharField(max_length=200, blank=True, null=True)
    compensation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class Cookings(models.Model):
    meta_item_id = models.IntegerField(blank=True, null=True)
    user_id = models.UUIDField(blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    order_id = models.UUIDField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    kitchen_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cookings'


class DelayedJobs(models.Model):
    priority = models.IntegerField()
    attempts = models.IntegerField()
    handler = models.TextField()
    last_error = models.TextField(blank=True, null=True)
    run_at = models.DateTimeField(blank=True, null=True)
    locked_at = models.DateTimeField(blank=True, null=True)
    failed_at = models.DateTimeField(blank=True, null=True)
    locked_by = models.CharField(max_length=200, blank=True, null=True)
    queue = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delayed_jobs'


class Deliveries(models.Model):
    id = models.UUIDField(primary_key=True)
    order_id = models.UUIDField(unique=True, blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    delivery_group_id = models.UUIDField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'deliveries'


class DeliveryGroups(models.Model):
    id = models.UUIDField(primary_key=True)
    agent_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    token = models.UUIDField(unique=True, blank=True, null=True)
    confirmation = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    kitchen_id = models.IntegerField(blank=True, null=True)
    should_confirm_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery_groups'


class Devices(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.UUIDField(blank=True, null=True)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attempts = models.IntegerField(blank=True, null=True)
    confirmatation_token = models.TextField(blank=True, null=True)
    push_token = models.TextField(blank=True, null=True)
    os = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices'


class EggsellentCards(models.Model):
    order_id = models.UUIDField(blank=True, null=True)
    user_id = models.UUIDField(blank=True, null=True)
    card_number = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'eggsellent_cards'


class Employments(models.Model):
    company_id = models.UUIDField(blank=True, null=True)
    user_id = models.UUIDField(blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_admin = models.BooleanField(blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employments'


class Groups(models.Model):
    position = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    kitchen_id = models.IntegerField(blank=True, null=True)
    from_field = models.IntegerField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.IntegerField(blank=True, null=True)
    colors = models.TextField(blank=True, null=True)  # This field type is a guess.
    horizontal = models.BooleanField(blank=True, null=True)
    collaboration = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class IdealGroups(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    from_field = models.IntegerField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.IntegerField(blank=True, null=True)
    colors = models.TextField(blank=True, null=True)  # This field type is a guess.
    week_start = models.DateField(blank=True, null=True)
    kitchen_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    horizontal = models.BooleanField(blank=True, null=True)
    collaboration = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ideal_groups'


class IdealItemGroups(models.Model):
    ideal_group_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ideal_item_groups'


class ItemGroups(models.Model):
    group_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    stop_list_reason = models.CharField(max_length=200, blank=True, null=True)
    stop_list_comment = models.TextField(blank=True, null=True)
    ideal_item_group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_groups'


class Items(models.Model):
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_deleted = models.BooleanField(blank=True, null=True)
    meta_item_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    kitchen_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class Keychains(models.Model):
    user_id = models.UUIDField(blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'keychains'


class Kitchens(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    points = models.TextField(blank=True, null=True)  # This field type is a guess.
    color = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    working_hours = models.TextField(blank=True, null=True)  # This field type is a guess.
    template_groups = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'kitchens'


class Locations(models.Model):
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    battery_level = models.IntegerField(blank=True, null=True)
    keychain_token = models.CharField(max_length=200, blank=True, null=True)
    arrival = models.IntegerField(blank=True, null=True)
    departure = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class LoveDayOrders(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.UUIDField(blank=True, null=True)
    time = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    payed_at = models.DateTimeField(blank=True, null=True)
    kitchen_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'love_day_orders'


class Messages(models.Model):
    user_id = models.UUIDField(blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    ticket_id = models.IntegerField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class MetaItems(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    cook_time = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    station = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    app_tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    content = models.TextField(blank=True, null=True)  # This field type is a guess.
    weight = models.IntegerField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)
    packed_image = models.TextField(blank=True, null=True)
    cook_video = models.CharField(max_length=200, blank=True, null=True)
    flow_sheet = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tag_title = models.CharField(max_length=200, blank=True, null=True)
    carb = models.IntegerField(blank=True, null=True)
    protein = models.IntegerField(blank=True, null=True)
    fat = models.IntegerField(blank=True, null=True)
    food_cost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_items'


class Orders(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.UUIDField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    cooked_at = models.DateTimeField(blank=True, null=True)
    taken_at = models.DateTimeField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    payed_at = models.DateTimeField(blank=True, null=True)
    payment_id = models.UUIDField(blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    basket = models.TextField(blank=True, null=True)  # This field type is a guess.
    time_to_deliver = models.IntegerField(blank=True, null=True)
    sucked_on_slow = models.BooleanField(blank=True, null=True)
    food_time = models.IntegerField(blank=True, null=True)
    kitchen_id = models.IntegerField(blank=True, null=True)
    should_deliver_at = models.DateTimeField(blank=True, null=True)
    partner = models.CharField(max_length=200, blank=True, null=True)
    partner_extra = models.TextField(blank=True, null=True)  # This field type is a guess.

    def to_html(self):
        records = self.objects.all()
        return read_frame(records)

    class Meta:
        managed = False
        db_table = 'orders'


class Packings(models.Model):
    user_id = models.UUIDField(blank=True, null=True)
    order_id = models.UUIDField(blank=True, null=True)
    cooking_id = models.IntegerField(blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    kitchen_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    meta_item_id = models.IntegerField(blank=True, null=True)
    extra = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'packings'


class Payments(models.Model):
    id = models.UUIDField(primary_key=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.UUIDField(blank=True, null=True)
    payment_type = models.CharField(max_length=200, blank=True, null=True)
    cloud_payment_transaction_id = models.CharField(max_length=200, blank=True, null=True)
    ip_address = models.CharField(max_length=200, blank=True, null=True)
    cardholder = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    amount = models.FloatField(blank=True, null=True)
    bonuses = models.IntegerField(blank=True, null=True)
    card_system = models.CharField(max_length=200, blank=True, null=True)
    card_bic = models.CharField(max_length=200, blank=True, null=True)
    card_pan = models.CharField(max_length=200, blank=True, null=True)
    merchant = models.CharField(max_length=200, blank=True, null=True)
    receipt_id = models.UUIDField(blank=True, null=True)
    company_id = models.UUIDField(blank=True, null=True)
    reference_id = models.UUIDField(blank=True, null=True)
    source_type = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'


class PromoCodeGroups(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'promo_code_groups'


class PromoCodes(models.Model):
    code_type = models.CharField(max_length=200, blank=True, null=True)
    user_id = models.UUIDField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=200, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    used_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    expires_on = models.DateTimeField(blank=True, null=True)
    used_times = models.IntegerField(blank=True, null=True)
    promo_code_group_id = models.IntegerField(blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'promo_codes'


class Receipts(models.Model):
    id = models.UUIDField(primary_key=True)
    payment_id = models.UUIDField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'receipts'


class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class Scores(models.Model):
    amount = models.IntegerField(blank=True, null=True)
    admin_user_id = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    order_id = models.UUIDField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'scores'


class StockItems(models.Model):
    stock_id = models.IntegerField(blank=True, null=True)
    meta_item_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stock_items'


class Stocks(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    stock_type = models.CharField(max_length=200, blank=True, null=True)
    unit = models.CharField(max_length=200, blank=True, null=True)
    cost_per_unit = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    station = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stocks'
# Unable to inspect table 'stop_lists'
# The error was: permission denied for relation stop_lists



class Supplies(models.Model):
    ideal_item_group_id = models.IntegerField(unique=True, blank=True, null=True)
    meta_item_id = models.IntegerField(blank=True, null=True)
    kitchen_id = models.IntegerField(blank=True, null=True)
    week_start = models.DateField(blank=True, null=True)
    sunday = models.IntegerField(blank=True, null=True)
    monday = models.IntegerField(blank=True, null=True)
    tuesday = models.IntegerField(blank=True, null=True)
    wednesday = models.IntegerField(blank=True, null=True)
    thursday = models.IntegerField(blank=True, null=True)
    friday = models.IntegerField(blank=True, null=True)
    saturday = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'supplies'


class Tickets(models.Model):
    status = models.CharField(max_length=200, blank=True, null=True)
    closed_at = models.DateTimeField(blank=True, null=True)
    user_id = models.UUIDField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tickets'


class Users(models.Model):
    id = models.UUIDField(primary_key=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    api_token = models.UUIDField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=200, blank=True, null=True)
    referral = models.CharField(max_length=200, blank=True, null=True)
    first_order_feedback = models.TextField(blank=True, null=True)  # This field type is a guess.
    loosing_feedback = models.TextField(blank=True, null=True)  # This field type is a guess.
    preferences = models.TextField(blank=True, null=True)
    display_name = models.CharField(max_length=200, blank=True, null=True)
    attribution = models.TextField(blank=True, null=True)  # This field type is a guess.
    food_settings = models.TextField(blank=True, null=True)  # This field type is a guess.
    coldstart_feedback = models.TextField(blank=True, null=True)  # This field type is a guess.
    app_settings = models.TextField(blank=True, null=True)  # This field type is a guess.
    avatar = models.TextField(blank=True, null=True)
    emoji = models.CharField(max_length=200, blank=True, null=True)
    next_order_gift_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
