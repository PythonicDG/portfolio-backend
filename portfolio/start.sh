set -e

# Wait for PostgreSQL to be ready
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  echo "Waiting for postgres..."
  sleep 2
done

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin','admin@example.com','adminpassword')"
hypercorn portfolio.asgi:application -b 0.0.0.0:8001 -w 4