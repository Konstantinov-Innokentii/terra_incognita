pip install requirements.txt\
npm install\
Создать config.py с параметром DATABASE_URI="postgresql://user:password@localhost:5432/database_name"\
alembic upgrade head\
Cобрать фронт (пока только в dev-режиме): npm run dev\
Запустить app.py\
