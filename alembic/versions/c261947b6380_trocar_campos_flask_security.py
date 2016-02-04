"""trocar campos flask security

Revision ID: c261947b6380
Revises: 7025a7cc15d1
Create Date: 2016-01-30 16:21:38.131000

"""

# revision identifiers, used by Alembic.
revision = 'c261947b6380'
down_revision = '7025a7cc15d1'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('ALTER TABLE agente RENAME COLUMN senha TO password')
    op.execute('ALTER TABLE agente RENAME COLUMN ativo TO active')

def downgrade():
    op.execute('ALTER TABLE agente RENAME COLUMN password TO senha')
    op.execute('ALTER TABLE agente RENAME COLUMN active TO ativo')
